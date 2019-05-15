from WebWorker import WebWorker
from PageStruct import PageStruct as Page

import sys

w = WebWorker()
p = Page(link='Python_(programming_language)')

iterations = 20
titles = [p.url_title]

for i in range(0, iterations):
    try:
        p = Page(link=w.get_top_link(p))    # iteratively get new links
        titles.append(p.url_title)
    except AssertionError:
        print(titles)
        sys.exit('finished with error')

# TODO: prevent cycles

print(titles)
