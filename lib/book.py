class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Initialize the internal page count attribute
        self.page_count = page_count  # Use the property setter to validate the initial value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

