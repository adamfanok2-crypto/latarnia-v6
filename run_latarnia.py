#!/usr/bin/env python3
"""
Latarnia v6 - Main Entry Point

This script launches the Latarnia web interface using Streamlit.
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Launch the Latarnia web UI."""
    # Get the path to the webui module
    webui_path = Path(__file__).parent / "latarnia" / "runtime" / "webui.py"
    
    if not webui_path.exists():
        print(f"Error: Web UI not found at {webui_path}", file=sys.stderr)
        sys.exit(1)
    
    # Run Streamlit with the webui module
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", str(webui_path)],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Streamlit not found. Install it with: pip install streamlit", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
