import ai_handler
import file_handler
from enum import Enum

class Status(Enum):
    STARTED = "STARTED"
    BROKEN = "BROKEN"
    DONE = "DONE"



if __name__ == "__main__":
    config = file_handler.read_yaml_file("config.yaml")
    memory = file_handler.read_yaml_file(config["memory_fp"])
    task_plan = file_handler.read_json_file(config["task_plan_json_fp"])
    model="deepseek-r1"
    #take full task_plan and enums, and let ai set task type for 
    task["task_type"] = ai_handler.prompt_ai(project_input, model=model) #should type actually be set in first prompt? prob not.
    project_input = input("> ")
    try:
        breakdown = ai_handler.prompt_ai(project_input, model=model)
        print("\n--- Generated Task Plan ---\n")
        print(breakdown)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        
    file_handler.create_json_file(breakdown)

    for task in task_plan:
        #make sure we have a memory and status for task
        if not task.get("status"):
            task["status"] = Status.STARTED.value

        task_memory = {task["id"]:{"status": task["status"]}}
        if not memory or task["id"] not in memory:
            file_handler.write_to_yaml_file(task_memory, config["memory_fp"])
        
        breakpoint()
        #check what type of task it is - creation of file structure or code, or nothing actionable like planning
        #we need a context text from ai to summarize the task, and maybe send all descriptions from all tasks ai can understand what file structure needed
        if not task.get("task_type"):
            continue

        #if file creation task, create a prompt requesting a terminal command for file structure build
            #run in safe environment or do not allow terminal access.
        
