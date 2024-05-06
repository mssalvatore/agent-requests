import click
import requests

AGENTS: tuple[str, ...] = (
    "AdsBot-Google/1.0",
    "anthropic-ai/1.0",
    "Applebot/1.0",
    "CCBot/1.0",
    "ChatGPT-User/1.0",
    "ClaudeBot/1.0",
    "Claude-Web/1.0",
    "DataForSeoBot/1.0",
    "FacebookBot/1.0",
    "FriendlyCrawler/1.0",
    "Google-Extended/1.0",
    "GoogleOther/1.0",
    "GPTBot/1.0",
    "img2dataset/1.0",
    "ImagesiftBot/1.0",
)


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
