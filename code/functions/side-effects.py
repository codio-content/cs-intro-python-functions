my_num = 0

def add_5(num):
    """Receive a number and return that number plus 5"""
    return(num + 5)
  
for i in range(10):
    print(add_5(i * 5))
    
print('The value of my_num is: {}'.format(my_num))