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
        print(f"{indice}. [{status}]")




tarefas = []
while True:
    print("=============== MENU DO GERENCIADOR ===============")
    print("\n1. Adicionar uma tarefa")
    print("2. Visualizar tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar uma tarefa")
    print("6. Sair")
    print("\n===================================================")


    escolha = input("O que deseja fazer? ")
    if escolha == "1":
        tf_nome = input("Digite o nome da tarefa: ")
        tf_adicionar(tarefas, tf_nome)
        
    elif escolha == "2":
        tf_visualizar(tarefas)
        
    elif escolha == "6":
        break
    
    
    
    
print("Programa finalizado.")