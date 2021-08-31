from tkinter import *
from tkinter import ttk
from random import seed
from random import randint
import timeit
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

#Made by Leonardo Barbosa and Paulo Ricardo

class Application:
    #construtor da GUI
    def __init__(self, master = None):

        #área dos containers
        self.primer = Frame(master)
        self.primer.pack()

        self.segundo = Frame(master)
        self.segundo.pack()

        self.terceiro = Frame(master)
        self.terceiro.pack()

        self.quarto = Frame(master)
        self.quarto.pack()

        self.quinto = Frame(master)
        self.quinto.pack()


        #área dos widgets
        self.msg0 = Label(self.primer, text = "BEM-VINDO!", font =("Arial",18))
        self.msg0.pack()    

        self.msg = Label(self.segundo, text = "Insira a qtde inicial da lista: ", font =("Arial",15))
        self.msg.pack()
        self.qtd = Entry(self.segundo)
        self.qtd.pack()

        self.bt = Button(self.terceiro)
        self.bt["text"] = "Calcular"
        self.bt["command"] = self.pega_num 
        self.bt.pack()

        #relacionado a tabela
        self.tb = Label(self.quarto, text="Tempos de Execução", font=("Arial",25)).grid(row=0, columnspan=3)
        cols = ("Qtd. de itens","Bubble Sort","Insertion Sort")  
        self.listBox = ttk.Treeview(self.quarto, columns=cols, show="headings")
        for col in cols:
            self.listBox.heading(col, text = col)

        self.listBox.grid(row=1, column=0, columnspan=1)

        #Botões para janela Pop-up e clear
        self.bt2 = Button(self.quinto)
        self.bt2["text"] = "Gerar Gráfico"
        self.bt2["command"] = self.abrir_janela
        self.bt2.pack(side = LEFT)

        self.bt3 = Button(self.quinto)
        self.bt3["text"] = "Limpar"
        self.bt3["command"] = self.limpar_tabela
        self.bt3.pack(side = RIGHT)



    #função que pega o número inserido
    def pega_num(self):
        num = self.qtd.get() 
        convert = int(num) #converte para int o valor

            
        for i in range(1,5): 
                
            lista = teste(convert)
            lista2 = list.copy(lista)#bubbleSort
            lista3 = list.copy(lista)#InsertionSort 

            #Funções
            tic = timeit.default_timer()
            bubbleSort(lista2) #chamando a função 
            toc = timeit.default_timer()
            tempo1 = toc - tic
            tempos1.append(tempo1)


            tic = timeit.default_timer()
            insertionSort(lista3) #chamando a função 
            toc = timeit.default_timer()
            tempo2 = toc - tic
            tempos2.append(tempo2)

            #insere as info na tabela
            qtd.append(convert)
            self.listBox.insert("","end",values = (convert,tempo1,tempo2))

            #incrementa o valor
            convert *= 10
            

    #reseta a tabela ao estado original
    def limpar_tabela(self):
        for i in self.listBox.get_children():
            self.listBox.delete(i)


    #abre outra janela para o gráfico  
    def abrir_janela(self):
        nv_janela = Toplevel(janela) #"chama" uma nova janela

        fig, ax = plt.subplots()  # Cria a área do gráfico

        #necessário adicionar os respectivos arrays nas linhas abaixo (convert, tempo1 e 2)

        ax.plot(qtd,tempos1,label = "Bubble Sort")  # inserção de info 1 no gráfico(e label)
        ax.plot(qtd,tempos2, label = "Insertion Sort") # inserção de info 2 no gráfico(e label)


        ax.set_xlabel("Qtd. de itens")
        ax.set_ylabel("Tempo em seg.")
        line2 = FigureCanvasTkAgg(fig, nv_janela)
        line2.get_tk_widget().pack()
        ax.set_title('Tamanho x Tempo')
        ax.legend()




def teste(num):
    seed(1)
    output = []
    for i in range(num):
        x = randint(0,500)
        output.append(x)

    return output        


def bubbleSort(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp


def insertionSort(lista):
   for i in range(1,len(lista)):

     valoratual = lista[i]
     posicao = i

     while posicao > 0 and lista[posicao-1] > valoratual:
         lista[posicao] = lista[posicao-1]
         posicao = posicao-1

     lista[posicao]=valoratual


janela = Tk()
janela.title ("APS Estrutura I")
Application(janela)

#inicialização de arrays
tempos1 = [] #bubble sort
tempos2 = [] #insertion sort
qtd = [] #tamanho das listas


janela.mainloop()