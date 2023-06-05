import subprocess
import os
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent

# Change to the Scrapy project directory
scrapy_project_path = BASE_PATH / "jobcrawler"
os.chdir(scrapy_project_path)

# Run the Scrapy spider
spider_name = "wwr_spider"
subprocess.run(["scrapy", "crawl", spider_name])
