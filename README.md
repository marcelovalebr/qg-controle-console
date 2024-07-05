# Sistema de Controle de Pessoas - QGControle

Este é um sistema de controle de pessoas que permite cadastrar, registrar entradas e saídas, listar pessoas dentro do quartel, gerar relatórios e mais. O sistema utiliza um banco de dados MySQL para armazenar informações sobre pessoas e seus registros de entrada e saída.

## Funcionalidades

- **Cadastrar Pessoa:** Insira o CPF e o nome da pessoa para cadastrá-la no sistema.
- **Registrar Entrada:** Registre a entrada de uma pessoa no quartel.
- **Registrar Saída:** Registre a saída de uma pessoa do quartel.
- **Listar Pessoas Dentro:** Liste todas as pessoas que estão atualmente dentro do quartel.
- **Listar Pessoas Cadastradas:** Liste todas as pessoas cadastradas no sistema.
- **Excluir Pessoa:** Exclua uma pessoa cadastrada no sistema e seus registros associados.
- **Gerar Relatório:** Gere um relatório PDF das movimentações de um dia específico.
- **Listar Movimentações do Dia:** Liste todas as movimentações de entrada e saída de um dia específico.

## Tecnologias Utilizadas

- Python
- MySQL (com a biblioteca `mysql-connector-python`)
- FPDF (para geração de PDFs)

## Pré-requisitos

- Python 3.x
- MySQL Server
- Bibliotecas Python:
  - `mysql-connector-python`
  - `fpdf`

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/qgcontrole.git
    cd qgcontrole
    ```

2. Instale as dependências:
    ```bash
    pip install mysql-connector-python fpdf
    ```

3. Configure o banco de dados MySQL:
    - Certifique-se de que o MySQL Server está instalado e em execução.
    - Altere as credenciais do banco de dados no código, se necessário.

4. Execute o script:
    ```bash
    python qgcontrole.py
    ```

## Uso

1. **Cadastrar Pessoa:**
    - Escolha a opção 1 no menu.
    - Insira o CPF e o nome da pessoa.

2. **Registrar Entrada:**
    - Escolha a opção 2 no menu.
    - Insira o CPF da pessoa.

3. **Registrar Saída:**
    - Escolha a opção 3 no menu.
    - Insira o CPF da pessoa.

4. **Listar Pessoas Dentro:**
    - Escolha a opção 4 no menu.

5. **Listar Pessoas Cadastradas:**
    - Escolha a opção 5 no menu.

6. **Excluir Pessoa:**
    - Escolha a opção 6 no menu.
    - Insira o CPF da pessoa a ser excluída.

7. **Gerar Relatório:**
    - Escolha a opção 7 no menu.
    - Insira a data do relatório no formato DD/MM/AAAA.

8. **Listar Movimentações do Dia:**
    - Escolha a opção 8 no menu.
    - Insira a data das movimentações no formato DD/MM/AAAA.

9. **Sair:**
    - Escolha a opção 9 no menu para sair do sistema.
