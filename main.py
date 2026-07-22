# Cadastrar Produto
print("--Sistema de Cadastro de Produtos--")
nomeProduto = input("Insira o nome do produto: ")
unidadeProduto = input("Tipo de unidade: ")
valorProduto = float(input("Valor unitário: "))
qtdEstoque = float(input("Estoque disponivel: "))

produtos = {
    "frutas": {
        "nome": nomeProduto,
        "unidade": unidadeProduto,
        "valor": valorProduto,
        "estoque": qtdEstoque
    }
}

print("Produto Cadastrado!")

#--------------------------

#Buscar Pordutos
buscarProduto = input("Qual produto deseja buscar?: ")

if buscarProduto == nomeProduto:
    for produto in produtos.values():
        print(produto)
else: 
    print("Produto não encontrado ou não cadastrado!")

#--------------------------

#Alterar valores do produto
alterarProduto = input("O que deseja alterar?: \n Valor do Produto - 1 \n Quantidade no estoque - 2 \n Nome do Produto - 3 \n Unidade de pesagem - 4 \n")
match alterarProduto:
    case "1":
        novoValor = float(input("Qual será o novo valor?: "))
        produtos["valor"] = novoValor
        print("Valor Alterado")
    case "2":
        novaQtd = float(input("Nova quantidade em estoque: "))
        produtos["estoque"] = novaQtd
        print("Estoque Alterado")
    case "3":
        novoNome = input("Qual o nome do produto: ")
        produtos["nome"] = novoNome
        print("Nome Alterado")
    case "4":
        novaUnidade = input("Qual unidade de pesagem?: ")
        produtos["unidade"] = novaUnidade
        print("Unidade Alterada")
    case _:
        print("Alteração não realizada!")
#--------------------

#Excluir produto
removerProduto = input("Qual produto deseja remover? ")

if removerProduto == 