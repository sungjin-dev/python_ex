import os
import json
import session
from todo import config as todo_config
import login_break
from todo import todo_delete
from todo import todo_complete
from todo import todo_update
from todo import todo_read
from todo import todo_write

class TodoService:

    def __init__(self):
        self.todos = {}
        self.init_database()

    def init_database(self):

        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR : {ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'todos.json')
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):       
            self.save_todos(self.todos)  
        else:
            self.todos = self.load_todos()  

    def save_todos(self, todos): 
            with open(self.dbFile, 'w', encoding= 'utf-8') as f:
                json.dump(todos, f, ensure_ascii = False, indent = 4) 

    def load_todos(self):   
            with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
                return json.load(f)   
            
    def isMyTodos(self):
        allTodos = self.load_todos()
        if session.getSigninedMemberId() in allTodos:
            return True 
             
        return False

    def run(self):

        login_break.commition()

        flag = True
        while flag:
            if not self.isMyTodos():
                self.todos[session.getSigninedMemberId()] = []   
                self.save_todos(self.todos)
            menuNum = int(input('1. WRITE  2.READ   3.UPDATE    4.DELETE    5.COMPLETE-CHANGE   99.SERVICE-OUT '))   

            if menuNum == todo_config.WRITE:              
                todo_write.Writetodo().write()
                
            elif menuNum == todo_config.READ:
                todo_read.ReadTodo().read()
            
            elif menuNum == todo_config.UPDATE:
                todo_update.UpdateAcc().update()
                   
            elif menuNum == todo_config.DELETE:
                todo_delete.DeleteTodo().delete()
                 
            elif menuNum == todo_config.COMPLETE_CHANGE:
                todo_complete.CompleteCheck().completeChange()
                 
            elif menuNum == todo_config.SERVICE_OUT:
                 flag = False

if __name__ == '__main__':
    todoService = TodoService()
    todoService.run()


