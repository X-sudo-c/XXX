import subprocess
import click
from typing import List

def run_command(cmd: List[str], input_data: str = None) -> str:
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(
            cmd,
            input=input_data,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        click.echo(f"Error running {' '.join(cmd)}: {e.stderr}", err=True)
        return ""

@click.group()
def cli():
    """Subdomain Reconnaissance Tool (AssetFinder + SubFinder)"""
    pass

@cli.command()
@click.argument("domain")
@click.option("--subs-only", is_flag=True, help="Only include subdomains (exclude related domains)")
@click.option("--alive", is_flag=True, help="Check which domains are live (using httprobe)")
@click.option("--output", "-o", type=click.Path(), help="Save results to a file")
def scan(domain, subs_only, alive, output):
    """Run AssetFinder and SubFinder on a domain."""
    # Run AssetFinder
    assetfinder_cmd = ["assetfinder"]
    if subs_only:
        assetfinder_cmd.append("--subs-only")
    assetfinder_cmd.append(domain)
    af_results = run_command(assetfinder_cmd)
    
    # Run SubFinder
    subfinder_cmd = ["subfinder", "-d", domain, "-silent"]
    sf_results = run_command(subfinder_cmd)
    
    # Combine and deduplicate
    all_domains = set(af_results.splitlines() + sf_results.splitlines())
    sorted_domains = sorted(all_domains)
    
    # Check for live hosts (if --alive)
    if alive:
        httprobe_input = "\n".join(sorted_domains)
        alive_domains = run_command(["httprobe"], input_data=httprobe_input)
        final_results = alive_domains.splitlines()
    else:
        final_results = sorted_domains
    
    # Output results
    if output:
        with open(output, "w") as f:
            f.write("\n".join(final_results))
        click.echo(f"✅ Saved {len(final_results)} domains to {output}")
    else:
        click.echo("\n".join(final_results))

if __name__ == "__main__":
    cli()