#!/usr/bin/env python3
"""
Startup script for SHL Assessment Agent
Runs the FastAPI server with proper configuration
"""
import subprocess
import sys
import os

def check_env():
    """Check if .env file exists and has GEMINI_API_KEY."""
    if not os.path.exists(".env"):
        print("ERROR: .env file not found!")
        print("Please copy .env.example to .env and add your GEMINI_API_KEY")
        return False
    
    with open(".env", "r") as f:
        content = f.read()
        if "GEMINI_API_KEY" not in content or "your_api_key_here" in content:
            print("ERROR: GEMINI_API_KEY not configured in .env")
            return False
    
    return True

def main():
    print("=" * 60)
    print("SHL Assessment Agent - Starting Server")
    print("=" * 60)
    
    # Check environment
    if not check_env():
        sys.exit(1)
    
    print("\nStarting FastAPI server...")
    print("\n✓ Access the server at: http://localhost:8000")
    print("✓ Health check: GET http://localhost:8000/health")
    print("✓ Chat endpoint: POST http://localhost:8000/chat")
    print("✓ API docs: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop the server.\n")
    
    # Run the server
    try:
        subprocess.run(
            [sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"],
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
