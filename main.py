from pprint import pprint
cook_book = {}

with open('recipes.txt') as f:
  read_file = f.readlines()
  result_file = []
  for_type_list = []
  for_digit = []
  for i in read_file:
    i = i.strip()
    if '|' in i:
      i = i.split('|')
    result_file.append(i)
  for i in result_file:
    if type(i) == str and i.isdigit() != True and i != '':
        cook_book[i] = []
  for i in result_file:
    if type(i) == str and i.isdigit():
        for_digit.append(int(i))
  for i in result_file:
    if type(i) == list:
      for_type_list.append(i)

  spisok_for_result = [] 
  for i in for_digit:
    for j in range(i):
      for m in range(len(for_type_list[j])):
        dict_for_result = {}
        dict_for_result['ingredient_name'] = for_type_list[j][0]
        dict_for_result['quantity'] = int(for_type_list[j][1])
        dict_for_result['measure'] = for_type_list[j][2]
      spisok_for_result.append(dict_for_result)
    for_type_list = for_type_list[(j + 1):]
  for h in cook_book:
    cook_book[h] = spisok_for_result[:for_digit[0]]
    spisok_for_result = spisok_for_result[for_digit[0]:]
    for_digit.pop(0)
  #print(cook_book)  


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
  if type(dishes) is not list:
    dishes = [dishes]
  result_food = {}   
  for i in dishes:
    for k in cook_book[i]:
      dict_for_result_food = {}
      for m, n in k.items():
          dict_for_result_food['measure'] = k['measure']
          dict_for_result_food['quantity'] = k['quantity'] * person_count
          result_food[n] = dict_for_result_food
          break

  pprint(result_food)


get_shop_list_by_dishes('Запеченный картофель', 3)