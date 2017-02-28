import multiprocessing
from joblib import Parallel, delayed
import time

def myFunction(i):
    time.sleep(2)
    print(i)
    return i

if __name__ == '__main__':
    # start = time.time()
    # for i in range(10):
    #     myFunction(i)
    # print("SERIAL",time.time() - start)

    start = time.time()
    num_cores = multiprocessing.cpu_count()
    print("number of cors" + str(num_cores))
    results = Parallel(n_jobs=num_cores)(delayed(myFunction)(i) for i in range(10))
    print("parallel", time.time() - start)
    print (results)