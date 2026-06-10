#!/usr/bin/env python3

class Coffee:
    """A class to represent a coffee product."""
    
    def __init__(self, size, price):
        """
        Initialize a Coffee instance.
        
        Args:
            size (str): The size of the coffee (Small, Medium, or Large)
            price (float): The price of the coffee
        """
        self.size = size
        self.price = price
    
    @property
    def size(self):
        """Get the size of the coffee."""
        return self._size
    
    @size.setter
    def size(self, value):
        """
        Set the size of the coffee.
        Validates that the size is Small, Medium, or Large.
        """
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    
    def tip(self):
        """Add a tip to the coffee and print a message."""
        print("This coffee is great, here\u2019s a tip!")
        self.price += 1