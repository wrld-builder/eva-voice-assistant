from config.config import SEARCH_SYSTEM
from googlesearch import search as google_search

def search_system_filter(response_text, message):
    if SEARCH_SYSTEM == 'google':
        buffer = ''
        for link in google_search(response_text, stop=3):
            buffer += link + '\n\n'

        return buffer

    else:
        raise TypeError('Wrong search system in config!')