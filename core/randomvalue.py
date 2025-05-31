"""
Módulo de geração de valores aleatórios.

Este módulo contém a classe RandomValue que fornece métodos estáticos para
gerar valores aleatórios como User-Agents, URLs de referência, strings e
números aleatórios para uso em testes e automação.
"""
import random
import string


class RandomValue:
    """
    Classe para geração de valores aleatórios.
    
    Esta classe fornece métodos estáticos para gerar diferentes tipos de
    valores aleatórios úteis em testes, automação e simulação de dados.
    """

    @staticmethod
    def get_user_agent_random() -> str:
        """
        Gera uma string User-Agent aleatória.
        
        Cria um User-Agent realista combinando navegadores, sistemas operacionais
        e locales de forma aleatória para simular diferentes ambientes de usuário.
        
        Returns:
            str: String User-Agent aleatória
            
        References:
            https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/User-Agent
        """
        browser = ['Firefox', 'Safari', 'Opera', 'Internet Explorer', 'Chrome']
        os = ['Windows', 'FreeBSD', 'Redhat',
              'Linux', 'Ubuntu', 'Fedora', 'Android']
        locais = ['cs-CZ', 'en-US', 'sk-SK', 'pt-BR', 'pt', 'ms', 'mt_MT']

        elements_user_agent = [browser, os, locais]
        for element_rand in elements_user_agent:
            random.shuffle(element_rand)

        awk_int, browser_int = random.randint(1, 537), random.randint(1, 537)
        user_agent_str = f'{browser[0]}/5.0 (X11; {os[0]} x86_64) AppleWebKit/{
            awk_int}.36 (KHTML, like Gecko) {browser[0]}/51.0.2704.103 {browser[0]}/{browser_int}.36'

        return user_agent_str
    

    @staticmethod
    def get_url_refer_random() -> str:
        """
        Gera uma URL de referência aleatória.
        
        Cria uma URL completa combinando aleatoriamente subdomínios, domínios,
        TLDs, caminhos, arquivos e extensões para simular referers realistas.
        
        Returns:
            str: URL de referência aleatória
        """
        sub = ['www', 'mail', 'ftp', 'admin', 'smtp', 'pop', 'webmail', 'blog',
               'webdisk', 'autodiscover', 'cpanel', 'whm', 'm', '_autodiscover',
               '_tcp', 'test', 'autoconfig', 'imap', 'default', '_domainkey']

        domain = ['instagram', 'yahoo', 'fbi', 'gmail', 'Dice', 'bing',
                   'hotjobs', 'linkedin', 'incruit', 'indeed', 'facebook',
                   'pubgene', 'daylife', 'google', 'aol', 'microsoft']

        gTLD = ['aero', 'arpa', 'biz', 'com', 'coop', 'edu', 'gov', 'info', 'io',
                'int', 'mil', 'museum', 'name', 'net', 'org', 'pro', 'tel']

        file = ['admin', 'index', 'wp-admin', 'info', 'shop', 'file', 'out', 'open',
                'news', 'add', 'profile', 'search', 'open', 'photo', 'insert', 'view']

        ext = ['exe', 'php', 'asp', 'aspx', 'jsf', 'html', 'htm',
               'lua', 'log', 'cgi', 'sh', 'css', 'py', 'sql', 'xml', 'rss']

        path = ['App_Files', 'Assets', 'CFFileServlet', 'CFIDE', 'Communication', 'Computers',
                 'Dynamic', 'FCKeditor', 'Feedback', 'Files', 'Flash', 'Forms', 'Help', 'ICEcore',
                 'IO', 'Image', 'JPG', 'getold', 'JSP', 'KFSI', 'Laguna', 'Login', 'Motors',
                 'Stress', 'getfull', 'Sugarcrm', 'Travel', 'UPLOAD', 'Urussanga', 'UserFiles']

        locais = ['ac', 'ad', 'ae', 'af', 'ag', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at',
                  'au', 'pt', 'cn', 'kr', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm',
                  'ec', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'br']

        elements_url_reference = [sub, domain, gTLD, file, ext, path, locais]
        for element_rand in elements_url_reference:
            random.shuffle(element_rand)

        url_ref = f"http://{sub[0]}.{domain[0]}.{gTLD[0]}.{locais[0]}/{path[0]}/{file[0]}.{ext[0]}"
        return url_ref

    @staticmethod
    def get_str_rand(len_int) -> str:
        """
        Gera uma string aleatória de caracteres alfanuméricos.
        
        Args:
            len_int: Comprimento da string a ser gerada
            
        Returns:
            str: String aleatória com o comprimento especificado
        """
        if len_int:
            len_int = int(len_int)
            rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len_int))
            return rand_str
        

    @staticmethod
    def get_int_rand(len_int) -> str:
        """
        Gera uma string de números aleatórios.
        
        Args:
            len_int: Quantidade de números a serem gerados
            
        Returns:
            str: String contendo números aleatórios concatenados
        """
        if len_int:
            len_int = int(len_int)
            numb_list = [random.randrange(len_int) for _ in range(len_int)]
            rand_str = ','.join(map(str, numb_list)).replace(",", "")
            return rand_str
