🐍 Curso Backend com Python e Django – BFD Softex (Turma 02-RJ-C1)

Este repositório reúne aulas, apostilas, exemplos e projetos práticos do curso Backend com Python e Django, promovido pela BFD Softex – Turma 02-RJ-C1.

📚 Conteúdo do Curso

Durante o curso, você vai aprender:

🐍 Fundamentos de Python

🔄 Lógica de programação e estruturas de controle

📦 Estruturas de dados (listas, dicionários, etc.)

🌐 Introdução ao desenvolvimento web

🏗️ Django e o padrão MTV (Model–Template–View)

💾 Banco de dados MySQL

🖥️ Criação de aplicações web completas

🔧 Versionamento de código com Git e GitHub

💡 Boas práticas de desenvolvimento backend

🤝 Projeto Integrador em equipe

🚀 Tecnologias

Python 3.10+

Django 4.x

MySQL 8.x

HTML/CSS básico (templates)

Git & GitHub

⚙️ Configuração do Ambiente (Passo a Passo)
1️⃣ Clonar o repositório
git clone https://github.com/MiguelFAraujo/Softex_BackEnd_Python.git
cd Softex_BackEnd_Python

2️⃣ Criar e ativar o ambiente virtual

O venv isola o projeto e suas dependências.

Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate

Linux / Mac
python3 -m venv .venv
source .venv/bin/activate


✅ Dica: Quando ativo, aparece (.venv) no início do prompt.

3️⃣ Instalar dependências
pip install -r requirements.txt


Instala todas as bibliotecas necessárias para o projeto.

4️⃣ Entrar no módulo
cd modulo_04

5️⃣ Rodar o servidor Django
python manage.py runserver


🌐 Acesse no navegador: http://127.0.0.1:8000

🔁 O servidor reinicia automaticamente se você alterar algum código.

6️⃣ Criar superusuário (para painel admin)
python manage.py createsuperuser


Acesse o admin: http://127.0.0.1:8000/admin

Permite criar, editar e visualizar dados direto pelo painel.

7️⃣ Comandos úteis do Django

💾 Migrar banco de dados (criar tabelas)

python manage.py makemigrations
python manage.py migrate


🐚 Abrir shell interativo

python manage.py shell


Exemplo:

from core.models import Tarefa
Tarefa.objects.create(nome="Estudar Django")


📄 Ver tabelas no SQLite (opcional)

from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

🌳 Estrutura Recomendada
Softex_BackEnd_Python/
│
├── modulo_01/              # Fundamentos e Python básico
├── modulo_02/              # Estruturas, lógica e coleções
├── modulo_03/              # Introdução ao Django
├── modulo_04/              # Aplicações práticas e CRUD
│   ├── materiais/
│   └── aulas/
│
├── projeto_integrador/     # Exercício de aplicação prática em grupo
├── materiais_gerais/       # Apostilas, ementas e slides
├── requirements.txt
└── README.md

📝 Comandos mais importantes do Git

🔍 Status do repositório

git status


➕ Adicionar arquivos

git add .


💾 Criar commit

git commit -m "Mensagem explicando a mudança"


📤 Enviar alterações para GitHub

git push


📥 Atualizar projeto local

git pull


🕰️ Histórico de commits

git log


⚠️ Dica: Não suba arquivos de ambiente (.venv, .env, __pycache__) ou banco SQLite se quiser preservar dados individuais.

💡 Boas Práticas

Mantenha o venv ativo.

Crie commits curtos e claros.

Revise conceitos antes de programar.

Documente dúvidas no código com comentários.

Use branches para trabalhar em equipe:

git checkout -b nome_do_grupo


Dedique tempo semanal para revisar e refatorar.

🤝 Colaboração e Agradecimentos

Material original: Anderson Costa Rodrigues

Atualizações e suporte: Miguel Ferreira de Araujo

O objetivo é manter prática, clareza e aprendizado real de mercado.

📖 Licença

Licença MIT. Consulte o arquivo LICENSE.

📘 Fique à vontade!

Clone, estude, pratique e contribua com o aprendizado coletivo da BFD Softex – Turma 02-RJ-C1.
