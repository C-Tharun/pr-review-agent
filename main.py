"""
PR Review Agent - Main Entry Point for Deployment

This is the main entry point for the PR Review Agent application.
It imports and runs the FastAPI app from the backend module.

"""

import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Import the FastAPI app
from simple_pr_app import app

# This is the entry point for deployment platforms
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
