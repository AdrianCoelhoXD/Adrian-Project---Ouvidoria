from Ouvidoria_functions import Commands

aux = Commands()

print("Bem vindo a versão 4 da Ouvidoria ")
nome = "Adrian" #input("Digite seu nome: ")
print(f" Bem vindo {nome} !! Você está no sistema de ouvidoria v4 ")
print()

condition = True
while condition:

    print()    
    print(" (1) Inserir ocorrência")
    print(" (2) Listar ocorrência")
    print(" (3) Apagar ocorrência")
    print(" (4) Alterar ocorrência")
    print(" (5) Sair")
    print()
    print(" Selecione um opção: ")

    option = input(">> ")

    if option == "1":
       
        print()   
        print(" (1) Sugestão ")
        print(" (2) Elogio")
        print(" (3) Reclamação ")
        print(" (4) Sair ")
        print()
        print("Qual ocorrência deseja inserir ?")

        ocorrencia = input()
        text = input("Digite >> ")

        if ocorrencia == "1":
            ocorrencia = "Sugestão"
            aux.insert(ocorrencia,text)
            print("Ocorrêcia inserida!")

        elif ocorrencia == "2":
            ocorrencia = "Elogio"
            aux.insert(ocorrencia,text)
            print("Ocorrêcia inserida!")

        elif ocorrencia == "3":
            ocorrencia = "Reclamação"   
            aux.insert(ocorrencia,text)
            print("Ocorrêcia inserida!")

        elif ocorrencia == "4":
            ocorrencia= ""
            text = ""
        else:
            print("Ocorrência inválida!")
            print()

    elif option == "2":

        print("Qual ocorrência deseja listar ?")
        print()
        print(" (1) Sugestão ")
        print(" (2) Elogio")
        print(" (3) Reclamação ")
        print(" (4) Todas ")
        print(" (5) Sair")

        ocorrencia = input()

        if ocorrencia == "1":
            ocorrencia = "Sugestão"
            aux.listing(ocorrencia)  

        elif ocorrencia == "2":
            ocorrencia = "Elogio"
            aux.listing(ocorrencia)

        elif ocorrencia == "3":
            ocorrencia = "Reclamação"
            aux.listing(ocorrencia)

        elif ocorrencia == "4":
            aux.listingAll()

        elif ocorrencia == "5":
            print("")
        else:
            print("Ocorrência inválida!")
            print()

    elif option == "3":

        print("O'que deseja apagar ?")
        print()
        print(" (1) Todas as Sugestões ")
        print(" (2) Todos os Elogios")
        print(" (3) Todas as Reclamaçãoes ")
        print(" (4) Tudo")
        print(" (5) Ocorrencia Específica ")
        print(" (6) Sair ")

        ocorrencia = input()

        if ocorrencia == "1":
            ocorrencia = 'Sugestão'
            aux.delete(ocorrencia) 
            print(" Você apagou todas suas sugestões !!")
            
        elif ocorrencia == "2":
            ocorrencia = 'Elogio'
            aux.delete(ocorrencia) 
            print(" Você apagou todos os seus elogios !!")
    
        elif ocorrencia == "3":
            ocorrencia = 'Reclamação'
            aux.delete(ocorrencia) 
            print(" Você apagou todas suas Reclamações !!")

        elif ocorrencia == "4":
            aux.deleteAll()
            print(" Você apagou todas suas ocorrências !!")

        elif ocorrencia == "5": 
            aux.listingAll()
            print("Digite o ID da ocorrencia que deseja apagar !")
            id = (input("Digite um ID >> "))
            aux.deleteID(id)
            print(f"Ocorrencia {id} apagada !")

        elif ocorrencia == "6":
            print("")

        else:
            print("Ocorrência inválida!")
            print()

    elif option == "4":

        print("Qual ocorrência deseja alterar ?")
        aux.listingAll()
        id = (input("Digite o ID que deseja alterar >> "))
        texto = (input("Digite o novo comentário: "))
        aux.change(texto,id) 
        print("Ocorrencia foi alterada !")
            
    elif option == "5":
        print("Até breve !!")
        print()
        condition = False
    else:
        print("Algo deu errado !!")
        print()