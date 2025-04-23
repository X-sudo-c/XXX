import click 
import os 
import sys
import subprocess



@click.command()
@click.argument('domain')
@click.option('--no-assetfinder',"-ns", help='This option disables assetfinder', is_flag=True)
@click.option("--no-subfinder", "-nsf", help='This option disables subfinder', is_flag=True)

def main(domain, no_assetfinder, no_subfinder):
    click.echo(f"Starting enumeration for: {domain}")


    if not no_assetfinder:
        click.echo("Running assetfinder...")

    if not no_subfinder:
        click.echo("Running subfinder...")

    
    
      






if __name__ == "__main__":
    main()




