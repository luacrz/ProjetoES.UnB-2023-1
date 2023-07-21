# Sistema de Realização de Exames

Este é um sistema desenvolvido para gerenciar a realização de exames, permitindo que professores criem e administrem exames, e estudantes os realizem e visualizem seus resultados. O sistema é projetado para fornecer uma interface amigável e intuitiva, adaptando-se a diferentes dispositivos, como computadores, tablets e smartphones. 

# Instruções para executar o Projeto
Para executar um projeto, siga estas instruções:

## Clone o repositório: 
No diretório onde você deseja clonar o repositório, execute o seguinte comando para clonar o repositório:

```
git clone https://github.com/luacrz/ProjetoES.UnB-2023-1.git
```

## Acesse o diretório do projeto: 
Após clonar o repositório, acesse o diretório do projeto usando o comando cd no terminal. Por exemplo:

```
cd nome_do_projeto
```

## Máquina virtural
1. Instale ou verifique se o pip está na última versão

windows:
```
py -m pip install --upgrade pip
py -m pip --version
```
Unix/macOS:
```
python3 -m pip install --user --upgrade pip
python3 -m pip --version
```

2. Instale o ambiente virtual

windows:
```
py -m pip install --user virtualenv
```
Unix/macOS:
```
python3 -m pip install --user virtualenv
```

3. Crie o ambiente virtual

windows:
```
py -m venv env
```
Unix/macOS:
```
python3 -m venv env
```

4. Ative o ambiente virtual

windows:
```
.\env\Scripts\activate
```
Unix/macOS:
```
source env/bin/activate
```

## Requisitos: 
Use o seguinte comando dentro do ambiente virtual para instalar as dependências listadas no arquivo:
```
pip install -r requirements.txt
```

## Execute o projeto
Para executar o projeto, tente utilizar o seguinte comando:
```
flask run
```
Talvez seja necessário definir a variável de ambiente FLASK_APP: antes de usar o comando ```flask run``` no terminal do VS Code. Defina a variável de ambiente FLASK_APP para o nome do arquivo Python que contém o aplicativo Flask. Por exemplo:
```
set FLASK_APP=run.py
```
O servidor Flask será iniciado e você verá a saída indicando em qual endereço IP e porta o aplicativo está sendo executado, copie e cole o endereço no navegador para visualizar.

Credencias validas para professor - username: "pedro" senha : "asdfg" 

Credencias validas para aluno - username: "ester" senha : "asdfg" 

Você pode estar também registrando professores e alunos, além de criar as questões e exames. 

O professor pode acessar qualquer um dos hyperlinks do cabeçalho (exceto "Visualizar Relatório de Notas", que está atualmente dentro da função de Listar Exames). 

 

O professor pode criar questões, exames, além de poder ver o conteúdo dessas provas como suas questões e um relatório que contém as questões respondidas dos alunos. No relatório os alunos estão separados como ID, seguido das respostas. 

O aluno pode fazer os exames, além de ver as questões que ele respondeu em um exame. Caso o exame já tiver sido feito o aluno não poderá editar e nem fazer novamente a prova. O aluno também não pode fazer a prova se a prova não tiver começado ou já tiver com o tempo esgotado. 
 