import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
    name="zenith_deck_of_cards",
    version="1.2.0",
    description="Deck and card classes",
    long_description=README,
    author="Zenith4",
    packages=["zenith_deck"],
    url="https://github.com/Zenith4/Zenith-Deck-of-Cards",    
)
