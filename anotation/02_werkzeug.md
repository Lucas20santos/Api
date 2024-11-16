# Werkzeug

Implementa o WSGI, a interface Python padrão entre aplicativos e servidores.

## Detalhes

- é uma biblioteca abrangente de aplicativos web WSGI.
- Um depurador interativo:
    - permite inspecionar rastreamentos da pilha e código-fonte no navegador.
- Um objeto de solicitação completo com objetos para interagir com:
    - cabeçalhos,
    - argumentos de consulta,
    - dados de formulário, 
    - arquivos e cookies
- Um objeto de resposta que pode encapsular outros aplicativos WSGI  e manipular dados de streaming.
- Um sistema de roteamento para corresponder URLs a endpoints e gerar URLs para endpoints, com um sistema extensível para capturar variáveis de URLs.
- Utilitários HTTP para manipular tags de entidade, controle de cache, datas, agentes de usuário, cookies, arquivs e muito mais.
- um servidor WSGI encadeado para uso durente o desenvolvimento de aplicativos localmente.
- um cliente de teste para simular solicitações HTTP durante os testes sem exigir execução de um servidor.
