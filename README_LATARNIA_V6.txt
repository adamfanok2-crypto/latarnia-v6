================================================================================
                           LATARNIA v6 - AI Ethics Framework
================================================================================

Latarnia v6 is a modular Python framework for an AI agent with components for
ethical reasoning, fact auditing, consequence simulation, and neutral mediation
while preserving user sovereignty.

--------------------------------------------------------------------------------
PACKAGE STRUCTURE
--------------------------------------------------------------------------------

latarnia/
├── __init__.py          # Main package initialization
├── core/                # Core logic module
│   ├── __init__.py
│   └── logic.py         # Central reasoning engine
├── tools/               # Tool integrations
│   └── __init__.py
├── security/            # Security components
│   └── __init__.py
├── runtime/             # Runtime environment
│   ├── __init__.py
│   └── webui.py         # Streamlit web interface
├── turbo/               # Performance optimizations
│   └── __init__.py
├── rag/                 # Retrieval-Augmented Generation
│   └── __init__.py
└── hive/                # Distributed processing
    └── __init__.py

--------------------------------------------------------------------------------
INSTALLATION
--------------------------------------------------------------------------------

Install the package in development mode:

    pip install -e .

For development dependencies:

    pip install -e ".[dev]"

--------------------------------------------------------------------------------
RUNNING THE WEB UI
--------------------------------------------------------------------------------

After installation, run the Streamlit web interface:

    streamlit run latarnia/runtime/webui.py

Or use the provided runner script:

    python run_latarnia.py

--------------------------------------------------------------------------------
COMPONENTS
--------------------------------------------------------------------------------

1. CORE (latarnia.core)
   - Central reasoning engine
   - Ethical decision framework
   - Logic processing

2. TOOLS (latarnia.tools)
   - External tool integrations
   - API connectors
   - Utility functions

3. SECURITY (latarnia.security)
   - Access control
   - Input validation
   - Audit logging

4. RUNTIME (latarnia.runtime)
   - Web UI via Streamlit
   - Command-line interface
   - Session management

5. TURBO (latarnia.turbo)
   - Performance optimizations
   - Caching mechanisms
   - Parallel processing

6. RAG (latarnia.rag)
   - Retrieval-Augmented Generation
   - Document indexing
   - Context retrieval

7. HIVE (latarnia.hive)
   - Distributed processing
   - Agent coordination
   - Task distribution

--------------------------------------------------------------------------------
CONFIGURATION
--------------------------------------------------------------------------------

Create a .env file in the project root for environment-specific settings:

    # Example .env (DO NOT COMMIT)
    LATARNIA_DEBUG=true
    LATARNIA_LOG_LEVEL=INFO

Note: The .env file is excluded from version control for security reasons.

--------------------------------------------------------------------------------
LICENSE
--------------------------------------------------------------------------------

MIT License - See LICENSE file for details.

================================================================================
