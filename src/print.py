#!/usr/bin/env python

# Utility to display pie translation data

import pdb
import time
import json
from pprint import pprint
from google.cloud import translate

pies = json.load(open("../data/all_the_pies.json"))

def get_language_dict():
    language_list = json.load(open("../data/languages.json"))
    language_dict = {}
    for l in language_list:
        if l['language'] in language_dict.keys():
            print "issue"
        language_dict[l['language']] = l['name']
    return language_dict

if __name__ == "__main__":
    languages = get_language_dict()
    
    for p in pies['foreign_to_pie']:
        print "{} - {}".format(p['to'][1], languages[p['from'][0]])
    
