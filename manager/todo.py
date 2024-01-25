#!/usr/bin/env python3.11 

import datetime
from typing import List, Type
import json
# This file will have the logic for creation, loading, saving

# This function is just to store the information of the task
class Task(object):
    def __init__(self) -> None:
       self.__completed: bool = False
       self.__title: str = ""
       self.__description: str = ""
       self.__due_date:datetime = None
       
       # Do these later not now
       self.__reminder:datetime = None
       self.__id: int = None 
    
    
    def build_task(self, task_data:dict):
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
        
        self.__title = task_data['title']
        self.__description = task_data['description']
        self.__completed = task_data['complete']
        self.__due_date = task_data['due-date']
        self.__id = task_data['id']
        self.__reminder = task_data['reminder']
        
        return self
    
    @property
    def is_completed(self) -> bool:
        '''The `is_completed` function is a property that returns the value of the private `__completed`
        attribute.
        
        Returns
        -------
            The method is returning the value of the private attribute "__completed".
        
        '''
        return self.__completed
    
    @is_completed.setter
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
        self.__file_path = f"docs/{file_name}.json"
        self.load_tasks()
        
    @property
    def tasks(self):
        '''The function is a property decorator that returns the value of the private attribute __tasks.
        
        Returns
        -------
            The tasks attribute is being returned.
        
        '''
        return self.__tasks
    
    def load_tasks(self) -> TaskList:        
        '''The function "load_tasks" reads a JSON file and saves the task objects into a variable called
        "self.tasks".
        
        '''
        with open(self.__file_path, "r") as f:
            # 1. Load Json file
            data = json.load(f)
            tasks = data['tasks']
            for task in tasks:
                self.__tasks.append(Task().build_task(task))
            # 2. Save Task objects from into self.tasks
        
        return None
    
    def save_tasks(self):
        '''The function `save_tasks` is used to save tasks into a file in JSON format.
        '''
        # 1. Open file with write / append
        # 2. Format tasks into json file
        # 3. Write json data into file
        pass
             
    

if __name__ == '__main__':
    test = TodoList("template")
    test.load_tasks()
    print(test.tasks[1].title)
    pass
