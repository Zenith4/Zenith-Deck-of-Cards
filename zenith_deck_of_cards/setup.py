import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
setup(
    name="zenith_deck_of_cards",
    version="1.1.2",
    description="Deck and card classes",
    packages=["zenith_deck"],
    url="https://github.com/Zenith4/Zenith-Deck-of-Cards",    
)
