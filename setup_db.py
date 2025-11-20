import sqlite3

NOME_DO_BANCO = 'clinica_vidamais.db'


def criar_tabela_pacientes():
    """Cria o banco de dados e a tabela 'pacientes'."""
    try:

        conn = sqlite3.connect(NOME_DO_BANCO)
        cursor = conn.cursor()

        sql_comando = """
                      CREATE TABLE IF NOT EXISTS pacientes \
                      ( \
                          id \
                          INTEGER \
                          PRIMARY \
                          KEY \
                          AUTOINCREMENT, \
                          nome \
                          TEXT \
                          NOT \
                          NULL, \
                          idade \
                          INTEGER \
                          NOT \
                          NULL, \
                          telefone \
                          TEXT
                      ); \
                      """

        cursor.execute(sql_comando)

        conn.commit()
        conn.close()

        print(f"✅ Sucesso! Tabela 'pacientes' criada no banco {NOME_DO_BANCO}.")

    except sqlite3.Error as e:
        print(f"❌ Erro ao criar a tabela: {e}")


if __name__ == "__main__":
    criar_tabela_pacientes()