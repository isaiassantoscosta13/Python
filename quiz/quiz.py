# -*- coding: utf-8 -*-
import random
import json
from time import sleep
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Configurações da janela principal
window = tk.Tk()
window.title("Quiz IFSC")
window.geometry("1000x600")
alfabeto = ['A','B','C','D']

# Carrega as perguntas do arquivo perguntas.json
with open("perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

# Função para apresentar uma pergunta aleatória
def fazer_pergunta():
    # Remove os widgets antigos 
    for widget in window.winfo_children():
        widget.destroy()

    # Seleciona uma pergunta aleatória
    pergunta = random.choice(perguntas)
    
    # Cria os widgets da pergunta
    pergunta_label = ttk.Label(window, text=pergunta["pergunta"], font=("Arial", 30))
    pergunta_label.pack(pady=20)
    
    opcoes_frame = ttk.Frame(window)
    opcoes_frame.pack()
    
    opcoes = pergunta["opcoes"]
    resposta = pergunta["resposta"]
    resposta_var = tk.StringVar(value="")
    
    # Cria uma string com as alternativas
    alternativas = ""
    for i, opcao in enumerate(pergunta["opcoes"]):
        alternativas += f"{alfabeto[i]}) {opcao}    "
   
    for i, opcao in enumerate(opcoes):
        opcao_radio = ttk.Radiobutton(opcoes_frame,  text=f"{alfabeto[i]}) {opcao}", value=alfabeto[i], variable=resposta_var)
        opcao_radio.pack(side="top", padx=10, pady=5)

    # Pede a resposta do usuário
    resposta_botao = ttk.Button(window, text="Responder", command=lambda: verificar_resposta(resposta_var.get(), resposta))
    resposta_botao.pack(pady=10)

    # Função para verificar a resposta do usuário
    def verificar_resposta(resposta_usuario, resposta_correta):
        if not resposta_usuario:
            messagebox.showerror("Erro", "Selecione uma resposta!")
            return
        
        # Cria uma nova janela de carregamento
        loading_window = tk.Toplevel(window)
        loading_window.title("Carregando...")
        loading_label = ttk.Label(loading_window, text="Sua resposta está ...", font=("Arial", 30))
        loading_label.pack(pady=20)
        
        # Agenda a execução da função que verifica a resposta
        window.after(4000, verificar_resposta_exec, resposta_usuario, resposta_correta, loading_window)

    # Função para verificar a resposta do usuário (execução real)
    def verificar_resposta_exec(resposta_usuario, resposta_correta, loading_window):
        # Fecha a janela de carregamento
        loading_window.destroy()

        # Verifica a resposta do usuário
        if resposta_usuario == resposta_correta:
            resultado_label.config(text="CORRETA ✅", font=("Arial", 30, "bold"), foreground="green")
            resultado_label2.config(text=f"A resposta correta é a letra ➡️{resposta_correta} \n\nAlternativas\n{alternativas}", font=("Arial", 20, "bold"))
        else:
            resultado_label.config(text="ERRADA ❌", font=("Arial", 30, "bold"), foreground="red")
            resultado_label2.config(text=f"A resposta correta é a letra ➡️{resposta_correta} \n\nAlternativas\n{alternativas}", font=("Arial", 20, "bold"))

        # Remove os widgets da pergunta
        pergunta_label.pack_forget()
        opcoes_frame.pack_forget()
        resposta_botao.pack_forget()
        resultado_label.pack(pady=20)
        resultado_label2.pack(pady=5)

    # Cria o widget para mostrar o resultado
    resultado_label = ttk.Label(window, text="")
    resultado_label2 = ttk.Label(window, text="")
    resultado_label.pack_forget()
    resultado_label2.pack_forget()

    # Cria o botão para jogar novamente
    jogar_novamente = ttk.Button(window, text="Jogar novamente", command=lambda: fazer_pergunta())
    jogar_novamente.pack(pady=10)

# Configurações iniciais da janela
alfabeto = ['A','B','C','D']
titulo_label = ttk.Label(window, text="Quiz UMP 2023", font=("Arial", 40, "bold"),foreground="sky blue")
titulo_label.pack(pady=10)

# Cria a imagem a partir de um arquivo
imagem = tk.PhotoImage(file=r"C:\Users\isaia\OneDrive\Documentos\Material\projPython\quizedit.png")
# Cria o widget para exibir a imagem
imagem_label = tk.Label(window, image=imagem, width=500, height=500)
imagem_label.pack(pady=10,padx=10)

iniciar_jogo_botao = ttk.Button(window, text="Iniciar jogo", command=lambda: fazer_pergunta())
iniciar_jogo_botao.pack(pady=10)

window.mainloop()
#Código no repositório https://github.com/isaiassantoscosta13/Python