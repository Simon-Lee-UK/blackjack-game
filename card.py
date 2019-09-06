"""This module contains the 'Card' class and related methods.
"""
import pandas as pd
import numpy as np


class Card:
    """ A class defining the properties of a card object.
    """
    def __init__(self):
        self._suit_array = []
