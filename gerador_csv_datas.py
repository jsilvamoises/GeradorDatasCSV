# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:33:21 2020

@author: MOISES.SILVA
"""

from math import ceil
from datetime import datetime,timedelta
import time
import pandas as pd


dia_semana_completo = ('segunda-feira','terca-feira','quarta-feira',
                 'quinta-feira','sexta-feira','sabado','domingo')

dia_semana_abrev = ('seg','ter','qua','qui','sex','sab','dom')

meses_completo=('janeiro','fevereiro','mar','abril','maio','junho',
           'julho','agosto','setembro','outubro','novembro','dezembro')

meses_abrev=('jan','fev','mar','abrl','mai','jun','jul','ago','set','out','nov','dez')


def week_of_month(dt):
    """ Returns the week of the month for the specified date.
    """

    first_day = dt.replace(day=1)

    dom = dt.day
    adjusted_dom = dom + first_day.weekday()
    
    x = first_day
    dia_semana = 1
    while x<=dt:
        #print(x)
        if x.weekday() == 6:
            dia_semana+=1
        x = x + timedelta(days=1)
        

    return dia_semana # int(ceil(adjusted_dom/7.0))

def week_of_year(dt):
    first_day = dt.replace(day=1,month=1)

    dom = dt.day
    adjusted_dom = dom + first_day.weekday()
    
    x = first_day
    dia_semana = 1
    while x<=dt:
        #print(x)
        if x.weekday() == 6:
            dia_semana+=1
        x = x + timedelta(days=1)
        

    return dia_semana # int(ceil(adjusted_dom/7.0))
    

def generate_csv_with_dates(dt_ini, dt_fim):    

    data_ini = datetime.strptime(dt_ini, '%Y-%m-%d').date()
    data_fim = datetime.strptime(dt_fim, '%Y-%m-%d').date()
    
    data_ini < data_fim
    items = []
    while data_ini <= data_fim: 
        item ={
            'data':data_ini.strftime('%Y-%m-%d'),
            'ano':data_ini.year,
            'semana_num':week_of_month(data_ini),
            'semana_do_ano':week_of_year(data_ini),
            'dia_do_ano':data_ini.timetuple().tm_yday,
            'dia_semana_num':data_ini.isocalendar()[2],            
            'dia_semana_completo':dia_semana_completo[data_ini.weekday()],
            'dia_semana_abrev':dia_semana_abrev[data_ini.weekday()],
            'mes_completo':meses_completo[data_ini.month-1],
            'mes_abrev':meses_abrev[data_ini.month-1],
            'mes_numero':data_ini.month
            
            }
        items.append(item)        
        data_ini = data_ini +timedelta(days=1)
        
    df = pd.DataFrame(items)
    df.reset_index()
    df.to_csv('datas.csv',index=False,sep=';',encoding='ISO-8859-1')
    df.to_json('data.json',orient = "records")
#data_ini.isocalendar()[1]      
if __name__ == '__main__':
    i = input('Informe a data inicio ex: yyyy-mm-dd _ ')
    f = input('Informe a data final ex: yyyy-mm-dd _ ')
    generate_csv_with_dates(i,f)
    
    
    
 