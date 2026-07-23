import time
from crud import mostrarProduto
# Inicio
print("--Sistema de Cadastro de Produtos--")
opcaoIniciar = input("1 - Cadastrar produto \n 2 - Buscar produto \n 3 - Editar produtos \n 4 - Excluir produto \n 5 - Sair \n")

# Cadastrar Produto
if opcaoIniciar == "1":
    tipoProduto = input("Qual o tipo de produto? Ex.: Frutas, Carnes, Bebidas, etc...: ")
    nomeProduto = input("Insira o nome do produto: ")
    valorProduto = float(input("Valor unitário: "))
    qtdEstoque = float(input("Estoque disponivel: "))

    produtos = {
        tipoProduto: {
            nomeProduto: {
                "valor": valorProduto,
                "estoque": qtdEstoque
            }
        }
    }

    print("Produto Cadastrado! \n")

#--------------------------

#Buscar Pordutos
if opcaoIniciar == "2":
    buscarProduto = input("Qual produto deseja buscar?: ")

    if buscarProduto == nomeProduto:
        mostrarProduto()
    else: 
        print("Produto não encontrado ou não cadastrado!")

#--------------------------

#Alterar valores do produto
if opcaoIniciar == "3":
    alterarProduto = input("Qual produto deseja alterar? insira o nome do produto: ")
    if alterarProduto == nomeProduto:
        alterarEscolha = input("O que deseja alterar?: \n Valor do Produto - 1 \n Quantidade no estoque - 2 \n Nome do Produto - 3 \n")
        match alterarEscolha:
            case "1":
                novoValor = float(input("Qual será o novo valor?: "))
                produtos[tipoProduto][nomeProduto]["valor"] = novoValor
                print("Valor Alterado")
            case "2":
                novaQtd = float(input("Nova quantidade em estoque: "))
                produtos[tipoProduto][nomeProduto]["estoque"] = novaQtd
                print("Estoque Alterado")
            case "3":
                novoNome = input("Qual o nome do produto: ")
                produtos[tipoProduto][nomeProduto] = novoNome
                print("Nome Alterado") 
            case _:
                print("Alteração não realizada!")
    else: 
        print("Produto não encontrado!")
#--------------------

#Excluir produto
if opcaoIniciar == "4":
    removerProduto = input("Qual produto deseja remover? ")

    if removerProduto == nomeProduto:
        del produtos[tipoProduto][nomeProduto]
        print(f"Produto {nomeProduto} removido")
if opcaoIniciar == "5":
    print("saindo...")
    time.sleep(1.5)
    print("Até a próxima!")
     