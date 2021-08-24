# Tina
Cantina Inteligente - Projeto IHM

## Minimundo

Tina é um sistema utilizado para entrega de merendas em escolas. Devido a problemas com falta de merendas para alunos e desperdício de comida em uma escola x, foi necessário tomar medidas que formassem um sistema mais rigoroso para distribuição de merendas na cantina. Nessa versão a Tina é responsável por reconhecer cada aluno e permitir determinada quantidade de repetição dependendo do cardápio, as ações esperadas são:
- Definir prato do dia e limite
- coletar identificação do aluno via reconhecimento facial
- verificar se o aluno está matriculado
- verificar se o aluno está dentro do limite de repetição da refeição
- caso esteja, entregar a comida e iterar o limite de refeição
- caso não esteja, informar ao aluno que ele já atingiu o limite de sua refeição diária

## Executando o projeto

### Requisitos
- Instalar o [vs code](https://code.visualstudio.com/)
- Instalar o [python3](https://www.python.org/downloads/)
- Instalar as estensões no vs code:
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [COde Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)


## Instruções
- após instalar os requisitos citados siga os passos desse [SITE](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) para ativar o ambiente virtual.

- apos criar o ambiente virtual (venv) instalar dentro deles as dependencias usando o `pip3 install -r requirements.txt`

- executar o projeto no arquivo `main.py` usando o botao run code no canto superior direito ou o atalho `ctrl+alt+n`