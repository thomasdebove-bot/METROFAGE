from __future__ import annotations

import os
import sys
import threading
import webbrowser
from pathlib import Path

import importlib.util

import uvicorn


def main() -> None:
    exe_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    sys.path.insert(0, str(exe_dir))
    host = os.getenv("METRONOME_HOST", "0.0.0.0")
    port = int(os.getenv("METRONOME_PORT", "8090"))
    app_module = None
    try:
        import app as app_module  # type: ignore
    except Exception:
        app_path = exe_dir / "app.py"
        if app_path.exists():
            spec = importlib.util.spec_from_file_location("app", app_path)
            if spec and spec.loader:
                app_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(app_module)

    def open_browser() -> None:
        webbrowser.open(f"http://127.0.0.1:{port}")

    threading.Timer(1.5, open_browser).start()
    if not app_module or not hasattr(app_module, "app"):
        raise RuntimeError("Impossible de charger le module app.py")
    uvicorn.run(app_module.app, host=host, port=port)


if __name__ == "__main__":
    main()
