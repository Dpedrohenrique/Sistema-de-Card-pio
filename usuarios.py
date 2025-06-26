"""Cria tabela e implementa CRUD

CRUD:
  Create
  Read
  Update
  Delete
"""
import sqlite3

ARQUIVO_DATABASE = 'base_dados.db'

class UsuarioJaExiste(Exception):
    pass

class UsuarioNaoExiste(Exception):
    pass

class TabelaJaExiste(Exception):
    pass


def cria_tabela():
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    try:
        cur.execute(SQL_CREATE_TABLE)
    except sqlite3.OperationalError:
        raise TabelaJaExiste('Tabela usuarios já existe')
    finally:
        con.close()


def novo_usuario(nome, endereco, tel):
    """Cria usuário novo na tabela
    
    """
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    try:
        cur.execute(SQL_NOVO_USUARIO,
                    {'nome': nome,
                     'endereco': endereco,
                     'tel': tel})
    except sqlite3.IntegrityError:
        raise UsuarioJaExiste(f'Usuário com telefone {tel} já existe!')
    else:
        con.commit()
    finally:
        con.close()


def obtem_dados(tel):
    """Obtem usuário da tabela
    
    """
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    res = cur.execute(SQL_OBTEM_USUARIO,
                      {'tel': tel})
    res = res.fetchall()
    con.close()
    if len(res) == 0:
        raise UsuarioNaoExiste(f'Não há usuário com telefone {tel}.')
    else:
        return {'id': res[0][0],
                'nome': res[0][1],
                'endereco': res[0][2],
                'tel': tel,
                }


def atualiza_informacoes(id_usuario, nome, endereco, tel):
    """Atualiza informações do usuário
    
    """
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    res = cur.execute(SQL_UPDATE_USUARIO,
                      {'id': id_usuario,
                       'nome': nome,
                       'endereco': endereco,
                       'tel': tel,
                       })
    con.commit()
    con.close()


def deleta_usuario(id_usuario):
    """Deleta usuário
    
    """
    con = sqlite3.connect(ARQUIVO_DATABASE)
    cur = con.cursor()
    res = cur.execute(SQL_DELETA_USUARIO,
                      {'id': id_usuario})
    con.commit()
    con.close()


SQL_CREATE_TABLE = """
CREATE TABLE
usuarios
(
  id integer primary key not null unique,
  nome text,
  endereco text,
  tel text unique not null
)
;
"""

SQL_NOVO_USUARIO = """
INSERT INTO
usuarios
(nome, endereco, tel)
values
(:nome, :endereco, :tel)
;
"""

SQL_OBTEM_USUARIO = """
SELECT
  id, nome, endereco
FROM
  usuarios
WHERE
  tel=:tel
;
"""

SQL_UPDATE_USUARIO = """
UPDATE
  usuarios
SET
  nome=:nome,
  endereco=:endereco,
  tel=:tel
WHERE
  id=:id
;
"""


SQL_DELETA_USUARIO = """
DELETE FROM
  usuarios
WHERE
  id=:id
;
"""
