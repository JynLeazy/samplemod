# -*- coding: utf-8 -*-
''' core module, imports evaluate if helpers.get_answer function '''

from . import helpers


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
