#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


Nome=input("Qual seu nome?")

idade=int(input("Em qual ano você nasceu ?"))

while True:

        try:

                idade=int(input("Em qual ano você nasceu ?"))

                if(idade<2021) and (idade>1922):

                        idade_atual=2022-idade

                print(Nome,", você completará:",idade_atual,"anos")

        except:
                idade=int(input("Em qual ano você nasceu ?"))
        

        