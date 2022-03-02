# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
import string


with open("project-euler/names.txt") as names:
    variables = names.read()

name_list = sorted(variables.replace('"', '').split(','))
lista_soma = []
for index, name in enumerate(name_list):
    value = 0
    for letter in name:
        value += (string.ascii_uppercase.index(letter) + 1)
    lista_soma.append(value * (index + 1))
print(sum(lista_soma))