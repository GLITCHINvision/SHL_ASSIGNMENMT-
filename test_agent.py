import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def test_health():
    """Test the /health endpoint."""
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200 and response.json().get("status") == "ok":
            print("✓ Health Check: PASSED")
            return True
        else:
            print(f"✗ Health Check: FAILED - {response.status_code} {response.json()}")
            return False
    except Exception as e:
        print(f"✗ Health Check: ERROR - {e}")
        return False

def test_chat(messages, test_name=""):
    """Test the /chat endpoint."""
    try:
        payload = {"messages": messages}
        response = requests.post(f"{BASE_URL}/chat", json=payload, timeout=30)
        
        if response.status_code != 200:
            print(f"✗ {test_name}: HTTP {response.status_code}")
            print(f"  Response: {response.text[:200]}")
            return False
        
        data = response.json()
        
        # Validate response schema
        required_fields = ["reply", "recommendations", "end_of_conversation"]
        for field in required_fields:
            if field not in data:
                print(f"✗ {test_name}: Missing field '{field}'")
                return False
        
        # Validate types
        if not isinstance(data["reply"], str):
            print(f"✗ {test_name}: 'reply' must be string")
            return False
        if not isinstance(data["recommendations"], list):
            print(f"✗ {test_name}: 'recommendations' must be list")
            return False
        if not isinstance(data["end_of_conversation"], bool):
            print(f"✗ {test_name}: 'end_of_conversation' must be bool")
            return False
        
        # Validate recommendations
        for rec in data["recommendations"]:
            if not all(k in rec for k in ["name", "url", "test_type"]):
                print(f"✗ {test_name}: Invalid recommendation format")
                return False
            if not isinstance(rec["test_type"], str) or len(rec["test_type"]) != 1:
                print(f"✗ {test_name}: test_type must be single character")
                return False
        
        print(f"✓ {test_name}")
        print(f"  Reply: {data['reply'][:80]}...")
        print(f"  Recommendations: {len(data['recommendations'])}")
        print(f"  End of conversation: {data['end_of_conversation']}")
        return True
    
    except Exception as e:
        print(f"✗ {test_name}: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("SHL Assessment Agent - Unit Tests")
    print("=" * 60)
    
    # Test 1: Health Check
    print("\n[TEST 1] Health Check")
    health_ok = test_health()
    
    if not health_ok:
        print("\nServer not running. Start with: python -m uvicorn main:app --reload")
        sys.exit(1)
    
    # Test 2: Simple Query (should ask clarifying questions)
    print("\n[TEST 2] Vague Query (should NOT recommend)")
    test_chat(
        [{"role": "user", "content": "I need an assessment."}],
        "Vague Query Test"
    )
    
    # Test 3: Senior Leadership (from C1)
    print("\n[TEST 3] Senior Leadership (C1 - Turn 1)")
    test_chat(
        [{"role": "user", "content": "We need a solution for senior leadership."}],
        "Senior Leadership Turn 1"
    )
    
    # Test 4: Comparison (should use catalog data)
    print("\n[TEST 4] Comparison Test")
    test_chat(
        [
            {"role": "user", "content": "We need a solution for senior leadership."},
            {"role": "assistant", "content": "I'd like to understand more. Is this for selection or development?"},
            {"role": "user", "content": "For selection. What's the difference between OPQ and GSA?"}
        ],
        "Comparison Test"
    )
    
    # Test 5: Refinement (should update recommendations)
    print("\n[TEST 5] Refinement Test")
    test_chat(
        [
            {"role": "user", "content": "Hiring a software engineer, 3 years experience."},
            {"role": "assistant", "content": "What specific skills are you assessing for?"},
            {"role": "user", "content": "Java and system design."},
            {"role": "assistant", "content": "I recommend Java 8 and System Design assessments."},
            {"role": "user", "content": "Actually, add a personality test too."}
        ],
        "Refinement Test"
    )
    
    print("\n" + "=" * 60)
    print("Unit tests complete!")
    print("=" * 60)

