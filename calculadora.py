#Importando Tkinter
from tkinter import *
from tkinter import ttk

#Cores da calculadora
cor1 = "#181618" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #Laranja

#Janela e dimensão da calculadora
janela =Tk()
janela.title("Calculadora")
janela.geometry("240x310")
janela.config(bg=cor1)
janela.iconbitmap('icon_calculadora.ico') #icone da Calculadora
janela.resizable(False, False)


frame_tela = Frame(janela, width=240, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_numero = Frame(janela, width=235, height=268)
frame_numero.grid(row=1, column=0)


#Para cada linha e coluna
for i in range(6):  # Supondo que você tenha 5 linhas
    frame_numero.grid_rowconfigure(i, weight=1)

for i in range(4):  # Supondo que você tenha 4 colunas
    frame_numero.grid_columnconfigure(i, weight=1)

#Variavel Todos os Valores
todos_valores = ''


#Criar a função 
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    

    #Passando valor para tela
    valor_texto.set(todos_valores)


#Função Para Calcular
def calcular():
    global todos_valores
    try:
        if "%" in todos_valores:
            porcentagem = todos_valores.split("+")
            todos_valores = str(float(porcentagem[0]) + (float(porcentagem[0]) * float(porcentagem[1].replace('%', ''))/100))
        resultado = eval(todos_valores)
        #Formatar o resultado
        if resultado > 1e10:
            resultado = '{:.2e}'.format(resultado)  # Notação científica com 2 casas decimais
        else:
            resultado = round(resultado, 2)  # Arredonda o resultado para 2 casas decimais
        valor_texto.set(str(resultado))
    except Exception as e:
        valor_texto.set("Erro")
    todos_valores = ""


#Função para verificar se a tecla "=" foi pressionada
def verificar_tecla(event):
    if event.keysym == 'equal' or event.keysym == 'return':
        calcular()


#Função Pra Limpar Tela
def limpar_tela(event=None):
    global todos_valores
    todos_valores =""
    valor_texto.set("")


#Função para apagar o último caractere
def apagar_ultimo(event=None):
    global todos_valores
    todos_valores = todos_valores[:-1]
    valor_texto.set(todos_valores)


#Vincular as teclas numéricas às funções correspondentes
janela.bind('1', lambda event: entrar_valores('1'))
janela.bind('2', lambda event: entrar_valores('2'))
janela.bind('3', lambda event: entrar_valores('3'))
janela.bind('4', lambda event: entrar_valores('4'))
janela.bind('5', lambda event: entrar_valores('5'))
janela.bind('6', lambda event: entrar_valores('6'))
janela.bind('7', lambda event: entrar_valores('7'))
janela.bind('8', lambda event: entrar_valores('8'))
janela.bind('9', lambda event: entrar_valores('9'))
janela.bind('0', lambda event: entrar_valores('0'))


#Vincular as teclas de operadores às funções correspondentes
janela.bind('+', lambda event: entrar_valores('+'))
janela.bind('-', lambda event: entrar_valores('-'))
janela.bind('*', lambda event: entrar_valores('*'))
janela.bind('/', lambda event: entrar_valores('/'))
janela.bind('%', lambda event: entrar_valores('%'))
janela.bind('<Key>', verificar_tecla) #Verificar se foi apertado o "="


#Vincular a tecla 'BackSpace' à função apagar_ultimo
janela.bind('<BackSpace>', apagar_ultimo)


#Vincular a tecla Enter à função calcular
janela.bind('<Return>', lambda event: calcular())


#Vincular a tecla ESC à função limpar_tela
janela.bind('<Escape>', limpar_tela)


#Criando Label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.grid(row=0,column=0)

#Botões da calculadora
#Operadores
b_1 = Button(frame_numero, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.grid(row=0, column=0, columnspan=2, sticky='nsew')  # Botão 'C' ocupa 2 colunas
b_2 = Button(frame_numero, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.grid(row=0, column=2, sticky='nsew')
b_3 = Button(frame_numero, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.grid(row=0, column=3, sticky='nsew')

#Numeros > (7 ao 9 e *)
b_4 = Button(frame_numero, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.grid(row=1, column=0, sticky='nsew')
b_5 = Button(frame_numero, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.grid(row=1, column=1, sticky='nsew')
b_6 = Button(frame_numero, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.grid(row=1, column=2, sticky='nsew')
b_7 = Button(frame_numero, command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.grid(row=1, column=3, sticky='nsew')

#Numeros > (4 ao 6 e -)
b_8 = Button(frame_numero, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.grid(row=2, column=0, sticky='nsew')
b_9 = Button(frame_numero, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.grid(row=2, column=1, sticky='nsew')
b_10 = Button(frame_numero, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.grid(row=2, column=2, sticky='nsew')
b_11 = Button(frame_numero, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.grid(row=2, column=3, sticky='nsew')

#Numeros > (1 ao 3 e +)
b_12 = Button(frame_numero, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.grid(row=3, column=0, sticky='nsew')
b_13 = Button(frame_numero, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.grid(row=3, column=1, sticky='nsew')
b_14 = Button(frame_numero, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.grid(row=3, column=2, sticky='nsew')
b_15 = Button(frame_numero, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.grid(row=3, column=3, sticky='nsew')

#Botão '='
b_16 = Button(frame_numero, command = calcular, text="=", width=11, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.grid(row=4, column=0, columnspan=2, sticky='nsew')

#Numeros > (0)
b_17 = Button(frame_numero, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.grid(row=4, column=2, columnspan=2, sticky='nsew')


janela.mainloop()