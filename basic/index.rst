=======================
Les bases de python
=======================


2 vs 3
======

Python est un language **de script** mature.

Deux versions stables mais "incompatibles"


L'interpréteur
===============

L'interpréteur python permet de:

Taper du code en direct::

    $ python
    >>> 1 + 1
    2

Interpréter un script::

    $ python hello_world.py

Interpréter une ligne de commande::

    $ python -c "print('Hello world')"

Un premier programme
====================

Ce programme s'assure qu'il est le module principal et affiche Hello world!

.. literalinclude:: hello_world.py

Types
=====

.. literalinclude:: py_types.py

Tout est objet!!
=================

Toute variable a des propriétés et méthodes::

    >>> 'a'.upper()
    'A'

Pour connaitre les attributs d'une variable::

    >>> dir('a')

Modules et fonctions
====================

Utilisation de modules réutilisables (stdlib/pypi/diy)

Et de fonctions (routines réutilisables)

.. literalinclude:: function.py


Classes
=======

Permet de définir un objet ayant un comportement qu' on lui assigne

.. literalinclude:: classes.py
