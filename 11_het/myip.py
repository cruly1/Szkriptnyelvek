#!/usr/bin/env python3

import requests
import json


def main():
    url = "https://jsonip.com"
    response = requests.get(url).text
    d = json.loads(response)
    result = d["ip"]
    print(f"Your IP address is: {result}")


if __name__ == "__main__":
    main()
