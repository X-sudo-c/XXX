import click 
import os 
import sys
import subprocess
from typing import List




def run_command(cmd: List[str], input_data: str = None) -> str:
    try:
        results = subprocess.run(cmd, input=input_data, capture_output = True, text=True, check=True)
        return results.stdout().strip()
    except subprocess.CalledProcessError as e:
        click.echo(f"Error running: {''.join(cmd)}:", err=True)
        





