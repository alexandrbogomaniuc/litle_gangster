const WARNING_TEXT = "Internal donor/scaffold preview only. Not approved for release. All scaffold assets require replacement or explicit approval.";

const STATE_FILTERS = ["cascade", "golden", "rainbow", "coin", "feature", "cap", "reconnect"];

function makeGridObjects() {
  const objects = [];
  for (let column = 1; column <= 6; column += 1) {
    for (let row = 1; row <= 5; row += 1) {
      const x = 18 + (column - 1) * 10.6;
      const y = 17 + (row - 1) * 11.6;
      objects.push({
        id: `scene.base.grid.cell.c${column}.r${row}.cascade_removed`,
        scene: "cascade_sequence",
        state: "cascade",
        label: "Removed",
        x, y, w: 9.5, h: 10.4,
        fields: ["base_game.cascade_steps[].removed_cells"],
        release: "pending_replacement",
        notes: "Removed-cell marker rendered from backend/runtime cascade step."
      });
      objects.push({
        id: `scene.base.grid.cell.c${column}.r${row}.drop_target`,
        scene: "cascade_sequence",
        state: "cascade",
        label: "Drop",
        x: x + 1.1, y: y + 1.1, w: 7.3, h: 8.2,
        fields: ["base_game.cascade_steps[].dropped_cells", "base_game.cascade_steps[].new_symbols"],
        release: "pending_replacement",
        notes: "Drop/refill marker rendered from backend/runtime cascade step."
      });
      objects.push({
        id: `scene.base.grid.cell.c${column}.r${row}.golden_overlay`,
        scene: "golden_square_overlay",
        state: "golden",
        label: "Golden",
        x: x + 0.4, y: y + 0.4, w: 8.7, h: 9.6,
        fields: ["base_game.golden_squares_before", "base_game.golden_square_events", "base_game.golden_squares_after"],
        release: "pending_replacement",
        notes: "Golden-square persistence overlay rendered from v0.3 result state."
      });
    }
  }
  return objects;
}

const SPECIAL_OBJECTS = [
  { id: "scene.base.rainbow.activation", scene: "rainbow_activation_scene", state: "rainbow", label: "Rainbow activation", x: 42, y: 36, w: 16, h: 14, fields: ["base_game.rainbow_positions", "base_game.rainbow_activation_events", "base_game.affected_golden_squares"], release: "pending_replacement", notes: "Activation effect only; client is not outcome authority." },
  { id: "scene.base.coin_reveal.bronze", scene: "coin_reveal_scene", state: "coin", label: "Bronze", x: 28, y: 69, w: 10, h: 8, fields: ["base_game.coin_reveals[].tier", "base_game.coin_reveals[].value_x_bet"], release: "pending_replacement", notes: "Bronze reveal tier placeholder." },
  { id: "scene.base.coin_reveal.silver", scene: "coin_reveal_scene", state: "coin", label: "Silver", x: 45, y: 69, w: 10, h: 8, fields: ["base_game.coin_reveals[].tier", "base_game.coin_reveals[].value_x_bet"], release: "pending_replacement", notes: "Silver reveal tier placeholder." },
  { id: "scene.base.coin_reveal.gold", scene: "coin_reveal_scene", state: "coin", label: "Gold", x: 62, y: 69, w: 10, h: 8, fields: ["base_game.coin_reveals[].tier", "base_game.coin_reveals[].value_x_bet"], release: "pending_replacement", notes: "Gold reveal tier placeholder." },
  { id: "scene.base.special_reveal.pot_of_gold", scene: "coin_reveal_scene", state: "coin", label: "Pot", x: 34, y: 80, w: 11, h: 7, fields: ["base_game.special_reveals[].reveal_type"], release: "pending_replacement", notes: "Optional candidate, not final confirmed release asset." },
  { id: "scene.base.special_reveal.four_leaf_clover", scene: "coin_reveal_scene", state: "coin", label: "Clover", x: 55, y: 80, w: 11, h: 7, fields: ["base_game.special_reveals[].reveal_type"], release: "pending_replacement", notes: "Optional candidate, not final confirmed release asset." },
  { id: "scene.feature.mode_1.panel", scene: "feature_mode_selection", state: "feature", label: "mode_1", x: 18, y: 12, w: 18, h: 10, fields: ["feature_mode_state.mode_key", "feature_mode_state.entry_source"], release: "pending_replacement", notes: "Feature mode panel placeholder." },
  { id: "scene.feature.mode_2.panel", scene: "feature_mode_selection", state: "feature", label: "mode_2", x: 41, y: 12, w: 18, h: 10, fields: ["feature_mode_state.mode_key", "feature_mode_state.entry_source"], release: "pending_replacement", notes: "Feature mode panel placeholder." },
  { id: "scene.feature.mode_3.panel", scene: "feature_mode_selection", state: "feature", label: "mode_3", x: 64, y: 12, w: 18, h: 10, fields: ["feature_mode_state.mode_key", "feature_mode_state.entry_source"], release: "pending_replacement", notes: "Feature mode panel placeholder." },
  { id: "scene.bonus_buy.mode_selection", scene: "bonus_buy_panel", state: "feature", label: "Buy mode", x: 32, y: 24, w: 36, h: 12, fields: ["bonus_buy_state.selected_mode", "bonus_buy_state.cost_x_bet"], release: "pending_replacement", notes: "Bonus-buy mode selection, EV remains pending." },
  { id: "scene.max_win.cap_overlay", scene: "max_win_cap_scene", state: "cap", label: "Cap reached", x: 22, y: 32, w: 56, h: 18, fields: ["max_win_cap.cap_reached", "max_win_cap.cap_reached_at_step"], release: "pending_replacement", notes: "Max-win cap overlay; cap calculation is backend/runtime authority." },
  { id: "scene.max_win.pre_cap_amount", scene: "max_win_cap_scene", state: "cap", label: "Pre-cap", x: 25, y: 53, w: 20, h: 7, fields: ["max_win_cap.pre_cap_win"], release: "pending_replacement", notes: "Pre-cap amount display." },
  { id: "scene.max_win.capped_amount", scene: "max_win_cap_scene", state: "cap", label: "Capped", x: 55, y: 53, w: 20, h: 7, fields: ["max_win_cap.capped_win"], release: "pending_replacement", notes: "Capped win display." },
  { id: "scene.win_tier.big", scene: "big_win_scene", state: "cap", label: "Big", x: 23, y: 63, w: 13, h: 8, fields: ["winRatio", "winTier"], release: "pending_replacement", notes: "Candidate advisory win-tier threshold." },
  { id: "scene.win_tier.huge", scene: "big_win_scene", state: "cap", label: "Huge", x: 43, y: 63, w: 13, h: 8, fields: ["winRatio", "winTier"], release: "pending_replacement", notes: "Candidate advisory win-tier threshold." },
  { id: "scene.win_tier.mega", scene: "big_win_scene", state: "cap", label: "Mega", x: 63, y: 63, w: 13, h: 8, fields: ["winRatio", "winTier"], release: "pending_replacement", notes: "Candidate advisory win-tier threshold." },
  { id: "scene.round_completion.ready", scene: "round_completion_state", state: "reconnect", label: "Round ready", x: 20, y: 75, w: 24, h: 8, fields: ["round_completion.final_state_ready"], release: "pending_replacement", notes: "Round completion marker from backend/runtime state." },
  { id: "scene.reconnect.restore_state", scene: "state_recovery_reconnect_scene", state: "reconnect", label: "Restore", x: 56, y: 75, w: 24, h: 8, fields: ["state_persistence", "state_persistence.lastAction_or_current_gs_equivalent"], release: "pending_replacement", notes: "Reconnect restore state marker." }
];

const OBJECTS = [...makeGridObjects(), ...SPECIAL_OBJECTS];
let activeState = "cascade";
let activeObject = OBJECTS[0];

function qs(selector) { return document.querySelector(selector); }
function qsa(selector) { return Array.from(document.querySelectorAll(selector)); }

function renderObjects() {
  const search = (qs("#objectSearch")?.value || "").toLowerCase();
  const board = qs("#sceneCanvas");
  if (!board) return;
  board.innerHTML = "";
  const filtered = OBJECTS.filter((obj) => obj.state === activeState && (!search || obj.id.toLowerCase().includes(search)));
  filtered.forEach((obj) => {
    const el = document.createElement("button");
    el.className = `scene-object state-${obj.state}`;
    el.type = "button";
    el.style.left = `${obj.x}%`;
    el.style.top = `${obj.y}%`;
    el.style.width = `${obj.w}%`;
    el.style.height = `${obj.h}%`;
    el.textContent = obj.label;
    el.title = obj.id;
    el.addEventListener("click", () => { activeObject = obj; renderDetails(); });
    board.appendChild(el);
  });
  const count = qs("#visibleCount");
  if (count) count.textContent = String(filtered.length);
}

function renderDetails() {
  const panel = qs("#objectDetails");
  if (!panel || !activeObject) return;
  panel.innerHTML = `
    <dl>
      <dt>Object ID</dt><dd>${activeObject.id}</dd>
      <dt>Scene ID</dt><dd>${activeObject.scene}</dd>
      <dt>v0.3 fields</dt><dd>${activeObject.fields.join(", ")}</dd>
      <dt>Ownership status</dt><dd>placeholder / scaffold_internal_only where scaffold previews exist</dd>
      <dt>Release status</dt><dd>${activeObject.release}</dd>
      <dt>Replacement required</dt><dd>true</dd>
      <dt>Dimensions</dt><dd>${activeObject.w.toFixed(1)}% x ${activeObject.h.toFixed(1)}%</dd>
      <dt>Notes</dt><dd>${activeObject.notes}</dd>
    </dl>`;
}

function renderBoundaryNotes() {
  const notes = qs("#sceneNotes");
  if (!notes) return;
  notes.innerHTML = `
    <p>${WARNING_TEXT}</p>
    <p>v0.3 mode: the client renders backend/runtime result payload only. Browser RNG and authoritative win calculation are forbidden.</p>
    <p>Wallet/accounting and registration metadata are separate from scene animation rendering. Current GS result owner remains unproven, so full GameClientBuilder remains blocked pending runtime/result API review.</p>`;
}

function bindControls() {
  qsa("[data-state]").forEach((button) => {
    button.addEventListener("click", () => {
      activeState = button.dataset.state;
      qsa("[data-state]").forEach((item) => item.classList.toggle("active", item === button));
      activeObject = OBJECTS.find((obj) => obj.state === activeState) || OBJECTS[0];
      renderObjects();
      renderDetails();
    });
  });
  const search = qs("#objectSearch");
  if (search) search.addEventListener("input", renderObjects);
}

document.addEventListener("DOMContentLoaded", () => {
  bindControls();
  renderBoundaryNotes();
  renderObjects();
  renderDetails();
});
