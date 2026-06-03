import session
from todo import todo_service

class ReadTodo:
    def __init__(self):
        self.todos = {}
    
    def read(self):

        self.todos = todo_service.TodoService().load_todos()
        myTodos = self.todos[session.getSigninedMemberId()]
        for idx, myTodo in enumerate(myTodos):
            print('-' * 50)
            print(f'[{idx + 1}]')
            print(f'TEXT : {myTodo["tTxt"]}')
            print(f'EXPIRATIONDATE : {myTodo["tExpDate"]}')
            print(f'REGISTE DATE : {myTodo["tRegDate"]}')
            print(f'MODIFY DATE : {myTodo["tModDate"]}')
            print(f'COMPLETE : {myTodo["tComplete"]}')