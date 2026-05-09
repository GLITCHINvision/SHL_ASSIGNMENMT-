import subprocess
import time
import requests
import json

def run_tests():
    print("Starting SHL Assessment Agent Verification...")
    
    # 1. Health Check
    try:
        health = requests.get("http://localhost:8000/health")
        print(f"Health Check: {health.json()}")
    except:
        print("Server not found. Please run 'python main.py' first.")
        return

    # 2. Run Comprehensive Traces
    print("\n--- Running all 10 Conversation Traces ---")
    print("Note: Adding 5s delay between requests to respect Free Tier TPM limits.")
    
    from test_all_traces import scenarios, run_scenario
    
    for i, (name, hist) in enumerate(scenarios.items()):
        run_scenario(f"[{i+1}/10] {name}", hist)
        time.sleep(5) 

if __name__ == "__main__":
    run_tests()
