import session
from todo import todo_service
from util import util_time
import config as root_config

class Writetodo:   
    def __init__(self):

        self.todos = {}

    def write(self):

        self.todos = todo_service.TodoService().load_todos()
        myTodos= self.todos[session.getSigninedMemberId()]

        tText = input('Input new todo txt: ')
        tExpDate = input('Input todo experation date(2026-08-05 06:09:09)') 
        
        todo = {
            'tTxt': tText,
            'tExpDate': tExpDate,
            'tRegDate': util_time.getCurrentDateTime(),
            'tModDate': util_time.getCurrentDateTime(),
            'tComplete': False
        }

        myTodos.insert(0, todo)
        todo_service.TodoService().save_todos(self.todos)
        print('WRITE SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_todos() : {todo_service.TodoService().load_todos()}')
            