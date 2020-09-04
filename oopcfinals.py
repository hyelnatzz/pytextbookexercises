import  random

class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return self.name + ' ($' + str(self.prizeMoney) + ')'


class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obsecuredPhrase, guessed):
        rep = self.name + ' has $' + str(self.prizeMoney) + '\n\n'
        rep += 'Category: {} \n Phrase: {} \n Guessed: {} \n\n'.format(category,obsecuredPhrase,guessed)
        return input(rep + "Guess a letter, phrase, or type 'exit' or 'pass'")

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self,name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        num = random.randint(1,10)
        if num > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        letters = LETTERS 
        if super().prizeMoney < VOWEL_COST:
            for i in VOWELS:
                if i in letters:
                    letters.replace(i,'')
        for j in guessed:
            if j in letters:
                letters.replace(j,'')
        return letters

    def getMove(self, category, obsecuredPhrase, guessed):
        letters = self.getPossibleLetters(guessed)
        if letters == '':
            return 'pass'
        choice_ = self.smartCoinFlip()
        if choice_:
            return WOFComputerPlayer.SORTED_FREQUENCIES[-1]
        else:
            return random.choice(WOFComputerPlayer.SORTED_FREQUENCIES)
