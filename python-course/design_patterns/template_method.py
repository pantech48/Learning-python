"""
Template Method (Шаблонный метод)
Поведенческий

Определяет основу алгоритма 
и позволяет наследникам переопределить некоторые шаги алгоритма,
не изменяя его структуру в целом.
"""

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def _do_execute(self):
        pass
    
    def execute(self):
        """Выполнить команду"""
        print('Действия до выполнения команды')
        self._do_execute()
        print('Действия после выполнения команды')


class ListTasksCommand(Command):
    def _do_execute(self):
        print('Список задач на текущий день.')


class ShowTaskCommand(Command):
    def __init__(self, task_id):
        self.task_id = task_id

    def _do_execute(self):
        print(f'Вывести на экран задачу с ID: {self.task_id}')


commands = {
    '1': ListTasksCommand(),
    '2': ShowTaskCommand(1)
}

cmd = input()
command = commands.get(cmd)

if command:
    command.execute()



