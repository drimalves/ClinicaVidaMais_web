from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
NOME_DO_BANCO = 'clinica_vidamais.db'


# --- Funções de Conexão com o Banco de Dados (CRUD - Create, Read, Update, Delete) ---

def get_conexao():
    """Cria e retorna a conexão com o banco de dados."""
    return sqlite3.connect(NOME_DO_BANCO)


def inserir_paciente_db(nome, idade, telefone):
    """Insere um novo registro de paciente no banco."""
    conn = get_conexao()
    cursor = conn.cursor()

    # O comando SQL usa '?' como placeholder para evitar injeção de SQL
    sql_comando = "INSERT INTO pacientes (nome, idade, telefone) VALUES (?, ?, ?)"
    cursor.execute(sql_comando, (nome, idade, telefone))

    conn.commit()
    conn.close()


def listar_todos_db():
    """Busca e retorna todos os pacientes do banco."""
    conn = get_conexao()
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome (ex: paciente['nome'])
    cursor = conn.cursor()

    sql_comando = "SELECT id, nome, idade, telefone FROM pacientes ORDER BY nome ASC"
    cursor.execute(sql_comando)

    # fetchall() pega todos os resultados da busca
    pacientes = cursor.fetchall()
    conn.close()
    return pacientes


# --- Rotas do Flask (Front-end) ---

@app.route('/')
def index():
    """Rota da página inicial: Lista todos os pacientes."""
    pacientes = listar_todos_db()
    # Envia os dados dos pacientes para o arquivo HTML
    return render_template('index.html', pacientes=pacientes)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Rota para o cadastro de novos pacientes."""
    if request.method == 'POST':
        # Se o método for POST, significa que o formulário foi enviado

        # Pega os dados enviados pelo formulário HTML (request.form)
        nome = request.form['nome']
        idade = request.form['idade']
        telefone = request.form['telefone']

        # Chama a função Python para inserir no Banco de Dados
        inserir_paciente_db(nome, int(idade), telefone)

        # Redireciona o usuário de volta para a lista inicial
        return redirect(url_for('index'))

    # Se o método for GET, apenas exibe o formulário HTML
    return render_template('cadastro.html')


if __name__ == '__main__':
    # Roda a aplicação no modo debug (ótimo para desenvolvimento)
    app.run(debug=True)