# Cabaré Django Project

**Atenção +18: Conteúdo para maiores de 18 anos.**

Este é um projeto web desenvolvido com Django para gerenciar conteúdos multimídia, encontros, galerias de imagens e vídeos. O projeto utiliza o framework Django e o Tailwind CSS para a interface.

## Funcionalidades

- Página inicial com slider de imagens.
- Cadastro e login de usuários.
- Página de contatos.
- Exibição de galerias de fotos e vídeos.
- Marcação e listagem de encontros.

## Estrutura do Projeto

- **core/**: Configurações principais do Django (URLs, settings, wsgi, asgi).
- **cabare/**: Aplicação principal com modelos (usuários, imagens, posts, vídeos, comentários), views e URLs.
- **templates/**: Arquivos HTML para renderização das páginas.
- **middlewares/**: Funções auxiliares para autenticação (hashing de senhas).
- **.vscode/**: Configurações do Visual Studio Code.

## Requisitos

- Python 3.8 ou superior
- Django 5.1.7
- bcrypt

## Instalação

1. Crie um ambiente virtual:
   ```sh
   python -m venv venv
   ```
