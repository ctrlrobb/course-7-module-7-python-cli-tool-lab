import argparse
from models import Task, User

# Global dictionary to store users and their tasks
users = {}

def add_task(args):
    # Check if the user exists, if not, create one
    if args.user not in users:
        users[args.user] = User(args.user)
    
    user = users[args.user]
    
    # Create a new Task and add it to the user
    new_task = Task(args.title)
    user.add_task(new_task)

def complete_task(args):
    # Look up the user by name
    user = users.get(args.user)
    
    if not user:
        print(f"❌ Error: User '{args.user}' not found.")
        return

    # Look up the task by title
    task = user.get_task_by_title(args.title)
    
    if task:
        task.complete()
    else:
        print(f"❌ Error: Task '{args.title}' not found for user {args.user}.")

# CLI entry point (rest of the code remains the same)
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()