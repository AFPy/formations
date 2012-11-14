class Voiture(object):

    def __init__(self, marque):
        self.marque = marque

    def roule(self):
        return 'Ma voiture de marque %s roule' % self.marque

la_valeureuse = Voiture('Citroen')
print(la_valeureuse.roule())
