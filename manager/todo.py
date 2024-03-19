#!/usr/bin/env python3.11 

from datetime import datetime
from typing import List, Type
import json

# The Task class is a basic template for creating tasks.
class Task(object):
    def __init__(self) -> None:
       self.__completed: bool = False
       self.__title: str = ""
       self.__description: str = ""
       self.__due_date:datetime = None
       self.__category: str = ""
       
       # Do these later not now
       self.__reminder:datetime = None
       self.__id: int = None 
    
    
    def build_task(self, task_data:dict, file_name: str):
        '''The function "build_task" takes in a dictionary of task data and assigns the values to the
        corresponding attributes of the object.
        
        Parameters
        ----------
        task_data : dict
            The `task_data` parameter is a dictionary that contains the data needed to build a task. It
        should have the following keys:
        
        Returns
        -------
            The `self` object is being returned.
        
        '''
        
        # BUILD FAIL CHECKS FOR THE ITEMS
        try:
            self.__title = task_data['title']
            self.__description = task_data['description']
            self.__completed = task_data['complete']
            self.__due_date = task_data['due-date']
            self.__id = task_data['id']
            self.__reminder = task_data['reminder']
            self.category = file_name
            return self
        except Exception as e:
            print(e)
    
    @property
    def completed(self) -> bool:
        '''The `is_completed` function is a property that returns the value of the private `__completed`
        attribute.
        
        Returns
        -------
            The method is returning the value of the private attribute "__completed".
        
        '''
        return self.__completed
    
    @completed.setter
    def completed(self, flag:bool):
        '''The above function is a setter method that sets the value of the private attribute "__completed"
        to the value of the "flag" parameter.
        
        Parameters
        ----------
        flag : bool
            The flag parameter is a boolean value that indicates whether the task is completed or not. If
        flag is True, it means the task is completed. If flag is False, it means the task is not
        completed.
        
        '''
        self.__completed = flag
    
    @property
    def category(self) -> str:
        '''The `category` function is a property decorator that returns the value of the private `__category`
        attribute.
        
        Returns
        -------
            The category of the task.
        
        '''
        return self.__category

    @category.setter
    def category(self, new_category: str):
        '''The above function is a setter method for the "category" attribute of a class.
        
        Parameters
        ----------
        new_category : str
            The new category that will be assigned to the task. It should be a string.
        
        '''
        self.__category = new_category
    
    @property
    def title(self) -> str:
        '''The `title` function is a property decorator that returns the value of the private `__title`
        attribute.
        
        Returns
        -------
            The title of the task.
        
        '''
        return self.__title

    @title.setter
    def title(self, new_title: str):
        '''The above function is a setter method for the "title" attribute of a class.
        
        Parameters
        ----------
        new_title : str
            The new title that will be assigned to the task. It should be a string.
        
        '''
        self.__title = new_title
    
    @property
    def description(self) -> str:
        '''The `description` function is a property decorator that returns the value of the private
        `__description` attribute.
        
        Returns
        -------
            The description of the task.
        
        '''
        return self.__description

    @description.setter
    def description(self, new_description: str):
        '''The function sets the description attribute of an task to a new value.
        
        Parameters
        ----------
        new_description : str
            The new description that will be assigned to the task's description attribute. It is of type
        str, which means it should be a string.
        
        '''
        self.__description = new_description
        
    @property
    def due_date(self) -> datetime:
        '''The above function is a property decorator that returns the value of the private attribute
        __due_date.
        
        Returns
        -------
            The due_date property is returning the value of the __due_date attribute.
        
        '''
        return self.__due_date

    @due_date.setter
    def due_date(self, new_due_date: datetime):
        '''The above function is a setter method that sets the due date of an task to a new value.
        
        Parameters
        ----------
        new_due_date : datetime
            The new_due_date parameter is a datetime task that represents the new due date for a task or
        assignment.
        
        '''
        self.__due_date = new_due_date
    
    @property
    def reminder(self) -> datetime:
        '''The above function is a property decorator that returns the value of the private attribute
        __reminder.
        
        Returns
        -------
            The reminder property is returning the value of the __reminder attribute.
        
        '''
        return self.__reminder

    @reminder.setter
    def reminder(self, new_reminder: datetime):
        '''The above function is a setter method that sets the due date of an task to a new value.
        
        Parameters
        ----------
        new_reminder : datetime
            The new_reminder parameter is a datetime task that represents the new due date for a task or
        assignment.
        
        '''
        self.__reminder = new_reminder
    
    @property
    def id(self) -> int:
        '''The above function is a property decorator that returns the value of the private attribute
        __id.
        
        Returns
        -------
            The id property is returning the value of the __id attribute.
        
        '''
        return self.__id

    @id.setter
    def id(self, new_id: int):
        '''The above function is a setter method that sets the due date of an task to a new value.
        
        Parameters
        ----------
        new_id : datetime
            The new_id parameter is a datetime task that represents the new due date for a task or
        assignment.
        
        '''
        self.__id = new_id
    
    @property
    def json_dump(self):
        task = {
            'id': self.__id,
            'title': self.__title,
            'description': self.__description,
            'complete': self.__completed,
            'due-date': self.__due_date,
            'reminder': self.__reminder,    
        }
        
        return task
    
    
    
    

# The TaskList class is a subclass of List that allows only instances of the Task class or its
# subclasses to be appended to the list.
class TaskList(List[Type[Task]]):
    def append(self, item: Type[Task]) -> None:
        '''The function appends an instance of the Task class to a list, raising an error if the item is
        not an instance of Task.
        
        Parameters
        ----------
        item : Type[Task]
            The parameter "item" is of type "Type[Task]", which means it expects an instance of the "Task"
        class or any of its subclasses to be passed as an argument.
        
        '''
        if not isinstance(item, Task):
            raise TypeError(f"Only instances of Task can be appended, not {type(item).__name__}")
        super().append(item)
    
class TodoList:
    def __init__(self, file_name: str) -> None:
        self.__tasks: TaskList = TaskList()
        self.__file_path: str = f"docs/{file_name.lower()}.json"
        self.file_name: str = file_name.capitalize()
        self.__json_data = {}
        self.load_tasks()
        
    @property
    def tasks(self):
        '''The function is a property decorator that returns the value of the private attribute __tasks.
        
        Returns
        -------
            The tasks attribute is being returned.
        
        '''
        return self.__tasks
    
    def create_task(self, _title: str, _descr: str = "", _status: bool = False, _due: datetime = None, _reminder: datetime = None):
        
        try:
            task_data = {}
            
            # Building data dictionary
            task_data['title'] = _title.lower()
            task_data['description'] = _descr.lower()
            task_data['complete'] = _status
            # Safety checks
            if _due:
                task_data['due-date'] = _due.isoformat()
            else:
                task_data['due-date'] = None
                
            # Safety checks
            if _reminder:
                task_data['reminder'] = _reminder.isoformat()
            else:
                task_data['reminder'] = None
            
            task_data['id'] = len(self.tasks) + 1
            
            # Building task and adding it to the tasks list
            task = Task().build_task(task_data, self.file_name)
            self.tasks.append(task)
            
        except Exception as e:
            print(e)
    
    def edit_task(self, task_id, data: dict):
        for task in self.tasks:
            if task.id != task_id:
                continue
            for key, value in data.items():
                if value is None:
                    continue
                
                print(key)
                match key:
                    case "title":
                        task.title = value
                    case "description":
                        task.description = value
                    case "complete":
                        task.is_completed = value
                    case "due-date":
                        task.due_date = value
                    case "reminder":
                        task.reminder = value
                    case "complete":
                        task.completed = value
                        
                    
            self.save_tasks()
            return task
        
                
                
            
    
    def load_tasks(self) -> TaskList:        
        '''The function "load_tasks" reads a JSON file and saves the task objects into a variable called
        "self.tasks".
        
        '''
        try:
            # Try to open the file in read-write mode
            with open(self.__file_path, "r+") as f:
                # 1. Load JSON file
                try:
                    data = json.load(f)
                    self.__json_data = data
                    tasks = data['tasks']
                    for task in tasks:
                        self.__tasks.append(Task().build_task(task, self.file_name))
                except json.decoder.JSONDecodeError:
                    data = {'tasks': []}
        except FileNotFoundError:
            # If the file doesn't exist, create a new one
            with open(self.__file_path, "w+") as f:
                data = {'tasks': []}
                print(f"New JSON file '{self.__file_path}' created.")
        
        return None
    
    def save_tasks(self):
        '''The function `save_tasks` is used to save tasks into a file in JSON format.
        '''
        # 1. Open file with write / append
        
        with open(self.__file_path, 'w+') as f:
            try:
                data = {
                    "tasks":[
                        task.json_dump for task in self.tasks
                    ]
                    
                }
                json.dump(data, f, indent=2)
            except Exception as e:
                print(e)
            
        # 2. Format tasks into json file
        # 3. Write json data into file
        pass
    
    def delete_task(self, id:int = None):
        '''The `delete_task` function deletes a task from a list of tasks based on either the task's title
        or id, and returns the deleted task.
        
        Parameters
        ----------
        title : str
            The title parameter is a string that represents the title of the task that you want to delete.
        If you provide a title, the function will search for a task with that title and delete it.
        id : int
            The `id` parameter is an optional integer that represents the unique identifier of a task. If
        provided, the function will search for a task with the matching `id` and delete it from the list
        of tasks.
        
        Returns
        -------
            the task that was deleted from the list of tasks.
        
        '''
        show_task = {}
        tasks = self.__tasks
        for task in tasks:
            if task.id == id:
                show_task = task
                self.tasks.remove(task)
        
        self.save_tasks()
        return show_task
        
    

# if __name__ == '__main__':
#     test = TodoList("template")
#     test.load_tasks()
#     print(test.tasks[1].title)
#     pass
