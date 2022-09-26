import random as r


class CBlackjack:

    def __init__(self):
        self.__couleur = ["de pique", "de carreau", "de trefle", "de coeur"]
        self.__valeur = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]
        self.__packet = [] # card deck
        self.__comptes = 0 # points of the current player
        self.__comptes1 = 0 # player 1's points
        self.__comptes2 = 0 # player 2's points
        self.__comptesC = 0 # Dealer's points
        self.__main1 = [] # player 1's card
        self.__main2 = [] # player 2's card
        self.__croupier = [] # dealer's card
        self.__tour = 0 # here's where I verify which player turn it is
        self.__perdant1 = False
        self.__perdant2 = False
        self.__perdantC = False

    def creation(self): # Here's where I create the card deck
        for x in self.__valeur:
            for y in self.__couleur:
                self.__packet.append((x, y))

    def debut(self): # here I give each player 2 card and then delete them from the card deck
        for i in range(2):
            R = r.randint(0, len(self.__packet) - 1)
            self.__croupier.append(self.__packet[R])
            del self.__packet[R]
        for i in range(2):
            R = r.randint(0, len(self.__packet)-1)
            self.__main1.append(self.__packet[R])
            del self.__packet[R]
        for i in range(2):
            R = r.randint(0, len(self.__packet)-1)
            self.__main2.append(self.__packet[R])
            del self.__packet[R]

    def hit(self):
        if self.__tour == 0:
            p = True
            print(self.__main1, CB.points())
            t = str(input('Hit or Stand ? '))
            if t.upper() == 'STAND': # here end his turn if he choose 'Stand'
                p = False
                self.__comptes1 = CB.points()
                self.__comptes = 0
                self.__tour = 1
            while p: # I give him another card if he choose 'Hit'
                R = r.randint(0, len(self.__packet)-1)
                self.__main1.append(self.__packet[R])
                del self.__packet[R]
                print(self.__main1, " ", CB.points())
                if CB.get_points() > 21: # if he has more than 21 points I end his turn and set his point to 0
                    p = False
                    self.__comptes = 0
                    self.__perdant1 = True
                    self.__tour = 1
                    break
                t = str(input('Hit or Stand ? '))
                if t.upper() == 'STAND': # here end his turn if he choose 'Stand'
                    p = False
                    self.__comptes1 = CB.points()
                    self.__comptes = 0
                    self.__tour = 1
                    break
        elif self.__tour == 1: # same thing but for player 2
            p = True
            print(self.__main2, CB.points())
            t = str(input('Hit or Stand ? '))
            if t.upper() == 'STAND':
                p = False
                self.__comptes2 = CB.points()
                self.__comptes = 0
                self.__tour = 2
            while p:
                R = r.randint(0, len(self.__packet) - 1)
                self.__main2.append(self.__packet[R])
                del self.__packet[R]
                print(self.__main2, " ", CB.points())
                if CB.get_points() > 21:
                    p = False
                    self.__comptes = 0
                    self.__perdant2 = True
                    self.__tour = 2
                    break
                t = str(input('Hit or Stand ? '))
                if t.upper() == 'STAND':
                    p = False
                    self.__comptes2 = CB.points()
                    self.__comptes = 0
                    self.__tour = 2
                    break
        elif self.__tour == 2: # same thing but for the dealer
            p = True
            print(self.__croupier, CB.points())
            t = str(input('Hit or Stand ? '))
            if t.upper() == 'STAND':
                p = False
                self.__comptesC = CB.points()
                self.__comptes = 0
            while p:
                R = r.randint(0, len(self.__packet)-1)
                self.__croupier.append(self.__packet[R])
                del self.__packet[R]
                print(self.__croupier, " ", CB.points())
                if CB.get_points() > 21:
                    p = False
                    self.__comptes = 0
                    self.__perdantC = True
                    break
                t = str(input('Hit or Stand ? '))
                if t.upper() == 'STAND':
                    p = False
                    self.__comptesC = CB.points()
                    self.__comptes = 0
                    break

    def points(self): # here's where I calculate the number of points depending on the hand of the player
        if self.__tour == 0:
            self.__comptes = 0
            valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10]
            for i in valeur:
                for y in range(-1, len(self.__main1)-1): # I look at every card between 2 and 10 and add him from 2 to 10 points if he has them
                    if i == self.__main1[y][0]: # I look at his hands and if he has them I add the points
                        self.__comptes += i
            valeur = ["As"]
            for i in valeur:
                for y in range(-1, len(self.__main1)-1):
                    if i == self.__main1[y][0]:
                        if self.__comptes > 10: # if he has more than 10 points I add only 1 points
                            self.__comptes += 1
                        else:
                            print(self.__main1)
                            i = int(input('1 or 11 ? \n')) # he choose if he want the ace to give 1 or 11 points
                            if i == 1:
                                self.__comptes += 1
                            else:
                                self.__comptes += 11
            valeur = ["valet", "dame", "roi"]
            for i in valeur:
                for y in range(-1, len(self.__main1)-1): # if he has 1 of them I give him 10 points
                    if i == self.__main1[y][0]:
                        self.__comptes += 10
            return self.__comptes
        if self.__tour == 1: # same for player 2
            self.__comptes = 0
            valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10]
            for i in valeur:
                for y in range(-1, len(self.__main2) - 1):
                    if i == self.__main2[y][0]:
                        self.__comptes += i
            valeur = ["As"]
            for i in valeur:
                for y in range(-1, len(self.__main2) - 1):
                    if i == self.__main2[y][0]:
                        if self.__comptes > 10:
                            self.__comptes += 1
                        else:
                            print(self.__main2)
                            i = int(input('1 or 11 ? \n'))
                            if i == 1:
                                self.__comptes += 1
                            else:
                                self.__comptes += 11
            valeur = ["valet", "dame", "roi"]
            for i in valeur:
                for y in range(-1, len(self.__main2) - 1):
                    if i == self.__main2[y][0]:
                        self.__comptes += 10
            return self.__comptes
        if self.__tour == 2: # same for the dealer
            self.__comptes = 0
            valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10]
            for i in valeur:
                for y in range(-1, len(self.__croupier) - 1):
                    if i == self.__croupier[y][0]:
                        self.__comptes += i
            valeur = ["As"]
            for i in valeur:
                for y in range(-1, len(self.__croupier) - 1):
                    if i == self.__croupier[y][0]:
                        if self.__comptes > 10:
                            self.__comptes += 1
                        else:
                            print(self.__croupier)
                            i = int(input('1 or 11 ? \n'))
                            if i == 1:
                                self.__comptes += 1
                            else:
                                self.__comptes += 11
            valeur = ["valet", "dame", "roi"]
            for i in valeur:
                for y in range(-1, len(self.__croupier) - 1):
                    if i == self.__croupier[y][0]:
                        self.__comptes += 10
            return self.__comptes

    def get_joueur1(self): # return if the player 1 is out and his number of points
        if CB.get_points() < 21:
            return self.__main1, self.__comptes1
        else:
            return 'out'

    def get_joueur2(self): # return if the player 2 is out and his number of points
        if CB.get_points() < 21:
            return self.__main2, self.__comptes2
        else:
            return 'out'

    def get_croupier(self): # return if the dealer is out and his number of points
        if CB.get_points() < 21:
            return self.__croupier, self.__comptesC
        else:
            return 'out'

    def get_tour(self): # I return which player's turn it is
        return self.__tour

    def get_points(self): # return the number of points
        return self.__comptes

    def get_vainqueur(self): # return the winner
        if CB.get_joueur1()[1] > CB.get_joueur2()[1]:
            if CB.get_joueur1()[1] > CB.get_croupier()[1]:
                return 'joueur 1'
            return 'croupier'
        else :
            if CB.get_joueur2()[1] > CB.get_croupier()[1]:
                return 'joueur 2'
            else:
                return 'Croupier'


def partie():
    CB.creation()
    CB.debut()
    CB.hit()
    print('joueur 1 : ', CB.get_joueur1()[1])
    CB.hit()
    print('joueur 2 : ', CB.get_joueur2()[1])
    CB.hit()
    print('croupier : ', CB.get_croupier()[1])
    print('Le vainqueur est : ', CB.get_vainqueur())


CB = CBlackjack()
partie()
