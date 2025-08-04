"""
CP1404 - Prac_10 - yufei
Program using an API to access Wikipedia
"""

import wikipedia

def main():

    entry = input("Enter a Wikipedia Search: ")
    while entry != '':
        try:
            wiki_result = wikipedia.page(entry, auto_suggest=True, )
            print(wiki_result.title, '\n', wiki_result.summary, '\n', wiki_result.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print('We need a more specific title. Try one of the following, or a new search:\n', e.options)
        except wikipedia.exceptions.PageError as e:
            print(e)
        entry = input("Enter a Wikipedia Search: ")
    print('Thank you!')


if __name__ == "__main__":
    main()