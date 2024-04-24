import runpy
import re
import sys

for i in range(1, 31):
    # CEC 2017 has 30 functions but we are skipping 2.
    #if i == 2:
    #    continue
    for j in [10, 30]:
        for k in range(1, j):
            args = {
                'arg1': str(i),
                'arg2': str(j),
                'arg3': str(k)
            }
            
            runpy.run_path('./run-tests.py', init_globals=args)


