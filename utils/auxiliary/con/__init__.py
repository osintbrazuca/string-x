#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
String-X - Módulos de Conexão (CON)
====================================

Este pacote contém módulos especializados em estabelecer e gerenciar conexões
com serviços externos, protocolos de rede e APIs.

Os módulos CON (Connection) são responsáveis por:
- Conexões SSH, FTP, SFTP
- Conexões com bancos de dados
- Integração com APIs REST
- Protocolos de rede específicos
- Autenticação e sessões

Estrutura de um módulo CON:
    def connect(target, **kwargs):
        '''
        Estabelece conexão com o alvo.
        
        Args:
            target (str): Endereço ou identificador do alvo
            **kwargs: Parâmetros específicos do protocolo
            
        Returns:
            object: Objeto de conexão ou resultado da conexão
        '''
        pass

Uso com String-X:
    ./strx -l targets.txt -st "{STRING}" -module "con:ssh" -pm

Autor: MrCl0wn
Email: mrcl0wnlab@gmail.com
Versão: 1.0.0
Licença: MIT
"""

__version__ = "1.0.0"
__author__ = "MrCl0wn"
__email__ = "mrcl0wnlab@gmail.com"

# Lista de módulos disponíveis neste pacote
__all__ = []

# Metadados do pacote
PACKAGE_INFO = {
    "name": "con",
    "description": "Módulos de conexão para String-X",
    "type": "connection",
    "version": __version__,
    "modules": __all__
}
