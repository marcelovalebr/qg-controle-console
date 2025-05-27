
# 🛡️ Sistema de Controle de Acesso e Relatórios

Sistema de controle de acessos e geração de relatórios utilizando **Python**, **MySQL** e **FPDF**.  
Ideal para ambientes organizacionais e militares que demandam segurança, rastreabilidade e automatização de processos de movimentação de pessoas.

---

## 🚀 Funcionalidades

✅ Cadastro de pessoas com CPF e nome.  
✅ Registro de entradas e saídas com **timestamp**.  
✅ Listagem de pessoas presentes no ambiente.  
✅ Exclusão de pessoas e seus registros associados.  
✅ Geração de relatórios diários em **PDF**.  
✅ Consulta de movimentações por data.  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**  
- **MySQL**  
- **FPDF** (para geração de relatórios)  
- **datetime** (para manipulação de datas)  

---

## ⚙️ Como usar

1. Clone o repositório:  
```bash
git clone https://github.com/marcelovalebr/qg-controle-console.git
cd qg-controle-console
```

2. Instale as dependências:  
```bash
pip install mysql-connector-python fpdf
```

3. Configure as credenciais de acesso ao banco no script:  
- Usuário  
- Senha  
- Banco de Dados

4. Execute o script:  
```bash
python qg_controle.py
```

5. Use o menu interativo para:  
- Cadastrar pessoas  
- Registrar entradas/saídas  
- Gerar relatórios  
- Consultar movimentações  

---

## 📄 Relatórios

Relatórios são gerados em **formato PDF** contendo:  
- Lista de todas as movimentações do dia.  
- Relação de pessoas que permanecem no ambiente.  

---

## 👨‍💻 Autor

**Marcelo Vale**  
Especialista em Automação de Processos, Infraestrutura e Segurança da Informação.  

[GitHub](https://github.com/marcelovalebr) | [LinkedIn](https://www.linkedin.com/in/marcelovalebr/)

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License** — veja o arquivo **LICENSE** para mais detalhes.
