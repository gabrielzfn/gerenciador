def tf_adicionar(tarefas, tf_nome):
    tarefa = {"Tarefa": tf_nome, "Completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa {tf_nome} foi adicionada com sucesso!")
    return


def tf_visualizar(tarefas):
    print("\nLista de tarefas: ")
    for indice, tarefa in enumerate(tarefas, start=1):
        status  = "✓" if tarefa ["Completada"] else " "
        tf_nome = tarefa["tarefa"]
        print(f"{indice}. [{status}] {tf_nome}")
        
        
def tf_atualizar(tarefas, tf_indice, tf_novo_nome):
    tf_ajustado = int(tf_indice) - 1
    if tf_ajustado >= 0 and tf_ajustado < len(tarefas):
        tarefas[tf_ajustado]["tarefa"] =  tf_novo_nome
        print(f"A tarefa {tf_indice} foi alterada para {tf_novo_nome}.")
    else:
        print("Índice da tarefa inválido.")
    return


def tf_completar(tarefas, tf_indice):
    tf_ajustado = int(tf_indice) - 1
    tarefas[tf_ajustado]["completada"] = True
    print(f"Tarefa {tf_indice} completada!")
    return




tarefas = []
while True:
    print("=============== MENU DO GERENCIADOR ===============")
    print("1. Adicionar uma tarefa")
    print("2. Visualizar tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar uma tarefa")
    print("6. Sair")
    print("===================================================")


    escolha = input("O que deseja fazer? ")
    if escolha == "1":
        tf_nome = input("Digite o nome da tarefa: ")
        tf_adicionar(tarefas, tf_nome)
        
    elif escolha == "2":
        tf_visualizar(tarefas)
        
    elif escolha == "3":
        tf_visualizar(tarefas)   
        tf_indice = input("Selecione a tarefa que deseja atualizar: ")
        tf_nvnome = input("Digite o novo nome da tarefa selecionada:")
        tf_atualizar(tarefas, tf_indice, tf_nvnome)
        
    elif escolha == "4":
        tf_visualizar(tarefas)
        tf_indice = int(input("Selecione a tarefa a ser completada: "))
        tf_completar
        
    
    elif escolha == "6":
        break
    
    
    
    
print("Programa finalizado.")