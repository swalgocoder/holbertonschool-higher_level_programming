#!/usr/bin/python
def multiple_returns(sentence):
    if not sentence:
        return (None)
    return (len(sentence), sentence[0])
