# Task Cli - TODO App



## Description

This is a lightweight command-line interface (CLI) application for task management. It will allow you to add, update, delete, and track tasks directly from terminal.

--- 

## Features
- **Add a Task** → Create tasks with descriptions. Each task gets a unique ID and a default `todo` status.
- **Update a Task** → Modify the description or status of a task.
- **Mark as In-Progress** → Quickly change a task’s status to `in-progress`.
- **Mark as Done** → Quickly change a task’s status to `done`.
- **Delete a Task** → Remove tasks by their ID.
- **List Tasks** → Display all tasks or filter them by:
  - **status**: `todo`, `in-progress`, `done`, or `all`

  ## Installation

  Can install Task Cli directly from GitHub:

  ```bash
  pip install git+https://github.com/ter-h/task-cli.git
  ```

  ## Usage

  ```bash
$ taskly add description

$ taskly update [-d description] [-s {done,in-progress,todo}] id

$ taskly mark-done id

$ taskly mark-in-progress id

$ taskly delete id

$ taskly list {todo, in-progress, done} [-s {id, status, createdAt, updatedAt, description}]
```
