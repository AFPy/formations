#! /bin/env python
# -*- coding: latin1 -*-

def loopAndPrint(seq):
    '''boucle sur la séquence seq, et imprime chaque élément.'''

    for element in seq:
        print element

    return len(seq)

datum = 'ga bu zo meu'

def tstloop():
    print 'tst 1\n'
    loopAndPrint(datum)
    print 'tst 2\n'
    liste = datum.split()
    loopAndPrint(liste)
    

tstloop()
