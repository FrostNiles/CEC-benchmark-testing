import subprocess
import multiprocessing
import os
import time
import concurrent.futures

skipped = {2, 9, 27}

#14,15,16,18, 20 - Hybrid functions - very sensitive to deleting floating point number 
#2 - deleted function
#29, 30 composite functions - put together at least one of the very sensitive hybrid functions
#9, 27 
# 29, 30, include at least one of the very sensitive hybrid functions


#27 
#1: HGBat Function F18’
#g2: Rastrigin’s Function F5’
#g3: Modified Schwefel's Function F10’
#g4: Bent-Cigar Function F11’
#g4: High Conditioned Elliptic Function F11’
#g5: Expanded Scaffer’s F6 Function F6’

#20 
#g1 : Happycat Function f17
#g2 : Katsuura Function f16 
#g3: Ackley’s Function f13
#g4: Rastrigin’s Function f5
#g5 : Modified Schwefel’s Function f10
#g6: Schaffer’s F7 Function f20

#9 levy function

#18 
#g1 : High Conditioned Elliptic Function f1
#g2 : Ackley’s Function f13
#g3: Rastrigin’s Function f5
#g4: HGBat Function f18
#g4: Discus Function f12

#16
#g1 : Expanded Schaffer F6 Function f6
#g2 : HGBat Function f18
#g3: Rosenbrock’s Function f4
#g4: Modified Schwefel’s Function f10

#15
#g1 : Bent Cigar Function f1
#g2 : HGBat Function f18
#g3: Rastrigin’s Function f5
#g4: Rosenbrock’s Function f4

#14
#g1 : High Conditioned Elliptic Function f11
#g2 : Ackley’s Function f13
#g3: Schaffer’s F7 Function f20
#g4: Rastrigin’s Function f5

"""
		case 9:	
			levy_func(&x[i*nx],&f[i],nx,OShift,M,1,1);
			f[i]+=900.0;
			break;
		case 14:	
			hf04(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);
			f[i]+=1400.0;
			break;
		case 15:	
			hf05(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);
			f[i]+=1500.0;
			break;
		case 16:	
			hf06(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);
			f[i]+=1600.0;
			break;
		case 18:	
			hf08(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);
			f[i]+=1800.0;
			break;
		case 20:	
			hf10(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);
			f[i]+=2000.0;
			break;
		case 27:
			cf07(&x[i*nx],&f[i],nx,OShift,M,1);
			f[i]+=2700.0;
			break;
		case 29:
			cf09(&x[i*nx],&f[i],nx,OShift,M,SS,1);
			f[i]+=2900.0;
			break;
		case 30:
			cf10(&x[i*nx],&f[i],nx,OShift,M,SS,1);
			f[i]+=3000.0;
			break;
"""
# Compile the C++ file
if not os.path.exists('./main'):
    subprocess.run(["g++", "main.cpp", "cec_test_func.cpp", "-o", "main"], check=True)

def run_test(i):
    for j in [10, 30, 50, 100]:
        for k in range(1, j+1):
            # Set the dimension as a command line argument for the C++ program
            args = [str(i), str(j), str(k)]
            subprocess.run(['python', './run-tests.py'] + args)

if __name__ == '__main__':
    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(1, 30): # skip the composite functions 21 - 31
            if i in skipped:
                continue
            # Run the test in a separate thread
            futures.append(executor.submit(run_test, i))

        # Wait for all the tests to finish
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except concurrent.futures.TimeoutError:
                print("A test took too long and was cancelled.")