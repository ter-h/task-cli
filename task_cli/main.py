#!/usr/bin/env python3
import argparse
from task_cli.TaskManager import TaskManager
from task_cli.TaskNotFoundError import TaskNotFoundError
from tabulate import tabulate

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
    mark_todo = sub.add_parser("mark-todo", help="Mark task as todo")
    mark_todo.add_argument("id", type=int)

    # Mark in-progress
    mark_ip_p = sub.add_parser("mark-in-progress", help="Mark task as in-progress")
    mark_ip_p.add_argument("id", type=int)

    # Mark done
    mark_done_p = sub.add_parser("mark-done", help="Mark task as done")
    mark_done_p.add_argument("id", type=int)

    # List tasks
    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument("status", nargs="?", help="Optional status filter")
    list_p.add_argument(
        "-s", "--sort",
        choices=["status", "createdAt", "name", "lastUpdated", "id"],
        help="Sort tasks by status, date, id, or name"
    )

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
        
        elif args.command == "mark-todo":
            tasks.task_mark_todo(args.id)
            print("Marked todo")

        elif args.command == "mark-in-progress":
            tasks.task_mark_in_progress(args.id)
            print("Marked in progress.")

        elif args.command == "mark-done":
            tasks.task_mark_done(args.id)
            print("Marked done.")

        elif args.command == "list":
            task_list = list(tasks.task_list(args.status))

            if args.sort == "status":
                task_list.sort(key=lambda t: t.status)

            elif args.sort == "date":
                task_list.sort(key=lambda t: t.createdAt)

            elif args.sort == "name":
                task_list.sort(key=lambda t: t.description.lower())
            
            elif args.sort == "id":
                task_list.sort(key=lambda t: t.id)

            rows = [
                [
                    t.id,
                    t.status,
                    t.description,
                    t.createdAt.strftime("%Y-%m-%d %H:%M"),
                    t.updatedAt.strftime("%Y-%m-%d %H:%M"),
                ]
                for t in task_list
            ]

            print(tabulate(
                rows,
                headers=["ID", "Status", "Description", "Created At", "Last Updated"],
                tablefmt="grid"
            ))

        else:
            parser.print_help()

    except TaskNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
