#!/usr/bin/env python3
"""
SHL Assessment Agent - Project Overview
Shows how the project components work together
"""
import os
import json

def show_project_structure():
    """Display the project structure."""
    print("=" * 60)
    print("SHL Assessment Agent - Project Structure")
    print("=" * 60)

    for root, dirs, files in os.walk('.'):
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            if file.endswith(('.py', '.md', '.txt', '.json')):
                print(f'{subindent}{file}')
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']

def show_how_it_works():
    """Explain how the project works."""
    print("\n" + "=" * 60)
    print("How the SHL Assessment Agent Works")
    print("=" * 60)

    print("""
1. CATALOG LOADING (catalog_manager.py)
   ├── Fetches SHL assessment catalog from API
   ├── Processes 377+ assessments into structured format
   ├── Creates fast lookup index for validation
   └── Each assessment has: name, URL, test_type, description

2. FASTAPI SERVER (main.py)
   ├── Starts web server on http://localhost:8000
   ├── Handles /health endpoint for status checks
   ├── Processes /chat requests with conversation history
   └── Validates responses against Pydantic schemas

3. CONVERSATION FLOW
   ├── User sends vague query → Agent asks clarifying questions
   ├── User provides details → Agent recommends 1-10 assessments
   ├── User refines request → Agent updates recommendations
   ├── User compares assessments → Agent uses catalog data only

4. GEMINI LLM INTEGRATION
   ├── System prompt includes entire catalog for accuracy
   ├── Stateless design - full history in each request
   ├── Strict JSON output requirements
   ├── Rate limit handling with exponential backoff

5. RESPONSE VALIDATION
   ├── Pydantic models ensure schema compliance
   ├── Catalog validation prevents hallucinations
   ├── Single test type per assessment (A/K/P/S/C/B/D)
   ├── Turn limit enforcement (max 8 turns)
""")

def show_api_examples():
    """Show API usage examples."""
    print("\n" + "=" * 60)
    print("API Usage Examples")
    print("=" * 60)

    print("""
HEALTH CHECK:
GET http://localhost:8000/health
Response: {"status": "ok"}

CHAT REQUEST:
POST http://localhost:8000/chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "We need assessments for senior leadership."}
  ]
}

CHAT RESPONSE:
{
  "reply": "Happy to help narrow that down. Who is this meant for?",
  "recommendations": [],
  "end_of_conversation": false
}

INTERACTIVE DOCS:
Visit: http://localhost:8000/docs
- Try API endpoints interactively
- See request/response schemas
- Test with sample data
""")

def show_technologies():
    """Show the technology stack."""
    print("\n" + "=" * 60)
    print("Technology Stack")
    print("=" * 60)

    tech_stack = {
        "Backend Framework": "FastAPI (async, high-performance)",
        "LLM Provider": "Google Gemini 2.5 Flash",
        "Data Validation": "Pydantic (strict schemas)",
        "HTTP Client": "Requests (catalog fetching)",
        "Environment": "python-dotenv (config management)",
        "Server": "Uvicorn (ASGI server)",
        "Testing": "Built-in unit tests + trace validation",
        "Deployment": "Stateless design (Docker/K8s ready)"
    }

    for component, description in tech_stack.items():
        print(f"• {component}: {description}")

def main():
    """Main overview function."""
    show_project_structure()
    show_how_it_works()
    show_api_examples()
    show_technologies()

    print("\n" + "=" * 60)
    print("Getting Started")
    print("=" * 60)
    print("""
1. Install dependencies: pip install -r requirements.txt
2. Configure API key: copy .env.example .env
3. Start server: python start_server.py
4. Test agent: python demo.py
5. Run tests: python test_agent.py

Visit http://localhost:8000/docs for interactive API testing!
""")

if __name__ == "__main__":
    main()