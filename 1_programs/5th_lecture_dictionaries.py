"""

"""
from typing import Dict
from typing import List

color: str = 'red'
if color == 'red':
    trans_color = 'cherveno'
elif color == 'green':
    trans_color = 'zeleno'

rainbow_color: dict = {'red': 'cherveno', 'green': 'zeleno', 'blue': 'sinyo'}
print(rainbow_color['red'])

translator: Dict = dict()
# or
translator2: Dict = {'bike': 'kolelo', 'car': 'kola'}

print(translator)
translator2['bike'] = 'kolelo'

# Get all dict values
colors: List[str] = rainbow_color.values()
print (colors)

#Get all keys
colors2: List[str] = rainbow_color.keys()
print(colors2)

def histogram(word:str) -> Dict:
    """
    :param word:
    :return:
    """

    letter_freq: Dict = dict()
    for letter in word:
        if letter not in letter_freq:
            letter_freq[letter] = 1
        else:
            letter_freq[letter] += 1

    return letter_freq

print(histogram('Data Science Students'))

