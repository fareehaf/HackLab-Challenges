from typing import List
from operator import itemgetter

def duplicates(s: str) -> str:
    '''Return all duplicate letters in s in alphabetical order
    
    >>> duplicates('')
    ''
    >>> duplicates('Bookkeeper')
    'eko'
    >>> duplicates('Java')
    'a'
    '''
    repeat = []
    repeated_letters = ''
    
    for letter in s:
        if s.count(letter) > 1 and letter not in repeat:
            repeat.append(letter)
    repeat.sort()
    for letter in repeat:
        repeated_letters += letter
    
    return repeated_letters
    
def shuffle(first: str, second: str, third: str) -> bool:
    '''Return True if third is a shuffle of first and second.
    
    >>> shuffle('abc', 'def', 'aafedc')
    False
    >>> shuffle('ab', 'cd', 'dabc')
    True
    '''
    letter_counts = []
    combined = first + second
    
    if len(third) != len(combined):
        return False
    
    letter_counts.extend(combined)
    
    for letter in third:
        if letter in letter_counts:
            letter_counts.remove(letter)
        else:
            return False
        
    return len(letter_counts) == 0

def remove_vowels(s: str) -> str:
    '''Return s with all vowels removed
    
    >>> remove_vowels('banana')
    'bnn'
    '''
    vowels = 'aeiouAEIOU'
    no_vowels = ''
    
    for letter in s:
        if not (letter in vowels):
            no_vowels += letter
    
    return no_vowels

def new_word(a: str, b: str):
    '''Return a new string if a and b share 3 consecutive letters, that begins
    with a up to and including the 3 letters and ends with b.
    
    >>> new_word('windspeaker','special')
    windspecial
    >>> new_word('cat','rebound')
    ''
    >>> new_word("beansprouts","unanswered")
    'beanswered'
    '''
    for i in range(len(a) - 2):
        if a[i:i+3] in b:
            return a[:i] + b[b.find(a[i:i+3]):]
    return ''

def word_score(words: List[str]) -> List[str]:
    '''
    >>> word_score([])
    []
    >>> word_score(['a', 'cat', 'banana'])
    ['cat', 'banana', 'a']
    >>> word_score(['ff', 'b'])
    ['b', 'ff']
    '''
    scores = []
    ordered_words = []
    
    for word in words:
        score = 0
        repeats = False
        
        for letter in word:
            if word.count(letter) > 1:
                repeats = True
            if letter.islower():
                score += ord(letter) - 96
            else:
                score += ord(letter) - 64
        
        if not repeats:
            score += 10
        scores.append((score, word))
    
    scores.sort(reverse=True)
    scores.sort(key=itemgetter(1))
    
    for (point, string) in scores:
        ordered_words.append(string)
        
    return ordered_words