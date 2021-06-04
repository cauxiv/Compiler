import sys

class Analyzer():
    
    symbol_stack = []
    code_stack = []

    def __init__(self):
        pass


def syntax_analyzer():
    
    '''
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()

    file_name = sys.argv[1]
    
    '''
    analyzer = Analyzer()

    with open('input_stream3.txt', 'r') as f:
        lines = f.readlines()
        print(lines)




if __name__ == "__main__":
    
    syntax_analyzer()