import click
import requests

AGENTS: tuple[str, ...] = ("AGENT 1", "AGENT 2", "AGENT 3", "AGENT 4", "AGENT 5")


@click.command()
@click.option("--target", "-t", help="The target URL to send requests to", required=True, type=str)
@click.option(
    "--num-runs",
    "-n",
    required=True,
    help="The number of requests to send for each user agent",
    type=click.IntRange(min=0),
)
def main(target: str, num_runs: int):
    for _ in range(num_runs):
        for agent in AGENTS:
            requests.get(target, headers={"User-Agent": agent})


if __name__ == "__main__":
    main()
