import click


@click.group()
def cli():
    """zkSync Era commands for Ape."""


@cli.command()
@click.pass_context
def info(ctx):
    """Show connected zkSync Era network info."""
    from ape import networks

    ecosystem = networks.get_ecosystem("zksync")
    click.echo(f"Ecosystem: {ecosystem.name}")
    for name, network in ecosystem.networks.items():
        click.echo(f"  {name}: chain_id={network.chain_id}")
