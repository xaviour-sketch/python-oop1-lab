#!/usr/bin/env python3

class Book:
    """A class to represent a book."""
    
    def __init__(self, title, page_count):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            page_count (int): The number of pages in the book
        """
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Get the page count of the book."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """
        Set the page count of the book.
        Validates that the value is an integer.
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        """Print a message when turning a page."""
        print("Flipping the page...wow, you read fast!")