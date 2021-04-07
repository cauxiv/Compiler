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
            exit()
        nextState = self.table[self.currentState][_input]
        if nextState == "":
            return "Rejected"
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
            return "Unknown Token"

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
        "T1": "ArithmeticOperator",
        "T2": "ArithmeticOperator",
        "T3": "ArithmeticOperator",
        "T4": "ArithmeticOperator"
    },
    "Table": {
        "T0": {"+": "T1", "-": "T2", "*": "T3", "/": "T4"},
        "T1": {"+": "",   "-": "",   "*": "",   "/": ""},
        "T2": {"+": "",   "-": "",   "*": "",   "/": ""},
        "T3": {"+": "",   "-": "",   "*": "",   "/": ""},
        "T4": {"+": "",   "-": "",   "*": "",   "/": ""},
    }
}


# DFA를 ARITHMETIC_OPERATOR로 초기화
dfa = FiniteAutomaton()
dfa.LoadTransitionTable(ARITHMETIC_OPERATOR)
# DFA 사용
# print("---TEST---")
# print("Input이 \"-\"일 때")


with open("input_stream.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        for ch in line:
            print(ch)
            input_char = ch
            nextState = dfa.PeekNextState(input_char)
            dfa.SetState(nextState)
            print("Accepted State입니까?", dfa.IsAccepted())
            print("나의 현재 State:", dfa.GetState())
            print("토큰이 {}로 분류되었습니다.".format(dfa.GetToken()))
            dfa.Reset()
            print("-----------")
