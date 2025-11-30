"""
Latarnia v6 - An ethical reasoning framework for AI systems.

This package provides a modular framework for AI agents with components for:
- Core logic and reasoning
- Tool integrations
- Security controls
- Runtime environment (Web UI)
- Performance optimizations (Turbo)
- Retrieval-Augmented Generation (RAG)
- Distributed processing (Hive)
"""

__version__ = "6.0.0"
__author__ = "adamfanok2-crypto"

from latarnia.core import logic

__all__ = [
    "__version__",
    "__author__",
    "logic",
]
