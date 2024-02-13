#!/usr/bin/env python3.11 
from os import listdir
from manager.todo import TodoList
from renderer.terminal import CustomTerminal


# This file will manage the calls creation, loading, and saving of tasks. Nothing else

class Manager:
    def __init__(self) -> None:
        self.TodoList = {}
        self.term = CustomTerminal(self)

    def __load(self):
        '''The function "start" initializes a dictionary called "TodoList" with instances of the "TodoList"
        class, using names obtained from a JSON file.
        
        '''
        names = self.__get_jsons_names()
        for name in names:
            self.TodoList[name] = TodoList(name)

    def get_all_tasks(self):
        self.__load()
        return self.TodoList.values()

    def get_tasks_by_category(self, category:str =""):
        return self.TodoList[category].tasks

    def __get_jsons_names(self):
        '''The function `__get_jsons_names` retrieves the names of all JSON files in the "./docs"
        directory.
        
        '''
        path = "./docs"
        files = listdir(path)
        names = []
        for file in files:
            if '.json' in file:
                name = file.split('.')[0]
                names.append(name)

        return names    
    
    @property
    def __print_lists(self):
        for list in self.TodoList.values():
            self.term.printf(list.tasks)
    
    def run(self, gui: bool = False):
        self.__load()
        if not gui:
            self.term.start()
        

if __name__ == "__main__":
    Manager().get_jsons()