#!/usr/bin/env python3

import argparse
from TaskNotFoundError import TaskNotFoundError
from TaskManager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="Task CLI")
    sub = parser.add_subparsers(dest="command")

    add_p = sub.add_parser("add")
    add_p.add_argument("description")

    update_p = sub.add_parser("update")
    update_p.add_argument("id", type=int)
    update_p.add_argument("description")

    delete_p = sub.add_parser("delete")
    delete_p.add_argument("id", type=int)

    mark_ip_p = sub.add_parser("mark-in-progress")
    mark_ip_p.add_argument("id", type=int)

    mark_done_p = sub.add_parser("mark-done")
    mark_done_p.add_argument("id", type=int)

    list_p = sub.add_parser("list")
    list_p.add_argument("status", nargs="?")

    args = parser.parse_args()
    tasks = TaskManager()
    tasks.load_from_file()
    try:
        if args.command == "add":
            t = tasks.task_add(args.description)
            tasks.save_to_file()
            print(f"Task added successfully (ID: {t.id})")

        elif args.command == "update":
            tasks.task_update(args.id, args.description)
            tasks.save_to_file()
            print("Task updated.")

        elif args.command == "delete":
            tasks.task_delete(args.id)
            tasks.save_to_file()
            print("Task deleted.")

        elif args.command == "mark-in-progress":
            tasks.task_mark_in_progress(args.id)
            tasks.save_to_file()
            print("Marked in progress.")

        elif args.command == "mark-done":
            tasks.task_mark_done(args.id)
            tasks.save_to_file()
            print("Marked done.")

        elif args.command == "list":
            for t in tasks.task_list(args.status):
                print(f"[{t.id}] {t.status} - {t.description}")
    except TaskNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
