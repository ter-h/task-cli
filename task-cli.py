#!/usr/bin/env python3
import argparse
from TaskManager import TaskManager
from TaskNotFoundError import TaskNotFoundError

def main():
    parser = argparse.ArgumentParser(
        prog="task-cli",
        description="CLI to manage tasks"
    )
    sub = parser.add_subparsers(dest="command")

    # Add
    add_p = sub.add_parser("add", help="Add a new task")
    add_p.add_argument("description")

    # Update
    update_p = sub.add_parser("update", help="Update task description")
    update_p.add_argument("id", type=int)
    update_p.add_argument("description")

    # Delete
    delete_p = sub.add_parser("delete", help="Delete a task")
    delete_p.add_argument("id", type=int)

    # Mark in-progress
    mark_ip_p = sub.add_parser("mark-in-progress", help="Mark task as in-progress")
    mark_ip_p.add_argument("id", type=int)

    # Mark done
    mark_done_p = sub.add_parser("mark-done", help="Mark task as done")
    mark_done_p.add_argument("id", type=int)

    # List tasks
    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument("status", nargs="?", help="Optional status filter")

    args = parser.parse_args()
    tasks = TaskManager()  # automatically loads file

    try:
        if args.command == "add":
            t = tasks.task_add(args.description)
            print(f"Task added successfully (ID: {t.id})")

        elif args.command == "update":
            tasks.task_update(args.id, args.description)
            print("Task updated.")

        elif args.command == "delete":
            tasks.task_delete(args.id)
            print("Task deleted.")

        elif args.command == "mark-in-progress":
            tasks.task_mark_in_progress(args.id)
            print("Marked in progress.")

        elif args.command == "mark-done":
            tasks.task_mark_done(args.id)
            print("Marked done.")

        elif args.command == "list":
            for t in tasks.task_list(args.status):
                print(f"[{t.id}] {t.status} - {t.description}")

        else:
            parser.print_help()

    except TaskNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
