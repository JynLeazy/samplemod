# -*- coding: utf-8 -*-
from . import helpers
""" core module, imports evaluate if helpers.get_answer function """

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
