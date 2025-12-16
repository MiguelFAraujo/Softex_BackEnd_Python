🚀 Softex – Back-End com Python e Django

Este repositório reúne materiais didáticos, códigos‑modelo e projetos práticos desenvolvidos para o Curso de Back-End com Python e Django, aplicado na formação da turma 02‑RJ‑C1 (Softex).

O objetivo principal é servir como guia de estudo progressivo, partindo dos fundamentos da linguagem Python até o desenvolvimento de APIs REST profissionais com Django REST Framework.

🎯 Objetivo do Projeto

Ensinar programação back-end de forma gradual e acessível.

Aplicar conceitos teóricos por meio de códigos práticos.

Introduzir o aluno ao desenvolvimento web com Django.

Capacitar na criação de APIs REST utilizadas no mercado.

Estimular boas práticas de organização, versionamento e documentação.

🧠 Público-Alvo

Estudantes iniciantes em programação.

Alunos de cursos profissionalizantes (Softex, técnicos ou similares).

Pessoas interessadas em Back-End com Python.

Desenvolvedores iniciantes que desejam aprender Django na prática.

🧱 Estrutura do Repositório

O conteúdo está organizado em módulos didáticos, seguindo uma progressão lógica de aprendizado:

Softex_BackEnd_Python/
├── modulo_01_python_basico/
├── modulo_02_logica_programacao/
├── modulo_03_introducao_django/
├── modulo_04_crud_banco_dados/
├── modulo_05_api_rest_drf/
└── projeto_integrador/


Cada módulo contém:

📄 Apostilas e explicações teóricas.

🧪 Exercícios práticos.

💻 Códigos‑modelo comentados para estudo em sala de aula.

📚 Conteúdo por Módulo

🔹 Módulo 01 – Fundamentos de Python

Sintaxe básica

Tipos de dados

Variáveis

Entrada e saída de dados

🔹 Módulo 02 – Lógica de Programação

Estruturas condicionais

Estruturas de repetição

Listas, tuplas e dicionários

Funções

🔹 Módulo 03 – Introdução ao Django

Conceito de framework

Arquitetura MVT (Model, View, Template)

Criação de projetos e apps

Rotas e templates HTML

🔹 Módulo 04 – CRUD e Banco de Dados

Models e migrations

Banco de dados SQLite

Django Admin

Operações CRUD completas

🔹 Módulo 05 – APIs REST com Django REST Framework

Introdução a APIs REST

Serializers

Views e ViewSets

Rotas de API

Boas práticas para APIs

🚀 Tecnologias Utilizadas

Python 3.10+

Django 5.x

Django REST Framework (DRF)

SQLite (ambiente de desenvolvimento)

Virtualenv

Git & GitHub

▶️ Como Executar o Projeto

1️⃣ Clonar o repositório

git clone [https://github.com/MiguelFAraujo/Softex_BackEnd_Python.git](https://github.com/MiguelFAraujo/Softex_BackEnd_Python.git)
cd Softex_BackEnd_Python


2️⃣ Criar e ativar o ambiente virtual

# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate


3️⃣ Instalar dependências

pip install -r requirements.txt


4️⃣ Aplicar migrations

python manage.py migrate


5️⃣ Executar o servidor

python manage.py runserver


Acesse em: http://127.0.0.1:8000/

🧪 Roteiro de Testes da API (Thunder Client)

Este projeto utiliza JWT (JSON Web Token) para autenticação das rotas protegidas.
Para testar corretamente a API, recomenda-se o uso do Thunder Client (extensão do VS Code).

Este roteiro segue exatamente o fluxo ensinado em aula e valida todas as funcionalidades do módulo de API REST com Django REST Framework.

🔐 1️⃣ Autenticação – Obter Token JWT

Antes de acessar qualquer rota protegida, é necessário autenticar um usuário existente.

Método: POST

Endpoint: /api/token/

Body (JSON):

{
  "username": "seu_usuario",
  "password": "sua_senha"
}


Resposta esperada:

{
  "refresh": "token_refresh_string...",
  "access": "token_access_string..."
}


📌 Importante: Guarde o valor do access token, ele será utilizado nas próximas requisições.

🔑 2️⃣ Configurar Authorization no Thunder Client

Para todas as rotas protegidas listadas abaixo:

Abra a requisição no Thunder Client.

Vá até a aba Headers.

Adicione o seguinte cabeçalho:

Key: Authorization

Value: Bearer SEU_ACCESS_TOKEN_AQUI

⚠️ Caso esse cabeçalho não seja enviado, a API retornará 401 Unauthorized, o que é o comportamento esperado.

📋 3️⃣ Listar Tarefas do Usuário Autenticado

Método: GET

Endpoint: /api/tarefas/

✔ Retorna apenas as tarefas vinculadas ao usuário autenticado via token JWT.

➕ 4️⃣ Criar Nova Tarefa

Método: POST

Endpoint: /api/tarefas/

Body (JSON):

{
  "titulo": "Estudar Django REST Framework"
}


✔ O campo user é atribuído automaticamente pelo backend, conforme visto em aula.

🔍 5️⃣ Detalhar Tarefa por ID

Método: GET

Endpoint: /api/tarefas/1/

✔ Retorna os dados de uma tarefa específica pertencente ao usuário autenticado.

✏️ 6️⃣ Atualizar Tarefa

Método: PUT (atualização completa) ou PATCH (atualização parcial)

Endpoint: /api/tarefas/1/

Exemplo de Body (JSON):

{
  "titulo": "Revisar Django REST",
  "concluida": true
}


❌ 7️⃣ Remover Tarefa

Método: DELETE

Endpoint: /api/tarefas/1/

✔ Remove a tarefa do banco de dados (Status 204 No Content).

🚪 8️⃣ Logout – Invalidar Refresh Token

Método: POST

Endpoint: /api/logout/

Body (JSON):

{
  "refresh": "SEU_REFRESH_TOKEN_AQUI"
}
