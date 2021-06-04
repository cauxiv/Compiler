import sys


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
        # lex변수에 각각의 단어들을 넣어줍니다.
        lex = ''
        # preValidLex는 이전에 tokenList에 넣어진 lex를 저장합니다
        preValidLex = ''
        # quoteCount를 주어 만약 문자나 문자열 처리했으면 해당 길이만큼 continue해줍니다
        # 파이썬 enum 특성상 iterator를 조작할 수 없어서 이렇게 처리했습니다
        quoteCount = 0
        # 파싱 시작 부분입니다.
        for i, ch in enumerate(stream):
            # Array out of Index 에러를 방지하기 위해 처음 iterator는 continue해줍니다
            if i == 0:
                lex = ch
                continue
            # quoteCount가 있으면 그만큼 continue해줍니다
            if quoteCount != 0:
                quoteCount -= 1
                continue

            # 문자 처리 부분입니다
            if ch == "'":
                # lex가 비어있지 않으면 해당값을 lexemList에 넣고 append합니다
                if lex != '':
                    self.lexemList.append(lex)
                    preValidLex = lex
                    lex = ''
                # /를 lex에 넣어줍니다
                lex = ch
                # 현재 iterator+1에서 stream길이까지의 범위만큼 검사합니다
                for iStr in range(i+1, len(stream)):
                    # 스킵할 만큼 quoteCount에 넣어줍니다
                    quoteCount += 1
                    # 만약 문자열에 들어갈 수 있는 문자를 제한하고 싶으면 여기에 추가하면 됩니다
                    # 만약 두번째 '가 나왔다면 해당 문자열을 lexemList에 넣고 continue해줍니다
                    # 해당 문자가 valid, 즉 한 문자만 받았는지는 TypeChecker에서 검사합니다
                    if stream[iStr] == "'":
                        lex += stream[iStr]
                        self.lexemList.append(lex)
                        preValidLex = lex
                        lex = ''
                        break
                    lex += stream[iStr]
                continue

            # 문자열 처리 부분입니다
            if ch == '"':
                # lex가 비어있지 않으면 해당값을 lexemList에 넣고 append합니다
                if lex != '':
                    self.lexemList.append(lex)
                    preValidLex = lex
                    lex = ''
                lex = ch
                for iStr in range(i+1, len(stream)):
                    # 스킵할 만큼 quoteCount에 넣어줍니다
                    quoteCount += 1
                    # 만약 문자열에 들어갈 수 있는 문자를 제한하고 싶으면 여기에 추가하면 됩니다
                    # 만약 두번째 "가 나왔다면 해당 문자열을 lexemList에 넣고 continue해줍니다
                    # 해당 문자가 valid, 즉 한 문자만 받았는지는 TypeChecker에서 검사합니다
                    if stream[iStr] == '"':
                        lex += stream[iStr]
                        self.lexemList.append(lex)
                        preValidLex = lex
                        lex = ''
                        break
                    lex += stream[iStr]
                continue

            # 12345b와 같은 문자열 처리부분입니다.
            # 위의 문자열에서 b가 나왔을을때 lex에 저장된 부분의 첫번째가 -또는 0~9일 경우
            # lex부분이 Integer라는 것을 알 수 있으며 해당 lex를 lexemList에 넣습니다.
            if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or ch == '_':
                if lex != '':
                    if lex[0] == '-' or (lex[0] >= '0' and lex[0] <= '9'):
                        self.lexemList.append(lex)
                        lex = ''
            # -0000, +0000같은 문자를 위한 예외처리 부분입니다.
            #
            if ch == '0':
                if lex != '':
                    if not ((lex[0] >= 'A' and ch <= 'Z') and (lex[0] >= 'a' and ch <= 'Z') or lex[0] == '_'):
                        if stream[i-1] == '0':
                            self.lexemList.append(lex)
                            lex = ''
            # (,),{,},[,],; 처리
            # 이전에 있는 lexem을 lexemList에 넣고 자신도 lexemList에 넣습니다
            if ch == '(' or ch == ')' or ch == '{' or ch == '}' or ch == '[' or ch == ']' or ch == ';':
                if lex != '':
                    self.lexemList.append(lex)
                    lex = ''
                self.lexemList.append(ch)
                preValidLex = ch
                continue
            # -를 제외한 operator 처리부분입니다
            # 이전에 있는 lexem을 lexemList에 넣고 자신도 lexemList에 넣습니다
            elif ch == '+' or ch == '*' or ch == '/':
                if lex != '':
                    self.lexemList.append(lex)
                    lex = ''
                self.lexemList.append(ch)
                preValidLex = ch
                continue
            # - 를 받는 부분입니다
            # preValidLex로 operator 또는 integer sign을 구분했습니다
            elif ch == '-':
                # 이전에 있는 lexem을 lexemList에 넣습니다.
                if lex != '':
                    self.lexemList.append(lex)
                    preValidLex = lex
                    lex = ''
                # 만약 이전에 들어간 lex가 +,-,*,/ 아닐경우 자신을 lexemList에 넣습니다
                # 이 경우 lexemList에 - 로만 들어가서 TypeChecker에서 operator로 구분됩니다
                if not(preValidLex == '+' or preValidLex == '-' or preValidLex == '*' or preValidLex == '/'):
                    self.lexemList.append(ch)
                    preValidLex = ch
                    continue
                # 그 외의 경우(preValidLex가 +,-,*,/ 일 경우 integer처리에서 -와 함께 들어갑니다)
                # 따라서 TypeChecker에서 해당 lexem을 integer로 처리합니다
            # 공백문자 처리 부분입니다
            # 만약 lex에 값이 있으면 lexemList에 넣어줍니다
            # ch의 아스키코드가 !보다 낮으면(공백, 개행 등) 무시합니다(이 경우 continue)
            elif ch < '!':
                if lex != '':
                    self.lexemList.append(lex)
                    preValidLex = lex
                    lex = ''
                continue
            # 대입자 처리 부분입니다
            elif ch == '=':
                # stream[i-1]은 현재 ch의 바로 앞에 나온 글자입니다
                # stream[i-1]이 <, >, =, !이라면 lexemList에 lext[:-1]부분을 넣어줍니다
                # 이렇게 하는 이유는 abcd< 가 lex에 저장되어 있을 수 있기 때문입니다
                # 그 후 lexemList에 lex[-1]과 ch를 합쳐서 넣어줍니다.
                # 이렇게 되면 abcd <=가 각각 lexemList에 저장될 수 있습니다
                if stream[i-1] == '<' or stream[i-1] == '>' or stream[i-1] == '=' or stream[i-1] == '!':
                    self.lexemList.append(lex[:-1])
                    self.lexemList.append(lex[-1]+ch)
                    preValidLex = lex[-1]+ch
                # <, >, =, !이 아니라면 그냥 대입자이기 때문에
                # lex에 값이 있으면 lexemList에 넣어주고 대입자를 lexemList에 넣습니다
                else:
                    if lex != '':
                        self.lexemList.append(lex)
                    self.lexemList.append(ch)
                    preValidLex = ch
                lex = ''
                continue
            # lex에 현재 문자를 넣습니다
            lex += ch

    def TypeChecker(self, word):
        # lexem이 int, char, boolean, string일 경우 2번 타입을 반환합니다
        if word == 'int' or word == 'char' or word == 'boolean' or word == 'string':
            return 2
        # lexem이 if, else, while, class일 경우 3번 타입을 반환합니다
        elif word == 'if':
            return 3
        elif word == 'else':
            return 4
        elif word == 'while':
            return 5
        elif word == 'class':
            return 6
        # lexem이 >, <, ==, !=, <=, >= 일 경우 4번 타입을 반환합니다
        elif word == '>' or word == '<' or word == '==' or word == '!=' or word == '<=' or word == '>=':
            return 7
        # lexem이 +, -, *, /일 경우 5번 타입을 반환합니다
        # WordClassifier에서 이렇게 저장했기 때문에 아래와 같이 판별해도 괜찮습니다
        elif word == '+' or word == '-':
            return 8
        elif word == '*' or word == '/':
            return 9
        # lexem이 true false일 경우 6번 타입을 반환합니다
        elif word == 'true' or word == 'false':
            return 10
        # lexem이 return일 경우 7번 타입을 반환합니다
        elif word == 'return':
            return 11
        # lexem이 ;일 경우 8번 타입을 반환합니다
        elif word == ';':
            return 12
        # lexem이 (일 경우 9번 타입을 반환합니다
        elif word == '(':
            return 13
        # lexem이 )일 경우 10번 타입을 반환합니다
        elif word == ')':
            return 14
        # lexem이 {일 경우 11번 타입을 반환합니다
        elif word == '{':
            return 15
        # lexem이 }일 경우 12번 타입을 반환합니다
        elif word == '}':
            return 16
        # lexem이 [일 경우 13번 타입을 반환합니다
        elif word == '[':
            return 17
        # lexem이 ]일 경우 14번 타입을 반환합니다
        elif word == ']':
            return 18
        # lexem이 =일 경우 15번 타입을 반환합니다
        elif word == '=':
            return 19
        # lexem이 ,일 경우 16번 타입을 반환합니다
        elif word == ',':
            return 20
        # 아래는 처음 단어로 구별해야하는 lexem들에 대한 처리입니다
        # 처음 단어를 fst에 넣습니다
        fst = word[0]
        # 만약 처음 단어가 -또는 0~9라면 17번 타입을 반환합니다.
        # 이렇게 판별해도 되는 이유는 WordClassifier에서 -에 대한 처리를
        # 미리 해줬기 때문에 가능합니다
        if fst == '-' or (fst >= '0' and fst <= '9'):
            return 21
        # 만약 처음 단어가'일 경우 18번 타입을 반환합니다
        # 미리 WordClassifier에서 처리를 해줘서 해당 방식으로 처리 가능합니다
        elif fst == "'":
            # 만약 단일 문자가 아니면 21번 타입을 반환합니다.
            if len(word) > 2:
                return 25
            return 22
        # 만약 처음 단어가"일 경우 19번 타입을 반환합니다
        # 미리 WordClassifier에서 처리를 해줘서 해당 방식으로 처리 가능합니다
        elif fst == '"':
            return 23
        # 처음단어가 영어 단어 또는 _로 시작할 경우 20번 타입을 반환합니다
        elif (fst >= 'A' and fst <= 'Z') or (fst >= 'a' and fst <= 'z') or fst == '_':
            return 24
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
            for token in self.tokenList:
                data = "<{}, {}>\n".format(
                    self.tokenTable[token.getID()], token.getLexeme())
                f.write(data)


TokenTable = {
    1: "unknown",
    2: "vtype",
    3: "if",
    4: "else",
    5: "while",
    6: "class",
    7: "comp",
    8: "addsub",
    9: "multdiv",
    10: "boolstr",
    11: "return",
    12: "semi",
    13: "lparen",
    14: "rparen",
    15: "lbrace",
    16: "rbrace",
    17: "lbracket",
    18: "rbracket",
    19: "assign",
    20: "comma",
    21: "num",
    22: "character",
    23: "literal",
    24: "id",
    25: "invalid char"
}

Analyzer = LexicalAnalyzer(TokenTable)
Analyzer.ReadFile(sys.argv[1])
Analyzer.PrintTokenTable()
Analyzer.SaveTokens("./symbol_table.txt")

# if ch >= '0' and ch <= '9':
#     if lex != '':
#         if not ((lex[0] >= 'A' and ch <= 'Z') and (lex[0] >= 'a' and ch <= 'Z') or lex[0] == '_'):
#             if stream[i-1] == '0':
#                 self.lexemList.append(lex)
#                 lex = ''
