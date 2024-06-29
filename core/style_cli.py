import argparse
from rich.theme import Theme
from rich.console import Console
from rich.highlighter import RegexHighlighter


class StyleHighlighter(RegexHighlighter):
    """
        ref:
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
        r"(?P<func>((md5|sha256|decode64|encode64|sha1|hex|decodehex)\((.*?)\)))",
        r"(?P<error>(error|not found|timed out))",
        r"(?P<info>\[\!\])",
        r"(?P<label>(TEMPLATE|COMMAND|PIPE):)",
        r"(?P<string>(\{.*\}))",
        r"(?P<strx>strx)",
        r"(?P<domain>(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9])",
        r"(?P<url>(/^http[s]?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$/))",
        r"(?P<ipv6>([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|(([a-f0-9:]+:+)+[a-f0-9]+)$)",
        r"(?P<ipv4>(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))",
        
    ]


class RichArgumentParser(argparse.ArgumentParser):
    def _print_message(self, message, file=None):
        if message:
            obj_cli = StyleCli()
            return obj_cli.console.print(message)

    def _add_argument(self, *args, **kwargs):
        group = super().add_argument(*args, **kwargs)
        group_option_strings = []
        group_option_strings.extend(group.option_strings)
        group.option_strings.clear()
        [group.option_strings.append(f"[green]{line.replace("\n", "")}[/green]") for line in group_option_strings]
        return group

    def _add_argument_dest(self, *args, **kwargs):
        group = super().add_argument(*args, **kwargs)
        group.dest = f"[red]{group.dest}[/red]"
        return group.dest


class RawDescriptionHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _split_lines(self, text: str, width):
        if text:
            help_list = [f"[bright_white]{line}[/bright_white]" for line in text.splitlines()]
            return help_list


class StyleCli(RegexHighlighter):
    def __init__(self):
        self.console_highlighter = StyleHighlighter()
        self.console = Console(
            # TODO:
            # Verificar melhor formato de highlighter
            highlighter=self.console_highlighter, 
            theme=self.console_highlighter.theme,
            log_path=False,
            highlight=True
        )

    def verbose(self, value: str, verbose:bool):
        if value:
            _console = Console(
                    highlighter=self.console_highlighter, 
                    theme=self.console_highlighter.theme,
                    log_path=False,
                    highlight=True
                )
            if verbose is True:
                return _console.log(value)


