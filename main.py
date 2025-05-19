import ai_handler
import file_handler

if __name__ == "__main__":
    project_input = input("> ")
    try:
        breakdown = ai_handler.generate_task_plan(project_input, model="deepseek-r1")
        print("\n--- Generated Task Plan ---\n")
        print(breakdown)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        
    file_handler.create_json_file(breakdown)



