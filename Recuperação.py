import sqlite3 as sql
import flet as ft

def main(page: ft.Page):

    page.title = "Sistema de Cadastro"
    def click(e):
        banco = sql.connect('cadastro.db')
        cursor = banco.cursor()
        #cursor.execute("CREATE TABLE cadastro (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, email TEXT,cpf INTEGER,telefone INTEGER)")
        nome1 = nome.value
        email1=email.value
        cpf1 = cpf.value
        telefone1=telefone.value
        print(f"nome é: {nome1}")
        print(f"O email é:{email1}")
        print(f"ó cpf é: {cpf1}")
        print(f"O telefone é:{telefone1}")
        cursor.execute(f"INSERT INTO cadastro('nome','email','cpf','telefone') values('{nome1}','{email1}',{cpf1},{telefone1})")
        cursor.execute("SELECT * FROM cadastro")
        print(cursor.fetchall())
        banco.commit()
        
            
    nome = ft.TextField(label="Nome:", width=200)
    email = ft.TextField(label="Email:", width=200)
    cpf = ft.TextField(label="cpf:", width=200)
    telefone = ft.TextField(label="telefone:", width=200)
    confirmar = ft.ElevatedButton("Confirmar", bgcolor="green", color="white", on_click=click)
    page.add(nome, email, cpf, telefone, confirmar)

ft.app(target=main)
