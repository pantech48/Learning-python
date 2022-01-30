"""
Command/Action (Команда)
Поведенческий

Инкапсулирует запрос как объект,
позволяя тем самым задавать параметры клиентов для обработки соответсвующих запросов,
ставить запросы в очередь или протоколировать их,
а также поддерживать отмену операций.
"""

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        """Выполнить команду"""


class ListTasksCommand(Command):
    def execute(self):
        print('Список задач на текущий день.')


class ShowTaskCommand(Command):
    def __init__(self, task_id):
        self.task_id = task_id

    def execute(self):
        print(f'Вывести на экран задачу с ID: {self.task_id}')


commands = {
    '1': ListTasksCommand(),
    '2': ShowTaskCommand(1)
}

cmd = input()
command = commands.get(cmd)

if command:
    command.execute()



