import ipdb
class Anagram:
    def __init__(self, word):
        self.word = word
        self.letter_list =  sorted(letter for letter in self.word)

    def match(self, match_list):
        matches = []
        for word in match_list:
            possible_anagram = sorted(letter for letter in word)
            if (possible_anagram == self.letter_list):
                matches.append(word)
        return matches


# ipdb.set_trace()