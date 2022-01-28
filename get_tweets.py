from snscrape.modules.twitter import TwitterTweetScraperMode, TwitterTweetScraper
import json
from alive_progress import alive_bar

with open("twitterids") as ids:
    ids = ids.read().strip("\n").split("\n")
try:
    with open("finished") as finished_ids:
        finished = json.load(finished_ids)
except IOError:
    finished = []

def writejson(finished, ourjson):
    to_write = ""
    for tweet in ourjson:
        to_write += f"{tweet}\n"
    with open("tweets.jsonl", "w+") as fil:
        fil.write(to_write)
    with open("finished", "w+") as fin:
        fin.write(json.dumps(finished))

with alive_bar(total=len(ids)) as bar:
    for identifier in ids:
        if int(identifier) in finished:
            print(f"{identifier} already in archive file; skipping")
            bar()
            continue
        ourjson = []
        bar.text(identifier)
        scraper = TwitterTweetScraper(identifier, mode=TwitterTweetScraperMode.RECURSE)
        for tweet in scraper.get_items():
            tweetdata = tweet.json()
            finished.append(tweet.id)
            ourjson.append(tweetdata)
        writejson(finished, ourjson)
        bar()
