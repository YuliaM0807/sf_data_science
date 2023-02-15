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
print(f'количество попыток {random_predict()}') 

def score_game (random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает алгоритм

    Args:
        random_predict ([_type_]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed (1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint (1, 101, size=(1000)) # задаем список чисел
   
    for number in random_array:
       count_ls.append (random_predict(number))
    score = int (np.mean (count_ls)) # находим среднее количество
    
    print (f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)
    
if __name__ == '__main__':
    score_game (random_predict)
       
     