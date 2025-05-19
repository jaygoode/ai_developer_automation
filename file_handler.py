import json
import re

def create_json_file(text):
    pattern = re.compile(r'\[.*?\]', re.DOTALL)
    match = pattern.search(text)
    if match:
        json_str = match.group(0)

        # Load the JSON string to Python object
        data = json.loads(json_str)

        # Save to a JSON file
        with open('task_plan.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        print("JSON successfully extracted and saved to 'task_plan.json'")
    else:
        print("No JSON found in the text.")


def read_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data