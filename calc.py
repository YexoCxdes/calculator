from pystyle import Colorate, Colors, Center
import time
import os
# define dat shi
ascii_art = """

 ▄████▄   ▄▄▄       ██▓     ▄████▄  
▒██▀ ▀█  ▒████▄    ▓██▒    ▒██▀ ▀█  
▒▓█    ▄ ▒██  ▀█▄  ▒██░    ▒▓█    ▄ 
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    ▒▓▓▄ ▄██▒
▒ ▓███▀ ░ ▓█   ▓██▒░██████▒▒ ▓███▀ ░
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ░▒ ▒  ░
  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░  ░  ▒   
░          ░   ▒     ░ ░   ░        
░ ░            ░  ░    ░  ░░ ░      
░                          ░        



"""

def add(a, b):
    answer = a + b
    a = f'{a} + {b} = ' + str(f'{answer}')
    print(Colorate.Vertical(Colors.blue_to_purple, a))
    time.sleep(1.5)

def sub(a, b):
    answer = a - b
    a = f'{a} - {b} = ' + str(f'{answer}')
    print(Colorate.Vertical(Colors.blue_to_purple, a))
    time.sleep(1.5)


def mul(a, b):
    answer = a * b
    a = f'{a} x {b} = ' + str(f'{answer}')
    print(Colorate.Vertical(Colors.blue_to_purple, a))
    time.sleep(1.5)


def div(a, b):
    answer = a / b
    a = str(f'{a} ÷ {b} = ') + str(answer)
    print(Colorate.Vertical(Colors.blue_to_purple, a))
    time.sleep(1.5)

while True:
    os.system('cls')
    choices = f"""
{ascii_art}
[+] Addition
[-] Subtraction
[*] Multiplication
[/] Division
"""
    print(Colorate.Vertical(Colors.blue_to_purple, choices))
    choice = input(Colorate.Horizontal(Colors.purple_to_blue, '===>'))
    if choice == '+':
        num1 = int(input(Colorate.Vertical(Colors.blue_to_purple, '1 ===>')))
        num2 = int(input(Colorate.Vertical(Colors.blue_to_purple, '2 ===>')))
        add(num1, num2)
    elif choice == '-':
        num1 = int(input(Colorate.Vertical(Colors.blue_to_purple, '1 ===>')))
        num2 = int(input(Colorate.Vertical(Colors.blue_to_purple, '2 ===>')))
        sub(num1, num2)
    elif choice == '*':
        num1 = int(input(Colorate.Vertical(Colors.blue_to_purple, '1 ===>')))
        num2 = int(input(Colorate.Vertical(Colors.blue_to_purple, '2 ===>')))
        mul(num1, num2)
    elif choice == '/':
        num1 = int(input(Colorate.Vertical(Colors.blue_to_purple, '1 ===>')))
        num2 = int(input(Colorate.Vertical(Colors.blue_to_purple, '2 ===>')))
        div(num1, num2)
    else:
        print(Colorate.Vertical(Colors.blue_to_green, 'Wrong answer!'))
        time.sleep(1.5)



