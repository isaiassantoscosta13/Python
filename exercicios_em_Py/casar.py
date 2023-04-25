#código de mini interfaces ultilizando tkinter
import tkinter
from tkinter import messagebox

count = 0

msg_box = messagebox.showwarning("IMPORTANTE!", "NOME DA PESSOA !!! \n VOCÊ FOI HACKEADA")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("PREPARADA?", "PARA SER DESHACKEADA PRECISO QUE ME RESPONDA UMA PERGUNTA...")

if msg_box == 'ok':
    msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA CASAR COMIGO?")

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA CASAR COMIGO?")
    if (count == 5):
        msg_box = messagebox.showerror("TENTOU ISSO TUDO?", "PEDIDO NEGADO, VOCÊ VAI CASAR SIM !!!")

    if msg_box == 'ok':
        msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA CASAR COMIGO?")
        break

if msg_box == 'yes':
    msg_box = messagebox.showinfo("BOA!", "SABIA ESCOLHA!")
    