# batch-get-tweets
Use snscrape to batch download tweets recursively!

## Usage
`twitterids` should be in the current working directory. Newline-delimited Twitter IDs.

Stuff is saved to `tweets.jsonl`; the archive file is `finished`. For this reason it's recommended to do this in an isolated directory
