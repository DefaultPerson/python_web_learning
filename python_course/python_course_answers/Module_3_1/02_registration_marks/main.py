import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
pattern_private = r'\b\D{1}\d{3}\D{2}\d{3}'
pattern_taxi = r'\b\D{2}\d{3}\d{2,3}'
print(f"Список номеров частных автомобилей: {re.findall(pattern_private, text)}")
print(f"Список номеров такси: {re.findall(pattern_taxi, text)}")


