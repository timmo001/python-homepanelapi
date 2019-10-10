"""Enable CLI."""
import click


@click.command()
@click.option("--host", "-h", help="Home Panel's Hostname.")
@click.option("--port", "-P", help="The Home Panel Port.")
@click.option("--ssl", "-s", is_flag=True, help="Use ssl?")
@click.option("--username", "-u", help="Your Home Panel Username.")
@click.option("--password", "-p", help="Your Home Panel Password.")
@click.option("--page", "-a", help="The page.")
@click.option("--card", "-c", help="The card.")
@click.option("--command", "-C", help="The command.")
def cli(
    host: str,
    port: str,
    ssl: bool,
    username: str,
    password: str,
    page: str,
    card: str,
    command: str,
):
    """CLI for this package."""
    from homepanelapi.api import HomePanelApi

    home_panel_api = HomePanelApi(host, port, ssl)
    home_panel_api.authenticate(username, password)
    print(home_panel_api.send_command(page, card, command))


cli()  # pylint: disable=E1120
