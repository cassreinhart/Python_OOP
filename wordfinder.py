"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Finds random words in a file"""
    

    def __init__(self, path):
        "reads file and returns words in file"
        self.path = path
        self.words = words = []

        with open(path, 'r') as file:
            for line in file:
                only_word = line.replace('\n', '')
                self.words.append(only_word)

        print(self.describe())

    def __repr__(self):
        return f"<WordFinder path={this.path}>"
    
    def describe(self):
        return f"{len(self.words)} words read"

    def random(self):
        "get random word from file"
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    reads file with blank lines and comments and returns 
    random word, ignoring blank lines and comments
    """
    def __init__(self, path):
        self.path = path
        self.words = words = []

        with open(path, 'r') as file:
            
            for line in file:
                if not line.startswith('#'):
                    if len(line) != 0: 
                        only_word = line.replace('\n', '')
                        self.words.append(only_word)

        print(self.describe())
        
        # super().__init__(path)

        # with open(path, 'r') as file:

        #     for line in file:
        #         if not line.startswith('#') and len(line) != 0:
        #             only_word = line.replace('\n', '')
        #             self.words.append(only_word)
        # print(self.describe())
                    


    

