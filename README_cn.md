<center>

<h1 align="center">
  <br>
  🔧 String-X (STRX)
</h1>

<h4 align="center">字符串操作自动化工具</h4>

<p align="center">
模块化自动化工具，旨在通过Linux命令行中的动态字符串操作协助分析师进行OSINT、渗透测试和数据分析。基于模板的系统，具有并行处理和可扩展模块。
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

## 📋 目录

- [特性](#-特性)
- [安装](#-安装)
- [基本概念](#-基本概念)
- [模块化架构](#-模块化架构)
- [工具使用](#-工具使用)
- [实际示例](#-实际示例)
- [集成函数](#-集成函数)
- [模块系统](#-模块系统)
- [贡献](#-贡献)
- [作者](#-作者)

## ✨ 特性

- 🚀 **并行处理**：可配置的线程系统，实现高性能
- 🔧 **模块化架构**：通过EXT、CLC、OUT和CON模块可扩展
- 🔄 **动态模板**：使用`{STRING}`占位符的字符串替换系统
- 🛠️ **集成函数**：哈希、编码、请求和随机值生成函数
- 📁 **多种输入源**：支持文件、stdin和管道
- 🎯 **高级过滤**：选择性处理的过滤系统
- 💾 **灵活输出**：自动时间戳保存到文件

## 📦 安装

### 系统要求
- Python 3.8+
- Linux/MacOS
- `requirements.txt`中列出的库

### 快速安装
```bash
# 克隆仓库
git clone https://github.com/osintbrazuca/string-x.git
cd string-x

# 安装依赖
pip install -r requirements.txt

# 设置执行权限
chmod +x strx

# 测试安装
./strx --help
```

### 通过Pip安装（即将推出）
```bash
pip install string-x
```

## 🧠 基本概念

### 模板系统 {STRING}
该工具使用`{STRING}`占位符作为动态值替换的关键字。该系统允许单独处理每个输入行，将`{STRING}`替换为当前值。

```bash
# 输入文件
host-01.com.br
host-02.com.br
host-03.com.br

# 带模板的命令
./strx -l hosts.txt -st "host '{STRING}'"

# 生成的结果
host 'host-01.com.br'
host 'host-02.com.br'
host 'host-03.com.br'
```

### 处理流程
1. **输入**：通过文件(`-l`)或stdin(管道)的数据
2. **模板**：使用`{STRING}`应用模板
3. **处理**：命令/模块执行
4. **管道**：可选的额外处理(`-p`)
5. **输出**：最终结果（屏幕或文件）

<center>

![Screenshot](/asset/fluxo.jpg)

</center>

## 🏗️ 模块化架构

String-X使用可扩展的模块化架构，具有四种主要模块类型：

### 模块类型

| 类型 | 代码 | 描述 | 位置 |
|------|------|------|------|
| **提取器** | `ext` | 特定数据提取（email、URL、domain、phone） | `utils/auxiliary/ext/` |
| **收集器** | `clc` | 信息收集和聚合（DNS、whois） | `utils/auxiliary/clc/` |
| **输出** | `out` | 结果格式化和发送（DB、API、files） | `utils/auxiliary/out/` |
| **连接** | `con` | 专用连接（SSH、FTP等） | `utils/auxiliary/con/` |

### 目录结构
```
string-x/
├── strx                    # 主执行文件
├── config/                 # 全局配置
├── core/                   # 应用核心
│   ├── command.py         # 命令处理
│   ├── auto_module.py     # 动态模块加载
│   ├── thread_process.py  # 线程系统
│   ├── format.py          # 格式化和编码
│   └── style_cli.py       # 样式化CLI界面
└── utils/
    ├── auxiliary/         # 辅助模块
    │   ├── ext/          # 提取器模块
    │   ├── clc/          # 收集器模块
    │   ├── out/          # 输出模块
    │   └── con/          # 连接模块
    └── helper/           # 辅助函数
```

## 🚀 工具使用

### 帮助和参数
```bash
./strx --help
```

### 主要参数

| 参数 | 描述 | 示例 |
|------|------|------|
| `-l, --list` | 用于处理的字符串文件 | `-l hosts.txt` |
| `-st, --str` | 带`{STRING}`的命令模板 | `-st "curl {STRING}"` |
| `-o, --out` | 结果输出文件 | `-o results.txt` |
| `-p, --pipe` | 通过管道的额外命令 | `-p "grep 200"` |
| `-v, --verbose` | 详细模式 | `-v` |
| `-t, --thread` | 并行线程数 | `-t 50` |
| `-f, --filter` | 字符串选择过滤器 | `-f ".gov.br"` |
| `-module` | 特定模块选择 | `-module "ext:email"` |
| `-pm` | 只显示模块结果 | `-pm` |
| `-pf` | 只显示函数结果 | `-pf` |
| `-of` | 将函数结果保存到文件 | `-of` |
| `-sleep` | 线程间延迟（秒） | `-sleep 2` |

## 💡 实际示例

### 基本示例

#### 1. 主机验证
```bash
# 通过文件
./strx -l hosts.txt -st "host {STRING}" -v

# 通过管道
cat hosts.txt | ./strx -st "host {STRING}" -v
```

#### 2. HTTP请求与分析
```bash
# 检查URL状态
./strx -l urls.txt -st "curl -I {STRING}" -p "grep 'HTTP/'" -t 20

# 提取页面标题
./strx -l domains.txt -st "curl -sL https://{STRING}" -p "grep -o '<title>.*</title>'" -o titles.txt
```

#### 3. 日志和数据分析
```bash
# 在泄露数据中搜索CPF
./strx -l cpfs.txt -st "grep -Ei '{STRING}' -R ./database/" -v

# 处理SQL转储
./strx -l dump.txt -st "echo '{STRING}'" -module "ext:email" -pm | sort -u
```

### 高级示例

#### 1. OSINT和侦察
```bash
# IP信息
cat ips.txt | ./strx -st "curl -s 'https://ipinfo.io/{STRING}/json'" -p "jq -r '.org, .country'"

# 钓鱼验证
./strx -l suspicious.txt -st "curl -skL https://{STRING}/" -p "grep -i 'phish\|scam\|fake'" -t 30

# DNS枚举
./strx -l subdomains.txt -st "dig +short {STRING}" -module "clc:dns" -pm
```

#### 2. 安全和渗透测试
```bash
# 使用nmap进行端口扫描
./strx -l targets.txt -st "nmap -p 80,443 {STRING}" -p "grep 'open'" -t 10

# SQL注入测试
./strx -l urls.txt -st "sqlmap -u '{STRING}' --batch" -p "grep 'vulnerable'" -o sqli_results.txt

# 目录暴力破解
./strx -l wordlist.txt -st "curl -s -o /dev/null -w '%{http_code}' https://target.com/{STRING}" -p "grep '^200$'"
```

## 🔧 集成函数

String-X包含可在`{STRING}`模板和管道命令中使用的内置函数。这些函数在shell命令执行之前被处理。

### 可用函数表

| 函数 | 描述 | 参数 | 示例 |
|------|------|------|------|
| `clear` | 删除空格、制表符和换行符 | str | `clear({STRING})` |
| `base64` | 将字符串编码为Base64 | str | `base64({STRING})` |
| `debase64` | 解码Base64字符串 | str | `debase64({STRING})` |
| `sha1` | 生成SHA1哈希 | str | `sha1({STRING})` |
| `sha256` | 生成SHA256哈希 | str | `sha256({STRING})` |
| `md5` | 生成MD5哈希 | str | `md5({STRING})` |
| `hex` | 转换为十六进制 | str | `hex({STRING})` |
| `dehex` | 从十六进制转换 | str | `dehex({STRING})` |
| `str_rand` | 生成随机字符串 | int | `str_rand(10)` |
| `int_rand` | 生成随机数字 | int | `int_rand(5)` |
| `ip` | 从主机名解析IP | str | `ip({STRING})` |
| `replace` | 替换字符串中的值 | str | `replace(old,new,{STRING})` |
| `get` | 发起HTTP GET请求 | str | `get(https://{STRING})` |
| `urlencode` | URL编码 | str | `urlencode({STRING})` |
| `rev` | 反转字符串 | str | `rev({STRING})` |

## 🧩 模块系统

String-X使用可扩展的模块化架构，允许在不修改主代码的情况下添加特定功能。模块按类型组织并动态加载。

### 提取器模块 (EXT)

提取器模块使用正则表达式从字符串中提取特定数据。

#### 可用模块：
- **`email`**：提取有效的电子邮件地址
- **`domain`**：提取域名和子域名
- **`url`**：提取完整的URL（HTTP/HTTPS）
- **`phone`**：提取电话号码（巴西格式）

```bash
# 从数据转储中提取电子邮件
./strx -l database_dump.txt -st "echo '{STRING}'" -module "ext:email" -pm

# 从日志中提取域名
cat access.log | ./strx -st "echo '{STRING}'" -module "ext:domain" -pm | sort -u
```

### 收集器模块 (CLC)

收集器模块向外部服务发出请求以获取额外信息。

#### 可用模块：
- **`dns`**：收集DNS记录（A、MX、TXT等）

```bash
# 收集DNS信息
./strx -l domains.txt -st "{STRING}" -module "clc:dns" -pm
```

## 🎯 过滤器和选择性处理

过滤系统允许只处理满足特定条件的字符串。

```bash
# 只过滤.gov.br域名
./strx -l domains.txt -st "curl {STRING}" -f ".gov.br"

# 只过滤HTTPS URL
./strx -l urls.txt -st "curl {STRING}" -f "https"
```

## ⚡ 并行处理

String-X通过线程支持并行处理，以加速大量数据的操作。

```bash
# 快速HTTP状态验证
./strx -l big_url_list.txt -st "curl -I {STRING}" -p "grep 'HTTP/'" -t 100

# 大规模DNS解析
./strx -l huge_domain_list.txt -st "dig +short {STRING}" -t 50 -sleep 1
```

---

### 终端输出

-  使用的示例命令: ```cat hosts.txt  | ./strx -str 'host {STRING}'```

![Screenshot](/asset/img1.png)

-  使用的示例命令: ```cat hosts.txt | ./strx -str "curl -Iksw 'CODE:%{response_code};IP:%{remote_ip};HOST:%{url.host};SERVER:%header{server}' https://{STRING}"  -p "grep -o -E 'CODE:.(.*)|IP:.(.*)|HOST:.(.*)|SERVER:.(.*)'" -t 30``` 

![Screenshot](/asset/img3.png)

### 详细模式
> 使用 -v / -verbose

-  使用的示例命令: ```cat hosts.txt  | ./strx -str 'host {STRING}' -v```

![Screenshot](/asset/img2.png)

### 输出文件
> 输出文件格式

```
output-%d-%m-%Y-%H.txt > output-15-06-2025-11.txt
```

---


## 🤝 贡献

欢迎贡献！请：

1. Fork项目
2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开Pull Request

## 👨‍💻 作者

```bash
 + 作者:   MrCl0wn
 + 博客:   http://blog.mrcl0wn.com
 + GitHub: https://github.com/osintbrazuca
 + GitHub: https://github.com/MrCl0wnLab
 + Twitter: https://twitter.com/MrCl0wnLab
 + 邮箱:   mrcl0wnlab@gmail.com
```

## 📄 许可证

该项目基于MIT许可证 - 详见[LICENSE](LICENSE)文件。


<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

**💡 Sugestões e feedbacks são sempre bem-vindos!**

**💀 Hacker Hackeia!**

</div>

