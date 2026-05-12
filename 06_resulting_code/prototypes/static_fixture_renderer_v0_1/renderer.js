(() => {
  'use strict';

  const manifestPath = 'fixtures_manifest.json';
  const state = {
    manifest: null,
    fixtures: [],
    activeIndex: 0,
    loadedById: new Map()
  };

  const els = {
    select: document.getElementById('fixture-select'),
    count: document.getElementById('fixture-count'),
    list: document.getElementById('fixture-list'),
    loadStatus: document.getElementById('load-status'),
    previous: document.getElementById('previous-fixture'),
    next: document.getElementById('next-fixture'),
    fileInput: document.getElementById('fixture-file-input'),
    title: document.getElementById('fixture-title'),
    runtimeStatus: document.getElementById('runtime-status'),
    extensionStatus: document.getElementById('extension-status'),
    id: document.getElementById('fixture-id'),
    name: document.getElementById('fixture-name'),
    purpose: document.getElementById('fixture-purpose'),
    grid: document.getElementById('symbol-grid'),
    overlay: document.getElementById('overlay-panel'),
    badges: document.getElementById('state-badges'),
    fields: document.getElementById('field-list'),
    scenes: document.getElementById('scene-states'),
    objects: document.getElementById('object-states'),
    notes: document.getElementById('notes-list'),
    template: document.getElementById('cell-template')
  };

  const symbolLabels = {
    cash: '$',
    badge: 'BDG',
    thief: 'THF',
    car: 'CAR',
    vault: 'VLT',
    coin: 'COIN',
    rainbow: 'RNB',
    clover: 'CLV',
    pot: 'POT'
  };

  const symbolClasses = ['cash', 'badge', 'thief', 'car', 'vault', 'coin', 'rainbow'];

  async function init() {
    wireEvents();
    try {
      const response = await fetch(manifestPath, { cache: 'no-store' });
      if (!response.ok) {
        throw new Error(`Fixture manifest load failed with status ${response.status}`);
      }
      state.manifest = await response.json();
      state.fixtures = Array.isArray(state.manifest.fixtures) ? state.manifest.fixtures : [];
      renderFixtureControls();
      await loadFixtureByIndex(0);
    } catch (error) {
      showLoadError(error);
    }
  }

  function wireEvents() {
    els.select.addEventListener('change', () => loadFixtureByIndex(Number(els.select.value)));
    els.previous.addEventListener('click', () => loadFixtureByIndex(wrapIndex(state.activeIndex - 1)));
    els.next.addEventListener('click', () => loadFixtureByIndex(wrapIndex(state.activeIndex + 1)));
    els.fileInput.addEventListener('change', handleFileInput);
  }

  function wrapIndex(index) {
    if (!state.fixtures.length) return 0;
    return (index + state.fixtures.length) % state.fixtures.length;
  }

  function renderFixtureControls() {
    els.count.textContent = `${state.fixtures.length} / ${state.manifest.fixtureExamplesExpectedCount || 24}`;
    els.select.innerHTML = '';
    els.list.innerHTML = '';

    state.fixtures.forEach((entry, index) => {
      const option = document.createElement('option');
      option.value = String(index);
      option.textContent = `${entry.fixtureId} - ${entry.fixtureName}`;
      els.select.appendChild(option);

      const item = document.createElement('li');
      item.dataset.index = String(index);
      item.textContent = `${entry.fixtureId}: ${entry.fixtureName}`;
      item.addEventListener('click', () => loadFixtureByIndex(index));
      els.list.appendChild(item);
    });
  }

  async function loadFixtureByIndex(index) {
    if (!state.fixtures.length) return;
    state.activeIndex = wrapIndex(index);
    els.select.value = String(state.activeIndex);
    highlightActiveListItem();
    const entry = state.fixtures[state.activeIndex];

    try {
      let data = state.loadedById.get(entry.fixtureId);
      if (!data) {
        const response = await fetch(entry.path, { cache: 'no-store' });
        if (!response.ok) {
          throw new Error(`Fixture load failed with status ${response.status}`);
        }
        data = await response.json();
        state.loadedById.set(entry.fixtureId, data);
      }
      els.loadStatus.textContent = 'Loaded from local planning fixture JSON.';
      renderFixture(data);
    } catch (error) {
      showLoadError(error, entry);
    }
  }

  function highlightActiveListItem() {
    [...els.list.children].forEach((item) => {
      item.classList.toggle('active', Number(item.dataset.index) === state.activeIndex);
    });
  }

  function handleFileInput(event) {
    const file = event.target.files && event.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const data = JSON.parse(String(reader.result));
        els.loadStatus.textContent = `Loaded fallback file: ${file.name}`;
        renderFixture(data);
      } catch (error) {
        showLoadError(error);
      }
    };
    reader.readAsText(file);
  }

  function showLoadError(error, entry) {
    const suffix = entry ? ` Selected fixture: ${entry.fixtureId}.` : '';
    els.loadStatus.textContent = `Local fixture load blocked or failed.${suffix}`;
    els.grid.innerHTML = `<div class="error-box">${escapeHtml(error.message)}. Use a local-only static server or the JSON file fallback.</div>`;
  }

  function renderFixture(fixture) {
    const payload = getRenderPayload(fixture);
    const base = payload.base_game || {};
    const grid = normalizeGrid(firstArray(
      base.final_grid,
      lastCascadeGridAfter(base.cascade_steps),
      base.grid_before,
      fixture.presentationPayload && fixture.presentationPayload.symbolGrid
    ));
    const stateMarks = collectStateMarks(fixture, payload);

    els.title.textContent = fixture.fixtureName || fixture.fixtureId || '-';
    els.runtimeStatus.textContent = fixture.runtimeEnvelopeStatus || 'candidate_unproven';
    els.extensionStatus.textContent = fixture.presentationPayloadExtensionStatus || 'pending_schema_review';
    els.id.textContent = fixture.fixtureId || '-';
    els.name.textContent = fixture.fixtureName || '-';
    els.purpose.textContent = fixture.purpose || '-';

    renderBadges(fixture, payload);
    renderGrid(grid, stateMarks);
    renderOverlayCards(fixture, payload);
    renderFields(payload);
    renderTagList(els.scenes, fixture.expectedSceneStates || []);
    renderObjectStates(fixture.expectedObjectStates || []);
    renderNotes(fixture.notes || []);
  }

  function getRenderPayload(fixture) {
    return fixture.v0_3_payload
      || (fixture.presentationPayload && fixture.presentationPayload.gamePayload && fixture.presentationPayload.gamePayload.payload)
      || {};
  }

  function firstArray(...values) {
    return values.find((value) => Array.isArray(value));
  }

  function lastCascadeGridAfter(steps) {
    if (!Array.isArray(steps) || !steps.length) return null;
    const last = steps[steps.length - 1];
    return Array.isArray(last.grid_after) ? last.grid_after : null;
  }

  function normalizeGrid(grid) {
    const fallback = [
      ['cash', 'badge', 'car', 'vault', 'coin', 'rainbow'],
      ['thief', 'cash', 'badge', 'car', 'vault', 'coin'],
      ['car', 'vault', 'cash', 'coin', 'badge', 'thief'],
      ['vault', 'coin', 'thief', 'cash', 'car', 'badge'],
      ['badge', 'rainbow', 'vault', 'car', 'cash', 'coin']
    ];
    if (!Array.isArray(grid) || !grid.length) return fallback;
    const rows = grid.map((row) => Array.isArray(row) ? row.slice(0, 6) : []);
    while (rows.length < 5) rows.push([]);
    return rows.slice(0, 5).map((row, rowIndex) => {
      const out = row.slice(0, 6);
      while (out.length < 6) out.push(fallback[rowIndex][out.length]);
      return out;
    });
  }

  function collectStateMarks(fixture, payload) {
    const marks = new Map();
    const base = payload.base_game || {};
    const steps = Array.isArray(base.cascade_steps) ? base.cascade_steps : [];
    const allRemoved = flatten([base.removed_cells, ...steps.map((step) => step.removed_cells)]);
    const allDropped = flatten([base.dropped_cells, ...steps.map((step) => step.dropped_cells)]);
    const allNew = flatten([base.new_symbols, ...steps.map((step) => step.new_symbols)]);
    const allClusters = flatten([base.clusters, ...steps.map((step) => step.clusters), ...steps.map((step) => step.winning_clusters)]);
    const allGolden = flatten([
      base.golden_squares_before,
      base.golden_squares_after,
      base.golden_square_positions,
      base.golden_square_events,
      ...steps.map((step) => step.golden_squares_before),
      ...steps.map((step) => step.golden_squares_after)
    ]);
    const allRainbow = flatten([base.rainbow_positions, base.rainbow_activation_events, base.affected_golden_squares]);
    const allCoins = flatten([base.coin_reveals, ...steps.map((step) => step.coin_reveals)]);

    allRemoved.forEach((cell) => addMark(marks, cell, 'removed'));
    allDropped.forEach((cell) => addMark(marks, cell.to || cell, 'dropped'));
    allNew.forEach((cell) => addMark(marks, cell.position || cell, 'new-symbol'));
    allClusters.forEach((cluster) => (cluster.cells || []).forEach((cell) => addMark(marks, cell, 'cluster')));
    allGolden.forEach((cell) => addMark(marks, cell.position || cell.cell || cell, 'golden'));
    allRainbow.forEach((cell) => addMark(marks, cell.position || cell.cell || cell, 'rainbow-active'));
    allCoins.forEach((cell) => addMark(marks, cell.position || cell.cell || cell, 'coin-reveal'));

    applySyntheticMarksWhenPositionsMissing(marks, fixture.fixtureId || '');
    return marks;
  }

  function flatten(groups) {
    return groups.flatMap((group) => Array.isArray(group) ? group : []);
  }

  function addMark(marks, cell, mark) {
    const key = cellKey(cell);
    if (!key) return;
    if (!marks.has(key)) marks.set(key, new Set());
    marks.get(key).add(mark);
  }

  function cellKey(cell) {
    if (!cell || typeof cell !== 'object') return null;
    const column = Number(cell.column || cell.col || cell.c || (cell.position && cell.position.column));
    const row = Number(cell.row || cell.r || (cell.position && cell.position.row));
    if (!column || !row) return null;
    return `${column}:${row}`;
  }

  function applySyntheticMarksWhenPositionsMissing(marks, fixtureId) {
    const hasAny = (name) => [...marks.values()].some((set) => set.has(name));
    const mark = (key, name) => {
      if (!marks.has(key)) marks.set(key, new Set());
      marks.get(key).add(name);
    };
    if (fixtureId.includes('golden') && !hasAny('golden')) mark('3:3', 'golden');
    if (fixtureId.includes('rainbow') && !hasAny('rainbow-active')) mark('4:2', 'rainbow-active');
    if (fixtureId.includes('coin') && !hasAny('coin-reveal')) mark('5:3', 'coin-reveal');
    if (fixtureId.includes('cascade') && !hasAny('removed')) mark('1:1', 'removed');
    if (fixtureId.includes('cascade') && !hasAny('dropped')) mark('1:2', 'dropped');
    if (fixtureId.includes('cascade') && !hasAny('new-symbol')) mark('1:5', 'new-symbol');
  }

  function renderGrid(grid, stateMarks) {
    els.grid.innerHTML = '';
    grid.forEach((row, rowIndex) => {
      row.forEach((symbol, columnIndex) => {
        const cell = els.template.content.firstElementChild.cloneNode(true);
        const cleanSymbol = String(symbol || 'empty');
        const column = columnIndex + 1;
        const rowNumber = rowIndex + 1;
        const key = `${column}:${rowNumber}`;
        const marks = [...(stateMarks.get(key) || [])];
        const baseSymbol = cleanSymbol.replace(/^new_/, '');
        const symbolClass = symbolClasses.find((name) => baseSymbol.includes(name));
        if (symbolClass) cell.classList.add(`symbol-${symbolClass}`);
        marks.forEach((mark) => cell.classList.add(mark));
        cell.querySelector('.cell-position').textContent = `c${column} r${rowNumber}`;
        cell.querySelector('.cell-symbol').textContent = symbolLabels[baseSymbol] || cleanSymbol.toUpperCase();
        cell.querySelector('.cell-flags').textContent = marks.map(shortMark).join(' ');
        els.grid.appendChild(cell);
      });
    });
  }

  function shortMark(mark) {
    return {
      removed: 'REM',
      dropped: 'DROP',
      'new-symbol': 'NEW',
      cluster: 'CL',
      golden: 'GOLD',
      'rainbow-active': 'RNB',
      'coin-reveal': 'COIN'
    }[mark] || mark;
  }

  function renderBadges(fixture, payload) {
    const states = new Set();
    const id = fixture.fixtureId || '';
    const base = payload.base_game || {};
    if (id.includes('idle')) states.add('base idle');
    if (id.includes('no_win')) states.add('no win');
    if ((base.cascade_steps || []).length) states.add('cascade');
    if (id.includes('golden')) states.add('golden square');
    if (id.includes('rainbow')) states.add('rainbow');
    if (id.includes('coin')) states.add('coin reveal');
    if (id.includes('pot') || id.includes('clover')) states.add('special reveal');
    if (id.includes('feature_mode')) states.add('feature mode');
    if (id.includes('bonus_buy')) states.add('bonus buy');
    if (id.includes('big_win') || id.includes('huge') || id.includes('mega')) states.add('win tier');
    if (id.includes('max_win')) states.add('max cap');
    if (id.includes('completion')) states.add('round completion');
    if (id.includes('reconnect')) states.add('reconnect');
    if (id.includes('error')) states.add('recovery pending');

    els.badges.innerHTML = '';
    [...states].forEach((stateName) => {
      const badge = document.createElement('span');
      badge.className = `badge ${badgeClass(stateName)}`;
      badge.textContent = stateName;
      els.badges.appendChild(badge);
    });
  }

  function badgeClass(name) {
    if (name.includes('golden')) return 'gold';
    if (name.includes('rainbow')) return 'rainbow';
    if (name.includes('feature') || name.includes('bonus')) return 'feature';
    if (name.includes('win') || name.includes('completion')) return 'win';
    if (name.includes('error')) return 'danger';
    return 'neutral';
  }

  function renderOverlayCards(fixture, payload) {
    const base = payload.base_game || {};
    const cards = [
      ['Cascade steps', String((base.cascade_steps || []).length)],
      ['Total win', String(payload.totalWin ?? 0)],
      ['Win ratio / tier', `${payload.winRatio ?? 0} / ${payload.winTier || 'none'}`],
      ['Feature mode', describeObject(payload.feature_mode_state)],
      ['Bonus buy', describeObject(payload.bonus_buy_state)],
      ['Max-win cap', describeObject(payload.max_win_cap)],
      ['Round completion', describeObject(payload.round_completion)],
      ['State persistence', describeObject(payload.state_persistence)]
    ];
    els.overlay.innerHTML = '';
    cards.forEach(([title, text]) => {
      const card = document.createElement('div');
      card.className = 'overlay-card';
      card.innerHTML = `<strong>${escapeHtml(title)}</strong><span>${escapeHtml(text)}</span>`;
      els.overlay.appendChild(card);
    });
  }

  function describeObject(value) {
    if (!value || typeof value !== 'object') return 'not present';
    const keys = Object.keys(value).slice(0, 4);
    if (!keys.length) return 'empty object';
    return keys.map((key) => `${key}: ${compact(value[key])}`).join(', ');
  }

  function compact(value) {
    if (value === null || value === undefined) return 'none';
    if (Array.isArray(value)) return `[${value.length}]`;
    if (typeof value === 'object') return '{...}';
    return String(value);
  }

  function renderFields(payload) {
    const fields = collectFieldNames(payload);
    els.fields.innerHTML = '';
    fields.forEach((field) => {
      const tag = document.createElement('span');
      tag.className = 'tag';
      tag.textContent = field;
      els.fields.appendChild(tag);
    });
  }

  function collectFieldNames(payload) {
    const fields = [];
    Object.keys(payload || {}).forEach((key) => fields.push(key));
    const base = payload.base_game || {};
    ['cascade_steps', 'removed_cells', 'dropped_cells', 'new_symbols', 'clusters', 'golden_square_events', 'rainbow_activation_events', 'coin_reveals', 'special_reveals'].forEach((key) => {
      if (key in base) fields.push(`base_game.${key}`);
    });
    return [...new Set(fields)].slice(0, 36);
  }

  function renderTagList(container, items) {
    container.innerHTML = '';
    items.forEach((item) => {
      const tag = document.createElement('span');
      tag.className = 'tag';
      tag.textContent = typeof item === 'string' ? item : JSON.stringify(item);
      container.appendChild(tag);
    });
  }

  function renderObjectStates(items) {
    els.objects.innerHTML = '';
    items.forEach((item) => {
      const li = document.createElement('li');
      li.textContent = typeof item === 'string' ? item : JSON.stringify(item);
      els.objects.appendChild(li);
    });
  }

  function renderNotes(items) {
    els.notes.innerHTML = '';
    if (!items.length) {
      const li = document.createElement('li');
      li.textContent = 'No fixture notes provided.';
      els.notes.appendChild(li);
      return;
    }
    items.forEach((item) => {
      const li = document.createElement('li');
      li.textContent = String(item);
      els.notes.appendChild(li);
    });
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  init();
})();
