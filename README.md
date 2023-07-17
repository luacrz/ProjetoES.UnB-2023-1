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
O servidor Flask será iniciado e você verá a saída indicando em qual endereço IP e porta o aplicativo está sendo executado, copie e cole o endereço no navegador para visualizar. Você pode usar \login, \register ou qualquer rota que já esteja pronta no arquivo default.py da pasta controllers.

Um professor já pode criar questões, exames e adicionar essas questões nos exames. Ele também pode ver isso, basta logar um professor valido como "pedro" e "asdfg", clickar em página do professor, e clickar em qualquer um dos hyperlinks do cabeçalho (exceto "Visualizar Relatório de Notas")

