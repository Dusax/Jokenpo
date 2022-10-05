import random
import PySimpleGUI as sg
from time import sleep

# função que sorteia a escolha da máquina
def jokenpo():
    list = ['pedra', 'papel', 'tesoura']
    number = random.randint(0, 2)
    choice_maquina = list[number]
    return choice_maquina

# função que verifica o resultado final e retorna um valor dependendo do resultado
def verification(choice, machine):
    if machine == 'pedra':

        if choice == 'Pedra':
            draw = 0
            return draw
        
        elif choice == "Papel":
            win_player = 1
            return win_player
        
        elif choice == 'Tesoura':
            win_machine = 2
            return win_machine
    
    if machine == 'papel':

        if choice == 'Papel':
            draw = 0
            return draw
        
        elif choice == "Tesoura":
            win_player = 1
            return win_player
        
        elif choice == 'Pedra':
            win_machine = 2
            return win_machine
    
    if machine == 'tesoura':

        if choice == 'Tesoura':
            draw = 0
            return draw
        
        elif choice == "Pedra":
            win_player = 1
            return win_player
        
        elif choice == 'Papel':
            win_machine = 2
            return win_machine

# criando o layout da interface
sg.theme('DarkAmber') 
layout = [[sg.Text('Seja bem vindo ao Jokenpô!')], 
            [sg.Text(key=1)],
            [sg.Text(key='-OUTPUT-')], 
            [sg.Text(key=2)],
          [sg.Button('Papel'), sg.Button('Pedra'), sg.Button('Tesoura'), sg.Button('Sair')]]
          

window = sg.Window('Jokenpô', layout) 

# inicío do jogo
while True: 
    event, values = window.read() 
    print(event, values) 
      
    if event in  (None, 'Sair'): 
        break
      
    if event == 'Pedra': 
        choice = str(jokenpo())
        window[1].update("JO..\nKEN..\nPÔ..")
        window['-OUTPUT-'].update(f"A escolha da máquina foi {choice.upper()}")

        result = verification(event, choice)

        if result == 1:
            window[2].update("Você venceu!")
        elif result == 2:
            window[2].update("A máquina venceu!")
        elif result == 0:
            window[2].update("Empate!")



    if event == 'Papel': 
        choice = str(jokenpo())
        window[1].update("JO..\nKEN..\nPÔ..")
        window['-OUTPUT-'].update(f"A escolha da máquina foi {choice.upper()}")
        
        result = verification(event, choice)

        if result == 1:
            window[2].update("Você venceu!")
        elif result == 2:
            window[2].update("A máquina venceu!")
        elif result == 0:
            window[2].update("Empate!")


    if event == 'Tesoura': 
        choice = str(jokenpo())
        window[1].update("JO..\nKEN..\nPÔ..")
        window['-OUTPUT-'].update(f"A escolha da máquina foi {choice.upper()}")  

        result = verification(event, choice)

        if result == 1:
            window[2].update("Você venceu!")
        elif result == 2:
            window[2].update("A máquina venceu!")
        elif result == 0:
            window[2].update("Empate!")

window.close() 