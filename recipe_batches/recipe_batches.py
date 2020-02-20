#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    if not len(recipe.keys())==len(ingredients.keys()):
      return 0
    counting_dict = {}
    for key in recipe.keys():
      counting_dict[key] = ingredients[key] // recipe[key]
      
    return min(counting_dict.values())


    
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))