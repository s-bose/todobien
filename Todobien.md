
# Available commands

| Command | flag            | description                 | example                                            |
| ------- | --------------- | --------------------------- | -------------------------------------------------- |
| `help`  | None            | show all available commands | `todo help`                                        |
| `add`   | -p --path       | add a resource              | `todo add`                                         |
|         |                 | add a project               | `todo add`                                         |
|         |                 | add a task for a project    | `todo add -p <project_id>`                         |
|         |                 | add a subtask for a task    | `todo add -p <project_id>/<task_id>`               |
| `view`  | -p --path --all | view all projects           | `todo view`                                        |
|         |                 | view a project details      | `todo view -p <project_id>`                        |
|         |                 | view a task details         | `todo view -p <project_id>/<task_id>`              |
|         |                 | view a subtask details      | `todo view -p <project_id>/<task_id>/<subtask_id>` |
| `edit`    | -p --path       | edit a project              | `todo edit -p <project_id>`                        |
|         |                 | edit a task details         | `todo edit -p <project_id>/<task_id>`              |
|         |                 | edit a subtask details      | `todo edit -p <project_id>/<task_id>/<subtask_id>` |
| `delete`  | -p --path       | delete a project            | `todo delete -p <project_id>`                        | 
|         |                 | delete a task details         | `todo delete -p <project_id>/<task_id>`              |
|         |                 | delete a subtask details      | `todo delete -p <project_id>/<task_id>/<subtask_id>` |



## Flags

- `view -all` - show all details for a project / task / subtask.
	- Project will show all its constituent tasks and their status and %-completion.
	- Task will show all its constituent subtasks their %-completion.
	- Subtask will show all its constituent sub-subtasks and their %-completion.
- `view --all --extended` - show a nested structure of a project | task details (not available for subtasks).
	- Depth level == 3 for extended views. Meaning for Projects it will be `project -> task -> subtask` being shown, for tasks it will be `task -> subtask -> sub-subtask`
- `stat` - show a project-wide statistics and %-completion, kinda like a dashboard
	- `stat --minimal` - show minimal info
	- `stat --extended` - show extended info
- `view | edit | add | delete -p (--path)` - `-p` or `--path` is used to specify a nested path to a project / task / subtask that we can view / edit / add / delete.

### Shortcuts
- `set [-xX -S -E -D] <path>` - path can be a valid path to any resource.
	- `-xX --priority` ==> *set priority of the resource.*
	**Example**:
		1. `set -X todobien/TDB-001 MEDIUM` 
		2. `set -x todobien/TDB-001 1`
	"-x" to use numeric priority values, "-X" to use fullnames, "--priority" for verbose.
	**Available options:**
		1. LOW
		2. MEDIUM
		3. HIGH
		4. URGENT

	- `-sS --status` ==> *set status of the resource.*
	**Example**:
		1. `set -S xyz/X-001 IN_PROGRESS`
		2. `set -s xyz 1`
	"-s" = numeric value, "-S" = fullnames, "--status" = verbose
	**Available options:**
		1. TODO
		2. IN_PROGRESS
		3. PAUSED
		4. BACKLOG
		5. DONE
		6. CANCELED

	. `-E --estimate` ==> *put your estimates for a resource completion.*
	**Example**:
		1. `set -E xyz 6d`
		2. `set --estimate xyz 6d3h`
	**Available options:**
		1. d - day
		2. mo - month
		3. y - year
		4. h - hour
		5. mi - minute
		6. s - second

	- `-D --due` ==> *put your due date for the completion of resource*
	**Example**:
		1. `set -D xyz/ID-001 2023-02-01`
	**Available options:**
	0. datetime format - yyyy-mm-dd

	- 