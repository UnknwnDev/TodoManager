from manager.todo import Task
#!/usr/bin/env python3.11 

class Terminal:
    def __init__(self) -> None:
        pass
    
    def __format_task(self, task):
        pass
    
    def __print_task_info(self, task: Task):
        print("="*50)
        print(f"Category            : {task.category}")
        print(f"       Title        : {task.title}")
        print(f"       ID           : {task.id}")
        print(f"       Descr        : {task.description}")
        print(f"       Due          : {task.due_date}")
        print(f"       Remind       : {task.reminder}")
        print(f"       Done         : {task.completed}")
        print("="*50)
    
    def printf(self, tasks):
        for task in tasks:
            self.__print_task_info(task)