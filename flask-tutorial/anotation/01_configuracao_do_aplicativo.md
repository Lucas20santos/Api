# Configuração do aplicativo

- Um aplicativo Flask é uma instância da classe Flask.
- A maneira mais direta de criar um aplicativo Flask é criar uma instãncia Flask global e diretamente no todo do seu código.
- Isso pode dar problema complicados conforme o proejto cresce.
- Criaremos dentro de uma função.
- Essa função é conhecida como application factory.

# A Application Factory

- Tem duas funções:
    - conterá a application factory
    - e transforma o diretorio flaskr em um pacote

# Explicando o codigo

1. app = Flask(__name__, instance_relative_config=True) cria nossa instância do Flask
    a. __name__ é o nome do modulo python altual, ele diz aonde o aplicativo está localizado.
    b. instance_relative_config=True
        1. informa ao aplicativo que os arquivos de configuração são relativos a pasta de instância.
        2. a pasta de instância está fora da pasta flaskr e pode contem dados locais que não devem ser confirmados no controle de versão, como segredos de configuração e o arquivo de banco de dados.
        3. O Flask 0.8 instroduziu o conceito de pasta de instãncia e novo atributo foi introduzido: Flask.instance_path.
        4. a pasta de instância foi proejtada para não estr sob controle de versão e ser específica da implantação.
2. app.config.from_mapping() define algumas configurações padrão que o aplicativo usará:
    - SECRET_KEY é usado pelo Flask e extensões para manter os dados seguros.
    - DATABASE é o caminho onde o sarquivo do banco de dados SQLite será seguros. Ele está em app.instance_path, que o caminho que o Flask escolheu para a pasta da instância.
3. app.config.from_pyfile()
