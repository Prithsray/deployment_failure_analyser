from rich.console import (
    Console
)

from rich.panel import (
    Panel
)

console = Console()


def print_header(
    title
):

    console.print(
        Panel.fit(
            title,
            style="bold cyan"
        )
    )


def print_section(
    title,
    content
):

    console.print(
        f"\n[bold green]{title}[/bold green]"
    )

    console.print(content)