import random

# init
class Task:
    def __init__(self, id, description, assignee, reporter, priority, status):
        self.id = id
        self.description = description
        self.assignee = assignee
        self.reporter = reporter
        self.priority = priority
        self.status = status

# creating 
def create_task(tasks, assignees, reporters, priorities):
    id = len(tasks) + 1
    description = input('Enter task description: ')
    assignee = random.choice(assignees)
    reporter = random.choice(reporters)
    priority = random.choice(priorities)
    status = 'Todo'
    task = Task(id, description, assignee, reporter, priority, status)
    tasks.append(task)
    return task

# deleting 
def remove_task(tasks):
    task_id = int(input('Enter task ID to remove: '))
    tasks = [task for task in tasks if task.id != task_id]

# modify 
def move_task(tasks):
    task_id = int(input('Enter task ID to move: '))
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        new_status = input('Enter new status: ')
        task.status = new_status

# display
def display_tasks(tasks):
    print('Kanban Board')
    for status in ['Todo', 'In Progress', 'Done']:
        print(f'{status}:')
        for task in tasks:
            if task.status == status:
                print(f'{task.id}. {task.description} (Assignee: {task.assignee}, Reporter: {task.reporter}, Priority: {task.priority}, Status: {task.status})')

# Main
def main():
    tasks = []
    assignees = ['John', 'Jane', 'Mike']
    reporters = ['Alex', 'Bob', 'Charlie']
    priorities = ['High', 'Medium', 'Low']
    while True:
        display_tasks(tasks)
        action = input('Action (t=create task, r=remove task, m=move task, q=quit): ').lower()
        if action == 'q':
            break
        elif action == 't':
            create_task(tasks, assignees, reporters, priorities)
        elif action == 'r':
            remove_task(tasks)
        elif action == 'm':
            move_task(tasks)

if __name__ == '__main__':
    main()
