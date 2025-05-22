import subprocess
import file_handler

config = file_handler.read_yaml_file("config.yaml")

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

def build_structured_prompt(description):
    return file_handler.read_yaml_file(config["prompts_fp"])["task_plan_prompt"] 