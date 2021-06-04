import sys

class Analyzer:
  def __init__(self):
    self.trace_symbol_stack = [0]
    self.trace_input = []
    self.trace_input_code = []

    #slr_table에서 읽어야할 state(row)
    self.slr_table_state = []
    #slr_table에서 읽어야할 column
    self.slr_table_type = []
    #slr_table에서 실제 하는것들
    self.slr_table_do = [] 
    #reduce rule
    self.reduce_rule = {}

    self.cursor = 0
    self.action_state = ''
    self.stack_top = ''
    self.input_top = ''
    #stack_top과 input_top를 비교해서 action_state를 구하고 그에 따른 행동을 해야한다.

  def read_slr_table(self,row, column):
    action=''
    for x, i in enumerate(self.slr_table_state):
      for y in self.slr_table_type:
        if(x == row and y == column):
          action = self.slr_table_do[int(i)]
          break
    return action
        

  def parse(self):
    print(self.trace_symbol_stack, self.trace_input)
    self.stack_top = self.trace_symbol_stack[-1]
    self.input_top = self.trace_input[0]
    self.action_state = self.read_slr_table(self.stack_top, self.input_top)
    print(self.stack_top, self.input_top)
    print(self.action_state)

    if(self.action_state == ''):
      #Error
      print("E")
      pass

    elif(self.action_state[0] == 'r'):
      #reduce
      print("R")
      pass
    
    elif(self.action_state[0] == 'a'):
      #accept
      print("A")
      pass
    elif(self.action_state[0] == 's'):
      #error
      self.trace_symbol_stack.append(self.input_top)
      self.trace_symbol_stack.append(self.action_state[1])
      self.trace_input = self.trace_input[1:]
      self.parse()
      pass
    else:
      #goto number
      pass
    

  def prepare_slr_table(self):
    with open("slr_table.csv", 'r') as f:
      parse_slr_table = f.read().splitlines()
      for x in parse_slr_table:
        table_split = x.split(",")
        self.slr_table_state.append(table_split[0])
        self.slr_table_type.append(table_split[1])
        self.slr_table_do.append(table_split[2])

  def prepare_reduce_rule(self):
    with open("reduce_rule.csv", "r") as f:
      reduce_table = f.read().splitlines()
      for x in reduce_table:
        table_split = x.split(",")
        self.reduce_rule[table_split[0]] = [table_split[1], table_split[2], table_split[3:]]
        # key reduce rule number : [감소해야할 문자 수, 변환 후 noneterminal, 변환 전 sequence]
      

#여기까지 class Analyzer

def syntax_analyzer():
    
  '''
  if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

  file_name = sys.argv[1]
  
  '''
  analyzer = Analyzer()
  analyzer.prepare_slr_table()
  analyzer.prepare_reduce_rule()

  with open('symbol_table.txt', 'r') as f:
    parse_list = f.read().splitlines()
      
    for x in parse_list:
      symbol, code = x.split(",")
      analyzer.trace_input.append(symbol)
      analyzer.trace_input_code.append(code)

    analyzer.trace_input.append('$')
    analyzer.trace_input_code.append('$')\
  
  #praser start
  analyzer.parse()



if __name__ == "__main__":
    #program start
    syntax_analyzer()