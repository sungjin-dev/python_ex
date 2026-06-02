import os
import json
import session
from todo import config as todo_config
import config as root_config
from util import util_time

class TodoService:

    def __init__(self):
        self.todos = {}
        self.init_database()

    def init_database(self):
        # 현재 파일 위치              절대값 경로
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR : {ROOT_DIR}')

        # db/accounts.json                  폴더명      파일명
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'todos.json')
        print(f'self.dbFile: {self.dbFile}')
        # C:\pjt\python\python_ex\myDashboardPjt\db\todos.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):       
            self.save_todos(self.todos)  # 파일이 없으면 파일 만드는 함수로 가는거임
        else:
            self.todos = self.load_todos()  # 장기 데이터에 세이브  

    def save_todos(self, todos):   # {}
            with open(self.dbFile, 'w', encoding= 'utf-8') as f:
                json.dump(todos, f, ensure_ascii = False, indent = 4) 

    # 데이터 무결성 검증 클래스를 만들어서 관리하기 
    # JSON파일을 읽어서 애플리케이션으로 데이터를 가져오는 것   
    def load_todos(self):   
            with open(self.dbFile, 'r' , encoding = 'utf-8') as f:
                return json.load(f)   # load() 메서드 확인하기 
            
    def isMyTodos(self):
        allTodos = self.load_todos()
        if session.getSigninedMemberId() in allTodos:
            return True 
             
        return False

    def run(self):

        if session.getSigninedMemberId() == '':
            print('Please Sign-in')
            return

        flag = True
        while flag:
            if not self.isMyTodos():
                self.todos[session.getSigninedMemberId()] = []   # 리스트로 한거 주의!!!!!!!!!!
                self.save_todos(self.todos)
            menuNum = int(input('1. WRITE  2.READ   3.UPDATE    4.DELETE    5.COMPLETE-CHANGE   99.SERVICE-OUT '))   

            if menuNum == todo_config.WRITE:
                self.todos = self.load_todos()
                myTodos= self.todos[session.getSigninedMemberId()]

                tText = input('Input new todo txt: ')
                tExpDate = input('Input todo experation date(2026-08-05 06:09:09)')  # 06 (o) 6 (x)  2자리수로 표기

                todo = {
                    'tTxt': tText,
                    'tExpDate': tExpDate,
                    'tRegDate': util_time.getCurrentDateTime(),
                    'tModDate': util_time.getCurrentDateTime(),
                    'tComplete': False
                }

                myTodos.insert(0, todo)
                self.save_todos(self.todos)
                print('WRITE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos() : {self.load_todos()}')
            
            
            elif menuNum == todo_config.READ:
                 self.todos = self.load_todos()
                 myTodos = self.todos[session.getSigninedMemberId()]
                 for idx, myTodo in enumerate(myTodos):
                      print('-' * 50)
                      print(f'[{idx + 1}]')
                      print(f'TEXT : {myTodo["tTxt"]}')
                      print(f'EXPIRATIONDATE : {myTodo["tExpDate"]}')
                      print(f'REGISTE DATE : {myTodo["tRegDate"]}')
                      print(f'MODIFY DATE : {myTodo["tModDate"]}')
                      print(f'COMPLETE : {myTodo["tComplete"]}')
            
            elif menuNum == todo_config.UPDATE:
                 self.todos = self.load_todos()
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
                 self.save_todos(self.todos)
                 print('UPDATE SUCCESS')

                 if root_config.DEV_MOD:
                      print(f'self.load_todos(): {self.load_todos()}')
            
            elif menuNum == todo_config.DELETE:
                 self.todos = self.load_todos()
                 myTodos = self.todos[session.getSigninedMemberId()]
                 for idx, myTodo in enumerate(myTodos):
                      print('-' * 100)
                      print(f'[{idx + 1}] {myTodo["tTxt"]} [{myTodo["tExpDate"]}] [{myTodo["tComplete"]}]' )
                      print('-' * 100)

                 todoNumber = int(input('Enter the todo number: '))
                 myTodos.pop(todoNumber-1)
                #  del myTodos[todoNumber-1]
                 self.save_todos(self.todos)
                 print('DELETE SUCCESS')   

                 if root_config.DEV_MOD:
                      print(f'self.load_todos() : {self.load_todos()}')

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
                 self.save_todos(self.todos)
                 print('UPDATE SUCCESS')

                 if root_config.DEV_MOD:
                      print(f'self.load_todos(): {self.load_todos()}')
            
            
            elif menuNum == todo_config.COMPLETE_CHANGE:
                 self.todos = self.load_todos()
                 myTodos = self.todos[session.getSigninedMemberId()]

                 for idx, myTodo in enumerate(myTodos):
                      print('-' * 100)
                      print(f'[{idx + 1}] {myTodo["tTxt"]} [{myTodo["tExpDate"]}] [{myTodo["tComplete"]}]' )
                      print('-' * 100)
                 todoNumber = int(input('Enter the todo number: '))
                #  if myTodos[todoNumber -1 ]['tComplete'] == True:
                #       myTodos[todoNumber -1 ]['tComplete'] == False
                #  else:    
                #     myTodos[todoNumber -1 ]['tComplete'] == True
                 myTodos[todoNumber-1]['tComplete'] = not myTodos[todoNumber-1]['tComplete']
                 self.save_todos(self.todos)
                 print('COMPLETE CHANGE SUCCESS!!')

                 if root_config.DEV_MOD:
                      print(f'self.load_todos(): {self.load_todos()}')
            
            elif menuNum == todo_config.SERVICE_OUT:
                 flag = False

if __name__ == '__main__':
    bankService = TodoService()
    bankService.run()


# python -m todo.todo_service   위 화살표 