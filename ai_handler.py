import subprocess

def generate_task_plan(description, model="llama2"):
    system_prompt = build_structured_prompt(description)
    
    print("[*] Sending request to Ollama...")

    result = subprocess.run(
        ["ollama", "run", model, system_prompt],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    if result.returncode != 0:
        raise RuntimeError(f"Ollama error:\n{result.stderr}")

    return result.stdout.strip()

if __name__ == "__main__":
    print("Enter a short description of your project:")
    project_input = input("> ")

    try:
        breakdown = generate_task_plan(project_input)
        print("\n--- Generated Task Plan ---\n")
        print(breakdown)
    except Exception as e:
        print(f"\n[!] Error: {e}")

def build_structured_prompt(description):
    return f"""
You are an expert Python software architect.

Your task is to take the following project description and break it down into a list of atomic, actionable development steps, each suitable to be used as an individual prompt for a code-generation AI.

---

🔧 Requirements:

- All steps must be relevant to building the project using Python.
- Output must follow the exact JSON format shown below. your answer should only contain the json structure so it can be sent directly to a json file.
- Every step must contain:
  - "id" (integer step number)
  - "phase" (e.g., "Setup", "Backend", "Frontend", "Integration", "Testing", "Deployment")
  - "title" (short task name)
  - "description" (detailed instruction suitable to generate Python code)

---

📦 Example Output Format:

```json
[
  {{
    "id": 1,
    "phase": "Setup",
    "title": "Create project directory",
    "description": "Create a new folder named 'image_app' and initialize a Git repository inside it."
  }},
  {{
    "id": 2,
    "phase": "Setup",
    "title": "Initialize virtual environment",
    "description": "Use Python's built-in venv module to create and activate a virtual environment."
  }}
]

IMPORTANT! 
do not add anything else to your response except the json. your response will be directly sent to a JSON file.
"""