import session
from todo import todo_service
from util import util_time
import config as root_config

class UpdateAcc:
    def __init__(self):
        self.todos = {}
    
    def update(self):

        self.todos = todo_service.TodoService().load_todos()

        myTodos = self.todos[session.getSigninedMemberId()]
        for idx, myTodo in enumerate(myTodos):
            print('-' * 100)
            print(f'[{idx + 1}] {myTodo["tTxt"]} [{myTodo["tExpDate"]}] [{myTodo["tComplete"]}]' )
            print('-' * 100)
        todoNumber = int(input('Enter the todo number: '))

        tText = input('Input todo txt: ')
        tExpDate = input('Input todo experation date(2026-08-05 06:09:09)')

        todo = {
        'tTxt': tText,
        'tExpDate': tExpDate,
        'tRegDate': myTodo[todoNumber-1]['tRegDate'],
        'tModDate': util_time.getCurrentDateTime(),
        'tComplete': myTodo[todoNumber-1]['tComplete']
    }
        
        myTodos[todoNumber-1] = todo 
        todo_service.TodoService().save_todos(self.todos)
        print('UPDATE SUCCESS')

        if root_config.DEV_MOD:
            print(f'self.load_todos(): {todo_service.TodoService().load_todos()}')