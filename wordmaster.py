import os
import sys
from datetime import datetime
from functools import partial
from typing import List, NoReturn, Tuple

import ety
from nltk.corpus import wordnet
from textblob import TextBlob

from langcodes import langcodes

# clear screen func
clear_screen = partial(os.system, ('cls' if os.name == 'nt' else 'clear'),)


def etymology(word: str) -> NoReturn:
    """
    prints out the etymology tree of the provided word
    """
    etymology = str(ety.tree(word))

    print(' Etymology tree:')
    print(' {}'.format('\n '.join(etymology.split('\n'))))
    print()


def translate_word_to(tb: TextBlob, lang_code: str) -> NoReturn:
    """
    prints out the translation of the TextBlob to the provided
    language code
    """
    try:
        translation = tb.translate(to=lang_code)
    except:
        print(' Could not translate {}'.format(tb.string))
    else:
        print(' "{}" translated into "{}" is: -> {}'.format(
            tb.string, langcodes[lang_code], translation.string))

    print()


def word_meaning(word: str, word_en: str):
    # get the first three meanings at most
    syns = wordnet.synsets(word_en)[:3]
    if syns:
        fmt = ' The most common meaning of "{}" in English is:'
        if len(syns) > 1:
            fmt = ' The most common meanings of "{}" in English are:'

        print(fmt.format(word))
        for syn in syns:
            print(' * {}'.format(syn.definition()))
    else:
        print(' Could not find the meaning(s) of "{}".'.format(word))

    print()


def word_to_en(blob: TextBlob) -> str:
    try:
        return blob.translate(to='en').string
    except:
        return blob.string


def usage() -> NoReturn:
    print(
        ' You can do the following things with your word:\n'
        '  1. Know the meaning\n'
        '  2. Translate it to another language\n\n'
        ' The etymological tree will be displayed in any case\n'
    )


def get_choice() -> Tuple[str, str]:
    # get the word
    word = None
    while not word:
        word = input(' >>> Input your word: ').strip().lower()
        if not word:
            print(' [ERROR] Please enter a word!')

    # get the choice
    choice = None
    while not choice:
        choice = input(' >>> Enter your choice as a number: ')
        if choice not in ('1', '2'):
            print(' [ERROR] Invalid choice. Choices are "1" and "2".')
            choice = None

    # return them both
    return word, choice


def get_to_lang(word: str) -> str:
    while True:
        lang = input(' Enter the language you want to translate "{}" to?\n >>> '.format(word))
        lang = lang.strip().lower()

        if not lang or len(lang) < 2:
            print(' Please enter a valid language!')
            continue

        # is it a language code?
        if len(lang) == 2:
            if lang not in langcodes:
                print(' [ERROR] Invalid/Unsupported language code "{}" entered!'.format(lang))
                continue
            # return it
            return lang

        # otherwise its a word ... try to get the language code
        lang_cap = lang.capitalize()
        if not langcodes.get(lang_cap):
            print(' [ERROR] Invalid/Unsupported language "{}" entered!'.format(lang_cap))
            continue

        return langcodes.get(lang_cap)


def eval_choice(word: str, choice: str) -> NoReturn:
    blob = TextBlob(word)
    lang = blob.detect_language()

    print('\n The detected language of the word "{}" is: {}\n'.format(
        word,
        langcodes.get(lang, 'Unknown language "{}"'.format(lang))
    ))

    # get the english representation of the word entered
    word_en = word if lang == 'en' else word_to_en(blob)

    # Know the meaning
    if choice == '1':
        word_meaning(word, word_en)
    # Translate it to another language
    elif choice == '2':
        to_lang = get_to_lang(word)
        translate_word_to(blob, to_lang)

    # print the etymology
    etymology(word_en)


def repl():
    while True:
        usage()  # print what can be done

        word, choice = get_choice()  #
        eval_choice(word, choice)    #

        # exit? or continue?
        cont = input(' Continue? [Y/n]: ')
        if cont.lower().startswith('n'):
            print('Goodbye!')
            return

        clear_screen()


def main(args: List[str]) -> NoReturn:
    print(
        '\n Hey there! I am the Word Master.\n'
        ' I can tell you everything you want to know about the word that is bugging your mind.\n'
        ' So, welcome to my v1.0 on this fine day in {}\n'.format(datetime.now().strftime('%B.'))
    )

    try:
        repl()
    except KeyboardInterrupt:
        print('\nGoodbye!')
    except:
        raise


if __name__ == '__main__':
    main(sys.argv[1:])
