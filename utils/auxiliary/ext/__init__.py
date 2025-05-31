"""
Módulos extratores (extraction) do String-X.

Este subpacote contém módulos especializados na extração de dados específicos
de strings de texto. Cada módulo implementa funcionalidade para identificar
e extrair tipos específicos de informação usando expressões regulares.

Módulos disponíveis:
    email: Extrai endereços de email de textos
    url: Extrai URLs válidas de textos
    domain: Extrai domínios com validação de TLD
    phone: Extrai números de telefone de textos

Uso:
    Os módulos são carregados automaticamente usando a sintaxe 'ext:nome_modulo'
    através do sistema AutoModulo.

Exemplo:
    ./strx -l arquivo.txt -st 'echo "{STRING}"' -module 'ext:email' -pm
"""