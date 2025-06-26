"""Cria tabela e implementa CRUD

CRUD:
    Create
    Read
    Update
    Delete
"""
import sqlite3

ARQUIVO_DATABASE = 'base_dados.db'

class PratoJaExiste(Exception):
    pass

class PratoNaoExiste(Exception):
    pass

class TabelaJaExiste(Exception):
    pass


def cria_tabela():
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    try:
        cur.execute(SQL_CREATE_TABLE)
    except sqlite3.OperationalError:
        raise TabelaJaExiste('Tabela pratos já existe')
    finally:
        con.close()


def novo_prato(nome, ingredientes, preco):
    """Cria prato novo na tabela
    
    """
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    try:
        cur.execute(SQL_NOVO_PRATO,
                    {'nome': nome,
                     'ingredientes': ingredientes,
                     'preco': preco})
    except sqlite3.IntegrityError:
        raise PratoJaExiste(f'Prato com nome {nome} já existe!')
    else:
        con.commit()
    finally:
        con.close()


def obtem_dados(nome):
    """Obtem prato da tabele
    
    """
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    res = cur.execute(SQL_OBTEM_PRATO,
                      {'nome': nome})
    res = res.fetchall()
    con.close()
    if len(res) == 0:
        raise PratoNaoExiste(f'Não há prato com nome {nome}.')
    else:
        return {'id': res[0][0],
                'ingredientes': res[0][1],
                'preco': res[0][2],
                'nome': nome,
                }


def atualiza_informacoes(id_prato, nome, ingredientes, preco):
    """Atualiza informações do prato
    
    """
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    try:
        res = cur.execute(SQL_UPDATE_PRATO,
                          {'id': id_prato,
                           'nome': nome,
                           'ingredientes': ingredientes,
                           'preco': preco,
                           })
    except sqlite3.IntegrityError:
        raise PratoJaExiste(f'Prato com nome {nome} já existe!')
    else:
        con.commit()
    finally:
        con.close()


def deleta_prato(id_prato):
    """Deleta usuário
    
    """
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    res = cur.execute(SQL_DELETA_PRATO,
                      {'id': id_prato})
    con.commit()
    con.close()


def obtem_todos_pratos():
    """Obtem todos os pratos"""
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    res = cur.execute(SQL_TODOS_PRATOS)
    res = res.fetchall()
    con.close()
    return [{'id': r[0],
             'nome': r[1],
             'preco': r[2]}
            for r in res]
    

SQL_CREATE_TABLE = """
CREATE TABLE
pratos
(
  id integer primary key not null unique,
  nome text unique not null,
  ingredientes text,
  preco real
)
;
"""


SQL_NOVO_PRATO = """
INSERT INTO
pratos
(nome, ingredientes, preco)
values
(:nome, :ingredientes, :preco)
;
"""


SQL_OBTEM_PRATO = """
SELECT
  id, ingredientes, preco
FROM
  pratos
WHERE
  nome=:nome
;
"""

SQL_TODOS_PRATOS = """
SELECT
  id, nome, preco
from
  pratos
"""


SQL_UPDATE_PRATO = """
UPDATE
  pratos
SET
  nome=:nome,
  ingredientes=:ingredientes,
  preco=:preco
WHERE
  id=:id
;
"""

SQL_DELETA_PRATO = """
DELETE FROM
  pratos
WHERE
  id=:id
;
"""

def main():
    cria_tabela()
    novo_prato("Arroz e Feijão", #nome do prato
               "Arroz e Feijão", # ingredientes
                15.0) # preço
    novo_prato("Macarrão ao sugo",
               "macarrão, molho de tomate",
                15.0)
    novo_prato("Baião de dois",
               "Arroz, feijão fradinho, bacon, calabresa, ovo",
                15.0)
    
if __name__ == '__main__':
    main()

