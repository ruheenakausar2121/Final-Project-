import json
import os

# --- Constants ---
TASK_FILE = 'tasks.json'
CATEGORIES = ['Work', 'Personal', 'Urgent', 'Shopping', 'Other']

# --- Task Class Definition ---
class Task:
    """Represents a single To-Do item."""
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def __repr__(self):
        """String representation for display."""
        status = "[DONE]" if self.completed else "[TODO]"
        return f"{status} [{self.category}] {self.title}: {self.description}"

# --- File Handling Functions ---

def save_tasks(tasks):
    """Saves the list of Task objects to a JSON file."""
    try:
        # Convert Task objects to dictionaries for JSON serialization
        # The __dict__ attribute holds all instance attributes.
        task_data = [task.__dict__ for task in tasks]
        with open(TASK_FILE, 'w') as f:
            json.dump(task_data, f, indent=4)
        print(f"\n✅ All tasks saved successfully to {TASK_FILE}.\n")
    except IOError as e:
        print(f"\n❌ Error saving tasks: {e}")

def load_tasks():
    """Loads tasks from the JSON file and returns a list of Task objects."""
    tasks = []
    try:
        if not os.path.exists(TASK_FILE):
            print(f"INFO: {TASK_FILE} not found. Starting with an empty list.")
            return []
            
        with open(TASK_FILE, 'r') as f:
            data = json.load(f)
            
            # Reconstruct Task objects from the loaded dictionaries
            for task_data in data:
                # Use dictionary unpacking to initialize the Task object
                # We need to handle the 'completed' field separately if it wasn't in the original constructor
                
                # Pop 'completed' status to ensure Task(**data) works if it has fewer fields
                completed_status = task_data.pop('completed', False) 
                
                try:
                    task = Task(**task_data)
                    task.completed = completed_status
                    tasks.append(task)
                except TypeError:
                    # Handle cases where the loaded data might not match the current Task class structure
                    print(f"WARNING: Could not load task due to structure mismatch: {task_data}")

        print(f"INFO: Loaded {len(tasks)} tasks from {TASK_FILE}.")
    except json.JSONDecodeError:
        print(f"\n❌ Error reading {TASK_FILE}. File is corrupt or empty. Starting new session.")
    except IOError as e:
        print(f"\n❌ Unexpected file error: {e}")
        
    return tasks

# --- Core Application Functions ---

def add_task(tasks):
    """Prompts the user for task details and adds a new Task."""
    print("\n--- ADD NEW TASK ---")
    title = input("Enter task title: ").strip()
    if not title:
        print("❌ Task title cannot be empty.")
        return

    description = input("Enter task description (optional): ").strip()

    print("\nAvailable Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
        
    while True:
        try:
            cat_choice = input(f"Choose a category (1-{len(CATEGORIES)}): ")
            cat_index = int(cat_choice) - 1
            if 0 <= cat_index < len(CATEGORIES):
                category = CATEGORIES[cat_index]
                break
            else:
                print("❌ Invalid category choice. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    new_task = Task(title, description, category)
    tasks.append(new_task)
    print(f"\n✅ Task '{title}' added to category '{category}'.")


def view_tasks(tasks):
    """Displays all tasks, separating them into TODO and DONE sections."""
    if not tasks:
        print("\n📝 Your To-Do list is currently empty!")
        return

    print("\n====================================")
    print("        PERSONAL TO-DO LIST         ")
    print("====================================")
    
    todo_tasks = [t for t in tasks if not t.completed]
    done_tasks = [t for t in tasks if t.completed]
    
    # Display TODO Tasks
    print("\n--- PENDING TASKS ---")
    if todo_tasks:
        for i, task in enumerate(todo_tasks, 1):
            print(f"[{i}] {task}")
    else:
        print("✨ No pending tasks! You are all caught up.")

    # Display Completed Tasks
    if done_tasks:
        print("\n--- COMPLETED TASKS ---")
        for task in done_tasks:
            print(f"  {task}")
    
    print("\n------------------------------------\n")


def select_task_by_index(tasks, prompt_message):
    """Helper function to get a valid index for a non-completed task."""
    todo_tasks = [t for t in tasks if not t.completed]
    if not todo_tasks:
        print("\n❌ No pending tasks to select from.")
        return None

    # Map the index in the filtered list back to the index in the main 'tasks' list
    # This is complex, so let's simplify by using the displayed index only for TODO items
    view_tasks(tasks) 
    
    print("NOTE: You can only select pending tasks by their displayed index.")

    while True:
        try:
            choice_index = input(prompt_message)
            if not choice_index:
                return None
                
            choice_num = int(choice_index)
            if 1 <= choice_num <= len(todo_tasks):
                # We need the actual task object to operate on it
                return todo_tasks[choice_num - 1] 
            else:
                print(f"❌ Invalid number. Please enter a number between 1 and {len(todo_tasks)}.")
        except ValueError:
            print("❌ Invalid input. Please enter a number or press Enter to cancel.")


def mark_completed(tasks):
    """Marks a selected pending task as completed."""
    print("\n--- MARK TASK AS COMPLETED ---")
    task_to_complete = select_task_by_index(tasks, "Enter the number of the task to mark completed (or Enter to cancel): ")
    
    if task_to_complete:
        task_to_complete.mark_completed()
        print(f"\n✅ Task '{task_to_complete.title}' marked as completed!")


def delete_task(tasks):
    """Deletes a selected task (pending or completed)."""
    if not tasks:
        print("\n❌ Task list is empty. Nothing to delete.")
        return

    # For deletion, we show all tasks (including completed ones) with an index
    print("\n--- DELETE TASK ---")
    all_indexed_tasks = [t for t in tasks] # Create a copy for indexing
    
    print("\n--- ALL TASKS FOR DELETION ---")
    for i, task in enumerate(all_indexed_tasks, 1):
        status = "✅" if task.completed else "⏳"
        print(f"[{i}] {status} [{task.category}] {task.title}")
    print("------------------------------------\n")


    while True:
        try:
            choice_index = input("Enter the number of the task to delete (or Enter to cancel): ")
            if not choice_index:
                print("Operation cancelled.")
                return

            choice_num = int(choice_index)
            if 1 <= choice_num <= len(all_indexed_tasks):
                # Get the task object to delete it by reference/value from the main list
                task_to_delete = all_indexed_tasks[choice_num - 1]
                tasks.remove(task_to_delete)
                print(f"\n🗑️ Task '{task_to_delete.title}' deleted successfully.")
                break
            else:
                print(f"❌ Invalid number. Please enter a number between 1 and {len(all_indexed_tasks)}.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred during deletion: {e}")


# --- Main CLI Loop ---

def main():
    """The main entry point for the To-Do List application."""
    print("========================================")
    print("  Welcome to the Personal To-Do List CLI  ")
    print("========================================")
    
    tasks = load_tasks() 

    while True:
        print("\n---------------- MENU ------------------")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit and Save")
        print("----------------------------------------")
        
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("👋 Goodbye! Your progress has been saved.")
            break
        else:
            print("\n❌ Invalid choice. Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()