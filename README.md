<center>

<h1 align="center">
  <br>
  🔧 String-X (STRX)
</h1>

<h4 align="center">Ferramenta de Automatização para Manipulação de Strings</h4>

<p align="center">
Ferramenta modular de automatização desenvolvida para auxiliar analistas em OSINT, pentest e análise de dados através da manipulação dinâmica de strings em linhas de comando Linux. Sistema baseado em templates com processamento paralelo e módulos extensíveis.
</p>

<p align="center">
  <a href="#/"><img src="https://img.shields.io/badge/python-3.12-orange.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/Supported_OS-Linux-orange.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/Supported_OS-Mac-orange.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
</p>

<p align="center">
  <a href="https://github.com/osintbrazuca/string-x/blob/main/LICENSE"><img src="https://img.shields.io/github/license/osintbrazuca/string-x?color=blue"></a>
  <a href="https://github.com/osintbrazuca/string-x/graphs/contributors"><img src="https://img.shields.io/github/contributors-anon/osintbrazuca/string-x"></a>
  <a href="https://github.com/osintbrazuca/string-x/issues"><img src="https://img.shields.io/github/issues-raw/osintbrazuca/string-x"></a>
  <a href="https://github.com/osintbrazuca/string-x/network/members"><img src="https://img.shields.io/github/forks/osintbrazuca/string-x"></a>
  <img src="https://img.shields.io/github/stars/osintbrazuca/string-x.svg?style=social" title="Stars" /> 
</p>

</center>

## 📋 Índice

- [Características](#-características)
- [Instalação](#-instalação)
- [Conceitos Fundamentais](#-conceitos-fundamentais)
- [Arquitetura Modular](#-arquitetura-modular)
- [Uso da Ferramenta](#-uso-da-ferramenta)
- [Exemplos Práticos](#-exemplos-práticos)
- [Funções Integradas](#-funções-integradas)
- [Sistema de Módulos](#-sistema-de-módulos)
- [Contribuição](#-contribuição)
- [Autor](#-autor)

## ✨ Características

- 🚀 **Processamento Paralelo**: Sistema de threads configurável para alta performance
- 🔧 **Arquitetura Modular**: Extensível através de módulos EXT, CLC, OUT e CON
- 🔄 **Template Dinâmico**: Sistema de substituição de strings com placeholder `{STRING}`
- 🛠️ **Funções Integradas**: Funções de hash, encoding, requests e geração de valores aleatórios
- 📁 **Múltiplas Fontes**: Suporte a arquivos, stdin e pipes
- 🎯 **Filtragem Avançada**: Sistema de filtros para processamento seletivo
- 💾 **Output Flexível**: Salvamento em arquivos com timestamp automático

## 📦 INSTALAÇÃO

### Requisitos
- Python 3.8+
- Linux/MacOS
- Bibliotecas listadas em `requirements.txt`

### Instalação Rápida
```bash
# Clone o repositório
git clone https://github.com/osintbrazuca/string-x.git
cd string-x

# Instale as dependências
pip install -r requirements.txt

# Torne o arquivo executável
chmod +x strx

# Teste a instalação
./strx --help
```

### Instalação via Pip (em breve)
```bash
pip install string-x
```

## 🧠 CONCEITOS FUNDAMENTAIS

### Sistema de Template {STRING}
A ferramenta utiliza o placeholder `{STRING}` como palavra-chave para substituição dinâmica de valores. Este sistema permite que cada linha de entrada seja processada individualmente, substituindo `{STRING}` pelo valor atual.

```bash
# Arquivo de entrada
host-01.com.br
host-02.com.br
host-03.com.br

# Comando com template
./strx -l hosts.txt -st "host '{STRING}'"

# Resultado gerado
host 'host-01.com.br'
host 'host-02.com.br'
host 'host-03.com.br'
```

### Fluxo de Processamento
1. **Entrada**: Dados via arquivo (`-l`) ou stdin (pipe)
2. **Template**: Aplicação do template com `{STRING}`
3. **Processamento**: Execução de comandos/módulos
4. **Pipe**: Processamento adicional opcional (`-p`)
5. **Saída**: Resultado final (tela ou arquivo)

<center>

![Screenshot](/asset/fluxo.jpg)

</center>

## 🏗️ ARQUITETURA MODULAR

String-X utiliza uma arquitetura modular extensível com quatro tipos principais de módulos:

### Tipos de Módulos

| Tipo | Código | Descrição | Localização |
|------|--------|-----------|-------------|
| **Extractor** | `ext` | Extração de dados específicos (email, URL, domain, phone) | `utils/auxiliary/ext/` |
| **Collector** | `clc` | Coleta e agregação de informações (DNS, whois) | `utils/auxiliary/clc/` |
| **Output** | `out` | Formatação e envio de resultados (DB, API, files) | `utils/auxiliary/out/` |
| **Connection** | `con` | Conexões especializadas (SSH, FTP, etc) | `utils/auxiliary/con/` |

### Estrutura de Diretórios
```
string-x/
├── strx                    # Executável principal
├── config/                 # Configurações globais
├── core/                   # Núcleo da aplicação
│   ├── command.py         # Processamento de comandos
│   ├── auto_module.py     # Carregamento dinâmico de módulos
│   ├── thread_process.py  # Sistema de threads
│   ├── format.py          # Formatação e encoding
│   └── style_cli.py       # Interface CLI estilizada
└── utils/
    ├── auxiliary/         # Módulos auxiliares
    │   ├── ext/          # Módulos extratores
    │   ├── clc/          # Módulos coletores
    │   ├── out/          # Módulos de saída
    │   └── con/          # Módulos de conexão
    └── helper/           # Funções auxiliares
```

## 🚀 USO DA FERRAMENTA

### Ajuda e Parâmetros
```bash
./strx --help
```

### Parâmetros Principais

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-l, --list` | Arquivo com strings para processamento | `-l hosts.txt` |
| `-st, --str` | Template de comando com `{STRING}` | `-st "curl {STRING}"` |
| `-o, --out` | Arquivo de saída para resultados | `-o results.txt` |
| `-p, --pipe` | Comando adicional via pipe | `-p "grep 200"` |
| `-v, --verbose` | Modo verboso com detalhes | `-v` |
| `-t, --thread` | Número de threads paralelas | `-t 50` |
| `-f, --filter` | Filtro para seleção de strings | `-f ".gov.br"` |
| `-module` | Seleção de módulo específico | `-module "ext:email"` |
| `-pm` | Mostrar apenas resultados do módulo | `-pm` |
| `-pf` | Mostrar apenas resultados de funções | `-pf` |
| `-of` | Salvar resultados de funções em arquivo | `-of` |
| `-sleep` | Delay entre threads (segundos) | `-sleep 2` |

### Interface da Aplicação

```bash
usage: strx [-h] [-list file] -str cmd [-out file] [-pipe cmd] [-verbose] 
            [-thread <10>] [-pf] [-of] [-filter value] [-sleep <5>] 
            [-module <type:module>] [-pm]

 
                                             _
                                            (T)          _
                                        _         .=.   (R)
                                       (S)   _   /\/(`)_         ▓
                                        ▒   /\/`\/ |\ 0`\      ░
                                        b   |░-.\_|_/.-||
                                        r   )/ |_____| \(    _
                            █               0  #/\ /\#  ░   (X)
                             ░                _| + o |_                ░
                             b         _     ((|, ^ ,|))               b
                             r        (1)     `||\_/||`                r  
                                               || _ ||      _
                                ▓              | \_/ ░     (V)
                                b          0.__.\   /.__.0   ░
                                r           `._  `"`  _.'           ▒
                                               ) ;  \ (             b
                                        ░    1'-' )/`'-1            r
                                                 0`     
                        
                              ██████    ▄▄▄█████▓    ██▀███     ▒██   ██▒ 
                            ▒██    ▒    ▓  ██▒ ▓▒   ▓██ ▒ ██▒   ░▒ █ █ ▒░
                            ░ ▓██▄      ▒ ▓██░ ▒░   ▓██ ░▄█ ▒   ░░  █   ░
                              ▒   ██▒   ░ ▓██▓ ░    ▒██▀▀█▄      ░ █ █ ▒ 
                            ▒██████▒▒     ▒██▒ ░    ░██▓ ▒██▒   ▒██▒ ▒██▒
                            ▒ ▒▓▒ ▒ ░     ▒ ░░      ░ ▒▓ ░▒▓░   ▒▒ ░ ░▓ ░
                            ░ ░▒  ░ ░       ░         ░▒ ░ ▒░   ░░   ░▒ ░
                            ░  ░  ░       ░           ░░   ░     ░    ░  
                                  ░                    ░         ░    ░  
                                  ░                                      
                                
                        String-X: Ferramenta de Automatização para Manipulação de Strings

Parâmetros disponíveis:
             -h, --help             Exibe esta mensagem de ajuda
             -list, -l file         Arquivo com strings para execução
             -str, -st cmd          Template de comando com placeholder {STRING}
             -out, -o file          Arquivo de saída para resultados
             -pipe, -p cmd          Comando executado após pipe |
             -verbose, -v           Modo verboso com informações detalhadas
             -thread, -t <10>       Quantidade de threads para processamento paralelo
             -pf                    Mostrar apenas resultados de funções
             -of                    Salvar resultados de funções em arquivo
             -filter, -f value      Filtro para seleção específica de strings
             -sleep <5>             Delay em segundos entre execução de threads
             -module <type:module>  Especificar tipo e nome do módulo
             -pm                    Mostrar apenas resultados do módulo
```

## 💡 EXEMPLOS PRÁTICOS

### Exemplos Básicos

#### 1. Verificação de Hosts
```bash
# Via arquivo
./strx -l hosts.txt -st "host {STRING}" -v

# Via pipe
cat hosts.txt | ./strx -st "host {STRING}" -v
```

#### 2. Requisições HTTP com Análise
```bash
# Verificar status de URLs
./strx -l urls.txt -st "curl -I {STRING}" -p "grep 'HTTP/'" -t 20

# Extrair títulos de páginas
./strx -l domains.txt -st "curl -sL https://{STRING}" -p "grep -o '<title>.*</title>'" -o titles.txt
```

#### 3. Análise de Logs e Dados
```bash
# Buscar CPFs em leaks
./strx -l cpfs.txt -st "grep -Ei '{STRING}' -R ./database/" -v

# Processar dump SQL
./strx -l dump.txt -st "echo '{STRING}'" -module "ext:email" -pm | sort -u
```

### Exemplos Avançados

#### 1. OSINT e Reconhecimento
```bash
# Informações de IP
cat ips.txt | ./strx -st "curl -s 'https://ipinfo.io/{STRING}/json'" -p "jq -r '.org, .country'"

# Verificação de phishing
./strx -l suspicious.txt -st "curl -skL https://{STRING}/" -p "grep -i 'phish\|scam\|fake'" -t 30

# DNS enumeration
./strx -l subdomains.txt -st "dig +short {STRING}" -module "clc:dns" -pm
```

#### 2. Segurança e Pentest
```bash
# Port scanning com nmap
./strx -l targets.txt -st "nmap -p 80,443 {STRING}" -p "grep 'open'" -t 10

# SQL injection testing
./strx -l urls.txt -st "sqlmap -u '{STRING}' --batch" -p "grep 'vulnerable'" -o sqli_results.txt

# Directory bruteforce
./strx -l wordlist.txt -st "curl -s -o /dev/null -w '%{http_code}' https://target.com/{STRING}" -p "grep '^200$'"
```

#### 3. Processamento de Dados
```bash
# Extração de emails de múltiplos arquivos
./strx -l files.txt -st "cat {STRING}" -module "ext:email" -pm > all_emails.txt

# Conversão de encoding
./strx -l base64_data.txt -st "debase64({STRING})" -pf -of

# Geração de hashes
./strx -l passwords.txt -st "md5({STRING}); sha256({STRING})" -pf -o hashes.txt
```

### Combinação com Pipes do Sistema
```bash
# Pipeline complexo com jq
curl -s 'https://api.github.com/users' | jq -r '.[].login' | ./strx -st "curl -s 'https://api.github.com/users/{STRING}'" -p "jq -r '.name, .location'"

# Processamento de logs do Apache
cat access.log | awk '{print $1}' | sort -u | ./strx -st "whois {STRING}" -p "grep -i 'country'" -t 5

# Análise de certificados SSL
./strx -l domains.txt -st "echo | openssl s_client -connect {STRING}:443 2>/dev/null" -p "openssl x509 -noout -subject"
```

## 🔧 FUNÇÕES INTEGRADAS

String-X inclui funções built-in que podem ser utilizadas dentro dos templates `{STRING}` e comandos pipe. Estas funções são processadas antes da execução dos comandos shell.

### Sintaxe
```bash
# Função simples
./strx -l data.txt -st "funcao({STRING})" -pf

# Múltiplas funções
./strx -l data.txt -st "{STRING}; md5({STRING}); base64({STRING})" -pf

# Função com parâmetros
./strx -l data.txt -st "str_rand(10); int_rand(5)" -pf
```

### Tabela de Funções Disponíveis

| FUNÇÃO | DESCRIÇÃO | PARÂMETRO | EXEMPLO |
|--------|-----------|-----------|---------|
| `clear` | Remove espaços, tabs e quebras de linha | str | `clear({STRING})` |
| `base64` | Codifica string em Base64 | str | `base64({STRING})` |
| `debase64` | Decodifica string Base64 | str | `debase64({STRING})` |
| `sha1` | Gera hash SHA1 | str | `sha1({STRING})` |
| `sha256` | Gera hash SHA256 | str | `sha256({STRING})` |
| `md5` | Gera hash MD5 | str | `md5({STRING})` |
| `hex` | Converte para hexadecimal | str | `hex({STRING})` |
| `dehex` | Converte de hexadecimal | str | `dehex({STRING})` |
| `str_rand` | Gera string aleatória | int | `str_rand(10)` |
| `int_rand` | Gera número aleatório | int | `int_rand(5)` |
| `ip` | Resolve IP de um hostname | str | `ip({STRING})` |
| `replace` | Substitui valores na string | str | `replace(old,new,{STRING})` |
| `get` | Faz requisição HTTP GET | str | `get(https://{STRING})` |
| `urlencode` | Codifica URL | str | `urlencode({STRING})` |
| `rev` | Inverte string | str | `rev({STRING})` |

### Exemplos de Uso das Funções

#### Hashing e Encoding
```bash
# Gerar múltiplos hashes
./strx -l passwords.txt -st "md5({STRING}); sha1({STRING}); sha256({STRING})" -pf

# Trabalhar com Base64
./strx -l data.txt -st "base64({STRING})" -pf
echo "SGVsbG8gV29ybGQ=" | ./strx -st "debase64({STRING})" -pf
```

#### Geração de Valores Aleatórios
```bash
# Gerar strings aleatórias
./strx -l domains.txt -st "https://{STRING}/admin?token=str_rand(32)" -pf

# Gerar números aleatórios
./strx -l apis.txt -st "curl '{STRING}?id=int_rand(6)'" -pf
```

#### Requisições e Resolução
```bash
# Resolver IPs
./strx -l hosts.txt -st "{STRING}; ip({STRING})" -pf

# Fazer requisições GET
./strx -l urls.txt -st "get(https://{STRING})" -pf
```

#### Manipulação de Strings
```bash
# Substituir protocolos
./strx -l urls.txt -st "replace(http:,https:,{STRING})" -pf

# Inverter strings
./strx -l data.txt -st "rev({STRING})" -pf

# URL encoding
./strx -l params.txt -st "urlencode({STRING})" -pf
```

### Parâmetros de Controle

- **`-pf`**: Mostrar apenas resultados das funções (ignora execução shell)
- **`-of`**: Salvar resultados das funções em arquivo de saída

```bash
# Apenas mostrar resultado das funções
./strx -l domains.txt -st "{STRING}; md5({STRING})" -pf

# Salvar funções em arquivo
./strx -l data.txt -st "base64({STRING})" -pf -of -o encoded.txt
```

> **💡 Dica**: Você pode adicionar funções personalizadas editando o arquivo `utils/helper/functions.py`


## 🧩 SISTEMA DE MÓDULOS

String-X utiliza uma arquitetura modular extensível que permite adicionar funcionalidades específicas sem modificar o código principal. Os módulos são organizados por tipo e carregados dinamicamente.

### Tipos de Módulos Disponíveis

| Tipo | Código | Descrição | Localização |
|------|--------|-----------|-------------|
| **Extractor** | `ext` | Extração de dados específicos usando regex | `utils/auxiliary/ext/` |
| **Collector** | `clc` | Coleta de informações de APIs/serviços | `utils/auxiliary/clc/` |
| **Output** | `out` | Formatação e envio de dados | `utils/auxiliary/out/` |
| **Connection** | `con` | Conexões especializadas | `utils/auxiliary/con/` |

### Módulos Extractor (EXT)

Os módulos extratores utilizam expressões regulares para extrair dados específicos de strings.

#### Módulos Disponíveis:
- **`email`**: Extrai endereços de email válidos
- **`domain`**: Extrai domínios e subdomínios
- **`url`**: Extrai URLs completas (HTTP/HTTPS)
- **`phone`**: Extrai números de telefone (formato brasileiro)

```bash
# Extrair emails de dump de dados
./strx -l database_dump.txt -st "echo '{STRING}'" -module "ext:email" -pm

# Extrair domínios de logs
cat access.log | ./strx -st "echo '{STRING}'" -module "ext:domain" -pm | sort -u

# Extrair URLs de arquivos HTML
./strx -l html_files.txt -st "cat {STRING}" -module "ext:url" -pm

# Extrair telefones de documentos
./strx -l documents.txt -st "cat {STRING}" -module "ext:phone" -pm
```

### Módulos Collector (CLC)

Os módulos coletores fazem requisições para serviços externos para obter informações adicionais.

#### Módulos Disponíveis:
- **`dns`**: Coleta registros DNS (A, MX, TXT, etc.)

```bash
# Coletar informações DNS
./strx -l domains.txt -st "{STRING}" -module "clc:dns" -pm

# DNS lookup com verbose
./strx -l subdomains.txt -st "{STRING}" -module "clc:dns" -pm -v
```

### Módulos Output (OUT)

Os módulos de saída formatam e enviam resultados para diferentes destinos.

#### Módulos Disponíveis:
- **`sqlite`**: Salva dados em banco SQLite
- **`mysql`**: Salva dados em banco MySQL
- **`telegram`**: Envia resultados via Telegram Bot
- **`slack`**: Envia resultados via Slack Webhook

```bash
# Salvar em SQLite
./strx -l data.txt -st "process {STRING}" -module "out:sqlite" -pm

# Enviar para Telegram
./strx -l alerts.txt -st "echo '{STRING}'" -module "out:telegram" -pm

# Enviar para Slack
./strx -l reports.txt -st "generate_report {STRING}" -module "out:slack" -pm
```

### Uso de Módulos

#### Sintaxe Básica
```bash
./strx -module "tipo:nome_do_modulo"
```

#### Parâmetros Relacionados
- **`-module tipo:nome`**: Especifica o módulo a ser utilizado
- **`-pm`**: Mostra apenas resultados do módulo (omite saída shell)

#### Exemplos Práticos

```bash
# 1. Extrair emails e salvar ordenados
./strx -l breach_data.txt -st "echo '{STRING}'" -module "ext:email" -pm | sort -u > emails.txt

# 2. Verificar DNS de domínios suspeitos
./strx -l suspicious_domains.txt -st "{STRING}" -module "clc:dns" -pm -v

# 3. Pipeline com múltiplos módulos
cat logs.txt | ./strx -st "echo '{STRING}'" -module "ext:domain" -pm | ./strx -st "{STRING}" -module "clc:dns" -pm

# 4. Extrair URLs e verificar status
./strx -l pages.txt -st "cat {STRING}" -module "ext:url" -pm | ./strx -st "curl -I {STRING}" -p "grep 'HTTP/'"
```

### Desenvolvimento de Novos Módulos

Para criar novos módulos, siga a estrutura padrão:

#### Módulo Extractor (ext)
```python
"""
Módulo extrator personalizado.
"""

import re

def extract(data):
    """
    Função principal de extração.
    
    Args:
        data (str): Dados de entrada para extração
        
    Returns:
        list: Lista de itens extraídos
    """
    pattern = r'seu_regex_aqui'
    matches = re.findall(pattern, data, re.IGNORECASE)
    return matches
```

#### Módulo Collector (clc)
```python
"""
Módulo coletor personalizado.
"""

import requests

def collect(target):
    """
    Função principal de coleta.
    
    Args:
        target (str): Alvo para coleta de informações
        
    Returns:
        dict: Dados coletados
    """
    # Implementar lógica de coleta
    pass
```

### Filtros e Módulos

Você pode combinar filtros com módulos para processamento mais específico:

```bash
# Extrair apenas emails de domínios .gov
./strx -l data.txt -st "echo '{STRING}'" -module "ext:email" -pm -f ".gov"

# DNS lookup apenas para domínios .br
./strx -l domains.txt -st "{STRING}" -module "clc:dns" -pm -f ".br"
```

## 🎯 FILTROS E PROCESSAMENTO SELETIVO

O sistema de filtros permite processar apenas strings que atendam critérios específicos, otimizando performance e precisão.

### Uso de Filtros
```bash
./strx -f "valor_filtro" / ./strx --filter "valor_filtro"
```

### Exemplos de Filtros
```bash
# Filtrar apenas domínios .gov.br
./strx -l domains.txt -st "curl {STRING}" -f ".gov.br"

# Filtrar apenas URLs HTTPS
./strx -l urls.txt -st "curl {STRING}" -f "https"

# Filtrar IPs específicos
./strx -l logs.txt -st "analyze {STRING}" -f "192.168"

# Filtrar extensões de arquivo
./strx -l files.txt -st "process {STRING}" -f ".pdf"
```

### Combinação com Módulos
```bash
# Extrair emails apenas de domínios específicos
./strx -l data.txt -st "echo '{STRING}'" -module "ext:email" -pm -f "gmail.com"

# DNS lookup apenas para subdomínios
./strx -l domains.txt -st "{STRING}" -module "clc:dns" -pm -f "sub."
```

## ⚡ PROCESSAMENTO PARALELO

String-X suporta processamento paralelo através de threads para acelerar operações em grandes volumes de dados.

### Configuração de Threads
```bash
# Definir número de threads
./strx -t 50 / ./strx --thread 50

# Definir delay entre threads
./strx -sleep 2
```

### Exemplos com Threading
```bash
# Verificação rápida de status HTTP
./strx -l big_url_list.txt -st "curl -I {STRING}" -p "grep 'HTTP/'" -t 100

# Resolução DNS em massa
./strx -l huge_domain_list.txt -st "dig +short {STRING}" -t 50 -sleep 1

# Scanning de portas
./strx -l ip_list.txt -st "nmap -p 80,443 {STRING}" -t 20 -sleep 3
```

### Boas Práticas para Threading
- **Rate limiting**: Use `-sleep` para evitar sobrecarga de serviços
- **Número adequado**: Ajuste `-t` conforme recursos disponíveis
- **Monitoramento**: Use `-v` para acompanhar progresso
## 📸 EXEMPLOS VISUAIS

### Execução Básica
**Comando**: `cat hosts.txt | ./strx -str 'host {STRING}'`

![Screenshot](/asset/img1.png)

### Processamento com Threading
**Comando**: `cat hosts.txt | ./strx -str "curl -Iksw 'CODE:%{response_code};IP:%{remote_ip};HOST:%{url.host};SERVER:%header{server}' https://{STRING}" -p "grep -o -E 'CODE:.(.*)|IP:.(.*)|HOST:.(.*)|SERVER:.(.*)'" -t 30`

![Screenshot](/asset/img3.png)

### Modo Verbose
**Comando**: `cat hosts.txt | ./strx -str 'host {STRING}' -v`

![Screenshot](/asset/img2.png)

### Formato de Arquivo de Saída
```
output-%d-%m-%Y-%H.txt > output-15-06-2025-11.txt
```

## 🤝 CONTRIBUIÇÃO

Contribuições são bem-vindas! Para contribuir:

1. **Fork** o repositório
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### Tipos de Contribuição
- 🐛 **Bug fixes**
- ✨ **Novas funcionalidades**
- 📝 **Melhoria da documentação**
- 🧩 **Novos módulos**
- ⚡ **Otimizações de performance**

### Desenvolvimento de Módulos
Para criar novos módulos, consulte a seção [Sistema de Módulos](#-sistema-de-módulos) e siga os padrões estabelecidos.

## 📄 LICENÇA

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 AUTOR

**MrCl0wn**
- 🌐 **Blog**: [http://blog.mrcl0wn.com](http://blog.mrcl0wn.com)
- 🐙 **GitHub**: [@osintbrazuca](https://github.com/osintbrazuca) | [@MrCl0wnLab](https://github.com/MrCl0wnLab)
- 🐦 **Twitter**: [@MrCl0wnLab](https://twitter.com/MrCl0wnLab)
- 📧 **Email**: mrcl0wnlab@gmail.com

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

**💡 Sugestões e feedbacks são sempre bem-vindos!**

**💀 Hacker Hackeia!**

</div>
