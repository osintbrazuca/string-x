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
            "sty.info":     "bright_yellow",
            "sty.string":   "bright_magenta",
            "sty.strx":     "bright_magenta",
        }
    )
    base_style = "sty."
    highlights = [
        r"(?P<info>\[\!\] [\w:].*+)",
        r"(?P<param>[\-\w].*)",
        r"(?P<string>\{.*\})",
        r"(?P<strx>strx)"
    ]


class RichArgumentParser(argparse.ArgumentParser):
    def _print_message(self, message, file=None):
        if message:
            obj_style_console = StyleConsole()
            return obj_style_console.console.print(message)

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


class StyleConsole(RegexHighlighter):
    def __init__(self):
        self.console_highlighter = StyleHighlighter()
        self.console = Console(
            # TODO:
            # Verificar melhor formato de highlighter
            #   highlighter=self.console_highlighter, 
            theme=self.console_highlighter.theme,
            log_path=False,
            height=True
        )
