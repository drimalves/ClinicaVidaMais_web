from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
NOME_DO_BANCO = 'clinica_vidamais.db'



def get_conexao():
    return sqlite3.connect(NOME_DO_BANCO)


def inserir_paciente_db(nome, idade, telefone):
    conn = get_conexao()
    cursor = conn.cursor()

    sql_comando = "INSERT INTO pacientes (nome, idade, telefone) VALUES (?, ?, ?)"
    cursor.execute(sql_comando, (nome, idade, telefone))

    conn.commit()
    conn.close()


def listar_todos_db():
    conn = get_conexao()
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome (ex: paciente['nome'])
    cursor = conn.cursor()

    sql_comando = "SELECT id, nome, idade, telefone FROM pacientes ORDER BY nome ASC"
    cursor.execute(sql_comando)

    pacientes = cursor.fetchall()
    conn.close()
    return pacientes



@app.route('/')
def index():
    pacientes = listar_todos_db()
    return render_template('index.html', pacientes=pacientes)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':

        nome = request.form['nome']
        idade = request.form['idade']
        telefone = request.form['telefone']

        inserir_paciente_db(nome, int(idade), telefone)

        return redirect(url_for('index'))

    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)