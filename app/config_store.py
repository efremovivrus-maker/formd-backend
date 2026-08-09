from datetime import datetime, timezone
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
VERSIONS_DIR = DATA_DIR / "versions"

SYSTEM_PROMPT_PATH = DATA_DIR / "system_prompt.txt"
MANUFACTURING_RULES_PATH = DATA_DIR / "manufacturing_rules.md"
META_PATH = DATA_DIR / "config_meta.json"


def _read_meta() -> dict:
    if not META_PATH.exists():
        return {"version": 1, "updated_at": None}
    return json.loads(META_PATH.read_text(encoding="utf-8"))


def get_config() -> dict:
    meta = _read_meta()
    return {
        "version": meta["version"],
        "updated_at": meta.get("updated_at"),
        "system_prompt": SYSTEM_PROMPT_PATH.read_text(encoding="utf-8"),
        "manufacturing_rules": MANUFACTURING_RULES_PATH.read_text(encoding="utf-8"),
    }


def save_config(system_prompt: str, manufacturing_rules: str) -> dict:
    current = get_config()

    timestamp = datetime.now(timezone.utc)
    stamp = timestamp.strftime("%Y%m%dT%H%M%SZ")

    version_dir = VERSIONS_DIR / f"v{current['version']}_{stamp}"
    version_dir.mkdir(parents=True, exist_ok=False)

    (version_dir / "system_prompt.txt").write_text(
        current["system_prompt"], encoding="utf-8"
    )
    (version_dir / "manufacturing_rules.md").write_text(
        current["manufacturing_rules"], encoding="utf-8"
    )

    new_version = current["version"] + 1

    SYSTEM_PROMPT_PATH.write_text(system_prompt, encoding="utf-8")
    MANUFACTURING_RULES_PATH.write_text(manufacturing_rules, encoding="utf-8")

    META_PATH.write_text(
        json.dumps(
            {
                "version": new_version,
                "updated_at": timestamp.isoformat(),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return get_config()
