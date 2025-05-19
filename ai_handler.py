import subprocess
import json

def ollama_prompt(prompt, model="llama2"):
    # Run the ollama CLI command with prompt input
    process = subprocess.run(
        ["ollama", "run", model, prompt],
        capture_output=True,
        text=True,
        encoding="utf-8"

    )
    breakpoint()
    if process.returncode != 0:
        raise Exception(f"Ollama CLI error: {process.stderr}")
    return process.stdout.strip()

import subprocess

def generate_task_plan(description, model="llama2"):
    system_prompt = f"""
You are a highly skilled software architect and project planner.

Your task is to take a short project description and deconstruct it into extremely detailed, step-by-step tasks required to fully build the project, suitable for a developer or automation system to follow without ambiguity.

Instructions:
- The project must be built using the Python programming language
- Interpret the project description with precision.
- Break down the implementation into very small, atomic tasks.
- Include all necessary setup, tools, and environments (e.g., language setup, framework installation, repo creation, etc.).
- Ensure the steps follow a logical and efficient sequence.
- Clearly label major phases (e.g., Setup, Development, Integration, Testing, Deployment).
- Number every task or step.
- Avoid high-level generalizations—be as specific and actionable as possible.
- Output in clean, readable Markdown.

Project Description:
{description}
"""

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

