import ai_handler
import file_handler
from enum import Enum

class Status(Enum):
    STARTED = "STARTED"
    BROKEN = "BROKEN"
    DONE = "DONE"



if __name__ == "__main__":
    config = file_handler.read_yaml_file("config.yaml")

    project_input = input("> ")
    try:
        breakdown = ai_handler.generate_task_plan(project_input, model="deepseek-r1")
        print("\n--- Generated Task Plan ---\n")
        print(breakdown)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        
    file_handler.create_json_file(breakdown)

    task_plan = file_handler.read_json_file(config["task_plan_json_fp"])
    for task in task_plan:
        #add to memory started id
        breakpoint()
        if not task in file_handler.read_yaml_file(config["memory_fp"]):
            task["status"] = Status.STARTED

        file_handler.write_to_yaml_file(task, config["memory_fp"])
        #check what type of task it is - creation of file structure or code, or nothing actionable like planning
        
        #if file creation task, create a prompt requesting a terminal command for file structure build
            #run in safe environment or do not allow terminal access.
        
        pass

    breakpoint()