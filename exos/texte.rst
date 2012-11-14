=======================================
 Formation python: traitement de texte
=======================================


On va travailler sur un recueil de poèmes de Rimbaud, disponibles en ligne:

- http://www.gutenberg.org/cache/epub/29302/pg29302.txt
- http://pierre.imbaud.fr/rimbaud/les-assis.txt
- http://pierre.imbaud.fr/rimbaud/les-orphelins.txt
- http://pierre.imbaud.fr/rimbaud/pg29302.txt

Chargement du fichier
=====================
On chargera le fichier, soit depuis une clef usb, soit directement depuis internet, pour les linuxiens "connectés"::
   
  wget http://pierre.imbaud.fr/rimbaud/pg29302.txt

Alternativement, on pourra travailler sur un fichier plus court,
contenant un seul poème::

  wget http://pierre.imbaud.fr/rimbaud/les-assis.txt

X1: longueur de ligne
=====================

Ouvrir l'un des fichiers. Imprimer la longueur de chaque ligne, en
nombre de caractères; On pourra la faire précéder du no de ligne.

La sortie doit ressembler à::

  1: 65
  2: 1
  3: 37
  4: 42

etc.

X2: longueur triée
==================
On produit le même type de lignes, mais triées par nombre de
caractères.
*On ne peut plus imprimer avant d'avoir tout lu!*

X3 Nombre de mots:
==================

Imprimer chaque mot, avec le nombre d'occurrences (même type
d'affichage).

X4 Index de mots:
=================

Imprimer un index des mots: pour chaque mot, imprimer la liste de ses
occurrences: (ligne, colonne).

X5 Index de complétion:
=======================
 Pour chaque "radical", donner la liste des mots commençant par ce
 radical.
*classique: cf complétion bash, complétion emacs*




