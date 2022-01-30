"""
name 			- Имя пакета 
version 		- Версия пакета

description 	- Краткое описание пакета
url 			- URL-адрес пакета
license			- Лицензия
author			- Автор пакета
author_email 	- E-Mail автора пакета

packages		- Пакеты, которые нужно скопирвать при установке
py_modules		- Модули, которые нужно скопировать при установке
scripts			- Запускаемые из консоли команды

install_requires- Прямые зависимости, которые нужно установить 

"""

from setuptools import setup, find_packages


setup(
	name='task-diary',
	version='1.0.0',
	description='Console diary.',
	license='MIT',
	author='Putrin Evgeniy',
	author_email='evgeniy.putrin@gmail.com',
	packages=find_packages(),
	package_data={
		'task_diary': ['resources/*'],
	},
	entry_points={
		'console_scripts': [
			'diary=task_diary:main',
		],
	},
	install_requires=[
		'appdirs>=1.4',
		'prettytable>=0.7',
	]
)


