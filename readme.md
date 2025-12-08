🐍 Curso Backend com Python e Django – BFD Softex (Turma 02-RJ-C1)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)

Este repositório centraliza as aulas, apostilas, gabaritos e o **Projeto Integrador** do curso de Backend com Python e Django. Aqui você encontrará desde a lógica de programação até a construção de APIs RESTful profissionais.

---

## 📚 Conteúdo Programático

O curso está dividido em módulos progressivos:

| Módulo | Foco Principal | Conteúdo |
| :--- | :--- | :--- |
| **Módulo 01** | 🐍 **Fundamentos** | Sintaxe Python, Variáveis e Tipos de Dados. |
| **Módulo 02** | 🔄 **Lógica** | Estruturas de Repetição, Listas, Dicionários e Funções. |
| **Módulo 03** | 🏗️ **Django Intro** | Padrão MVT, Rotas e Templates HTML. |
| **Módulo 04** | 🖥️ **Aplicações** | CRUD Completo, Banco de Dados e Admin. |
| **Módulo 05** | 🌐 **API Rest (DRF)** | Serializers, ViewSets, JWT e Autenticação. |

---

## 🚀 Tecnologias e Ferramentas

* **Linguagem:** Python 3.10+
* **Framework Web:** Django 5.x
* **API:** Django Rest Framework (DRF)
* **Banco de Dados:** SQLite (Dev) / MySQL (Prod)
* **Versionamento:** Git & GitHub
* **Ambiente:** Virtualenv (`.venv`)
* **Segurança:** Django-Environ (`.env`)

---

## ⚙️ Configuração do Ambiente (Passo a Passo)

Siga estes passos para rodar o projeto na sua máquina:

### 1️⃣ Clonar o repositório
```bash
git clone [https://github.com/MiguelFAraujo/Softex_BackEnd_Python.git](https://github.com/MiguelFAraujo/Softex_BackEnd_Python.git)
cd Softex_BackEnd_Python
2️⃣ Criar e ativar o ambiente virtualIsolamos as dependências do projeto para evitar conflitos.Windows (PowerShell):PowerShellpython -m venv .venv
.\.venv\Scripts\Activate
⚠️ Se der erro de permissão no Windows, rode: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope ProcessLinux / Mac:Bashpython3 -m venv .venv
source .venv/bin/activate
✅ Dica: O terminal deve mostrar (.venv) no início da linha.3️⃣ Instalar dependênciasBashpip install -r requirements.txt
4️⃣ Configurar Variáveis de Ambiente (Segurança)Crie um arquivo chamado .env dentro da pasta do módulo (junto ao arquivo manage.py) e adicione o seguinte conteúdo:Ini, TOMLDEBUG=on
SECRET_KEY=sua-chave-secreta-aqui
5️⃣ Executar Migrações e ServidorBash# Entre na pasta do módulo atual (ex: modulo_05)
cd modulo_05

# Crie as tabelas no banco
python manage.py migrate

# Inicie o servidor
python manage.py runserver
🌐 Acesse: http://127.0.0.1:8000/api/tarefas/



📝 Cheat Sheet: Comandos Git
Guia rápido para os alunos não esquecerem:

Baixar atualizações: git pull origin main

Verificar status: git status

Adicionar arquivos: git add .

Salvar versão (Commit): git commit -m "Mensagem aqui"

Enviar para nuvem: git push

Trocar de branch: git checkout nome-da-branch

⚠️ Atenção: Nunca suba arquivos .env, .venv ou db.sqlite3 para o GitHub.

🤝 Créditos e Contribuição
Material Original: Anderson Costa Rodrigues

Instrutor e Maintainer: Miguel Ferreira de Araujo

Este projeto é mantido para fins educacionais da BFD Softex. Fique à vontade para abrir Issues ou Pull Requests para melhorias!
