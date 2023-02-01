#!/usr/bin/env python

import random

def generate_name():
    syllables = ['ab', 'ad', 'ag', 'al' 'am', 'an' 'akh', 'al', 'am', 'an', 'ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'fri', 'fra', 'fla', 'flu' 'fu', 'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho', 'hu', 'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu', 'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu', 'wa', 'we', 'wi', 'wo', 'wu', 'za', 'ze', 'zi', 'zo', 'zu', 'zhu', 'zic']
    name = ''
    name_length = random.randint(2, 5)
    for i in range(name_length):
        name += random.choice(syllables)
    return name.capitalize()

print(generate_name())

