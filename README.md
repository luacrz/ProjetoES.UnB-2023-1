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



## Instruções de uso do Sistema

Credencias validas para professor - username: "pedro" senha : "asdfg" 

Credencias validas para aluno - username: "ester" senha : "asdfg" 

Você pode estar também registrando professores e alunos, além de criar as questões e exames. 


Para o professor, é possível fazer criação de questões dos tipo V e F, múltipla escolha e valor numérico. Isso pode ser acessado através do menu na aba “Criar Questão”.  As questões podem ser utilizadas em mais de um exame, e sua nota é atribuída quando a questão é adicionada ao exame. O professor pode também criar exames através do “Criar Exames”. Os exames possuem enunciado, data de abertura e de término, além das questões e notas atribuídas a estas. O professor pode também ver suas questões, através do “Questões” presente no menu. E por fim, no “Exames” presente no menu é possível listar os exames criados pelo professor, é possível listar as questões presentes nesse exame, é possível deletar um exame, e o professor pode ver o relatório do exame, onde os alunos que fizeram o exame são listados, e a partir daí, o professor pode ver detalhes do exame feito pelo aluno.  

Para o aluno, é possível listar os exames, através do “Procurar Exames” presente no menu. Serão listados todos os exames, porém, somente será possível ser respondido os exames que estão abertos e que não estão previamente respondidos. Se o tempo do exame expira enquanto o aluno o faz, suas questões respondidas são automaticamente enviadas. O aluno poderá ver seus exames concluídos a partir do “Exames feitos” contido no menu. Lá será listados os exames feitos, e será possível ver seus detalhes. Detalhes esses como nota do aluno, nota atribuída a cada questão, a questão em si, como também a alternativa assinada e qual era a alternativa correta. 
