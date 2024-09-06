import multiprocessing
import time
import concurrent.futures
def func1(x):
    time.sleep(1)
    print(f'value is {x*2}')


def main():
    time1=time.perf_counter()
    lst=[]
    # basic with general syntax
    # process1 = multiprocessing.Process(target=func1 , args=[2])
    # process1.start()
    # process1.join()

    # exectuing for an range 
    # for _ in range(10):
    #     process1 = multiprocessing.Process(target=func1 , args=[2])
    #     process1.start()
    #     lst.append(process1)
    # for item in lst:
    #   item.join()

    # using pprocess pool executor 
    # with concurrent.futures.ProcessPoolExecutor() as executor :
    #     process = executor.submit(func1,2)
    # print(process.result())

    # for range in process pool executor 
    # with concurrent.futures.ProcessPoolExecutor() as executor :
    #     process = [executor.submit(func1,2) for _ in range(10)]
    # for element in concurrent.futures.as_completed(process):
    #     print(element.result()) # <<<<< return future result
    #     print(process) # <<<< return future object 

    # # using map()
    # element=[2]
    # with concurrent.futures.ProcessPoolExecutor() as executor :
    #     process = executor.map(func1,element)
    #     for item in process:
    #         print(item)

    time2=time.perf_counter()
    finaltime=time2-time1
    print(finaltime)

if __name__ == "__main__":
    main()