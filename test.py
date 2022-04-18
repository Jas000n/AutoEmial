import random
import time
time_tuple = time.localtime(time.time())
print("当前时间为{}年{}月{}日{}点{}分{}秒".format(time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5]))

i =  random.randint(1,4)
print(i)