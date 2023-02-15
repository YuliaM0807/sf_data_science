""" Игра угадай число. Компьютер сам загадывает и 
    угадывает число
  """

import numpy as np
def random_predict (number:int=1) ->int:
    """ Рандомно угадываем число
    
    args:
        number(int,optional): Загаданное число. Defaults to 1.
    Returns:
        int: число попыток
    """

# количествр попыток
    count = 0
    while True:
        count +=1
        predict_number = np.random.randint(1,101) #предполагаемое число
    
        if number == predict_number:
            break # конец игры, выход из цикла
    return(count)
print(f'количество попыток{random_predict()}') 
   
     