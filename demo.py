#!/usr/bin/env python3
"""
SHL Assessment Agent - Demo Script
Shows how to interact with the agent programmatically
"""
import requests
import json
import time

BASE_URL = "http://localhost:8000"

def chat_with_agent(messages):
    """Send a message to the agent and return the response."""
    payload = {"messages": messages}
    response = requests.post(f"{BASE_URL}/chat", json=payload)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None

    return response.json()

def demo_conversation():
    """Demonstrate a complete conversation with the agent."""
    print("=" * 60)
    print("SHL Assessment Agent - Demo Conversation")
    print("=" * 60)

    # Check if server is running
    try:
        health = requests.get(f"{BASE_URL}/health")
        if health.status_code != 200:
            print("❌ Server not running. Start with: python start_server.py")
            return
    except:
        print("❌ Cannot connect to server. Start with: python start_server.py")
        return

    print("✅ Server is running\n")

    # Conversation history
    conversation = []

    # Turn 1: Vague query
    print("👤 User: We need a solution for senior leadership.")
    conversation.append({"role": "user", "content": "We need a solution for senior leadership."})

    response = chat_with_agent(conversation)
    if not response:
        return

    print(f"🤖 Agent: {response['reply']}")
    print(f"📋 Recommendations: {len(response['recommendations'])}")
    print(f"🔄 Continue: {not response['end_of_conversation']}\n")

    # Turn 2: Provide more details
    conversation.append({"role": "assistant", "content": response["reply"]})
    print("👤 User: The pool consists of CXOs, director-level positions; people with more than 15 years of experience.")
    conversation.append({"role": "user", "content": "The pool consists of CXOs, director-level positions; people with more than 15 years of experience."})

    response = chat_with_agent(conversation)
    if not response:
        return

    print(f"🤖 Agent: {response['reply']}")
    print(f"📋 Recommendations: {len(response['recommendations'])}")
    if response['recommendations']:
        print("Recommended assessments:")
        for rec in response['recommendations']:
            print(f"  • {rec['name']} ({rec['test_type']})")
    print(f"🔄 Continue: {not response['end_of_conversation']}\n")

    # Turn 3: Confirm selection
    conversation.append({"role": "assistant", "content": response["reply"]})
    print("👤 User: Perfect, that's what we need.")
    conversation.append({"role": "user", "content": "Perfect, that's what we need."})

    response = chat_with_agent(conversation)
    if not response:
        return

    print(f"🤖 Agent: {response['reply']}")
    print(f"📋 Recommendations: {len(response['recommendations'])}")
    print(f"🔄 Continue: {not response['end_of_conversation']}")

    print("\n" + "=" * 60)
    print("Demo completed! 🎉")
    print("=" * 60)

if __name__ == "__main__":
    demo_conversation()