# Flask Intalation

## Dependências 

- Werkzeup: implementa WSGI, a interface Python padrão entre aplicativos e servidores.
- Jinja: é uma linguagem de modelo que renderiza as páginas que seu aplicativo atende.
- O markupSafe vem com Jinja. Ele escapa entradas não confiáveis ao renderizar modelos para evitar ataques de injeção.
- IsDangerous: assina dados com segurança para garantir sua integridade. Isso é usado para proteger o cookie de sessão do Flask.
- Click é um framework para escrever aplicativos de linha de comando. Ele fornece o flask comando e permite adicionar comandos de gerenciamento personalizados.
- O Blinker fornece suporte para sinais.

## Dependênicas opcionais

- python-dotenv: habilita o suporte para Variávies de Ambiente do dotenv ao executar flask comandos.
- Watchdog: fornece um recarregador mais rápodo e eficiente para o servidor de desenvolvimento.

## Ambiente virtuais

- use um ambiente virtual para gerencias as dependências do seu projeto, tanto no desenvolvimento quanto na produção.
- possibilita trabalhar com versões de biblioteca diferente.
- módulo **venv** para criação de ambientes virtuais.

## Crie um ambiente

### Linux/macOS

1. $ mkdir myproject
2. $ cd myproject
3. $ python3 -m venv .venv

### ativnado o ambiente virtual

1. $. .venv/bin/activate

### saindo do ambiente virtual

1. deactivate

### Instalando o flask

1. $ pip install Flask
