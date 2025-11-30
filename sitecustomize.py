"""
Site customization for Latarnia v6

This module is automatically imported during Python startup when present
in the site-packages directory or project root. It can be used to configure
the Python environment for Latarnia.

Note: This file should be copied to site-packages for system-wide effect,
or kept in the project root for project-specific customization.
"""

import os
import sys


def setup_latarnia_environment():
    """Configure the Latarnia runtime environment."""
    # Add the project root to the Python path if not already present
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # Set default environment variables for Latarnia
    os.environ.setdefault("LATARNIA_VERSION", "6.0.0")
    os.environ.setdefault("LATARNIA_LOG_LEVEL", "INFO")


# Run setup on import
setup_latarnia_environment()
