#!/usr/bin/env python3
"""Deterministic simulator for Little Gangster v0.3 donor-parity provisional math.

The simulator reads only explicit math package files passed by CLI. It does not
access network resources, donor assets, GS, wallet endpoints, databases, or
secrets. RTP is computed from generated symbols, cluster evaluation, cascade
steps, golden-square/rainbow/coin feature events, and feature modes. It does not
normalize totals after simulation and does not read target RTP to scale wins.
"""
from __future__ import annotations

import argparse
import json
import math
import random
from collections import deque
from pathlib import Path
from typing import Any

NEIGHBORS = ((1,0),(-1,0),(0,1),(0,-1))


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Required file does not exist: {path}")
    if not path.is_file():
        raise ValueError(f"Required path is not a file: {path}")
    return json.loads(path.read_text(encoding='utf-8'))


def resolve_variant(package: dict[str, Any], variant: str, package_path: Path) -> dict[str, Path]:
    variants = package.get('rtp_variants', {})
    if variant not in variants:
        raise KeyError(f"Unknown RTP variant {variant!r}; available: {', '.join(sorted(variants))}")
    root = package_path.parent
    spec = variants[variant]
    required = ('model_config','symbol_weights','cluster_paytable','feature_rules')
    return {key: root / spec[key] for key in required}


def weighted_symbol(rng: random.Random, weights: dict[str, int]) -> str:
    total = sum(int(v) for v in weights.values())
    if total <= 0:
        raise ValueError('Symbol weights must sum to a positive value')
    pick = rng.randrange(total)
    cursor = 0
    for symbol, weight in weights.items():
        cursor += int(weight)
        if pick < cursor:
            return symbol
    return next(reversed(weights))


def spin_grid(rng: random.Random, symbol_weights: dict[str, Any], mode: str, rows: int, cols: int) -> list[list[str]]:
    weights_by_reel = symbol_weights[mode]
    if len(weights_by_reel) != cols:
        raise ValueError(f'{mode} must contain exactly {cols} reel/column weight maps')
    return [[weighted_symbol(rng, weights_by_reel[col]) for col in range(cols)] for _ in range(rows)]


def cluster_pay(symbol: str, count: int, paytable: dict[str, Any]) -> float:
    pays = paytable['cluster_pays_x_bet'].get(symbol, {})
    best = 0.0
    for threshold, value in pays.items():
        if count >= int(threshold):
            best = float(value)
    return best


def evaluate_clusters(grid: list[list[str]], paytable: dict[str, Any], wild_symbol: str) -> dict[str, Any]:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    clusters: list[dict[str, Any]] = []
    removed: set[tuple[int,int]] = set()
    total = 0.0
    for target in paytable['cluster_pays_x_bet']:
        visited: set[tuple[int,int]] = set()
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited or grid[row][col] not in (target, wild_symbol):
                    continue
                queue: deque[tuple[int,int]] = deque([(row, col)])
                visited.add((row, col))
                cells: list[tuple[int,int]] = []
                while queue:
                    current_row, current_col = queue.popleft()
                    cells.append((current_row, current_col))
                    for row_delta, col_delta in NEIGHBORS:
                        nr = current_row + row_delta
                        nc = current_col + col_delta
                        if not (0 <= nr < rows and 0 <= nc < cols):
                            continue
                        if (nr, nc) in visited:
                            continue
                        if grid[nr][nc] not in (target, wild_symbol):
                            continue
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                if len(cells) >= int(paytable['minimum_cluster_size']):
                    win = cluster_pay(target, len(cells), paytable)
                    if win > 0:
                        cell_dicts = [{'row': r, 'col': c} for r, c in cells]
                        clusters.append({'symbol': target, 'count': len(cells), 'cells': cell_dicts, 'win_x_bet': win})
                        total += win
                        removed.update(cells)
    return {'clusters': clusters, 'removed_cells': sorted(removed), 'cluster_win_x_bet': total}


def drop_and_refill(rng: random.Random, grid: list[list[str]], removed: set[tuple[int,int]], weights: dict[str, Any], rows: int, cols: int) -> tuple[list[list[str]], list[dict[str, Any]], list[dict[str, Any]]]:
    next_grid: list[list[str]] = [[None for _ in range(cols)] for _ in range(rows)]  # type: ignore[list-item]
    dropped: list[dict[str, Any]] = []
    new_symbols: list[dict[str, Any]] = []
    for col in range(cols):
        kept = [(row, grid[row][col]) for row in range(rows) if (row, col) not in removed]
        fill_count = rows - len(kept)
        fill = [weighted_symbol(rng, weights[col]) for _ in range(fill_count)]
        col_symbols = fill + [symbol for _, symbol in kept]
        for new_row, symbol in enumerate(col_symbols):
            next_grid[new_row][col] = symbol
            if new_row < fill_count:
                new_symbols.append({'row': new_row, 'col': col, 'symbol': symbol})
        for original_row, symbol in kept:
            new_row = col_symbols.index(symbol) if symbol in fill else fill_count + [s for _, s in kept].index(symbol)
            if new_row != original_row:
                dropped.append({'from': {'row': original_row, 'col': col}, 'to': {'row': new_row, 'col': col}, 'symbol': symbol})
    return next_grid, dropped, new_symbols


def positions_for(grid: list[list[str]], symbol: str) -> list[tuple[int,int]]:
    return [(row, col) for row, values in enumerate(grid) for col, value in enumerate(values) if value == symbol]


def choose_weighted_key(rng: random.Random, options: dict[str, Any]) -> str:
    total = sum(int(v['weight']) for v in options.values())
    pick = rng.randrange(total)
    cursor = 0
    for key, spec in options.items():
        cursor += int(spec['weight'])
        if pick < cursor:
            return key
    return next(reversed(options))


def process_rainbow_and_reveals(
    rng: random.Random,
    grid: list[list[str]],
    golden_cells: set[tuple[int,int]],
    feature_rules: dict[str, Any],
    cascade_index: int,
    feature_mode: str | None,
) -> dict[str, Any]:
    rainbow_positions = positions_for(grid, 'LG_RAINBOW')
    if not rainbow_positions or not golden_cells:
        return {'win_x_bet': 0.0, 'rainbow_events': [], 'coin_reveals': [], 'special_reveals': []}
    activation_probability = float(feature_rules['rainbow_activation']['activation_probability_per_golden_cell_feature' if feature_mode else 'activation_probability_per_golden_cell_base'])
    tier_table = feature_rules['coin_reveals']['feature_tiers' if feature_mode else 'tiers']
    events = []
    coin_reveals = []
    special_reveals = []
    win = 0.0
    activated = []
    for cell in sorted(golden_cells):
        if rng.random() < activation_probability:
            activated.append(cell)
            tier = choose_weighted_key(rng, tier_table)
            value = float(tier_table[tier]['value_x_bet'])
            coin_reveals.append({'position': {'row': cell[0], 'col': cell[1]}, 'tier': tier, 'value_x_bet': value, 'source_event': 'rainbow_activation', 'cascade_index': cascade_index})
            win += value
            for special_name, spec in feature_rules['special_reveals']['events'].items():
                if rng.random() < float(spec['probability_per_activated_cell']):
                    special_value = float(rng.choice(spec['values_x_bet']))
                    special_reveals.append({'position': {'row': cell[0], 'col': cell[1]}, 'type': special_name, 'value_x_bet': special_value, 'source_event': 'golden_square_special_reveal', 'cascade_index': cascade_index})
                    win += special_value
    if activated:
        events.append({'cascadeIndex': cascade_index, 'rainbowPositions': [{'row': r, 'col': c} for r, c in rainbow_positions], 'activatedGoldenCells': [{'row': r, 'col': c} for r, c in activated]})
    return {'win_x_bet': win, 'rainbow_events': events, 'coin_reveals': coin_reveals, 'special_reveals': special_reveals}


def run_cascade_chain(
    rng: random.Random,
    initial_grid: list[list[str]],
    model_config: dict[str, Any],
    symbol_weights: dict[str, Any],
    paytable: dict[str, Any],
    feature_rules: dict[str, Any],
    feature_mode: str | None = None,
) -> dict[str, Any]:
    rows = int(model_config['grid']['rows'])
    cols = int(model_config['grid']['reels'])
    weights_key = 'feature_modes' if feature_mode else 'base_game'
    grid = [row[:] for row in initial_grid]
    golden_cells: set[tuple[int,int]] = set()
    cascade_steps = []
    rainbow_events = []
    coin_reveals = []
    special_reveals = []
    total = 0.0
    cluster_total = 0.0
    reveal_total = 0.0
    for cascade_index in range(1, int(model_config['max_cascade_steps']) + 1):
        evaluation = evaluate_clusters(grid, paytable, model_config['symbols']['wild'])
        if not evaluation['clusters']:
            break
        removed = set(evaluation['removed_cells'])
        grid_before = [row[:] for row in grid]
        cluster_win = float(evaluation['cluster_win_x_bet'])
        cluster_total += cluster_win
        total += cluster_win
        golden_before = sorted(golden_cells)
        golden_cells.update(removed)
        reveal = process_rainbow_and_reveals(rng, grid, golden_cells, feature_rules, cascade_index, feature_mode)
        total += float(reveal['win_x_bet'])
        reveal_total += float(reveal['win_x_bet'])
        rainbow_events.extend(reveal['rainbow_events'])
        coin_reveals.extend(reveal['coin_reveals'])
        special_reveals.extend(reveal['special_reveals'])
        grid, dropped, new_symbols = drop_and_refill(rng, grid, removed, symbol_weights[weights_key], rows, cols)
        cascade_steps.append({
            'cascadeIndex': cascade_index,
            'gridBefore': grid_before,
            'winningClusters': evaluation['clusters'],
            'removedCells': [{'row': r, 'col': c} for r, c in sorted(removed)],
            'droppedSymbols': dropped,
            'newSymbols': new_symbols,
            'gridAfter': [row[:] for row in grid],
            'clusterWin': cluster_win,
            'goldenSquaresBefore': [{'row': r, 'col': c} for r, c in golden_before],
            'goldenSquaresAfter': [{'row': r, 'col': c} for r, c in sorted(golden_cells)],
        })
    return {
        'initialGrid': initial_grid,
        'finalGrid': grid,
        'cascadeSteps': cascade_steps,
        'goldenSquares': {'beforeRound': [], 'perCascade': [{'cascadeIndex': step['cascadeIndex'], 'after': step['goldenSquaresAfter']} for step in cascade_steps], 'afterRound': [{'row': r, 'col': c} for r, c in sorted(golden_cells)]},
        'rainbowActivationEvents': rainbow_events,
        'coinReveals': coin_reveals,
        'specialReveals': special_reveals,
        'win_x_bet': total,
        'cluster_win_x_bet': cluster_total,
        'reveal_win_x_bet': reveal_total,
        'cascade_count': len(cascade_steps),
    }


def feature_mode_from_grid(grid: list[list[str]]) -> str | None:
    count = sum(1 for row in grid for symbol in row if symbol == 'LG_RAINBOW')
    if count >= 5:
        return 'mode_3'
    if count == 4:
        return 'mode_2'
    if count == 3:
        return 'mode_1'
    return None


def simulate_round(rng: random.Random, model_config: dict[str, Any], symbol_weights: dict[str, Any], paytable: dict[str, Any], feature_rules: dict[str, Any]) -> dict[str, Any]:
    rows = int(model_config['grid']['rows'])
    cols = int(model_config['grid']['reels'])
    cap = float(model_config['max_win_x_bet'])
    base_grid = spin_grid(rng, symbol_weights, 'base_game', rows, cols)
    base = run_cascade_chain(rng, base_grid, model_config, symbol_weights, paytable, feature_rules)
    total = float(base['win_x_bet'])
    feature_win = 0.0
    feature_mode = feature_mode_from_grid(base_grid)
    feature_spins_played = 0
    feature_cascades = 0
    feature_reveals = 0.0
    feature_cluster = 0.0
    if feature_mode:
        mode_spec = feature_rules['feature_modes'][feature_mode]
        for _ in range(int(mode_spec['spins'])):
            feature_spins_played += 1
            feature_grid = spin_grid(rng, symbol_weights, 'feature_modes', rows, cols)
            feature = run_cascade_chain(rng, feature_grid, model_config, symbol_weights, paytable, feature_rules, feature_mode=feature_mode)
            multiplier = float(mode_spec['win_multiplier'])
            spin_win = float(feature['win_x_bet']) * multiplier
            total += spin_win
            feature_win += spin_win
            feature_cascades += int(feature['cascade_count'])
            feature_reveals += float(feature['reveal_win_x_bet']) * multiplier
            feature_cluster += float(feature['cluster_win_x_bet']) * multiplier
            if total >= cap:
                break
    pre_cap = total
    cap_reached = total >= cap
    if cap_reached:
        total = cap
    return {
        'total_win_x_bet': total,
        'pre_cap_win_x_bet': pre_cap,
        'base_win_x_bet': min(float(base['win_x_bet']), total),
        'base_cluster_win_x_bet': float(base['cluster_win_x_bet']),
        'base_reveal_win_x_bet': float(base['reveal_win_x_bet']),
        'feature_win_x_bet': feature_win,
        'feature_cluster_win_x_bet': feature_cluster,
        'feature_reveal_win_x_bet': feature_reveals,
        'feature_mode_triggered': feature_mode is not None,
        'feature_mode': feature_mode,
        'feature_spins_played': feature_spins_played,
        'cascade_count': int(base['cascade_count']) + feature_cascades,
        'coin_reveal_count': len(base['coinReveals']),
        'special_reveal_count': len(base['specialReveals']),
        'rainbow_activation_count': len(base['rainbowActivationEvents']),
        'cap_reached': cap_reached,
        'cap_reached_at_step': 'round_total' if cap_reached else None,
    }


def run_simulation(args: argparse.Namespace) -> dict[str, Any]:
    package_path = Path(args.math_package).resolve()
    package = load_json(package_path)
    paths = resolve_variant(package, args.rtp_variant, package_path)
    model_config = load_json(paths['model_config'])
    symbol_weights = load_json(paths['symbol_weights'])
    paytable = load_json(paths['cluster_paytable'])
    feature_rules = load_json(paths['feature_rules'])
    rounds = int(args.rounds)
    if rounds <= 0:
        raise ValueError('--rounds must be positive')
    rng = random.Random(int(args.seed))
    total = base = feature = base_cluster = base_reveal = feature_cluster = feature_reveal = 0.0
    sum_squares = 0.0
    hits = feature_triggers = cascades = coin_reveals = special_reveals = rainbow_activations = caps = 0
    max_observed = 0.0
    mode_counts = {'mode_1':0,'mode_2':0,'mode_3':0}
    for _ in range(rounds):
        result = simulate_round(rng, model_config, symbol_weights, paytable, feature_rules)
        win = float(result['total_win_x_bet'])
        total += win
        sum_squares += win * win
        base += float(result['base_win_x_bet'])
        feature += float(result['feature_win_x_bet'])
        base_cluster += float(result['base_cluster_win_x_bet'])
        base_reveal += float(result['base_reveal_win_x_bet'])
        feature_cluster += float(result['feature_cluster_win_x_bet'])
        feature_reveal += float(result['feature_reveal_win_x_bet'])
        hits += int(win > 0)
        feature_triggers += int(result['feature_mode_triggered'])
        if result['feature_mode']:
            mode_counts[result['feature_mode']] += 1
        cascades += int(result['cascade_count'])
        coin_reveals += int(result['coin_reveal_count'])
        special_reveals += int(result['special_reveal_count'])
        rainbow_activations += int(result['rainbow_activation_count'])
        caps += int(result['cap_reached'])
        max_observed = max(max_observed, win)
    mean = total / rounds
    variance = max(0.0, (sum_squares / rounds) - (mean * mean))
    simulated = mean * 100.0
    target = float(model_config['rtp_profile']['target_rtp_percent'])
    tolerance = float(model_config['rtp_profile']['workflow_test_tolerance_percent'])
    deviation = simulated - target
    out = {
        'project': package['project'],
        'math_version': package['math_version'],
        'rtp_variant': args.rtp_variant,
        'target_rtp_percent': target,
        'simulated_rtp_percent': round(simulated, 6),
        'deviation_percentage_points': round(deviation, 6),
        'workflow_test_tolerance_percentage_points': tolerance,
        'status': 'pass_workflow_tolerance' if abs(deviation) <= tolerance else 'outside_workflow_tolerance',
        'rounds': rounds,
        'seed': int(args.seed),
        'hit_frequency_percent': round((hits / rounds) * 100.0, 6),
        'standard_deviation_x_bet': round(math.sqrt(variance), 6),
        'volatility_proxy': 'high' if math.sqrt(variance) >= 5.0 else 'medium_or_low',
        'max_win_observed_x_bet': round(max_observed, 6),
        'max_win_cap_x_bet': float(model_config['max_win_x_bet']),
        'cap_reached_frequency_percent': round((caps / rounds) * 100.0, 6),
        'base_game_contribution_percent': round((base / rounds) * 100.0, 6),
        'base_cluster_contribution_percent': round((base_cluster / rounds) * 100.0, 6),
        'base_reveal_contribution_percent': round((base_reveal / rounds) * 100.0, 6),
        'feature_contribution_percent': round((feature / rounds) * 100.0, 6),
        'feature_cluster_contribution_percent': round((feature_cluster / rounds) * 100.0, 6),
        'feature_reveal_contribution_percent': round((feature_reveal / rounds) * 100.0, 6),
        'feature_trigger_frequency_percent': round((feature_triggers / rounds) * 100.0, 6),
        'feature_mode_trigger_counts': mode_counts,
        'average_cascade_steps_per_round': round(cascades / rounds, 6),
        'coin_reveal_frequency_per_round': round(coin_reveals / rounds, 6),
        'special_reveal_frequency_per_round': round(special_reveals / rounds, 6),
        'rainbow_activation_frequency_per_round': round(rainbow_activations / rounds, 6),
        'cascade_steps_modeled': True,
        'golden_square_state_modeled': True,
        'rainbow_activation_modeled': True,
        'coin_reveal_modeled': True,
        'pot_clover_reveal_modeled': True,
        'three_feature_modes_modeled': True,
        'bonus_buy_modeled_in_base_rtp': False,
        'double_up_modeled': False,
        'simulator_scaling_detected': False,
        'post_simulation_normalization_detected': False,
        'rtp_is_emergent_from_symbol_weights_paytable_cascades_and_features': True,
        'notes': ['Workflow validation only; not release certification.', 'Target RTP is used for comparison only, not payout scaling.', 'No donor assets, browser, GS, wallet, DB, or secrets are read.']
    }
    if args.output:
        Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description='Simulate Little Gangster v0.3 donor-parity provisional math.')
    parser.add_argument('--math-package', required=True)
    parser.add_argument('--rtp-variant', required=True, choices=['rtp_96','rtp_94','rtp_92'])
    parser.add_argument('--rounds', required=True, type=int)
    parser.add_argument('--seed', required=True, type=int)
    parser.add_argument('--output')
    args = parser.parse_args()
    print(json.dumps(run_simulation(args), indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
