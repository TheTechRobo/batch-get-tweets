# batch-get-tweets
Use snscrape to batch download tweets recursively!

## Usage
`twitterids` should be in the current working directory. Newline-delimited Twitter IDs.

Stuff is saved to `tweets.jsonl`; the archive (which has a list of already-completed tweets so it doesn't do them again if you restart the program) file is `finished`. For this reason it's recommended to do this in an isolated directory.
