import subprocess
import multiprocessing
import os
import time

skipped = {2, 9, 14, 15, 16, 18, 20, 29, 30, 27}

# Compile the C++ file
if not os.path.exists('./main'):
    subprocess.run(["g++", "main.cpp", "cec_test_func.cpp", "-o", "main"], check=True)

def run_test(i):
    for j in [50, 100]:
        for k in range(1, j+1):
            # Set the dimension as a command line argument for the C++ program
            args = [str(i), str(j), str(k)]
            subprocess.run(['python', './run-tests.py'] + args)

if __name__ == '__main__':
    # Create a pool of workers
    with multiprocessing.Pool() as pool:
        for i in range(13, 31):
            if i in skipped:
                continue
            # Run the test in a separate process
            pool.apply_async(run_test, (i,))

        # Wait for all the tests to finish
        pool.close()
        pool.join()