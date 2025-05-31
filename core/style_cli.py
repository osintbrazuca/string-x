"""
Módulo de estilização da interface CLI.

Este módulo fornece classes para estilização e highlight da interface de linha
de comando usando a biblioteca Rich, incluindo temas customizados, highlighters
de sintaxe e formatação de argumentos.
"""
import argparse
from rich.theme import Theme
from rich.console import Console
from rich.highlighter import RegexHighlighter


class StyleHighlighter(RegexHighlighter):
    """
    Classe para highlight de sintaxe customizado.
    
    Esta classe define temas e padrões de regex para colorir automaticamente
    diferentes tipos de dados na saída da CLI, incluindo IPs, URLs, domínios,
    funções e strings especiais.
    
    Attributes:
        theme (Theme): Tema Rich com cores customizadas
        base_style (str): Prefixo base para estilos
        highlights (list): Lista de padrões regex para highlight
        
    References:
        https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
        https://rich.readthedocs.io/en/stable/markup.html#console-markup
        https://rich.readthedocs.io/en/stable/style.html#styles
        https://github.com/Textualize/rich/blob/master/examples/highlighter.py
    """
    theme = Theme(
        {
            "sty.param":    "bright_yellow",
            "sty.info":     "bold yellow1",
            "sty.label":    "yellow3",
            "sty.string":   "bright_magenta",
            "sty.strx":     "bright_magenta",
            "sty.domain":   "bright_black",
            "sty.url":      "cyan1",
            "sty.ipv4":     "bright_green",
            "sty.ipv6":     "spring_green3",
            "sty.error":    "bright_red",
            "sty.func":     "blue_violet",
        }
    )
    
    base_style = "sty."
    highlights = [
        r"(?P<error>(error|not found|timed out))",
        r"(?P<info>\[\!\])",
        r"(?P<label>(TEMPLATE|COMMAND|PIPE):)",
        r"(?P<string>(\{.*\}))",
        r"(?P<strx>strx)",
        r"(?P<domain>(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9])",
        r"(?P<url>(/^http[s]?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$/))",
        r"(?P<ipv6>([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|(([a-f0-9:]+:+)+[a-f0-9]+)$)",
        r"(?P<ipv4>(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))",
        r"(?P<func>((clear|base64|debase64|sha1|sha256|md5|hex|dehex|str_rand|int_rand|ip|replace|get)\((.*?)\)))",
    ]


class RichArgumentParser(argparse.ArgumentParser):
    """
    Parser de argumentos customizado com suporte ao Rich.
    
    Esta classe estende ArgumentParser para suportar formatação Rich na
    exibição de mensagens e help do parser.
    """
    def _print_message(self, message, file=None):
        """
        Imprime mensagem usando console Rich.
        
        Args:
            message: Mensagem a ser impressa
            file: Arquivo de destino (não utilizado)
        """
        if message:
            cli = StyleCli()
            return cli.console.print(message)

    def _add_argument(self, *args, **kwargs):
        """
        Adiciona argumento com formatação Rich em verde.
        
        Args:
            *args: Argumentos posicionais do argparse
            **kwargs: Argumentos nomeados do argparse
            
        Returns:
            Grupo de argumentos formatado
        """
        group = super().add_argument(*args, **kwargs)
        group_option_strings = []
        group_option_strings.extend(group.option_strings)
        group.option_strings.clear()
        [group.option_strings.append(f"[green]{line.replace('\n', '')}[/green]") for line in group_option_strings]
        return group

    def _add_argument_dest(self, *args, **kwargs):
        """
        Adiciona argumento com destino formatado em vermelho.
        
        Args:
            *args: Argumentos posicionais do argparse
            **kwargs: Argumentos nomeados do argparse
            
        Returns:
            Destino formatado do argumento
        """
        group = super().add_argument(*args, **kwargs)
        group.dest = f"[red]{group.dest}[/red]"
        return group.dest


class RawDescriptionHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """
    Formatador customizado para descrições de help.
    
    Esta classe estende RawDescriptionHelpFormatter para aplicar formatação
    Rich às linhas de descrição do help dos argumentos.
    """
    def _split_lines(self, text: str, width):
        """
        Divide texto em linhas com formatação Rich.
        
        Args:
            text (str): Texto a ser dividido
            width: Largura máxima (não utilizado)
            
        Returns:
            Lista de linhas formatadas com markup Rich
        """
        if text:
            help_list = [f"[bright_white]{line}[/bright_white]" for line in text.splitlines()]
            return help_list


class StyleCli(RegexHighlighter):
    """
    Classe principal para interface CLI estilizada.
    
    Esta classe gerencia o console Rich com highlighter customizado e
    fornece métodos para saída formatada e logs verbose.
    
    Attributes:
        console_highlighter (StyleHighlighter): Instância do highlighter
        console (Console): Console Rich configurado
    """
    def __init__(self):
        """
        Inicializa StyleCli com console Rich configurado.
        """
        self.console_highlighter = StyleHighlighter()
        self.console = Console(
            highlighter=self.console_highlighter, 
            theme=self.console_highlighter.theme,
            log_path=False,
            highlight=True,
            log_time_format='[%f] %Y-%m-%d,%H:%M:%S'
        )

    def verbose(self, value: str, verbose: bool):
        """
        Exibe log verbose se habilitado.
        
        Args:
            value (str): Mensagem a ser exibida
            verbose (bool): Flag indicando se verbose está ativo
            
        Returns:
            Resultado do log ou None se verbose desabilitado
        """
        if value and verbose is True:
            return self.console.log(value)


