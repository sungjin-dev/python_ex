import session
from todo import todo_service
import config as root_config

class CompleteCheck:
    def __init__(self):
        self.todos = {}

    def completeChange(self):
            
        self.todos = todo_service.TodoService().load_todos()
        myTodos = self.todos[session.getSigninedMemberId()]

        for idx, myTodo in enumerate(myTodos):
            print('-' * 100)
            print(f'[{idx + 1}] {myTodo["tTxt"]} [{myTodo["tExpDate"]}] [{myTodo["tComplete"]}]' )
            print('-' * 100)
        todoNumber = int(input('Enter the todo number: '))
    
        myTodos[todoNumber-1]['tComplete'] = not myTodos[todoNumber-1]['tComplete']
        todo_service.TodoService().save_todos(self.todos)
        print('COMPLETE CHANGE SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_todos(): {todo_service.TodoService().load_todos()}')
            