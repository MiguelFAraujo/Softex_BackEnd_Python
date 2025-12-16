# 🚀 Softex – Back-End com Python e Django

Este repositório reúne **materiais didáticos, códigos‑modelo e projetos práticos** desenvolvidos para o **Curso de Back-End com Python e Django**, aplicado na formação da turma **02‑RJ‑C1 (Softex)**.

O objetivo principal é servir como **guia de estudo progressivo**, partindo dos fundamentos da linguagem Python até o desenvolvimento de **APIs REST profissionais com Django REST Framework**.

---

## 🎯 Objetivo do Projeto

* Ensinar **programação back-end** de forma gradual e acessível
* Aplicar conceitos teóricos por meio de **códigos práticos**
* Introduzir o aluno ao **desenvolvimento web com Django**
* Capacitar na criação de **APIs REST** utilizadas no mercado
* Estimular boas práticas de organização, versionamento e documentação

---

## 🧠 Público-Alvo

* Estudantes iniciantes em programação
* Alunos de cursos profissionalizantes (Softex, técnicos ou similares)
* Pessoas interessadas em **Back-End com Python**
* Desenvolvedores iniciantes que desejam aprender Django na prática

---

## 🧱 Estrutura do Repositório

O conteúdo está organizado em **módulos didáticos**, seguindo uma progressão lógica de aprendizado:

```text
Softex_BackEnd_Python/
├── modulo_01_python_basico/
├── modulo_02_logica_programacao/
├── modulo_03_introducao_django/
├── modulo_04_crud_banco_dados/
├── modulo_05_api_rest_drf/
└── projeto_integrador/
```

Cada módulo contém:

* 📄 Apostilas e explicações teóricas
* 🧪 Exercícios práticos
* 💻 Códigos‑modelo comentados para estudo em sala de aula

---

## 📚 Conteúdo por Módulo

### 🔹 Módulo 01 – Fundamentos de Python

* Sintaxe básica
* Tipos de dados
* Variáveis
* Entrada e saída de dados

### 🔹 Módulo 02 – Lógica de Programação

* Estruturas condicionais
* Estruturas de repetição
* Listas, tuplas e dicionários
* Funções

### 🔹 Módulo 03 – Introdução ao Django

* Conceito de framework
* Arquitetura MVT (Model, View, Template)
* Criação de projetos e apps
* Rotas e templates HTML

### 🔹 Módulo 04 – CRUD e Banco de Dados

* Models e migrations
* Banco de dados SQLite
* Django Admin
* Operações CRUD completas

### 🔹 Módulo 05 – APIs REST com Django REST Framework

* Introdução a APIs REST
* Serializers
* Views e ViewSets
* Rotas de API
* Boas práticas para APIs

---

## 🧩 Projeto Integrador

O **Projeto Integrador** tem como objetivo consolidar os conhecimentos adquiridos ao longo do curso.

Ele envolve:

* Estruturação de um projeto Django completo
* Implementação de CRUD
* Criação de uma API REST funcional
* Organização de código e documentação

📁 Localizado na pasta:

```text
/projeto_integrador
```

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **Django 5.x**
* **Django REST Framework (DRF)**
* **SQLite** (ambiente de desenvolvimento)
* **Virtualenv**
* **Git & GitHub**

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/MiguelFAraujo/Softex_BackEnd_Python.git
cd Softex_BackEnd_Python
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate # Linux/Mac
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migrations

```bash
python manage.py migrate
```

### 5️⃣ Executar o servidor

```bash
python manage.py runserver
```

Acesse em:

```
http://127.0.0.1:8000/
```

---

## 📌 Observações Importantes

* Este repositório possui **finalidade educacional**
* Os códigos são **exemplos didáticos**, podendo ser adaptados
* Recomenda-se que os alunos **executem e modifiquem os códigos** durante as aulas

---

## 👨‍🏫 Autor

**Miguel Ferreira de Araujo**
Professor e Desenvolvedor Back-End

📘 Curso: Back-End com Python e Django – Softex

---

## ⭐ Considerações Finais

Este material foi desenvolvido para **ensino prático**, priorizando clareza, organização e aplicação real dos conceitos de back-end.

Sugestões de melhoria, correções e contribuições são bem-vindas.
