import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency


chat_id = 1897874711 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    # Рассчитываем конверсию контрольной группы
    conv_control = x_success / x_cnt
    
    # Рассчитываем ожидаемое количество продаж в тестовой группе
    expected_sales = conv_control * y_cnt
    
    # Формируем таблицу сопряженности
    obs = [[x_success, x_cnt - x_success], [y_success, expected_sales - y_success]]
    
    # Рассчитываем статистику критерия хи-квадрат и p-value
    chi2, p, dof, ex = chi2_contingency(obs, correction=False)
    
    # Определяем критическое значение для заданного уровня значимости и кол-ва степеней свободы
    alpha = 0.07
    critical_value = chi2.ppf(1 - alpha, dof)
    
    # Сравниваем полученное значение статистики с критическим значением
    return chi2 > critical_value
