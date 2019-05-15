class PageStruct:

    """
    represents a wiki entry as a node in a linked list structure
    """

    url_title = None            # e.g. Python_(programming_language
    linked = None               # a linked PageStruct instance

    def __init__(self, link):
        super().__init__()
        self.url_title = link
