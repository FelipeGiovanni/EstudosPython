import sqlite3

def CriaTabela():
    conn = sqlite3.connect('db_estudos.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Armas (
        Nome varchar(20),
        Custo INTEGER,
        Dano INTEGER,
        Peso INTEGER
    );''')
    conn.close()


def InsereDados(nome, custo, dano, peso):
    conn = sqlite3.connect('db_estudos.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO Armas VALUES ('{nome}',{custo},{dano},{peso})")
    conn.commit()
    conn.close()

def ConsultaArsenal():
    conn = sqlite3.connect('db_estudos.db')
    c = conn.cursor()
    for row in c.execute("SELECT * FROM ARMAS"):
        print(row)
    conn.close()