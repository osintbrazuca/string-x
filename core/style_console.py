from rich.highlighter import RegexHighlighter
from rich.theme import Theme
import argparse
from rich.console import Console

class StyleConsole(RegexHighlighter):
        """
        ref:
            https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
            https://rich.readthedocs.io/en/stable/markup.html#console-markup
            https://rich.readthedocs.io/en/stable/style.html#styles
            https://github.com/Textualize/rich/blob/master/examples/highlighter.py
        """
        theme = Theme(
             {
                  "sty.param": "deep_sky_blue1",
                  "sty.info": "bold deep_sky_blue1",
                }
            )
        base_style = "sty."
        highlights = [r"(?P<info>\[\!\]\s[\w-].*+$)", r"(?P<param>[-\w].*+)"]


class RichArgumentParser(argparse.ArgumentParser):
    def _print_message(self, message, file=None):
        xx = StyleConsole()
        _console = Console(color_system="truecolor", highlighter=xx, theme=xx.theme)
        return _console.print(message)

    def _add_argument(self, *args, **kwargs):
        group = super().add_argument(*args, **kwargs)
        group_option_strings = []
        group_option_strings.extend(group.option_strings)
        group.option_strings.clear()
        [group.option_strings.append(f"[green]{line.replace("\n","")}[/green]") for line in group_option_strings]
        return group
    
    def _add_argument_dest(self, *args, **kwargs):
        group = super().add_argument(*args, **kwargs)
        group.dest = f"[red]{group.dest}[/red]"
        return group.dest


class RawDescriptionHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _split_lines(self, text, width):
        help = [f"[bold red]{line}[/bold red]" for line in text.splitlines()]
        return help
    