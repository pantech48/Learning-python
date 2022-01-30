"""
Observer (Наблюдатель)
Поведенческий

"""

from abc import ABCMeta, abstractmethod
from random import randrange


class Subject(metaclass=ABCMeta):
    """Субъект - тот за кем ведется наблюдение."""

    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer):
        """""Добавляет наблюдателя за субъектом"""
        self._observers.append(observer)

    def remove_observer(self, observer):
        """Удаляет наблюдателя за субъектом."""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self):
        """Оповещает наблюдателей об изменении субъекта."""
        ctx = self._make_result()

        for observer in self._observers:
            observer.update(ctx)

    @abstractmethod
    def _make_result(self):
        """Возвращает объект-результат"""


class Observer(metaclass=ABCMeta):
    """Наблюдатель."""
    
    @abstractmethod
    def update(self, ctx):
        """Реагирует на изменения субъекта."""

    
class Worker(Subject):
    """Исполнитель задачи"""

    def __init__(self):
        super().__init__()
        self.result = None

    def execute(self):
        """
        Результат работы:
            0. Успешно, ошибок нет
            1. Ошибка при исполнении
            2. Демон не доступен
        """
        self.result = randrange(3)
        self.notify_observers()
    
    def _make_result(self):
        return self.result


class LoggerObserver(Observer):
    def update(self, ctx):
        if ctx == 0:
            print('Пишем в access.log')


class ErrorObserver(Observer):
    def update(self, ctx):
        if ctx == 1:
            print('Пишем в error.log')


class MailObserver(Observer):
    def update(self, ctx):
        if ctx == 2:
            print('Посылка уведомления на E-Mail админитратору')



w = Worker()

w.add_observer(LoggerObserver())
w.add_observer(ErrorObserver())
w.add_observer(MailObserver())

w.execute()


