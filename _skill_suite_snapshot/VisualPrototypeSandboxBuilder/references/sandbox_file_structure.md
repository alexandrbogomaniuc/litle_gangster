# Sandbox File Structure

Use a project-local path:

```text
11_prototypes/<gameId>_<slug>_visual_sandbox/
  README.md
  PROTOTYPE_STATUS.md
  asset_inventory.json
  placeholder_binding.json
  scripted_outcomes.json
  screen_states.json
  SMOKE_TEST_CHECKLIST.md
  BLOCKERS.md
  assets_placeholder/
  scripts_reference/
  index.html              # optional static sandbox only
  prototype.css           # optional static sandbox only
  prototype.js            # optional static sandbox only
```

The path must not be inside Staging source, `Gamesv1/games/<gameId>`, production
client output folders, or public export folders.
