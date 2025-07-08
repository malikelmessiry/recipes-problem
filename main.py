# create a dictionary where the key is the chef's name and the value is a set of ingredients
# loop through list and loop through each tuple
# add second element of tuple as key of dictionary
# add third element of tuple (another tuple of ingredients) as a set as the dictionary value
# loop through dictionary values and return longest list then second longest list
# return as 2 tuples in a list
# {
# "Sam": {"Cheese", "Tortilla", "Beef"}, [3, 2]
# "Amy": {"cilantro", "chicken"}
#}

def most_varied(recipes):
    recipe_dict = {}

    for recipe in recipes:
        if recipe[1] not in recipe_dict:
            recipe_dict[recipe[1]] = set(recipe[2])
        else:
            for item in recipe[2]:
                recipe_dict[recipe[1]].add(item)


    length_of_ingredients = []
    for name, ingredients in recipe_dict.items():
        length_of_ingredients.append(((len(ingredients), name)))
    
    length_of_ingredients.sort(reverse=True)
    first_name = length_of_ingredients[0][1]
    second_name = length_of_ingredients[1][1]

    first_return = (first_name, sorted(recipe_dict[first_name]))
    second_return = (second_name, sorted(recipe_dict[second_name]))


    return [first_return, second_return]



recipes_1 = [
    ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
    ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
    ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
    ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]



print(most_varied(recipes_1))





recipes_1 = [
    ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
    ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
    ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
    ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
assert most_varied(recipes_1) == [
    ("Xinting", ["Beef", "Carrot", "Chicken Stock", "Onion", "Peas", "Tomato"]), 
    ("Amy", ["Cheese", "Chicken Cream", "Pepper", "Tater tots"])
]

recipes_2 = [
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]
assert most_varied(recipes_2) == [
    ("Sam", ["Beef", "Cheese", "Tortilla"]),
    ("Hallie", ["Oil", "Potato"])
]

print("All test cases passed!")
print("Finished early? Discuss time & space complexity.")