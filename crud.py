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

cursor.execute("""SELECT nome, valor, estoque FROM produtos""")
valores = cursor.fetchall()

conexao.commit()