from __future__ import annotations
from typing import Any
import requests
import time
import json
from typing import List

from typing_extensions import TypedDict


def getCreatedDateFromSubredditData(data: Any) -> float:
    return data['data']['created']


def downloadPostAboutData(subreddit: str):
    r = requests.get(url="https://www.reddit.com/r/" +
                     subreddit + "/about.json", headers={"User-agent": "Sussy Imposter Amongus"})
    return r.json()


def downloadPostMetaData(subredditName: str) -> Any:
    pass


def getSplit():
    pass


if __name__ == "__main__":
    a = downloadPostAboutData("whenthe")
    print(getCreatedDateFromSubredditData(a))
