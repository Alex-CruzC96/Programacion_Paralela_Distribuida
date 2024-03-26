#
#
#
#

import threading

def function(i):
    print(f"Function called by thread {i}")
    return 

threads=[]
for i in range(5):
    t=threading.Thread(target=function,args=(i,))
    threads.append(t)
    t.start()
    t.join()