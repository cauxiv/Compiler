class Token:
    def __init__(self, type, word):
        self.type = type
        self.word = word

    def __str__(self):
        return "{}, {}".format(self.type, self.word)


class LexicalAnalyzer:
    def __init__(self):
        self.tokenList = []

    def type_check(self, word):
        # https://www.notion.so/4-3300a033e8e548b790490c54c03f7e5f
        type = 1
        # 위쪽은 가능한 fsm없어도 판별 가능한 것들
        if word == 'int' or word == 'char' or word == 'boolean' or word == 'string':
            type = 2
        elif word == ";":
            type = 3
        elif word == "return":
            type = 4
        elif word == "(":
            type = 5
        elif word == ")":
            type = 6
        elif word == "{":
            type = 7
        elif word == "}":
            type = 8
        elif word == "=":
            type = 9
        # 여기서부터 fsm으로 판단하는 것들
        return type

    def read_file(self, fileName):
        with open(fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace(';', ' ; ')
                line = line.replace(',', ' , ')
                line = line.replace('{', ' { ')
                line = line.replace('}', ' } ')
                line = line.replace('(', ' ( ')
                line = line.replace(')', ' ) ')
                wordList = line.split()
                for word in wordList:
                    strType = self.type_check(word)
                    self.tokenList.append(Token(strType, word))

    def print_token_list(self):
        for token in self.tokenList:
            print(token)


Analyzer = LexicalAnalyzer()
Analyzer.read_file("input_stream.txt")
Analyzer.print_token_list()
