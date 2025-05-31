"""
Pacote de módulos auxiliares do String-X.

Este pacote contém módulos auxiliares organizados por tipo de funcionalidade.
Os módulos são carregados dinamicamente pelo sistema AutoModulo baseado
no tipo e nome especificados.

Tipos de módulos suportados:
    ext: Módulos extratores (extraction) - extraem dados específicos de textos
    clc: Módulos coletores (collector) - coletam e agregam informações
    out: Módulos de saída (output) - formatam e direcionam resultados
    con: Módulos de conexão (connection) - estabelecem conexões com serviços

Estrutura de módulos:
    Cada módulo deve herdar de BaseModule e implementar o método run().
    Os módulos são identificados pelo formato 'tipo:nome' (ex: 'ext:email').
"""