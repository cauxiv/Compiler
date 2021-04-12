class Token:
    def __init__(self, id, lexeme):
        self.id = id
        self.lexeme = lexeme

    def getID(self):
        return self.id

    def getLexeme(self):
        return self.lexeme


class LexicalAnalyzer:
    def __init__(self, TokenTable):
        self.lexemList = []
        self.tokenList = []
        self.tokenTable = TokenTable

    def WordClassfier(self, stream):
        lex = ''
        preValidLex = ''
        quotesTrigger = False
        idTrigger = False
        for i, ch in enumerate(stream):
            if i == 0:
                lex = ch
                continue
            # 문자열 처리(앞에 둬야함)
            if quotesTrigger == True and ch != '"':
                lex += ch
                continue
            if ch == '"':
                if quotesTrigger == True:
                    lex += ch
                    self.lexemList.append(lex)
                    preValidLex = lex
                    lex = ''
                else:
                    if lex != '':
                        self.lexemList.append(lex)
                        preValidLex = lex
                    lex = ch
                quotesTrigger = not quotesTrigger
                continue
            # 0a 12345b와 같은 문자열 처리
            if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or ch == '_':
                if lex != '':
                    if lex[0] == '-' or (lex[0] >= '0' and lex[0] <= '9'):
                        self.lexemList.append(lex)
                        lex = ''
            # Integer처리
            if ch >= '0' and ch <= '9':
                if lex != '':
                    if not ((lex[0] >= 'A' and ch <= 'Z') and (lex[0] >= 'a' and ch <= 'Z') or lex[0] == '_'):
                        if stream[i-1] == '0':
                            self.lexemList.append(lex)
                            lex = ''
            # (,),{,},[,],; 처리
            if ch == '(' or ch == ')' or ch == '{' or ch == '}' or ch == '[' or ch == ']' or ch == ';':
                if lex != '':
                    self.lexemList.append(lex)
                    lex = ''
                self.lexemList.append(ch)
                preValidLex = ch
                continue
            # 연산자 처리
            elif ch == '+' or ch == '*' or ch == '/':
                if lex != '':
                    self.lexemList.append(lex)
                    lex = ''
                self.lexemList.append(ch)
                preValidLex = ch
                continue
            # - 를 해결하기 위해 노력한 부분이 여기. preValidLex로 구현
            elif ch == '-':
                if lex != '':
                    self.lexemList.append(lex)
                    preValidLex = lex
                    lex = ''
                if not(preValidLex == '+' or preValidLex == '-' or preValidLex == '*' or preValidLex == '/'):
                    self.lexemList.append(ch)
                    preValidLex = ch
                    continue
            # 공백문자 처리
            elif ch < '!':
                if lex != '':
                    self.lexemList.append(lex)
                    preValidLex = lex
                    lex = ''
                continue
            # 대입자 처리
            elif ch == '=':
                if stream[i-1] == '<' or stream[i-1] == '>' or stream[i-1] == '=' or stream[i-1] == '!':
                    self.lexemList.append(lex[:-1])
                    self.lexemList.append(lex[-1]+ch)
                    preValidLex = lex[-1]+ch
                else:
                    if lex != '':
                        self.lexemList.append(lex)
                    self.lexemList.append(ch)
                    preValidLex = ch
                lex = ''
                continue
            lex += ch

    def TypeChecker(self, word):
        # https://www.notion.so/4-3300a033e8e548b790490c54c03f7e5f
        if word == 'int' or word == 'char' or word == 'boolean' or word == 'string':
            return 2
        elif word == 'if' or word == 'else' or word == 'while' or word == 'class':
            return 3
        elif word == '>' or word == '<' or word == '==' or word == '!=' or word == '<=' or word == '>=':
            return 4
        elif word == '+' or word == '-' or word == '*' or word == '/':
            return 5
        elif word == 'true' or word == 'false':
            return 6
        elif word == 'return':
            return 7
        elif word == ';':
            return 8
        elif word == '(':
            return 9
        elif word == ')':
            return 10
        elif word == '{':
            return 11
        elif word == '}':
            return 12
        elif word == '[':
            return 13
        elif word == ']':
            return 14
        elif word == '=':
            return 15
        elif word == ',':
            return 16
        fst = word[0]
        if fst == '-' or (fst >= '0' and fst <= '9'):
            return 17
        elif fst == "'":
            return 18
        elif fst == '"':
            return 19
        elif (fst >= 'A' and fst <= 'Z') or (fst >= 'a' and fst <= 'z') or fst == '_':
            return 20
        return 1

    def ReadFile(self, fileName):
        with open(fileName, "r") as f:
            wordStream = f.read()
            self.WordClassfier(wordStream)
            for word in self.lexemList:
                strType = self.TypeChecker(word)
                self.tokenList.append(Token(strType, word))

    def PrintTokenTable(self):
        for token in self.tokenList:
            print("<{}, {}>".format(
                TokenTable[token.getID()], token.getLexeme()))

    def SaveTokens(self, fileName):
        with open(fileName, "w") as f:
            for i, token in enumerate(self.tokenList):
                data = "<{}, {}>".format(
                    self.tokenTable[token.getID()], token.getLexeme())
                if i != len(self.tokenList)-1:
                    data += ",\n"
                f.write(data)


TokenTable = {
    1: "UNKNOWN",
    2: "VTYPE",
    3: "KEYWORD",
    4: "COMPARER",
    5: "OPERATOR",
    6: "BOOLEAN",
    7: "RETURN",
    8: "SEMI",
    9: "LPAREN",
    10: "RPAREN",
    11: "LBRACE",
    12: "RBRACE",
    13: "LBRACKET",
    14: "RBRACKET",
    15: "ASSIGN",
    16: "SEP",
    17: "INTEGER",
    18: "CHAR",
    19: "STRING",
    20: "ID",
}

Analyzer = LexicalAnalyzer(TokenTable)
Analyzer.ReadFile("./stream/input_stream.txt")
Analyzer.PrintTokenTable()
Analyzer.SaveTokens("./stream/symbol_table.txt")
