<center>

<h1 align="center">
  <br>
  STRX  - String X
</h1>

<h4 align="center">String-X: Tool for automating commands</h4>

<p align="center">
Ferramenta de automatização rápida e personalizável desenvolvida para auxiliar analistas em diversas tarefas que dizem respeito à manipulação de strings em linhas de comando (linux).
</p>

<p align="center">
  <a href="#/"><img src="https://img.shields.io/badge/python-3.12-orange.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/Supported_OS-Linux-orange.svg"></a>
  <a href="#"><img src="https://img.shields.io/badge/Supported_OS-Mac-orange.svg"></a>
</p>

<p align="center">
  <a href="https://github.com/osintbrazuca/string-x/blob/main/LICENSE"><img src="https://img.shields.io/github/license/osintbrazuca/string-x?color=blue"></a>
  <a href="https://github.com/osintbrazuca/string-x/graphs/contributors"><img src="https://img.shields.io/github/contributors-anon/osintbrazuca/string-x"></a>
  <a href="https://github.com/osintbrazuca/string-x/issues"><img src="https://img.shields.io/github/issues-raw/osintbrazuca/string-x"></a>
  <a href="https://github.com/osintbrazuca/string-x/network/members"><img src="https://img.shields.io/github/forks/osintbrazuca/string-x"></a>
  <img src="https://img.shields.io/github/stars/osintbrazuca/string-x.svg?style=social" title="Stars" /> 
</p>


</center>

```bash
 + Autor:   MrCl0wn
 + Blog:    http://blog.mrcl0wn.com
 + GitHub:  https://github.com/osintbrazuca
 + GitHub:  https://github.com/MrCl0wnLab
 + Twitter: https://twitter.com/MrCl0wnLab
 + Email:   mrcl0wnlab\@\gmail.com
```
## INSTALAÇÃO
```bash
$ pip install -r requirements.txt
$ chmod +x strx
```
Execução
```bash
./strx --help
```


## FLUXO

A ferramenta reconhece fontes de dados, seja por meio do resultado de um cat, script scam ou request via curl. Os dados coletados da source são tratados como string e manipulados via parâmetro reservado da ferramenta. O loop de todo processo está diretamente relacionado aos dados coletados da fonte.


### STRING
É usada uma palavra chave ```{STRING}``` para receber os valores da fonte e concatenar com os comandos definidos pelo usuário. A keyword ```{STRING}``` é usada dentro do parâmetro reservado ```-str, -st```. A ferramenta faz o trabalo de subistiruir a palavra ```{STRING}``` pela string coletada da fonte. O intuito principal é **concatenação + execução de comando**.

Ex:
```bash
ARQUIVO
    host-01.com.br
    host-02.com.br
    host-03.com.br

COMANDO
    1 - cat hosts.txt | ./strx -st "host '{STRING}'"
    2 - ./strx -l hosts.txt -st "host '{STRING}'"

RESULTADO
    host 'host-01.com.br'
    host 'host-02.com.br'
    host 'host-03.com.br'
```
<br>

<center>

![Screenshot](/asset/fluxo.jpg)

</center>

## USO DA FERRAMENTA
```bash 
--help / -h 
```
Isso exibirá ajuda para a ferramenta. Aqui estão todos os opções que ele suporta.

```bash
usage: strx [-h] [-list file] -str cmd [-out file] [-pipe cmd] [-verbose] [-thread <10>] [-pf] [-of] [-filter value] [-sleep <5>] [-module <type:module>] [-pm]

 
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
                                
                                 String-X: Tool for automating commands

options:
             -h, --help             show this help message and exit
             -list, -l file         Arquivo com strings para execução
             -str, -st cmd          String template de comando
             -out, -o file          Arquivo output de valores da execução shell
             -pipe, -p cmd          Comando que será executado depois de um pipe |
             -verbose, -v           Modo verboso
             -thread, -t <10>       Quantidade de threads
             -pf                    Mostrar resultados da execução de função, ignora shell
             -of                    Habilitar output de valores da execução de função
             -filter, -f value      Valor para filtrar strings para execução
             -sleep <5>             Segundos de delay entre threads
             -module <type:module>  Selectionar o tipo e module
             -pm                    Mostrar somente resultados de execução do module
```

### EXEMPLO DE COMANDOS

Comandos que podem ser úteis para a criação de suas tricks.

```bash
./strx -l ./wordlist.txt -str 'curl -skL https://PHISHING/{STRING}/' -p 'grep -E "<title>(.*)</title>"' -v
./strx -l ./desaparecidos.txt -str 'grep -Ei "{STRING}" -R ./encontrados/' -v
./strx -l ./bins.txt -str 'grep -Ei "{STRING}" -R ./telegram/' -o resultado.txt -verbose
./strx -l ./cpfs.txt -str 'curl -skL "https://SERVER/api?={STRING}"' -out resultado.txt
./strx -l ./vermelho.txt -st 'grep -Ei "{STRING}" -R ./cores/' -out resultado.txt
./strx -l ./strings.txt -st 'grep -Ei "{STRING}" -R ./targets/' -pipe "awk -F ':' '{print \$2}'"
./strx -l ../rgs.txt -st './script --rg "{STRING}"' | grep 'SP:' | sort -u
./strx -l ./dump_sql.txt -st 'echo "{STRING}"'  -module 'ext:email' -pm | sort -u
```
### RECEBENDO STRINGS VIA PIPE
Pipe: Envia a saída de um comando para a entrada do próximo comando para continuidade do processamento. Os dados enviados são processados pelo próximo comando que mostrará o resultado do processamento. Pode ser usado desde um simples cat até mesmo resultados de algum fuzzing.

```bash
{PROCESSO}  | ./strx -st '{COMANDO} "{STRING}"'
```

```bash
cat pastas.txt | ./strx -str 'rm -R {STRING}'
cat ips.txt    | ./strx -str 'curl -s https://ipinfo.io/{STRING}/json}'
cat cpfs.txt   | ./strx -str 'grep -Ei "{STRING}" -R ./leak/cpfs/'
cat apis .txt  | ./strx -str './exploit --target {STRING}'
cat hosts.txt  | ./strx -str 'host {STRING}'
curl -s 'https://ipinfo.io/8.8.8.8/json' --raw | jq -r  '.hostname' | ./strx -st 'host {STRING}' -v
curl -s 'https://raw.githubusercontent.com/Zaczero/pihole-phishtank/main/hosts.txt' | ./strx -str  'host {STRING}' -v
```

### USANDO PIPE PYTHON

É aceito o pipe via parâmetro da ferramenta, ele é executado usando o resultado do comando ```-str / -st```.

> **Nota:** Não recomendo usar o ```|``` (pipe) diretamente nos parâmetros da ferramenta, uma vez que a lib python não tem suporte. ainda é possível usar ```|``` (pipe) normalmente na saída.

```bash
-p '{COMMAND}' / -pipe '{COMMAND}'
```

```bash
cat host.txt  | ./strx -str 'host {STRING}' -p 'grep -Eo "[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}"'
cat sql.txt   | ./strx -str 'curl -skL https://TARGET/{STRING}' -pipe 'grep "SQL syntax;"'
cat phish.txt | ./strx -str 'python /tools/priv8.py -t "{STRING}"' -pipe 'grep "VULN"' | create_report
cat hosts.txt | ./strx -str "curl -Iksw 'CODE:%{response_code};IP:%{remote_ip}' https://{STRING}"  -p "grep -o -E 'CODE:.(.*)|IP:.(.*)'" -t 30 
```

**PIPE x {STRING}**

É possível usar a string reservada ```{STRING}``` dentro do contexto de ```-p / -pipe```.
```bash
./strx -l list.txt -str 'echo {STRING}' -p 'touch {STRING}.txt'
```

## FUNÇÕES

É possível usar strings reservadas do tipo **função** que aceitam parâmetros.
 palavras reservadas: ```clear, base64, debase64, sha1, sha256, hex, dehex, md5, str_rand, int_rand``` são identificadas como funções dentro do contexto de ```-str / -st``` e ```-p / -pipe```.

| FUNÇÃO | DESCRIÇÃO | PARÂMETRO |
|  ----  |  ----  |  :----:  |
|  clear  |  remove  \t\n\r e espaços direta e esquerda |  str  |
|  base64  |  converte valor em Base64 |  str  |
|  debase64  |  reverte valor de Base64  |  str  |
|  sha1  |  retorna hash  |  str  |
|  sha256  |   retorna hash    |  str  |
|  md5  |   retorna hash    |  str  |
|  hex  |  retorna hexadecimal  |  str  |
|  dehex  |  reverte valor hexadecimal  |  str  |
|  str_rand  |  valores string randômicos  |  int  |
|  int_rand  |  valores int randômicos  |  int  |
|  ip  |  retorna ip de um host  |  str  |
|  replace  |  substitui valores  |  str  |
|  get  |  envia um request get  |  str  |
|  urlencode  |  Encode de url  |  str  |
|  rev  |  String reversa  |  str  |


## Módulos

O String-X permite estender sua funcionalidade através de módulos especializados. Você pode definir o uso de módulos utilizando o parâmetro `-module` com o formato `tipo:nome_do_módulo`.

### Tipos de Módulos

| Tipo | Código | Descrição |
|------|--------|-----------|
| Output | `out` | Módulos para formatação de saída |
| Connection | `con` | Módulos para estabelecer conexões |
| Extractor | `ext` | Módulos para extrair dados específicos |
| Collector | `clc` | Módulos para coletar e agregar informações |

### Módulos Disponíveis

- **email**: Extrai e valida endereços de email de strings

### Parâmetros Relacionados

- `-module tipo:nome_do_módulo`: Especifica o tipo e nome do módulo a ser utilizado
- `-pm`: Exibe apenas os resultados da execução do módulo, omitindo outras saídas

### Exemplos de Uso

```bash
# Extrair emails de uma lista usando arquivo como entrada
./strx -l emails.txt -str 'echo {STRING}' -module 'ext:email'

# Extrair emails de uma lista via pipe e mostrar apenas resultados do módulo
cat emails.txt | ./strx -str 'echo {STRING}' -module 'ext:email' -pm

# Extrair emails de um dump SQL e ordená-los
./strx -l ./dump_sql.txt -str 'echo "{STRING}"' -module 'ext:email' -pm | sort -u
```

> **Nota:** Você pode adicionar novos módulos conforme a necessidade do seu projeto, seguindo o padrão de desenvolvimento da ferramenta.

### -pf / -op
- -pf Mostrar resultados da execução de função (o shell é ignorado)
- -of Habilitar output de valores da execução de função (salvar valores em arquivo)
```bash
./strx -l domains.txt -str '{STRING}; md5({STRING}); sha256({STRING})' -pf
./strx -l domains.txt -str 'https://{STRING}/index.php?id=int_rand(3)' -pf
./strx -l urls.txt -str 'curl  replace(http:,https:,{STRING})' 
./strx -l hosts.txt -str '{STRING}; ip({STRING})' -pf
./strx -l hosts.txt -str '{STRING}; get(https://{STRING})' -pf
```
> **Nota:** É possivel adicionar funções personalizadas via arquivo [**utils/functions.py**](./utils/functions.py)

## FILTER
Filtrar valores para execução de comando, é usado o parâmetro ```-f / -filter```.
```bash
./strx -l domains.txt -str 'curl {STRING};' -filter .gov.br
./strx -l url.txt -str 'curl {STRING};' -f https
```
---

### TERMINAL  OUTPUT

-  Comando exemplo usado: ```cat hosts.txt  | ./strx -str 'host {STRING}'```

![Screenshot](/asset/img1.png)

-  Comando exemplo usado: ```cat hosts.txt | ./strx -str "curl -Iksw 'CODE:%{response_code};IP:%{remote_ip};HOST:%{url.host};SERVER:%header{server}' https://{STRING}"  -p "grep -o -E 'CODE:.(.*)|IP:.(.*)|HOST:.(.*)|SERVER:.(.*)'" -t 30``` 

![Screenshot](/asset/img3.png)

### VERBOSE
> usando -v / -verbose

-  Comando exemplo usado: ```cat hosts.txt  | ./strx -str 'host {STRING}' -v```

![Screenshot](/asset/img2.png)

### ARQUIVO DE SAÍDA
> formato de arquivo output

```
output-%d-%m-%Y-%H.txt > output-15-06-2025-11.txt
```
