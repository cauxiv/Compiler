# This is nothing. Please see lexical.py
class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}

    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates.update(_dfa["AcceptedStates"])

    def PeekNextState(self, _input):
        if not _input in self.table[self.currentState]:
            print("Unknown Input Symbol is Given.")
            return -1
        nextState = self.table[self.currentState][_input]
        if nextState == "":
            self.Reset()
            return 0
        else:
            return nextState

    def GetState(self):
        return self.currentState

    def SetState(self, _state):
        self.currentState = _state

    def GetToken(self):
        if self.currentState in self.acceptedStates:
            return self.acceptedStates[self.currentState]
        else:
            return 0

    def IsAccepted(self):
        if self.currentState in self.acceptedStates:
            return True
        else:
            return False

    def Reset(self):
        self.currentState = "T0"


# Transition Table of Arithmetic Operator DFA
ARITHMETIC_OPERATOR = {
    "AcceptedStates": {
        "T1": "ARITHMETIC_OPERATOR"
    },
    "Table": {
        "T0": {"+": "T1", "-": "T1", "*": "T1", "/": "T1"},
        "T1": {"+": "",   "-": "",   "*": "",   "/": ""},
    }
}

INTEGER = {
    "AcceptedStates": {
        "T2": "INTEGER",
        "T3": "INTEGER"
    },
    "Table": {
        "T0": {"-": "T1", "0": "T2", "1": "T3", "2": "T3", "3": "T3", "4": "T3", "5": "T3", "6": "T3", "7": "T3", "8": "T3", "9": "T3"},
        "T1": {"-": "", "0": "T2", "1": "T3", "2": "T3", "3": "T3", "4": "T3", "5": "T3", "6": "T3", "7": "T3", "8": "T3", "9": "T3"},
        "T2": {"-": "", "0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""},
        "T3": {"-": "", "0": "T3", "1": "T3", "2": "T3", "3": "T3", "4": "T3", "5": "T3", "6": "T3", "7": "T3", "8": "T3", "9": "T3"},
    }
}

CHAR = {
    "AcceptedStates": {
        "T3": "CHAR"
    },
    "Table": {
        "T0": {"'": "T1", "A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": "", "a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "", "h": "", "i": "", "j": "", "k": "", "l": "", "m": "", "n": "", "o": "", "p": "", "q": "", "r": "", "s": "", "t": "", "u": "", "v": "", "w": "", "x": "", "y": "", "z": ""},
        "T1": {"'": "", "A": "T2", "B": "T2", "C": "T2", "D": "T2", "E": "T2", "F": "T2", "G": "T2", "H": "T2", "I": "T2", "J": "T2", "K": "T2", "L": "T2", "M": "T2", "N": "T2", "O": "T2", "P": "T2", "Q": "T2", "R": "T2", "S": "T2", "T": "T2", "U": "T2", "V": "T2", "W": "T2", "X": "T2", "Y": "T2", "Z": "T2", "a": "T2", "b": "T2", "c": "T2", "d": "T2", "e": "T2", "f": "T2", "g": "T2", "h": "T2", "i": "T2", "j": "T2", "k": "T2", "l": "T2", "m": "T2", "n": "T2", "o": "T2", "p": "T2", "q": "T2", "r": "T2", "s": "T2", "t": "T2", "u": "T2", "v": "T2", "w": "T2", "x": "T2", "y": "T2", "z": "T2"},
        "T2": {"'": "T3", "A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": "", "a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "", "h": "", "i": "", "j": "", "k": "", "l": "", "m": "", "n": "", "o": "", "p": "", "q": "", "r": "", "s": "", "t": "", "u": "", "v": "", "w": "", "x": "", "y": "", "z": ""},
        "T3": {"'": "", "A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": "", "a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "", "h": "", "i": "", "j": "", "k": "", "l": "", "m": "", "n": "", "o": "", "p": "", "q": "", "r": "", "s": "", "t": "", "u": "", "v": "", "w": "", "x": "", "y": "", "z": ""},
    }
}

STRING = {
    "AcceptedStates": {
        "T2": "STRING"
    },
    "Table": {
        "T0": {'"': "T1", "A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": "", "a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "", "h": "", "i": "", "j": "", "k": "", "l": "", "m": "", "n": "", "o": "", "p": "", "q": "", "r": "", "s": "", "t": "", "u": "", "v": "", "w": "", "x": "", "y": "", "z": ""},
        "T1": {'"': "T2", "A": "T1", "B": "T1", "C": "T1", "D": "T1", "E": "T1", "F": "T1", "G": "T1", "H": "T1", "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N": "T1", "O": "T1", "P": "T1", "Q": "T1", "R": "T1", "S": "T1", "T": "T1", "U": "T1", "V": "T1", "W": "T1", "X": "T1", "Y": "T1", "Z": "T1", "a": "T1", "b": "T1", "c": "T1", "d": "T1", "e": "T1", "f": "T1", "g": "T1", "h": "T1", "i": "T1", "j": "T1", "k": "T1", "l": "T1", "m": "T1", "n": "T1", "o": "T1", "p": "T1", "q": "T1", "r": "T1", "s": "T1", "t": "T1", "u": "T1", "v": "T1", "w": "T1", "x": "T1", "y": "T1", "z": "T1"},
        "T2": {'"': "", "A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": "", "a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "", "h": "", "i": "", "j": "", "k": "", "l": "", "m": "", "n": "", "o": "", "p": "", "q": "", "r": "", "s": "", "t": "", "u": "", "v": "", "w": "", "x": "", "y": "", "z": ""},
    }
}

ID = {
    "AcceptedStates": {
        "T1": "ID"
    },
    "Table": {
        "T0": {"_": "T1", "0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "A": "T1", "B": "T1", "C": "T1", "D": "T1", "E": "T1", "F": "T1", "G": "T1", "H": "T1", "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N": "T1", "O": "T1", "P": "T1", "Q": "T1", "R": "T1", "S": "T1", "T": "T1", "U": "T1", "V": "T1", "W": "T1", "X": "T1", "Y": "T1", "Z": "T1", "a": "T1", "b": "T1", "c": "T1", "d": "T1", "e": "T1", "f": "T1", "g": "T1", "h": "T1", "i": "T1", "j": "T1", "k": "T1", "l": "T1", "m": "T1", "n": "T1", "o": "T1", "p": "T1", "q": "T1", "r": "T1", "s": "T1", "t": "T1", "u": "T1", "v": "T1", "w": "T1", "x": "T1", "y": "T1", "z": "T1"},
        "T1": {"_": "T1", "0": "T1", "1": "T1", "2": "T1", "3": "T1", "4": "T1", "5": "T1", "6": "T1", "7": "T1", "8": "T1", "9": "T1", "A": "T1", "B": "T1", "C": "T1", "D": "T1", "E": "T1", "F": "T1", "G": "T1", "H": "T1", "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N": "T1", "O": "T1", "P": "T1", "Q": "T1", "R": "T1", "S": "T1", "T": "T1", "U": "T1", "V": "T1", "W": "T1", "X": "T1", "Y": "T1", "Z": "T1", "a": "T1", "b": "T1", "c": "T1", "d": "T1", "e": "T1", "f": "T1", "g": "T1", "h": "T1", "i": "T1", "j": "T1", "k": "T1", "l": "T1", "m": "T1", "n": "T1", "o": "T1", "p": "T1", "q": "T1", "r": "T1", "s": "T1", "t": "T1", "u": "T1", "v": "T1", "w": "T1", "x": "T1", "y": "T1", "z": "T1"},
    }
}


tokenList = []
# DFA를 ARITHMETIC_OPERATOR로 초기화
dfa = FiniteAutomaton()
dfa.LoadTransitionTable(CHAR)
# DFA 사용
# print("---TEST---")
# print("Input이 \"-\"일 때")


with open("input_stream.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        wordList = line.split()
        for word in wordList:
            if word == 'int' or word == 'char' or word == 'boolean' or word == 'string':
                tokenList.append(Token('VTYPE', word))
                continue
            init = word[0]
            if (init >= 'a' and init <= 'z') or (init >= 'A' and init <= 'Z'):
                dfa.LoadTransitionTable(ID)
            if init == "'":
                dfa.LoadTransitionTable(CHAR)
            if init == '"':
                dfa.LoadTransitionTable(STRING)
            lexem = ''
            for ch in word:
                lexem += ch
                nextState = dfa.PeekNextState(ch)
                if nextState == -1:
                    tokenList.append(Token(dfa.GetState(), lexem))
                    continue
                dfa.SetState(nextState)
                print("Accepted State입니까?", dfa.IsAccepted())
                print("나의 현재 State:", dfa.GetState())
                print("토큰이 {}로 분류되었습니다.".format(dfa.GetToken()))
        dfa.Reset()
        print("-----------")
