==============================
 Formation python: fonctions.
==============================

X1: test des arguments:
=======================

écrire une fonction qui reçoit des arguments quelconques, et doit vérifier que tous les arguments sont de même type. Elle doit alors renvoyer ce type. Si tous les arguments ne sont pas de même type, elle lève une exception.


X2: vérificateur de type:
=========================

Cette fonction reçoit un dictionnaire ``{nomArgument:type}``. Elle produit, et retourne une fonction qui devra s'assurer que tous ses arguments seront conformes au dictionnaire:

- tous les arguments seront nommés, le nom étant une des clefs du
  dictionnaire. 
- l'argument devra être une instance du type défini par le
  dictionnaire, ou d'un type dérivé.


