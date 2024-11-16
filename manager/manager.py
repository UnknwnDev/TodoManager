from os import listdir
from manager.todo import TodoList
from renderer.terminal import CustomTerminal

# This file will manage the calls creation, loading, and saving of tasks. Nothing else


class Manager:
    def __init__(self) -> None:
        self.TodoList: TodoList = {}
        self.term = CustomTerminal(self)
        self.selected_category: str = None

    def __load(self):
        """The function "start" initializes a dictionary called "TodoList" with instances of the "TodoList"
        class, using names obtained from a JSON file.

        """
        names = self.__get_jsons_names()
        for name in names:
            self.TodoList[name] = TodoList(name)

    def get_all_tasks(self):
        """The function `get_all_tasks` returns all the tasks in the TodoList.

        Returns
        -------
            all the values in the TodoList dictionary.

        """
        self.__load()
        return self.TodoList

    @property
    def get_list(self) -> TodoList:
        """The function `find_task` checks if a category is selected and then either prints the ID or the Title
        of the chosen task.

        Parameters
        ----------
        target : str
            The `target` parameter is a string that represents either the ID or the title of a task.

        Returns
        -------
            0.

        """
        if not self.selected_category:
            print("Please select a category/file. ( sel/select test )")
            return None

        try:
            return self.TodoList[self.selected_category]
        except Exception:
            print(f"List: {self.selected_category.capitalize()} DNE")
            return None

    def remove_task(self, id: str):
        if not self.selected_category:
            return -1

        task = self.TodoList[self.selected_category].delete_task(id=int(id))
        # print(task)
        print("=" * 50)
        self.term.show_task(task)
        print("=" * 50)

        return 0

    def save_task(self, category: str):
        """The function `save_task` saves a task in a specific category in a TodoList.

        Parameters
        ----------
        category : str
            The category parameter is a string that represents the category of the task.

        """
        self.TodoList[category].save_task()

    def get_tasks_by_category(self, category: str = ""):
        """The function `get_tasks_by_category` returns the tasks associated with a given category from a
        TodoList.

        Parameters
        ----------
        category : str
            The category parameter is a string that represents the category of tasks you want to retrieve. If
        no category is specified, it will return all tasks from all categories.

        Returns
        -------
            The tasks associated with the specified category are being returned.

        """
        self.__load()
        return self.TodoList[category].tasks

    def __get_jsons_names(self):
        """The function `__get_jsons_names` retrieves the names of all JSON files in the "./docs" directory.

        Returns
        -------
            The function `__get_jsons_names` returns a list of names of all JSON files in the "./docs"
        directory.

        """
        """The function `__get_jsons_names` retrieves the names of all JSON files in the "./docs"
        directory.
        
        """
        path = "./docs"
        files = listdir(path)
        names = []
        for file in files:
            if ".json" in file:
                name = file.split(".")[0]
                names.append(name)

        return names

    @property
    def __print_lists(self):
        """The function prints the tasks in each list in a TodoList object."""
        for list in self.TodoList.values():
            self.term.printf(list.tasks)

    def run(self):
        """The function runs a program, loading data and starting a terminal if the GUI flag is not set.

        Parameters
        ----------
        gui : bool, optional
            The `gui` parameter is a boolean flag that indicates whether the program should run in
        graphical user interface (GUI) mode or not. If `gui` is set to `True`, the program will run with
        a GUI interface. If `gui` is set to `False` (or not provided

        """

        self.term.start()


# if __name__ == "__main__":
# Manager().get_jsons()
