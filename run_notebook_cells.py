import json
import sys
import traceback


notebook_path = sys.argv[1]

with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

namespace = {"__name__": "__main__"}

for index, cell in enumerate(notebook.get("cells", [])):
    if cell.get("cell_type") != "code":
        continue

    source = "".join(cell.get("source", []))
    if not source.strip():
        continue

    print(f"\n--- executing cell {index} ---", flush=True)
    try:
        exec(compile(source, f"{notebook_path}:cell_{index}", "exec"), namespace)
    except Exception:
        print(f"\nNotebook failed in code cell {index}", file=sys.stderr)
        traceback.print_exc()
        raise SystemExit(1)

print("\nNotebook completed successfully.")
