#!/usr/bin/env python3

import requests
import json

from fake_useragent import UserAgent


def main():
    session = requests.Session()
    session.headers.update({'User-Agent': UserAgent().random})
    content = session.get("https://www.reddit.com/r/earthporn/.json").content
    d = [x["data"]["url_overridden_by_dest"] for x in json.loads(content)["data"]["children"] if "url_overridden_by_dest" in x["data"]]
    for e in d:
        with open(e.rsplit("/")[-1], "wb") as f:
           f.write(requests.get(e).content)
        print(e)


if __name__ == "__main__":
    main()
