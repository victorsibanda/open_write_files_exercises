from functions import *




while True:
    user_input = input('Do you want to make an order:1 \n list the order:2 \n change the order:3')
    if user_input == '1':
        count = 0
        amount_of_orders = int(input('How many items would you like to order'))
        while count <= amount_of_orders:
            user_food = input('What food do you want?')
            user_order = input('Which order list do you want to add to?')
            count += 1
            # for i in user_order:
            #print(count,open_and_append(user_order,user_food))
            open_and_append(user_order,user_food)


    elif user_input == '2':

        user_order = input('Which order do you want to see')
        open_and_print(user_order)

    elif user_input == '3':

        user_order = input('which order do you want to change?\n').title()
        user_food = input('What is your new order?\n')
        open_and_write(user_order,user_food)

    else:
        print('enter 1,2 or 3 please')



