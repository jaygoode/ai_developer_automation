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

if __name__ == "__main__":
    prompt = "Write a haiku about the sea"
    response = ollama_prompt(prompt)
    print("Ollama response:")
    print(response)