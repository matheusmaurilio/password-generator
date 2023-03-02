import string
import random
import tkinter as tk
from tkinter import filedialog

class Senha:
    def __init__(self, valor=''):
        self.valor = valor

    def gerar(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        tamanho = 16
        self.valor = ''.join(random.choice(caracteres) for _ in range(tamanho))

    def salvar(self, nome_arquivo):
        with open(nome_arquivo, 'w') as f:
            f.write(self.valor)


class App:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("400x500")
        self.master.configure(bg='#F0F0F0')
        self.master.title("Gerador de Senhas")

        self.frame = tk.Frame(self.master, bg='#F0F0F0')
        self.frame.pack(pady=50)

        self.senha = Senha()
        
        self.titulo = tk.Label(self.frame, text="Gerador de Senhas", bg='#F0F0F0', fg='#666666',
        font=('Arial', 24, 'bold'))
        
        self.titulo.pack(pady=20)

        self.gerar_senha_button = tk.Button(self.frame, text="Gerar senha",
        bg='#666666', fg='#F0F0F0', font=('Arial', 16), height=2, width=20, command=self.gerar_senha)
        
        self.gerar_senha_button.pack(pady=20)

        self.salvar_senha_button = tk.Button(self.frame, text="Salvar senha", bg='#666666',
        fg='#F0F0F0', font=('Arial', 16), height=2, width=20, command=self.salvar_senha)
        
        self.salvar_senha_button.pack(pady=20)

        self.result_frame = tk.Frame(self.master, bg='#F0F0F0')
        self.result_frame.pack(pady=20)

        self.result_label = tk.Label(self.result_frame, text="Senha gerada: ",
        bg='#F0F0F0', fg='#666666', font=('Arial', 16))
        
        self.result_label.pack(side=tk.LEFT)

        self.result_text = tk.Text(self.result_frame, height=1, width=20,
        font=('Arial', 16), bg='#FFFFFF', fg='#666666')
        
        self.result_text.pack(side=tk.LEFT, padx=10)

        self.master.mainloop()

    def gerar_senha(self):
        self.senha.gerar()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, self.senha.valor)

    def salvar_senha(self):
        nome_arquivo = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Arquivo de texto", "*.txt")])
        
        if nome_arquivo:
            self.senha.salvar(nome_arquivo)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Senha salva em {nome_arquivo}")


app = App()
