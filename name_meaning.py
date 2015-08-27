import hashlib

class NameMeaning:

    MEANINGS_PATH = 'meanings/meanings.txt'
    meanings = []

    @classmethod
    def _get_meanings(cls):
        if cls.meanings:
            return cls.meanings
        else:
            with open(MEANINGS_PATH, 'r') as file:
                cls.meanings = file.read().splitlines()
                return cls.meanings 

    @classmethod
    def get_meaning(cls, name):
        digest = hashlib.sha1(name).hexdigest()
        index = (int(digest[:5], 16) % len(_get_meanings)) 
        meaning = cls.get_meanings()[index]
