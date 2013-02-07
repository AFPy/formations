=======================
Les bases de python
=======================

Les slides sont en ligne ici: http://afpy.github.com/formations/


2 vs 3
======

Python est un language **de programmation** mature.

Deux versions stables mais à peu près "incompatibles":

* 2.x : Utilisées "en production" un peu partout;
* 3.x : Version en cours de développement

http://docs.python.org

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

Ce programme affiche Hello world!::

    print('Hello world!')


Types
=====

.. literalinclude:: py_types.py

Condition (1/2)
===============

Si::

  >>> if x == 1:
  ...     print('foo')

Si / Sinon::

  >>> if x != 1:
  ...     print('foo')
  ... else:
  ...     print('bar')

Condition (2/2)
===============

Si / Alors / Sinon::

  >>> if x > 3:
  ...     print('foo')
  ... elif x == 1:
  ...     print('bar')
  ... else:
  ...     print('babar')

  >>> if x > 3 and y < 2:
  ...    print('yeah')

  >>> if 3 < x < 5:
  ...    print('bar')

Boucles
=======

Boucle for. Itère sur une liste::

  >>> for i in [1, 2, 3]:
  ...     print(i)

Boucle while. (Tant que)::

  >>> x = 10
  >>> while x:
  ...     x = x - 1

Liste compréhension
====================

Boucle en une ligne. Renvoie une liste::

  >>> x = [a for a in [1, 2, 3]]
  >>> x = [a for a in x if a == 2]
  >>> x = [a for a in range(0, 21) if a % 2 == 0]
  >>> x = [a * 2 for a in range(0, 11)]

Modules et fonctions
====================

Utilisation de modules réutilisables (stdlib/pypi/diy)

Et de fonctions (routines réutilisables)

.. literalinclude:: function.py


Classes
=======

Permet de définir un objet ayant un comportement qu' on lui assigne

.. literalinclude:: classes.py

Tout est objet!!
=================

Toute variable a des propriétés et méthodes::

    >>> 'a'.upper()
    'A'

Pour connaitre les attributs d'une variable::

    >>> dir('a')
