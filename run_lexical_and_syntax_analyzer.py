#!/usr/bin/env python3
import subprocess
import sys

file_path = sys.argv[1]

if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

output_name = file_path.split(".")[-2] + "_output" + ".txt"

f = open(output_name, "w")
ps = subprocess.run(['python', 'lexical_analyzer.py', file_path], check=True)
processNames = subprocess.run(['python', 'syntax_analyzer.py', 'symbol_table.txt'],input=ps.stdout, stdout=f)