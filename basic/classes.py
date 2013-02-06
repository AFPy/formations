class Personnage(object):

    def __init__(self, type, force):
        self.type = type
        self.force = force

    def attaque(self):
        print("je suis un %s et je tape avec une force de %s" % (self.type, self.force))

merlin = Personnage('Magicien', 2)
merlin.attaque()

denver = Personnage('dino', 3)
denver.attaque()
