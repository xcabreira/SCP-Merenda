# Cadastrar Produto
print("--Sistema de Cadastro de Produtos--")
nomeProduto = input("Insira o nome do produto: ")
unidadeProduto = input("Tipo de unidade: ")
valorProduto = float(input("Valor unitário: "))
qtdEstoque = float(input("Estoque disponivel: "))

produtos = {
    "nome": nomeProduto,
    "unidade": unidadeProduto,
    "valor": valorProduto,
    "estoque": qtdEstoque
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
alterarProduto = input("Deseja alterar o produto?: y/n")
if alterarProduto == "y":
    alteracao = input("O que deseja alterar?: \n Valor do Produto - 1 \n Quantidade no estoque - 2 \n Nome do Produto - 3 \n Unidade de pesagem - 4")
    match alteracao:
        case 1:
            novoValor = float(input("Qual será o novo valor?: "))
            produtos["valor"] = novoValor
        case 2:
            novaQtd = float(input("Nova quantidade em estoque: "))
            produtos["estoque"] = novaQtd
        case 3:
            novoNome = input("Qual o nome do produto: ")
            produtos["nome"] = novoNome
        case 4:
            novaUnidade = input("Qual unidade de pesagem?: ")
            produtos["unidade"] = novaUnidade
            
#--------------------

#Excluir produto
