#Carregue a data atual do computador e, com base na data atual, 
#apresente a data de dois dias no futuro

from datetime import date, timedelta

dataatual = date.today()
dataemdoisdias = dataatual + timedelta(days=2)
print('A data atual é:', dataatual, 'e a A data em dois dias será:',dataemdoisdias)






