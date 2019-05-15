from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup as Parser
from PageStruct import PageStruct as Page


class WebWorker(object):

    BASE_PAGE_URL = 'https://en.wikipedia.org/wiki/'
    RANDOM_WIKI_URL = 'https://en.wikipedia.org/wiki/Special:Random'

    @staticmethod
    def make_request(url):
        """
        makes a web request
        :param url: url to open
        :return: raw html encoded as a string
        """
        request = Request(url)
        try:
            response = urlopen(request)
        except HTTPError:
            raise AssertionError('page has a broken link. Received url: ' + url)
        html = response.read().decode('utf-8')
        return html

    def retrieve_content(self, page):
        """
        get the html content associated with a page
        :param page: a PageStruct instance
        :return: data structure representing the nested html document
        """
        try:
            url = self.BASE_PAGE_URL + page.url_title
            html = self.make_request(url)
            info = Parser(html, 'html.parser')
        except AttributeError:
            raise AssertionError('page must be a PageStruct with an initialized '
                                 'url_title field')
        return info

    def get_random_page(self):
        """
        TODO: BROKEN
        generates a PageStruct representing a random entry
        :return: a PageStruct instance with a random (but valid) url_title
        and null linked page
        """
        p = Page(link=self.RANDOM_WIKI_URL)
        return p

    def get_top_link(self, page):
        """
        Get the primary link from a page
        :param page: a PageStruct instance
        :return: url title for the linked page e.g. Interpreted_language
        """
        info = self.retrieve_content(page)
        ps = info.find_all('p')
        # find the correct first paragraph
        intro_position = 0
        while ps[intro_position].get('class') is not None:
            intro_position += 1
        intro = ps[intro_position]
        intro_lns = intro.find_all('a')
        primary_ln = intro_lns[0]
        string = primary_ln.get('href')
        return string[6:]   # remove the leading '/wiki/'
