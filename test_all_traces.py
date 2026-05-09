import requests
import json

BASE_URL = "http://localhost:8000"

def run_scenario(name, messages):
    print(f"\n{'='*20} {name} {'='*20}")
    payload = {"messages": messages}
    try:
        response = requests.post(f"{BASE_URL}/chat", json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"Agent Reply: {data['reply']}")
            print(f"Recommendations ({len(data['recommendations'])}):")
            for rec in data['recommendations']:
                print(f" - [{rec['test_type']}] {rec['name']}")
            print(f"End of Conversation: {data['end_of_conversation']}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Connection Error: {e}")

scenarios = {
    "C1: Senior Leadership": [
        {"role": "user", "content": "We need a solution for senior leadership."},
        {"role": "assistant", "content": "Happy to help narrow that down. Who is this meant for?"},
        {"role": "user", "content": "The pool consists of CXOs, director-level postions; people with more than 15 years of experience."},
        {"role": "assistant", "content": "For such roles, the OPQ32r is the right instrument — it measures 32 workplace behaviour dimensions including strategic thinking, influencing style, and leadership. One question before I commit to a report format:is this for a newly created position, or developmental feedback for an executive already in role?"},
        {"role": "user", "content": "Selection — comparing candidates against a leadership benchmark."}
    ],
    "C2: Senior Rust Engineer": [
        {"role": "user", "content": "I'm hiring a senior Rust engineer for high-performance networking infrastructure. What assessments should I use?"},
        {"role": "assistant", "content": "SHL's catalog doesn't currently include a Rust-specific knowledge test. The closest fit for a senior IC is Smart Interview Live Coding — an adaptive live-coding interview where your panel can frame Rust-specific tasks directly. Linux Programming covers systems depth, and Networking and Implementation covers the infrastructure dimension. Want me to build a shortlist from these?"},
        {"role": "user", "content": "Yes, go ahead. Should I also add a cognitive test for this level?"}
    ],
    "C3: Contact Centre Agents": [
        {"role": "user", "content": "We're screening 500 entry-level contact centre agents. Inbound calls, customer service focus. What should we use?"},
        {"role": "assistant", "content": "Before I shape the stack — what language are the calls in? That drives which spoken-language screen we use."},
        {"role": "user", "content": "English."},
        {"role": "assistant", "content": "SVAR has four English variants in the catalog: US, UK, Australian, and Indian accent. The choice matters because the screen is calibrated for the accent your callers will hear. Which fits your operation?"},
        {"role": "user", "content": "US."}
    ],
    "C4: Graduate Financial Analysts": [
        {"role": "user", "content": "Hiring graduate financial analysts — final-year students, no work experience. We need numerical reasoning and a finance knowledge test."},
        {"role": "assistant", "content": "For graduate-level financial analysts: [Recommended stack...]."},
        {"role": "user", "content": "Good. Can you also add a situational judgement element — work-context decision making for graduates?"}
    ],
    "C5: Sales Re-skilling": [
        {"role": "user", "content": "As part of our restructuring and annual talent audit, we need to re-skill our Sales organization. What solutions do you recommend?"},
        {"role": "assistant", "content": "For a compact audit-and-development stack..."},
        {"role": "user", "content": "What’s the difference between OPQ and OPQ MQ Sales Report?"}
    ],
    "C6: Plant Operators (Safety)": [
        {"role": "user", "content": "We're hiring plant operators for a chemical facility. Safety is absolute top priority — reliability, procedure compliance, never cutting corners. What do you recommend?"},
        {"role": "assistant", "content": "For a safety-critical frontline role..."},
        {"role": "user", "content": "What's the difference between the DSI and the Safety & Dependability 8.0?"}
    ],
    "C7: Bilingual Healthcare Admin": [
        {"role": "user", "content": "We're hiring bilingual healthcare admin staff in South Texas — they handle patient records and need to be assessed in Spanish. HIPAA compliance is critical. What assessments work?"},
        {"role": "assistant", "content": "There's a real catalog constraint here... Which fits your candidate pool better?"},
        {"role": "user", "content": "They're functionally bilingual — English fluent for written work. Go with the hybrid."}
    ],
    "C8: Quick Admin Screen": [
        {"role": "user", "content": "I need to quickly screen admin assistants for Excel and Word daily."},
        {"role": "assistant", "content": "For a quick knowledge check..."},
        {"role": "user", "content": "In that case, I am OK with adding a simulation - we want to capture the capabilties."}
    ],
    "C9: Senior Full-Stack Engineer": [
        {"role": "user", "content": "Here's the JD for an engineer we need to fill. Can you recommend an assessment battery? Senior Full-Stack Engineer — 5+ years across Core Java, Spring, REST API design, Angular, SQL, AWS, and Docker."},
        {"role": "assistant", "content": "That JD spans seven distinct areas... Is this a backend-leaning role or a frontend-heavy role?"},
        {"role": "user", "content": "Backend-leaning. Day-one priorities are Core Java and Spring; SQL is constant. Angular is occasional — they'd review frontend PRs but not own features."}
    ],
    "C10: Graduate Trainee (Removal)": [
        {"role": "user", "content": "We run a graduate management trainee scheme. We need a full battery — cognitive, personality, and situational judgement. All recent graduates."},
        {"role": "assistant", "content": "For a graduate management trainee battery..."},
        {"role": "user", "content": "But can you remove the OPQ32r and replace it with something shorter? Candidates complain it takes too long."}
    ]
}

if __name__ == "__main__":
    print("Starting Comprehensive Trace Verification...")
    print("Note: Ensure the server is running at http://localhost:8000 and GEMINI_API_KEY is set.")
    for name, hist in scenarios.items():
        run_scenario(name, hist)
