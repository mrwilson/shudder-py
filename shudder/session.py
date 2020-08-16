from typing import List

import requests
from lxml import html

from shudder.models import Media, Movie, Series, Review
from shudder.urls import Urls
from os import getenv as env


class ShudderSession(object):
    def __init__(self):
        self.session = requests.session()

    def login(
        self, email: str = env("SHUDDER_EMAIL"), password: str = env("SHUDDER_PASSWORD")
    ):
        csrf_token_xpath = '/html/head/meta[@name="csrf-token"]/@content'

        result = self.session.get(Urls.PAGE_LOGIN)
        csrf_token = html.fromstring(result.text).xpath(csrf_token_xpath)[0]

        self.session.post(
            Urls.API_LOGIN,
            json={"email": email, "password": password},
            headers={"csrf-token": csrf_token},
        )

    def my_list(self) -> List[Media]:
        results = self.session.get(Urls.API_MY_LIST).json()

        def to_media(result: dict) -> Media:
            if result["videoType"] == "movie":
                return Movie(result["title"], result["id"], result)
            else:
                return Series(result["title"], result["id"], result)

        return [to_media(result) for result in results]

    def reviews(self, media: Media, per_page: int = 25) -> List[Review]:
        results = self.session.get(
            Urls.API_REVIEWS + "/" + media.id, params={"per": per_page}
        ).json()

        return [Review(result) for result in results["reviews"]]

    def search(self, search_term: str) -> List[Media]:
        results = self.session.get(
            Urls.API_SEARCH, params={"q": search_term, "field": "title"}
        ).json()

        def to_media(result: dict) -> Media:
            if result["videoType"] == "movie":
                return Movie(result["title"], result["links"]["detail"], result)
            else:
                return Series(result["title"], result["links"]["detail"], result)

        return [to_media(result) for result in results]
