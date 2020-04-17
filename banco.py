import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('./banco.db')
    
