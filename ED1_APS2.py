#projeto python de demonstração de manipulação de listas (estruturas de dados)
#simula um mini-sistema de logística, onde o user pode inserir e excluir itens do sistema
#também é possível a visualização das listas

#criado em dupla, por Leonardo Barbosa e Paulo Ricardo Egídio

from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

class Pilha(object):
    def __init__(self):
        self.dados = []
        self.dados.append("Vazio")
        self.tamanho = 0

    def empilha(self, elemento):
        #checa se o item já existe na lista
        existe = False
        if self.tamanho != 0:
           for i in self.dados:
               if elemento == i:
                   messagebox.showerror("Erro", "O item já existe nesse armazém!")
                   existe = True
                   break
        
        #checa se o tamnho máximo da lista foi atingido (4 itens)
        if self.tamanho < 3:
            if not existe: 
                self.dados.insert(0,elemento)
                messagebox.showinfo("Sucesso","Item inserido com sucesso") 
                self.tamanho +=1
                return True
        else:
            messagebox.showerror("Erro","Todos os armazéns estão cheios!")


   
    def desempilha(self,chave):
        self.dados.pop(0)
        messagebox.showinfo("Sucesso","Item excluído com sucesso") 
        self.tamanho -= 1


#exclui o item especificado
def apaga():
    id = entrada.get()
    if id == "":
        messagebox.showerror("Erro","Insira um valor no campo!")
    else:    
        resp = messagebox.askyesno("Excluir","Deseja mesmo apagar o item "+str(id)+"?")
        if resp:
            #checa se há itens nas listas
            if p.tamanho == 0 and p2.tamanho == 0 and p3.tamanho == 0 and p4.tamanho == 0: 
                messagebox.showerror("Erro","Todas as tabelas estão vazias!")
                
            #procura em qual lista o item está (necessita ser o primeiro item)
            elif id == p.dados[0]:
                p.desempilha(id)
                T.config(state = NORMAL)
                T.insert(tk.END,"Item "+str(id)+" apagado da lista 1\n")
                T.config(state = DISABLED)

            elif id == p2.dados[0]:
                p2.desempilha(id)
                T.config(state = NORMAL)
                T.insert(tk.END,"Item "+str(id)+" apagado da lista 2\n")
                T.config(state = DISABLED)

            elif id == p3.dados[0]:
                p3.desempilha(id)
                T.config(state = NORMAL)
                T.insert(tk.END,"Item "+str(id)+" apagado da lista 3\n")
                T.config(state = DISABLED)

            elif id == p4.dados[0]:
                p4.desempilha(id)
                T.config(state = NORMAL)
                T.insert(tk.END,"Item "+str(id)+" apagado da lista 4\n")
                T.config(state = DISABLED)        
            else:
                messagebox.showerror("Erro","Chave não está no topo em nenhuma lista")              

          
#adiciona o item especificado
def pega():
    id = entrada.get()
    if id == "":
        messagebox.showerror("Erro","Insira um valor no campo!")
    else:
        #checa em qual lista será adicionado (a menor lista)
        if p4.tamanho < p3.tamanho:
            resp = messagebox.askyesno("Inserir","Deseja mesmo inserir o item "+str(id)+" na lista 4?")
            if resp:
                if p4.empilha(id):
                    T.config(state = NORMAL)
                    T.insert(tk.END,"Item "+str(id)+" inserido na lista 4\n")
                    T.config(state = DISABLED)
                if p4.tamanho == 4:
                    T.config(state = NORMAL)
                    T.insert(tk.END,"AVISO - Lista 4 chegou ao limite de caixas\n")
                    T.config(state = DISABLED)

        if p3.tamanho < p2.tamanho:
            resp = messagebox.askyesno("Inserir","Deseja mesmo inserir o item "+str(id)+" na lista 3?")
            if resp:
                if p3.empilha(id):
                    T.config(state = NORMAL)
                    T.insert(tk.END,"Item "+str(id)+" inserido na lista 3\n")
                    T.config(state = DISABLED)
                if p3.tamanho == 4:
                    T.config(state = NORMAL)
                    T.insert(tk.END,"AVISO - Lista 3 chegou ao limite de caixas\n")
                    T.config(state = DISABLED)

        if p2.tamanho < p.tamanho:
            resp = messagebox.askyesno("Inserir","Deseja mesmo inserir o item "+str(id)+" na lista 2?")
            if resp:
                if p2.empilha(id):
                    T.config(state = NORMAL)
                    T.insert(tk.END,"Item "+str(id)+" inserido na lista 2\n")
                    T.config(state = DISABLED) 
                if p2.tamanho == 4:
                    T.config(state = NORMAL)
                    T.insert(tk.END,"AVISO - Lista 2 chegou ao limite de caixas\n")
                    T.config(state = DISABLED)


        if p.tamanho == p2.tamanho and p2.tamanho == p3.tamanho and p3.tamanho == p4.tamanho:
            resp = messagebox.askyesno("Inserir","Deseja mesmo inserir o item "+str(id)+" na lista 1?")
            if resp:
                if p.empilha(id):
                    T.config(state = NORMAL)
                    T.insert(tk.END,"Item "+str(id)+" inserido na lista 1\n")
                    T.config(state = DISABLED)
                if p.tamanho == 4:
                    T.config(state = NORMAL)
                    T.insert(tk.END,"AVISO - Lista 1 chegou ao limite de caixas\n") 
                    T.config(state = DISABLED)



#mostra todas as listas e seus conteúdos
def mostra():
    T.config(state = NORMAL)
    T.delete("1.0","end")
    T.insert(tk.END,"                   ---ARMAZÉNS---\nLista 1: "+str(p.dados)+"\nLista 2: "+str(p2.dados)+"\nLista 3: "+str(p3.dados)+"\nLista 4: "+str(p4.dados)+"\n")
    T.config(state = DISABLED)


#instanciando as pilhas
p = Pilha()
p2 = Pilha()
p3 = Pilha()
p4 = Pilha()

pad = 10 #espaçamento
janela = Tk()
janela.geometry("600x550") #tamanho inicial da janela
janela.title ("APS II - Ponto Certo Logísticas")

#área dos containers
primer = Frame()
primer.pack()

segundo = Frame()
segundo.pack()

terceiro = Frame()
terceiro.pack()

quarto = Frame()
quarto.pack()

quinto = Frame()
quinto.pack()

sexto = Frame()
sexto.pack()


#área dos widgets
    

msg = Label(segundo, text = "Ferramentas de administrador", font =("Arial",15),pady=pad)
msg.pack()

msg = Label(terceiro, text = "Insira o item: ", font =("Arial",12), pady=pad)
msg.pack(side = LEFT)
entrada = Entry(terceiro)
entrada.pack(side = RIGHT)

bt = Button(quarto, width= 40)
bt["text"] = "Adicionar"
bt["command"] = pega
bt.pack(pady=3)

bt2 = Button(quarto, width= 40)
bt2["text"] = "Excluir"
bt2["command"] = apaga
bt2.pack(pady=3)

bt3 = Button(quarto, width= 40)
bt3["text"] = "Mostrar Listas"
bt3["command"] = mostra
bt3.pack(pady=3)

T = Text(quinto, height = 18, width = 52)
T.pack(pady = 20)
dados = "                ---SEJA BEM VINDO!---\n"

sobre = Label(sexto,text = "Feito por Leonardo & Paulo Ricardo",fg="gray")
sobre.pack()

T.insert(tk.END, dados)
T.config(state = DISABLED) 
   

janela.mainloop()