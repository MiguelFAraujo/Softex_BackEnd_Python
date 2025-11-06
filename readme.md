# 🐍 Curso Backend com Python e Django – BFD Softex (Turma 02-RJ-C1)

Este repositório reúne as **aulas, apostilas, exemplos e projetos práticos** desenvolvidos no curso **Backend com Python e Django**, promovido pela **BFD Softex**.

O conteúdo foi estruturado com base no material original desenvolvido por **Anderson Costa Rodrigues** e continuará sendo atualizado e ampliado sob a orientação do professor **Miguel Ferreira de Araujo**, garantindo a continuidade do aprendizado e a evolução dos alunos da **Turma 02-RJ-C1** ao longo do módulo.

---

## 📚 Conteúdo do Curso

Durante o curso, os alunos serão conduzidos em uma jornada prática e progressiva pelo desenvolvimento backend com Python e Django, abordando:

* Fundamentos da programação com Python
* Lógica de programação e estruturas de controle
* Estruturas de dados em Python (listas, dicionários, etc.)
* Introdução ao desenvolvimento web
* Framework **Django** e o padrão **MTV (Model–Template–View)**
* Conexão com banco de dados **MySQL**
* Criação de aplicações web monolíticas completas
* Versionamento de código com **Git e GitHub**
* Boas práticas de desenvolvimento backend
* **Projeto Integrador com aplicação prática em equipe**

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **Django 4.x (monolítico)**
* **MySQL 8.x**
* **HTML e CSS** básico (para os templates)
* **Git e GitHub**

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/MiguelFAraujo/Softex_BackEnd_Python.git
cd Softex_BackEnd_Python
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o servidor Django

```bash
python manage.py runserver
```

Acesse o projeto no navegador:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🗂️ Estrutura Recomendada

```
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
```

---

## 💡 Boas Práticas e Dicas de Estudo

1. **Mantenha o ambiente virtual ativo** sempre que trabalhar no projeto.
2. **Crie commits significativos:**

   * Exemplo: `git commit -m "Adiciona model Aluno e configura admin"`
3. **Evite subir arquivos de ambiente** (`venv`, `.env`, `__pycache__`) — o `.gitignore` já faz isso.
4. **Revise os conceitos de cada aula antes de programar**, para entender o propósito de cada parte do código.
5. **Pesquise e documente dúvidas** — adicione comentários nos códigos quando descobrir algo novo.
6. **Trabalhe em equipe** usando branches (`git checkout -b nome_do_grupo`) para cada parte do projeto integrador.
7. **Mantenha um ritmo constante:** dedique tempo semanal para revisar e refatorar o código.

---

## 🤝 Colaboração e Agradecimentos

Este repositório é fruto da continuidade do trabalho conduzido por **Anderson Costa Rodrigues**, a quem deixamos nosso **agradecimento e reconhecimento** pela estrutura inicial do curso e pelo material didático desenvolvido.

As atualizações e novos conteúdos, sob a orientação de **Miguel Ferreira de Araujo**, têm como objetivo **complementar o aprendizado**, mantendo o padrão e a metodologia proposta pela Softex, com foco em prática, clareza e aplicação real no mercado.

---

## 📖 Licença

Este projeto está licenciado sob a licença **MIT**.
Consulte o arquivo `LICENSE` para mais informações.

---

📘 *Sinta-se à vontade para clonar, estudar e contribuir! Este repositório foi criado para apoiar o aprendizado colaborativo e o desenvolvimento contínuo dos alunos da BFD Softex – Turma 02-RJ-C1.*
