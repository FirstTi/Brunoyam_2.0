# Нужно данный список сохранить в файл, а затем прочитать из файла и вывести в консоль (использовать модуль json)

import json

countries = ["Canada", "Bulgaria", "Germany"]

# f = open("CountryList.json", "w")
# json.dump(countries, f)
# f.close()


with open("CountryList.json", "w") as f:
    json.dump(countries, f)

with open ("CountryList.json", "r") as f:
    countries = json.load(f)
    print(countries)

