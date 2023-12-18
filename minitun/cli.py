import rich_click as click

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.STYLE_HELPTEXT = ""


def _run_minitun(ssh_host: str, port_specs: tuple[str, ...]) -> None:
    import minitun

    minitun.open_tunnel(ssh_host, *port_specs)


@click.command(
    no_args_is_help=True,
)
@click.argument("ssh-host")
@click.argument("port-specs", nargs=-1)
@click.pass_context
def cli_app(ctx: click.Context, ssh_host: str, port_specs: tuple[str, ...]):
    """
    Makes ports of a remote host available on the current machine using local SSH port forwarding.

    \b
    The first argument [bold cyan]SSH_HOST[/] specifies the SSH host to connect to. Supports aliases from [magenta link={~/.ssh/config}]~/.ssh/config[/]
    All following arguments are [bold cyan]PORT_SPECS[/] which tell minitun how to forward ports. The syntax abbreviates [dim not bold]ssh \\[-L PORT_SPEC]... \\[SSH_HOST][/].

    \b
    [bold]Examples:[/]
    [bold green]  minitun my-server 8080[/]
    [grey]  Forwards port [cyan]8080[/] on [cyan]my-server[/] to port [cyan]8080[/] on [magenta]localhost[/][/]

    \b
    [bold green]  minitun my-server 8080:80[/]
    [grey]  Forwards port [cyan]80[/] on [cyan]my-server[/] to port [cyan]8080[/] on [magenta]localhost[/][/]

    \b
    [bold green]  minitun my-server 8080:10.0.8.42:80[/]
    [grey]  Forwards port [cyan]80[/] on interface [magenta]10.0.8.42[/] of [cyan]my-server[/] to port [cyan]8080[/] on [magenta]localhost[/][/]

    \b
    [bold green]  minitun my-server 192.168.1.42:8080:10.0.8.42:80[/]
    [grey]  Forwards port [cyan]80[/] on interface [magenta]10.0.8.42[/] of [cyan]my-server[/] to port [cyan]8080[/] on the local interface [magenta]192.168.1.42[/][/]

    """

    if len(port_specs) == 0:
        raise click.UsageError("No port specs provided.")

    _run_minitun(ssh_host, port_specs)
