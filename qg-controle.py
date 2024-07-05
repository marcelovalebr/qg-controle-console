import mysql.connector
from datetime import datetime
from fpdf import FPDF

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",  # Altere para seu usuário do MySQL
        password="sua_senha",  # Altere para sua senha do MySQL
        database="quartel"
    )

def create_database_and_tables():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="seu_usuario",  # Altere para seu usuário do MySQL
            password="sua_senha"  # Altere para sua senha do MySQL
        )
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS quartel")
        conn.database = 'quartel'
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            cpf VARCHAR(11) PRIMARY KEY,
            nome VARCHAR(100) NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cpf VARCHAR(11) NOT NULL,
            acao VARCHAR(10) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cpf) REFERENCES pessoas (cpf)
        )
        ''')
        
        conn.commit()
        conn.close()
        print("Banco de dados e tabelas criados/verificados com sucesso.")
    except mysql.connector.Error as err:
        print(f"Erro ao criar banco de dados e tabelas: {err}")

def cadastrar_pessoa(cpf, nome):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO pessoas (cpf, nome) VALUES (%s, %s)', (cpf, nome))
        conn.commit()
        print(f"{nome} cadastrado com sucesso.")
        
        conn.close()
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar pessoa: {err}")
    input("Pressione Enter para continuar...")

def registrar_entrada(cpf):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO registros (cpf, acao) VALUES (%s, %s)', (cpf, 'entrada'))
        conn.commit()
        print(f"Entrada registrada para CPF {cpf} às {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}.")
        
        cursor.execute('SELECT * FROM registros WHERE cpf = %s', (cpf,))
        registros = cursor.fetchall()
        print(f"Registros atuais para CPF {cpf}: {registros}")
        
        conn.close()
    except mysql.connector.Error as err:
        print(f"Erro ao registrar entrada: {err}")
    input("Pressione Enter para continuar...")

def registrar_saida(cpf):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO registros (cpf, acao) VALUES (%s, %s)', (cpf, 'saida'))
        conn.commit()
        print(f"Saída registrada para CPF {cpf} às {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}.")
        
        cursor.execute('SELECT * FROM registros WHERE cpf = %s', (cpf,))
        registros = cursor.fetchall()
        print(f"Registros atuais para CPF {cpf}: {registros}")
        
        conn.close()
    except mysql.connector.Error as err:
        print(f"Erro ao registrar saída: {err}")
    input("Pressione Enter para continuar...")

def listar_pessoas_dentro():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT p.nome, DATE_FORMAT(r.timestamp, '%d/%m/%Y %H:%i:%s') as formatted_date FROM pessoas p
        JOIN registros r ON p.cpf = r.cpf
        WHERE r.id IN (
            SELECT MAX(id) FROM registros GROUP BY cpf
        ) AND r.acao = 'entrada'
        ''')
        
        pessoas_dentro = cursor.fetchall()
        
        conn.close()
        
        print("Pessoas dentro do quartel:")
        for pessoa in pessoas_dentro:
            print(f"Nome: {pessoa[0]}, Entrada: {pessoa[1]}")
        if not pessoas_dentro:
            print("Nenhuma pessoa encontrada.")
    except mysql.connector.Error as err:
        print(f"Erro ao listar pessoas dentro: {err}")
    input("Pressione Enter para continuar...")

def listar_pessoas_cadastradas():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT cpf, nome FROM pessoas')
        pessoas = cursor.fetchall()
        
        conn.close()
        
        print("Pessoas cadastradas:")
        for pessoa in pessoas:
            print(f"CPF: {pessoa[0]}, Nome: {pessoa[1]}")
        if not pessoas:
            print("Nenhuma pessoa cadastrada encontrada.")
    except mysql.connector.Error as err:
        print(f"Erro ao listar pessoas cadastradas: {err}")
    input("Pressione Enter para continuar...")

def excluir_pessoa(cpf):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Excluir registros associados à pessoa
        cursor.execute('DELETE FROM registros WHERE cpf = %s', (cpf,))
        conn.commit()
        
        # Excluir a pessoa
        cursor.execute('DELETE FROM pessoas WHERE cpf = %s', (cpf,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Pessoa com CPF {cpf} excluída com sucesso.")
        else:
            print(f"Nenhuma pessoa encontrada com o CPF {cpf}.")
        
        conn.close()
    except mysql.connector.Error as err:
        print(f"Erro ao excluir pessoa: {err}")
    input("Pressione Enter para continuar...")

def gerar_relatorio(dia):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Formatar a data para a consulta SQL
        data_inicio = datetime.strptime(dia, '%d/%m/%Y').strftime('%Y-%m-%d 00:00:00')
        data_fim = datetime.strptime(dia, '%d/%m/%Y').strftime('%Y-%m-%d 23:59:59')

        # Consultar registros do dia
        query = '''
        SELECT p.nome, r.acao, DATE_FORMAT(r.timestamp, '%d/%m/%Y %H:%i:%s') as formatted_date
        FROM registros r
        JOIN pessoas p ON r.cpf = p.cpf
        WHERE r.timestamp BETWEEN '{}' AND '{}'
        ORDER BY r.timestamp
        '''.format(data_inicio, data_fim)
        cursor.execute(query)
        registros = cursor.fetchall()

        # Consultar pessoas dentro do quartel
        cursor.execute('''
        SELECT p.nome, DATE_FORMAT(r.timestamp, '%d/%m/%Y %H:%i:%s') as formatted_date
        FROM registros r
        JOIN pessoas p ON r.cpf = p.cpf
        WHERE r.id IN (
            SELECT MAX(id) FROM registros GROUP BY cpf
        ) AND r.acao = 'entrada'
        ''')
        
        pessoas_dentro = cursor.fetchall()
        
        conn.close()

        # Criar o PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt="Relatório de Entradas e Saídas", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Data: {dia}", ln=True, align='C')
        
        pdf.ln(10)
        pdf.cell(200, 10, txt="Entradas e Saídas:", ln=True)
        
        for registro in registros:
            pdf.cell(200, 10, txt=f"{registro[2]} - {registro[1]} - {registro[0]}", ln=True)
        
        pdf.ln(10)
        pdf.cell(200, 10, txt="Pessoas dentro do quartel:", ln=True)
        
        for pessoa in pessoas_dentro:
            pdf.cell(200, 10, txt=f"{pessoa[1]} - {pessoa[0]}", ln=True)
        
        # Salvar o PDF
        pdf_file = f"relatorio_{dia.replace('/', '-')}.pdf"
        pdf.output(pdf_file)
        
        print(f"Relatório gerado com sucesso: {pdf_file}")
    except mysql.connector.Error as err:
        print(f"Erro ao gerar relatório: {err}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    input("Pressione Enter para continuar...")

def listar_movimentacoes_dia(dia):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Formatar a data para a consulta SQL
        data_inicio = datetime.strptime(dia, '%d/%m/%Y').strftime('%Y-%m-%d 00:00:00')
        data_fim = datetime.strptime(dia, '%d/%m/%Y').strftime('%Y-%m-%d 23:59:59')

        # Consultar registros do dia
        query = '''
        SELECT p.nome, r.acao, DATE_FORMAT(r.timestamp, '%d/%m/%Y %H:%i:%s') as formatted_date
        FROM registros r
        JOIN pessoas p ON r.cpf = p.cpf
        WHERE r.timestamp BETWEEN '{}' AND '{}'
        ORDER BY r.timestamp
        '''.format(data_inicio, data_fim)
        cursor.execute(query)
        registros = cursor.fetchall()
        
        conn.close()

        # Exibir os registros
        print(f"Movimentações do dia {dia}:")
        for registro in registros:
            print(f"{registro[2]} - {registro[1]} - {registro[0]}")
        
        if not registros:
            print("Nenhuma movimentação encontrada.")
    except mysql.connector.Error as err:
        print(f"Erro ao listar movimentações: {err}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    input("Pressione Enter para continuar...")

def menu():
    while True:
        print("\nSistema de Controle de Pessoas - QGControle")
        print("1. Cadastrar Pessoa")
        print("2. Registrar Entrada")
        print("3. Registrar Saída")
        print("4. Listar Pessoas Dentro")
        print("5. Listar Pessoas Cadastradas")
        print("6. Excluir Pessoa")
        print("7. Gerar Relatório")
        print("8. Listar Movimentações do Dia")
        print("9. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cpf = input("CPF da pessoa: ")
            nome = input("Nome da pessoa: ")
            cadastrar_pessoa(cpf, nome)
        elif escolha == '2':
            cpf = input("CPF da pessoa: ")
            registrar_entrada(cpf)
        elif escolha == '3':
            cpf = input("CPF da pessoa: ")
            registrar_saida(cpf)
        elif escolha == '4':
            listar_pessoas_dentro()
        elif escolha == '5':
            listar_pessoas_cadastradas()
        elif escolha == '6':
            cpf = input("CPF da pessoa a ser excluída: ")
            excluir_pessoa(cpf)
        elif escolha == '7':
            dia = input("Digite a data do relatório (DD/MM/AAAA): ")
            gerar_relatorio(dia)
        elif escolha == '8':
            dia = input("Digite a data das movimentações (DD/MM/AAAA): ")
            listar_movimentacoes_dia(dia)
        elif escolha == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Criar o banco de dados e as tabelas, se ainda não existirem
create_database_and_tables()

# Executar o menu
menu()
