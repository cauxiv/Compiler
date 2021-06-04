import sys

class Analyzer:
  def __init__(self):
    self.trace_symbol_stack = [0]
    self.trace_input_stack = ['$']

    #slr_table에서 읽어야할 state(row)
    self.slr_table_state = []
    #slr_table에서 읽어야할 column
    self.slr_table_type = []
    #slr_table에서 실제 하는것들
    self.slr_table_do = [] 

def prepare_slr_table():
  pass

def prepare_reduce_rule():
  pass

def syntax_analyzer():
    
  '''
  if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

  file_name = sys.argv[1]
  
  '''
  analyzer = Analyzer()

  with open('symbol_table.txt', 'r') as f:
    parse_list = f.read().splitlines()
      
    for x in parse_list:
      symbol, code = x.split(",")
      analyzer.symbol_stack.append(symbol)
      analyzer.code_stack.append(code)
    





if __name__ == "__main__":
    
    syntax_analyzer()