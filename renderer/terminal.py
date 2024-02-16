#!/usr/bin/env python3.11 
import dateparser
from manager.todo import Task, TodoList
from datetime import datetime, timedelta

class Terminal:
    def __init__(self) -> None:
        self.__quit = ['q', 'quit', 'exit']
        
    def __format_date(self, date: datetime) -> str:
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
    
    def print_task_info(self, task: Task):
        
        if task.category:
            print(f"Category            : {task.category.capitalize()}")
        if task.title:
            print(f"       Title        : {task.title.capitalize()}")
        if task.id:
            print(f"       ID           : {task.id}")
        if task.description:
            print(f"       Descr        : {task.description.capitalize()}")
            
        if task.due_date:
            parsed_date = dateparser.parse(task.due_date)
            human_readable = self.__format_date(parsed_date)
            print(f'       Due          : {human_readable}')
            
        if task.reminder:
            parsed_date = dateparser.parse(task.reminder)
            human_readable = self.__format_date(parsed_date)
            print(f'       Remind       : {human_readable}')
            
        print(f"       Done         : {task.completed}")
        
                    
    def printf(self, tasks):
        print("="*50)
       
        for task in tasks:
            print("-"*50)      
            self.print_task_info(task)      
        
        print('-'*50)      
        print("="*50)
        

    @property     
    def quit(self):
        return self.__quit

class CustomTerminal(Terminal):
    def __init__(self, manager) -> None:
        super().__init__()
        from manager.manager import Manager
        self.manager:Manager = manager

    def start(self):
        '''This function takes user input and performs various commands based on the input, such as showing
        tasks, creating tasks, deleting tasks, and selecting/deselecting categories.
        
        '''
        while True:
            user_input = input("Enter command: ").strip().lower()
            
            # Commands
            if user_input in self.quit:
                print("Exiting...")
                break
           
            elif user_input.startswith("show"):
                print("="*50)
                if user_input in ["show", "show all"]:
                    if not self.manager.selected_category:
                        for list in self.manager.get_all_tasks():
                            print(f"Showing: {list.file_name}")
                            self.printf(list.tasks)
                    else:
                        print("**Note make sure to run dsel if not expected out come**")
                        print(f"Showing: {self.manager.selected_category.capitalize()}")
                        self.printf(self.manager.get_tasks_by_category(self.manager.selected_category))
                        
                else:
                    category = user_input.split(maxsplit=1)[-1].strip('"').lower()
                    print(f"Showing: {category.capitalize()}")
                    self.printf(self.manager.get_tasks_by_category(category))
           
            # Task Managing
            elif user_input.startswith(("create task", "create")):
                self.create_task() 
 
            elif user_input.startswith(("delete task", "remove task", "remove", "delete")):
                task = user_input.split(maxsplit=1) # Gets task title/id chosen
                
                # User dummy check
                if (len(task) < 2):
                    if len(task) > 1 and task[1].startswith("task"):
                        print("Please enter a task to remove. ( delete/remove task Clean )")
                    else:
                        if len(task) == 1:
                            print("Please enter a task to remove. ( delete/remove Clean )")
                        else:
                            print(task[-1].lower())
                            self.remove_task(task[-1].strip('"').lower())
                        
                else:
                    self.remove_task(task[-1].strip('"').lower())
            
            # Selectors
            elif user_input.startswith(('sel', 'select')):
                category = user_input.split(maxsplit=1)
                
                # User dummy check
                if (len(category) < 2):
                    print("Please enter a task to remove. ( sel/select chores )")
                else:
                    category = category[-1].strip('"').lower()
                    print(f"You have selected {category.capitalize()}")
                    self.manager.selected_category = category
                
            elif user_input.startswith(('dsel', 'deselect', 'de-select')):
                print(f"You have de-selected {self.manager.selected_category.capitalize()}")
                self.manager.selected_category = None
            
            else:
                print("Invalid command.")
        
        print(end='\r')

    def show_task(self, task):
        '''The function "show_task" takes a task as input and prints its information.
        
        Parameters
        ----------
        task
            The task parameter is the task object that you want to display information for.
        
        '''
        self.print_task_info(task)

    def create_task(self):
        '''The function `create_task` creates a new task with user-provided inputs and saves it to a todo
        list.
        
        '''
        
        if self.manager.selected_category:
            category = self.manager.selected_category
            print(f"Current Category: {category.capitalize()}")
        else:
            category = input("Enter category: ")
            
        title = input("Enter title: ")
        description = input("Enter description (optional): ")
        due_date = input("Enter due date (optional): ")
        reminder = input("Enter reminder (optional): ")
        
        due_date = dateparser.parse(due_date)
        reminder = dateparser.parse(reminder)
        
        self.new_list = TodoList(category)
        self.new_list.create_task(title, description, False, due_date, reminder)
        self.new_list.save_tasks()
        print("Task created successfully.")                
    
    def remove_task(self, target:str):
        '''The function removes a task from a manager and prints a success message if the task is found,
        otherwise it prints a failure message.
        
        Parameters
        ----------
        target : str
            The "target" parameter is a string that represents the task that needs to be removed.
        
        '''
        if self.manager.find_task(target) == 0:
        # print(target)
            print("Tasks removed successfully.")
        else:
            print("Faild to remove task.")
            
        