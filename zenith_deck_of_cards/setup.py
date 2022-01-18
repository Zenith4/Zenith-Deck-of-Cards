import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").readtext()
setup(
    name="zenith_deck_of_cards",
    version="1.1.3",
    description="Deck and card classes",
    long_description=README,
    long_descrption_content_type="text/markdown",
    author="Zenith4",
    packages=["zenith_deck"],
    url="https://github.com/Zenith4/Zenith-Deck-of-Cards",    
)
