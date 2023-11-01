from pprint import pprint

    # Кулинарная книга
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 300, 'measure': 'г'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
  'Яичница с сыром, ветчиной и помидорами': [
    {'ingredient_name': 'Куриное яйцр', 'quantity': 3, 'measure': 'шт'},
    {'ingredient_name': 'Подсолнечное масло', 'quantity': 1, 'measure': 'кусочек'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    {'ingredient_name': 'Ветчина', 'quantity': 100, 'measure': 'г'},
    {'ingredient_name': 'Помидор', 'quantity': 1, 'measure': 'шт'}
    ]
  }


    # Список из блюд, которые мы хотим приготовить.
list_diches = [
              "Омлет", "Утка по-пекински", "Утка по-пекински"
              "Запеченный картофель", "Яичница с сыром, ветчиной и помидорами"
              ]
person_count = 4  # Количество людей

    # Функция для создания словаря из всех ингредиетов, необходимых для блюд списка.
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    dict_ing = {}
    for dish_user in dishes:
        for dish in cook_book:
            if dish_user == dish:
                for ing in cook_book[dish_user]:
                    if ing["ingredient_name"] in dict_ing: # Сделана поправка, если ингредиент уже есть в словаре.
                        dict_ing[ing["ingredient_name"]]["quantity"] += (ing["quantity"] * person_count)
                    else:
                        dict_ing[ing["ingredient_name"]] = {"measure": ing["measure"], "quantity": ing["quantity"] * person_count}

    return dict_ing

result = get_shop_list_by_dishes(list_diches, person_count)
pprint(result)

    # Запись в файл информации о блюдах, которые находятся в поварской книге
with open(file="dishes.txt", mode="a", encoding="utf-8") as file:
    for dish in cook_book:
        text = f'{dish}\n{len(cook_book[dish])}\n'
        for ing in cook_book[dish]:
            text += f'{ing["ingredient_name"]} | {ing["quantity"]} | {ing["measure"]}\n'
            
        file.write(f'{text}\n')


