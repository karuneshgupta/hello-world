Python 3.7.0b4 (v3.7.0b4:eb96c37699, May  2 2018, 19:02:22) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import logging
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
logging.debug('add : {} + {}= {}'.format(num_1,num_2,add_result))

sub_result=subtract(num_1,num_2)
logging.debug('sub :{} - {} = {}'.format(num_1,num_2,sub_result))

div_result=divide(num_1,num_2)
logging.debug('div :{} / {} = {}').format(num_1,num_2,div_result)

mult_result=multiply(num_1,num_2)
logging.debug('mult : {} * {} = {}').format(num_1,num_2,mult_result)
