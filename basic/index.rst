=======================
Les bases de python
=======================


2 vs 3
======

Python est un language **de script** mature.

Deux versions stable mais "incompatible"


L'interpreteur
===============

L'interpreteur python permet de:

Taper du code en direct::

    $ python
    >>> 1 + 1
    2

Interpréter un script::

    $ python hello_world.py

Interpreter une ligne de commande::

    $ python -c "print('Hello world')"

Un premier programme
====================

Ce programme s'assure qu'il est le module principale et affiche Hello world!

.. literalinclude:: hello_world.py

Types
=====

.. literalinclude:: py_types.py

Tout est objet!!
=================

Tout variable a des propriétés et méthodes::

    >>> 'a'.upper()
    'A'

Pour connaitre les attributs d'une variable::

    >>> dir('a')

Modules et fonctions
====================

Utilisation de modules réutilisable (stdlib/pypi/diy)

Et de functions (routines réutilisable)

.. literalinclude:: function.py


Classes
=======

Permet de définir un objet ayant un comportement que l'on lui assigne

.. literalinclude:: classes.py
