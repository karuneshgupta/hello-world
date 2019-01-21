import logging
#debug= detailed information,typically of interest only when diagnosing problem
# info = confirmation that things are working as expected
#warning = an indiacation that something happened,or indicative of some problem in the near future (eg, disk space low)
#error= due to a more serious problem,the software has noot been able to perform some function
# critical = a serious error, indicating that the program itself may be unable to continue running

logging.basicConfig(filename='test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y

num_1=20
num_2=10


add_result=add(num_1,num_2)
logging.debug(f'add : {num_1} + {num_2}= {add_result}')
