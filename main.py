import ai_handler

if __name__ == "__main__":
    project_input = input("> ")
    try:
        breakdown = ai_handler.generate_task_plan(project_input)
        print("\n--- Generated Task Plan ---\n")
        print(breakdown)
    except Exception as e:
        print(f"\n[!] Error: {e}")
    response = ai_handler.ollama_prompt(breakdown)
    print("Ollama response:")
    print(response)
    print("Enter a short description of your project:")


