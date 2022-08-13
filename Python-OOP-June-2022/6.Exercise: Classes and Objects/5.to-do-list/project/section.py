from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        self.new_task = new_task
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):

        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"

        Task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        initial_len = len(self.tasks)
        completed_not = [compl for compl in self.tasks if not self.new_task.completed]
        result = initial_len -len(completed_not)
        return f"Cleared {result} tasks."

    def view_section(self):
        view_section = f"Section {self.name}:\n"
        for task in self.tasks:
            view_section += task.details() + f"\n"

        return view_section.strip()



    #    for task in Task.details():
    #    '''
    # {details of the first task}
    # {details of the second task}
    # {details of the n task}'''
