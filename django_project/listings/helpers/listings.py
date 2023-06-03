import json
from pathlib import Path

# file paths
WWR_PATH = Path(__file__).resolve().parent.parent.parent.parent / "jobcrawler"


def get_wwr_listings():
    with open(f"{WWR_PATH}/wwr_listings.json", "r") as f:
        json_content = f.read()

    listings = json.loads(json_content)
    return listings


if __name__ == "__main__":
    print(get_wwr_listings())
