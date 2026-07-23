from database import conexao
from main import produtos, tipoProduto, nomeProduto, valorProduto, qtdEstoque

cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                nome TEXT NOT NULL,
                valor FLOAT NOT NULL,
                estoque FLOAT NOT NULL
                )""")

cursor.execute("""INSERT INTO produtos (tipo, nome, valor, estoque) VALUES (?, ?, ?, ?)""", 
            (tipoProduto,
            nomeProduto,
            valorProduto,
            qtdEstoque))

def mostrarProduto():
    cursor.execute("""SELECT nome, valor, estoque FROM produtos""")
    dados = cursor.fetchall()

    for dado in dados:
        print(dado)

    cursor.close()
    conexao.close()

conexao.commit()