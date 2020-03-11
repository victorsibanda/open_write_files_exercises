from functions import *

while True:

    user_food = input('What food do you want?')
    user_order = input('Which order list do you want to add to?')

    open_and_append(user_order,user_food)



    open_and_print(user_order)