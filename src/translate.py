#!/usr/bin/env python

#
# Pie chart translations
# Michael Weissbacher 2019
#
# When running this don't forget to export the environment variable
# GOOGLE_APPLICATION_CREDENTIALS
#

import pdb
import time
import json
from pprint import pprint
from google.cloud import translate

translate_client = translate.Client()

def translate(text, src, target):
    translation = translate_client.translate(
        text,
        source_language=src,
        target_language=target)

    print(u'Text: {}'.format(text).encode('utf-8').strip())
    print(u'Translation: {}'.format(translation['translatedText']).encode('utf-8').strip())
    return translation['translatedText']

def get_languages():
    return translate_client.get_languages()

def piechart_to_all(languages):
    translations = []
    for l in languages:
        if l['language'] == 'en':
            continue
        foreign_pie = translate("pie chart", "en", l['language'])
        translations.append({"from":["en", "pie chart"], "to": [l['language'], foreign_pie]})
    return translations

def foreign_pie_to_english(foreign_pie):
    foreign_foreign_pie = []
    for x in foreign_pie:
        tr = translate(x["to"][1], x['to'][0], "en")
        foreign_foreign_pie.append({"to":["en", tr], "from": [x['to'][0], x["to"][1]]})
    return foreign_foreign_pie

def all_the_pies():
    languages = get_languages()
    foreign_pie = piechart_to_all(languages)
    foreign_foreign_pie = foreign_pie_to_english(foreign_pie)

    output = {}
    output['pie_to_foreign'] = foreign_pie
    output['foreign_to_pie'] = foreign_foreign_pie

    json.dump(output, open("output.json", "w"), sort_keys=True, indent=4, separators=(',', ': '))

def de_fr_only():
    for l in ["de", "fr"]:
        print l
        print translate(translate("pie chart", "en", l), l, "en")
        print

if __name__ == "__main__":
    all_the_pies()

