<center>

<h1 align="center">
  <br>
  🔧 String-X (STRX)
</h1>

<h4 align="center">Automation Tool for String Manipulation</h4>

<p align="center">
Modular automation tool developed to assist analysts in OSINT, pentesting, and data analysis through dynamic string manipulation in Linux command lines. Template-based system with parallel processing and extensible modules.
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

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Fundamental Concepts](#-fundamental-concepts)
- [Modular Architecture](#-modular-architecture)
- [Tool Usage](#-tool-usage)
- [Practical Examples](#-practical-examples)
- [Integrated Functions](#-integrated-functions)
- [Module System](#-module-system)
- [Contributing](#-contributing)
- [Author](#-author)

## ✨ Features

- 🚀 **Parallel Processing**: Configurable thread system for high performance
- 🔧 **Modular Architecture**: Extensible through EXT, CLC, OUT and CON modules
- 🔄 **Dynamic Template**: String substitution system with `{STRING}` placeholder
- 🛠️ **Integrated Functions**: Hash, encoding, requests and random value generation functions
- 📁 **Multiple Sources**: Support for files, stdin and pipes
- 🎯 **Advanced Filtering**: Filter system for selective processing
- 💾 **Flexible Output**: Save to files with automatic timestamp

## 📦 INSTALLATION

### Requirements
- Python 3.8+
- Linux/MacOS
- Libraries listed in `requirements.txt`

### Quick Installation
```bash
# Clone repository
git clone https://github.com/osintbrazuca/string-x.git
cd string-x

# Install dependencies
pip install -r requirements.txt

# Make file executable
chmod +x strx

# Test installation
./strx --help
```

### Installation via Pip (coming soon)
```bash
pip install string-x
```

## 🧠 FUNDAMENTAL CONCEPTS

### Template System {STRING}
The tool uses the `{STRING}` placeholder as a keyword for dynamic value substitution. This system allows each input line to be processed individually, replacing `{STRING}` with the current value.

```bash
# Input file
host-01.com.br
host-02.com.br
host-03.com.br

# Command with template
./strx -l hosts.txt -st "host '{STRING}'"

# Generated result
host 'host-01.com.br'
host 'host-02.com.br'
host 'host-03.com.br'
```

### Processing Flow
1. **Input**: Data via file (`-l`) or stdin (pipe)
2. **Template**: Template application with `{STRING}`
3. **Processing**: Command/module execution
4. **Pipe**: Optional additional processing (`-p`)
5. **Output**: Final result (screen or file)

<center>

![Screenshot](/asset/fluxo.jpg)

</center>

## 🏗️ MODULAR ARCHITECTURE

String-X uses an extensible modular architecture with four main types of modules:

### Module Types

| Type | Code | Description | Location |
|------|------|-------------|----------|
| **Extractor** | `ext` | Specific data extraction (email, URL, domain, phone) | `utils/auxiliary/ext/` |
| **Collector** | `clc` | Information collection and aggregation (DNS, whois) | `utils/auxiliary/clc/` |
| **Output** | `out` | Result formatting and sending (DB, API, files) | `utils/auxiliary/out/` |
| **Connection** | `con` | Specialized connections (SSH, FTP, etc) | `utils/auxiliary/con/` |

### Directory Structure
```
string-x/
├── strx                    # Main executable
├── config/                 # Global configurations
├── core/                   # Application core
│   ├── command.py         # Command processing
│   ├── auto_module.py     # Dynamic module loading
│   ├── thread_process.py  # Thread system
│   ├── format.py          # Formatting and encoding
│   └── style_cli.py       # Stylized CLI interface
└── utils/
    ├── auxiliary/         # Auxiliary modules
    │   ├── ext/          # Extractor modules
    │   ├── clc/          # Collector modules
    │   ├── out/          # Output modules
    │   └── con/          # Connection modules
    └── helper/           # Helper functions
```

## 🚀 TOOL USAGE

### Help and Parameters
```bash
./strx --help
```

### Main Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `-l, --list` | File with strings for processing | `-l hosts.txt` |
| `-st, --str` | Command template with `{STRING}` | `-st "curl {STRING}"` |
| `-o, --out` | Output file for results | `-o results.txt` |
| `-p, --pipe` | Additional command via pipe | `-p "grep 200"` |
| `-v, --verbose` | Verbose mode with details | `-v` |
| `-t, --thread` | Number of parallel threads | `-t 50` |
| `-f, --filter` | Filter for string selection | `-f ".gov.br"` |
| `-module` | Specific module selection | `-module "ext:email"` |
| `-pm` | Show only module results | `-pm` |
| `-pf` | Show only function results | `-pf` |
| `-of` | Save function results to file | `-of` |
| `-sleep` | Delay between threads (seconds) | `-sleep 2` |

## 💡 PRACTICAL EXAMPLES

### Basic Examples

#### 1. Host Verification
```bash
# Via file
./strx -l hosts.txt -st "host {STRING}" -v

# Via pipe
cat hosts.txt | ./strx -st "host {STRING}" -v
```

#### 2. HTTP Requests with Analysis
```bash
# Check URL status
./strx -l urls.txt -st "curl -I {STRING}" -p "grep 'HTTP/'" -t 20

# Extract page titles
./strx -l domains.txt -st "curl -sL https://{STRING}" -p "grep -o '<title>.*</title>'" -o titles.txt
```

#### 3. Log and Data Analysis
```bash
# Search CPFs in leaks
./strx -l cpfs.txt -st "grep -Ei '{STRING}' -R ./database/" -v

# Process SQL dump
./strx -l dump.txt -st "echo '{STRING}'" -module "ext:email" -pm | sort -u
```

### Advanced Examples

#### 1. OSINT and Reconnaissance
```bash
# IP information
cat ips.txt | ./strx -st "curl -s 'https://ipinfo.io/{STRING}/json'" -p "jq -r '.org, .country'"

# Phishing verification
./strx -l suspicious.txt -st "curl -skL https://{STRING}/" -p "grep -i 'phish\|scam\|fake'" -t 30

# DNS enumeration
./strx -l subdomains.txt -st "dig +short {STRING}" -module "clc:dns" -pm
```

#### 2. Security and Pentesting
```bash
# Port scanning with nmap
./strx -l targets.txt -st "nmap -p 80,443 {STRING}" -p "grep 'open'" -t 10

# SQL injection testing
./strx -l urls.txt -st "sqlmap -u '{STRING}' --batch" -p "grep 'vulnerable'" -o sqli_results.txt

# Directory bruteforce
./strx -l wordlist.txt -st "curl -s -o /dev/null -w '%{http_code}' https://target.com/{STRING}" -p "grep '^200$'"
```

## 🔧 INTEGRATED FUNCTIONS

String-X includes built-in functions that can be used within `{STRING}` templates and pipe commands. These functions are processed before shell command execution.

### Available Functions Table

| FUNCTION | DESCRIPTION | PARAMETER | EXAMPLE |
|----------|-------------|-----------|---------|
| `clear` | Removes spaces, tabs and line breaks | str | `clear({STRING})` |
| `base64` | Encodes string to Base64 | str | `base64({STRING})` |
| `debase64` | Decodes Base64 string | str | `debase64({STRING})` |
| `sha1` | Generates SHA1 hash | str | `sha1({STRING})` |
| `sha256` | Generates SHA256 hash | str | `sha256({STRING})` |
| `md5` | Generates MD5 hash | str | `md5({STRING})` |
| `hex` | Converts to hexadecimal | str | `hex({STRING})` |
| `dehex` | Converts from hexadecimal | str | `dehex({STRING})` |
| `str_rand` | Generates random string | int | `str_rand(10)` |
| `int_rand` | Generates random number | int | `int_rand(5)` |
| `ip` | Resolves IP from hostname | str | `ip({STRING})` |
| `replace` | Replaces values in string | str | `replace(old,new,{STRING})` |
| `get` | Makes HTTP GET request | str | `get(https://{STRING})` |
| `urlencode` | Encodes URL | str | `urlencode({STRING})` |
| `rev` | Reverses string | str | `rev({STRING})` |

## 🧩 MODULE SYSTEM

String-X uses an extensible modular architecture that allows adding specific functionalities without modifying the main code. Modules are organized by type and loaded dynamically.

### Extractor Modules (EXT)

Extractor modules use regular expressions to extract specific data from strings.

#### Available Modules:
- **`email`**: Extracts valid email addresses
- **`domain`**: Extracts domains and subdomains
- **`url`**: Extracts complete URLs (HTTP/HTTPS)
- **`phone`**: Extracts phone numbers (Brazilian format)

```bash
# Extract emails from data dump
./strx -l database_dump.txt -st "echo '{STRING}'" -module "ext:email" -pm

# Extract domains from logs
cat access.log | ./strx -st "echo '{STRING}'" -module "ext:domain" -pm | sort -u
```

### Collector Modules (CLC)

Collector modules make requests to external services to obtain additional information.

#### Available Modules:
- **`dns`**: Collects DNS records (A, MX, TXT, etc.)

```bash
# Collect DNS information
./strx -l domains.txt -st "{STRING}" -module "clc:dns" -pm
```

## 🎯 FILTERS AND SELECTIVE PROCESSING

The filter system allows processing only strings that meet specific criteria.

```bash
# Filter only .gov.br domains
./strx -l domains.txt -st "curl {STRING}" -f ".gov.br"

# Filter only HTTPS URLs
./strx -l urls.txt -st "curl {STRING}" -f "https"
```

## ⚡ PARALLEL PROCESSING

String-X supports parallel processing through threads to accelerate operations on large data volumes.

```bash
# Fast HTTP status verification
./strx -l big_url_list.txt -st "curl -I {STRING}" -p "grep 'HTTP/'" -t 100

# Mass DNS resolution
./strx -l huge_domain_list.txt -st "dig +short {STRING}" -t 50 -sleep 1
```


### TERMINAL OUTPUT

-  Example command used: ```cat hosts.txt  | ./strx -str 'host {STRING}'```

![Screenshot](/asset/img1.png)

-  Example command used: ```cat hosts.txt | ./strx -str "curl -Iksw 'CODE:%{response_code};IP:%{remote_ip};HOST:%{url.host};SERVER:%header{server}' https://{STRING}"  -p "grep -o -E 'CODE:.(.*)|IP:.(.*)|HOST:.(.*)|SERVER:.(.*)'" -t 30``` 

![Screenshot](/asset/img3.png)

### VERBOSE
> using -v / -verbose

-  Example command used: ```cat hosts.txt  | ./strx -str 'host {STRING}' -v```

![Screenshot](/asset/img2.png)

### OUTPUT FILE
> output file format

```
output-%d-%m-%Y-%H.txt > output-15-06-2025-11.txt
```

---

## 🤝 CONTRIBUTING

Contributions are welcome! Please:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 AUTHOR

```bash
 + Author:  MrCl0wn
 + Blog:    http://blog.mrcl0wn.com
 + GitHub:  https://github.com/osintbrazuca
 + GitHub:  https://github.com/MrCl0wnLab
 + Twitter: https://twitter.com/MrCl0wnLab
 + Email:   mrcl0wnlab@gmail.com
```

## 📄 LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

**💡 Sugestões e feedbacks são sempre bem-vindos!**

**💀 Hacker Hackeia!**

</div>

