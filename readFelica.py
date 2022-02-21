import nfc
import binascii

class MyCanpasPay(object):
    def onConnect(self, tag):
        idm = binascii.hexlify(tag.idm)
        self.idm = idm
        return False

    def getIdm(self):
        clf = nfc.ContactlessFrontend('usb')
        clf.connect(rdwr={'on-connect': self.onConnect})
        clf.close()

        return self.idm

    def setId(self, id):
        self.id = id

    def setPassword(self, password):
        self.password = password

    def setBalance(self, balance):
        self.balance = balance

    def setRanking(self, ranking):
        self.ranking = ranking


    def getId(self):
        return self.id

    def getPassword(self):
        return self.password

    def getBalance(self):
        return self.balance

    def getRanking(self):
        return self.ranking
