import random
import time

count = 0


def tokenserver():
    servertoken = int()
    for i in range(6):
        servertoken += str(random.randint(1, 9))
    return servertoken


def rantoken():
    token = ''
    for i in range(6):
        token += str(random.randint(1, 9))
    return token


class User:
    name = ''
    password = ''
    token = int()
    valid = False

    def regiser(self):
        username = input('Your username: ')
        password = input('Your Password: ')
        self.username = username
        self.password = password
        self.valid = True

    def logout(self):
        if self.valid is None:
            self.token = None
            return self.token

    def login(self, counts):
        username = input('\n Enter Username: ')
        password = input('\n Enter Password')
        while username == username and password == password:
            if counts == 3:
                User.token = 0
                print('You used your tries log after a while')
                time.sleep(30)

            elif username == User.name and password == User.password:
                print('You logged in')
                time.sleep(5)
                break
            elif username != User.name or password != User.password:
                counts += 1
                print(counts)
                time.sleep(5)
                print('Your password or Name is incorrect')
                username = input("\n\nUsername: ")
                password = input("Password: ")
                continue