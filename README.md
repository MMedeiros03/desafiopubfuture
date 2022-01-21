# desafiopubfuture
Desafio PubFuture 🚀🚀🚀

### Tabela de conteúdos
- Status
- Pré-Requisitos
- Ferramentas e Tecnologias
- Rest Api Framework
- Arquitetura
- Dependências e Libs Instaladas
- Como rodar a aplicação no seu PC
- Databases



## Este sistema está em desenvolvimento


## Pré-Requisitos 
- Python 3.9.4
- Django 3.2.7
- VSCode para edição dos códigos

## Ferramentas e tecnologias
No desenvolvimento deste projeto foi utilizado como ferramenta de gestão de tarefas o Trello, onde registrei as atividades que precisavam ser feitas durante os dias, o que garantiu um fluxo de trabalho produtivo e organizado. Para fazer o versionamento do projeto utilizei o GitHub.Para a edição de codigo utilizei o Visual Studio Code. A linguagem principal utilizada no projeto foi o Python e como framework o DJANGO que são muito utilizados no desenvolvimento de sites. Diversos gigantes utilizam python e django em suas paginas web, como por exemplo o Spotify,Youtube e Instagram. Também foi utilizado RestAPIFramework. 

## Rest Api Framework
O projeto utiliza uma api propria que armazena os dados em formato json. Para ter acesso ao espaço da api voce precisa:
- estar com o site rodando (utilize o comando python manage.py runserver);
- após isso, basta colar este link na barra de pesquisa do browser: http://127.0.0.1:8000/conta/ 
- a mesma coisa para as demais classes do projeto: http://127.0.0.1:8000/despesa/, http://127.0.0.1:8000/receita/ 

## Arquitetura
Este projeto utiliza arquitetura MTV que é muito utilizada quando desenvolvido com django. 
- M -> Model -> Modelos do banco de dados; 
- T -> Template -> Templates HTML;
- V -> Views -> Toda a parte lógica do site.

## Dependências e Libs Instaladas
Django == 4.0.1
Pillow == 8.3.1
djangorestframework == 3.13.1

## Como rodar a aplicação em sua maquina
- Primeiramente é necessário fazer a intalação do Python (versão utilizada: 3.9.6) .
- Em seguida instalação do django através do comando "pip install django" no prompt de comando. (versão utilizada: 3.2.6).
- No seu terminal local você vai criar seu ambiente virtual e ativa-lo através dos seguintes comandos na ordem descrita:
  -> python -m venv (nome do seu ambiente virtual)
  -> cd (nome do ambiente virtual)
  -> cd Scripts
  -> activate (se estiver utilizando um terminal powershell, utilize: activate.bat)
  -> cd .. (para sair da pasta scripts)
  
- Agora é a hora de fazer o clone do projeto no GitHub (https://github.com/MMedeiros03/desafiopubfuture). Apos acessar o link do repositório, clicar em "clone" e copiar o caminho HTTPS;
-  No repositório escolhido, caso seja uma pasta nova é necessário fazer um 'GIT INIT' antes de realizar o "GIT CLONE".                                                                      
- Ainda no seu terminal local: fazer o comando git "GIT CLONE" e ao lado adicionar o caminho HTTPS copiado anteriormente.

- Depois de clonar o repositório, digite no terminal: cd desafiopubfuture
                                  
- Agora que seu ambiente virtual já está ativado, você deve fazer o download de todas a bibliotecas co projeto através do comando "pip install requirements.txt".

- Após o termino da instalação deve-se executar o comando "python mange.py mekemigratios" para atualizar o banco de dados e os modelos.

- Em seguida "python mange.py migrate" para aplicar as modificações realizadas. 

- Depois de de concluir deve-se executar "python mange.py runserver"

- Com o servidor rodando, pode acessar o nosso projeto pelo seguinte link: http://127.0.0.1:8000/


## Databases
Neste projeto foi utilizado o banco de dados sqlite que vem por padrão quando um projeto django é criado;
Por ser uma aplicação simples, ele é adequado para a demanda. 


Muito obrigada por ter lido a documentação. Caso queira conversar comigo por favor me chame para a entrevista 😂😂😂😂
