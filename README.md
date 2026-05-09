# SHL Assessment Agent

A conversational AI agent that helps users find the right SHL assessments for their needs. Built with FastAPI and Google Gemini 2.5 Flash.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env with your GEMINI_API_KEY

# Start the server
python start_server.py

# Run tests in another terminal
python test_agent.py
```

## Features

- **Conversational Interface**: Multi-turn conversations with clarifying questions
- **SHL Catalog Integration**: Access to 377+ professional assessments
- **Schema Validation**: Strict JSON responses with Pydantic
- **Stateless Design**: Ready for deployment
- **Interactive API Docs**: FastAPI auto-generated documentation

## Architecture

### Core Components

1. **main.py** - FastAPI server with /health and /chat endpoints
2. **catalog_manager.py** - SHL assessment catalog loader and indexing
3. **test_agent.py** - Unit tests and API validation
4. **test_all_traces.py** - Tests against 10 sample conversations
5. **run_project.py** - Full test runner
6. **start_server.py** - Server startup script

### Technology Stack

- **Backend**: FastAPI (async web framework)
- **LLM**: Google Gemini 2.5 Flash
- **Validation**: Pydantic (strict schemas)
- **Server**: Uvicorn (ASGI)
- **Config**: python-dotenv

## API Endpoints

### Health Check
```http
GET /health
```
**Response**: `{"status": "ok"}`

### Chat
```http
POST /chat
```

**Request**:
```json
{
  "messages": [
    {"role": "user", "content": "We need assessments for senior leadership"}
  ]
}
```

**Response**:
```json
{
  "reply": "To provide the most relevant recommendations, could you tell me...",
  "recommendations": [],
  "end_of_conversation": false
}
```

## Assessment Types

- **A** - Ability Tests
- **K** - Knowledge Tests
- **P** - Personality Tests
- **S** - Situational Judgment Tests
- **C** - Competency Tests
- **B** - Behavioral Tests
- **D** - Development Tools

## Testing

```bash
# Unit tests
python test_agent.py

# Full trace validation (10 conversations)
python test_all_traces.py

# Complete test suite
python run_project.py
```

## Project Structure

```
SHL ASSIGNMENT/
├── main.py                      # FastAPI server
├── catalog_manager.py           # Catalog loader
├── test_agent.py               # Unit tests
├── test_all_traces.py          # Trace validation
├── run_project.py              # Test runner
├── start_server.py             # Server launcher
├── requirements.txt            # Dependencies
├── .env.example                # Config template
├── README.md                   # Documentation
└── GenAI_SampleConversations/  # 10 test traces
```