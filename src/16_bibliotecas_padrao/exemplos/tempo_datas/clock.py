from tkinter import *  # Importa todos os símbolos do módulo tkinter
from tkinter.ttk import *  # Importa todos os símbolos do submódulo ttk do tkinter
from time import strftime  # Importa a função strftime do módulo time

root = Tk()  # Cria uma instância da classe Tk para criar uma janela principal
root.title('Clock')  # Define o título da janela como 'Clock'

def time():  # Define uma função chamada time
    # Obtém a string formatada de hora atual no formato HH:MM:SS AM/PM
    string = strftime('%H:%M:%S %p')  
    lbl.config(text=string)  # Atualiza o texto do rótulo (label) com a hora atual
    lbl.after(1000, time)  # Chama a função time novamente após 1000ms (1 segundo)

# Cria um rótulo (label) para exibir o horário
lbl = Label(root, font=('calibri', 40, 'bold'), 
            background='purple', 
            foreground='white') 
lbl.pack(anchor='center')  # Empacota o rótulo no centro da janela

time()  # Chama a função time para iniciar a atualização do relógio

mainloop()  # Inicia o loop principal da interface gráfica (GUI)
