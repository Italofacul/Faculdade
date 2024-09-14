import tkinter as tk
from tkinter import PhotoImage
    
janela = tk.Tk()
janela.title("Botões com Imagens")

imagens = [f'imagem{i+1}.png' for i in range(10)]

imagens_carregadas = []

for i in range(10):
    try:
        imagem = PhotoImage(file=imagens[i])
        imagens_carregadas.append(imagem) 
    except tk.TclError:
        print(f"Erro ao carregar a imagem {imagens[i]}. Verifique o caminho e o formato do arquivo.")
        imagem = None

    linha = i // 5
    coluna = i % 5

    btn = tk.Button(janela, image=imagem, compound='top', command=lambda i=i: print(f'Botão {i+1} clicado'))
    btn.grid(row=linha, column=coluna, padx=10, pady=10) 

for i in range(5):  
    janela.grid_columnconfigure(i, weight=1)

for i in range(2):
    janela.grid_rowconfigure(i, weight=1)

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)

janela.mainloop()
