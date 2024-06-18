import random
import string


class RandomValue:

    @staticmethod
    def get_user_agent_random() -> str:
        ''' CREATE UA_STRING RANDOMIC
        Ref: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/User-Agent
        '''
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
    def get_string_random(len_int) -> str:
        if len_int:
            str_list = ','.join(str(string.ascii_uppercase+string.digits)).split(',')
            random.shuffle(str_list)
            rand_str = ','.join(map(str, str_list)).replace(",", "")
            return rand_str
        

    @staticmethod
    def get_int_random(len_int) -> str:
        if len_int:
            numb_list = [random.randrange(len_int) for x in range(len_int)]
            numb_str = ','.join(map(str, numb_list)).replace(",", "")
            return numb_str
