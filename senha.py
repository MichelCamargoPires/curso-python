from random import*
from time import sleep

acho = ""
senha = input('digite uma senha: ')

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
          'u', 'v', 'w', 'x', 'y', 'z', 'ç', '1', '2', '3', 
          '4', '5', '6', '7', '8', '9', '0', '!', '@', '#',
          '$', '%', '*', '(', ')', '{','}', '^', '~',' ?']
while (acho != senha):
    acho = ''
    for letra in senha:
        acholetra = letras [randint(0, 49)]
        acho = str(acholetra) + str(acho)
    print('\033[32m{}\033[m'.format(acho), end= '')
print('\n')       
print('\033[31m                               =  =\033[m')
sleep(1)
print('\033[31m                           =         $\033[m')
sleep(1)
print('\033[31m       > *                =           4\033[m')
sleep(1)
print('\033[31m     1     <              2           =\033[m')
sleep(1)
print('\033[31m    1     9                m        =\033[m')
sleep(1)
print('\033[31m     1 0                      + %\033[m')  
print('\033[31m                  =\033[m') 
sleep(1)    
print('\033[31m                 ===\033[m')
               
print('\033[31mSUA SENHA E: {}\033[m'.format(acho))                
