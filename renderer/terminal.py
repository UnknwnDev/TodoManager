#!/usr/bin/env python3.11 
from manager.todo import Task, TodoList
import dateparser
from datetime import datetime, timedelta

class Terminal:
    def __init__(self) -> None:
        self.__quit = ['q', 'quit', 'exit']
    
    def __format_task(self, task):
        pass
    
    def __format_date(self, date):
        today = datetime.today().date()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)

        if date.date() == today:
            return "Today"
        elif date.date() == yesterday:
            return "Yesterday"
        elif date.date() == tomorrow:
            return "Tomorrow"
        else:
            return date.strftime("%A, %B %d, %Y")
    
    def __print_task_info(self, task: Task):
        
        if task.category:
            print(f"Category            : {task.category}")
        if task.title:
            print(f"       Title        : {task.title}")
        if task.id:
            print(f"       ID           : {task.id}")
        if task.description:
            print(f"       Descr        : {task.description}")
            
        if task.due_date:
            parsed_date = dateparser.parse(task.due_date)
            human_readable = self.__format_date(parsed_date)
            print(f'       Due          : {human_readable}')
            
        if task.reminder:
            parsed_date = dateparser.parse(task.due_date)
            human_readable = self.__format_date(parsed_date)
            print(f'       Remind       : {human_readable}')
            
        print(f"       Done         : {task.completed}")
        
                    
    def printf(self, tasks):
        print("="*50)
       
        for task in tasks:
            print("-"*50)      
            self.__print_task_info(task)      
        
        print('-'*50)      
        print("="*50)
        

    @property     
    def quit(self):
        return self.__quit

class CustomTerminal(Terminal):
    def __init__(self, task_manager) -> None:
        super().__init__()
        self.task_manager = task_manager

    def start(self):
        while True:
            user_input = input("Enter command: ").strip().lower()
            if user_input in self.quit:
                print("Exiting...")
                break
            elif user_input.startswith("show"):
                if user_input in ["show", "show all"]:
                    for list in self.task_manager.get_all_tasks():
                        print(f"Showing: {list.file_name}")
                        self.printf(list.tasks)
                else:
                    category = user_input.split(maxsplit=1)[-1].strip('"')
                    self.printf(self.task_manager.get_tasks_by_category(category))
            elif user_input == "create task":
                self.create_task()
            elif user_input == "save task":
                self.save_task()
            else:
                print("Invalid command.")

    def create_task(self):
        category = input("Enter category: ")
        title = input("Enter title: ")
        description = input("Enter description (optional): ")
        due_date = input("Enter due date (optional): ")
        reminder = input("Enter reminder (optional): ")
        
        due_date = dateparser.parse(due_date)
        reminder = dateparser.parse(reminder)
        
        self.new_list = TodoList(category)
        self.new_list.create_task(title, description, False, due_date, reminder)
        self.save_task()
        print("Task created successfully.")

    def save_task(self):
        # Save tasks if necessary
        self.new_list.save_tasks()
        print("Tasks saved successfully.")