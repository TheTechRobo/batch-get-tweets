from snscrape.modules.twitter import TwitterTweetScraperMode, TwitterTweetScraper
import json
from alive_progress import alive_bar

with open("twitterids") as ids:
    ids = ids.read().strip("\n").split("\n")

ourjson = []

with alive_bar(total=len(ids)) as bar:
    for identifier in ids:
        bar.text(identifier)
        scraper = TwitterTweetScraper(identifier, mode=TwitterTweetScraperMode.RECURSE)
        for tweet in scraper.get_items():
            ourjson.append(tweet.json())
        bar()

jso = ""
for js in ourjson:
    jso += f"{js}\n"
with open("final", "w+") as f:
    f.write(jso)
