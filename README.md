<h1 align="center">
  <img alt="Django App" title="django-app" src="assets/python.png" />
</h1>

<p align="center">
  <a href="#technologist-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-licença">Licença</a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/licence-MIT-green" />
  <img alt="Issues" src="https://img.shields.io/github/issues/brenomr/drf-escola" />
  <img alt="Stars" src="https://img.shields.io/github/stars/brenomr/drf-escola" />
</p>

<p align="center">
  <img alt="Tela manipulação da API" src="assets/api_screen.png" width="100%">
</p>
<br />

## :technologist: Tecnologias

Este projeto faz uso das seguintes tecnologias:
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/).
<br />

## 💻 Projeto

O DRF-Escola é uma API para o simples gerenciamento de alunos, cursos, matrículas e clientes e foi desenvolvida com o propósito simples propósito de testar as funcionalidades do Django Rest Framework.
<br />
<br />

## 🚀 Como executar

- Clone o repositório
- No diretório do projeto inicie um ambiente virtual com `python -m venv venv`
- Ative o ambiente virtual, considerando que está utilizando o powershell no windows execute `.\venv\Scripts\activate`
- Atualize o pip com `python -m pip install --upgrade pip`
- Instale as dependências com `pip install -r requirements.txt`
- Execute as migrações com `python manage.py migrate`
- Crie o primeiro usuário com `python manage.py createsuperuser`
- Inicie o servidor com `python manage.py runserver`

O servidor deverá iniciar no endereço: [http://localhost:8000](http://localhost:8000)
<br />
<br />

## 📄 Licença

Acesse [LICENSE](LICENSE.md) para mais informações sobre a licença.
