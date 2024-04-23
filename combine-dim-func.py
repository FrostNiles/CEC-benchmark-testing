import runpy
import re
import sys

for i in range(1, 31):
    for j in [10, 30, 50, 100]:
        for k in range(1, j):
            args = {
                'arg1': str(i),
                'arg2': str(j),
                'arg3': str(k)
            }
            print(i)
            print(j)
            print(k)
            
            runpy.run_path('./run-tests.py', init_globals=args)


