"""
__________________________ Capstone Project IV - OOP __________________________
Follow these steps:
    ● Code a Python program that will read from the text file inventory.txt and
      perform the following on the data, to prepare for presentation to your
      managers:

        o Create a file named inventory.py, where a Shoe class should be
          defined.

        o Create a class named Shoes with the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● Quantity.

        o Inside this class define the following function:
            ▪ get_cost - which return the cost of the shoe
            ▪ get_quanty - which return the quantity of the shoes
            ▪ __str__ - This function returns a string representation of a
              class.

        o Outside this class create a variable with an empty list. This variable
          will be used to store a list of shoes objects

        o Then you must define the following functions:

            ▪ read_shoes_data - this function will open the file
              inventory.txt and read the data from this file the create shoes
              object and append this object into the shoes list. one line in
              this file represents data to create one object of shoes. You
              must use the try except in this function for error handling.

            ▪ capture_shoes - this function will allow a user to capture
              data about a shoe and use this data to create a shoe object
              and append this object inside the shoe list.

            ▪ view_all - this function will iterate over all the shoes list and
              print the details of the shoes that you return from the __str__
              function. (Optional: You can organise your data in a table
              format by using Python’s tabulate module )

            ▪ re_stock - this function will find the shoe object with the
              lowest quantity, which is the shoes that need to be
              restocked. Ask the user if he wants to add the quantity of
              these shoes and then update it. This quantity should be
              updated on the file for this shoe.

            ▪ search_shoe - This function will search for a shoe from the list
              using the shoe code and return this object so that it will be
              printed

            ▪ value_per_item - this function will calculate the total value
              for each item . (Please keep the formula for value in mind;
              value = cost * quantity). Print this information on the
              console for all the shoes.

            ▪ highest_qty - Write code to determine the product with the
              highest quantity and print this shoe as being for sale.

        o Now in your main create a menu that executes each function
          above. This menu should be inside the while loop. Be creative.
"""
from tabulate import tabulate  # installed the tabulate module


class Shoes:  # Create a class named Shoes with the following attributes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # get_quanty - which return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # get_cost - which return the cost of the shoe
    def get_cost(self):
        return self.cost

    # this will be used to change the quantity when the re_stock() function is called
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

    # this will be used when the search_shoe() function is called
    def get_code(self):
        return self.code

    # this will be used when the value_per_item() function is called
    def get_name(self):
        return self.product

    # this will display the inventory.txt file is called in a table format
    def __str__(self):
        table = {
            "Country": [self.country],
            "Code": [self.code],
            "Product": [self.product],
            "Cost": [self.cost],
            "Quantity": [self.quantity]
        }
        print(tabulate(table, headers="keys", tablefmt="fancy_grid"))

    # this method can be used to repopulate the inventory.txt file
    def original_details(self):
        line = '\n' + str(self.country) + ',' + str(self.code) + ',' + \
               str(self.product) + ',' + str(self.cost) + ',' + str(self.quantity)
        return line


# empty list created to store a list of shoes objects
shoe_list = []


def read_shoes_data():
    shoe_list = []  # reset shoe list
    f = open("inventory.txt", 'r')

    contents = ""  # store file contents here

    for line in f:
        contents += line

    line_list = contents.split("\n")  # line_list is a list where each element is a line
    del (line_list[0])  # delete the first row, so that the iteration can be done over the data

    list = []  # empty list to append data individually

    for i in range(0, len(line_list)):
        list.append(line_list[i].split(","))
    try:
        for i in range(0, len(list)):
            object_to_be_added = Shoes(list[i][0], list[i][1], list[i][2], list[i][3], list[i][4])
            shoe_list.append(object_to_be_added)
    except FileNotFoundError:
        print("File not found")
    f.close()
    return shoe_list


def capture_shoes():  # capturing new shoe data
    print(f"""
______________________________ 2. Capture shoes _______________________________""")
    country = input("\nEnter country	: ")
    code = input("Enter code	    : ")
    product = input("Enter product	: ")
    cost = input("Enter cost	    : ")
    quantity = input("Enter quantity	: ")
    new_shoe = Shoes(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    print(f"""
Task complete: new shoe added! 
Country     = {country}
Code        = {code}
Product     = {product}
Cost        = {cost}
Quantity    = {quantity}""")

    with open("inventory.txt", "a") as f:  # writing the new data to the inventory.txt file
        f.write(f'''\n{country},{code},{product},{cost},{quantity}''')


def view_all():  # viewing all data in table format
    print(f"""
______________________________ 1. View all shoes ______________________________""")
    shoe_list = read_shoes_data()
    for shoe in range(0, len(shoe_list)):
        shoe_list[shoe].__str__()


def re_stock():  # restocking and finding the lowest quantity
    print(f"""
______________________________ 3. Re-stock shoes ______________________________""")
    quantities_list = []
    shoe_list = read_shoes_data()

    for i in range(0, len(shoe_list)):
        quantities_list.append(int(shoe_list[i].get_quantity()))  # using our get quantity method

    lowest_quantity = min(quantities_list)
    lowest_quantity_index = int(quantities_list.index(lowest_quantity))  # now find the index of the lowest one

    print("\nThe shoe with the lowest quantity is: ")
    shoe_list[lowest_quantity_index].__str__()

    choice = input("\nWould you like to restock it? Y/N : ").lower()  # restocking option

    if choice == 'y':
        new_quantity = int(input("\nPlease enter the new quantity to be recorded: "))

        shoe_list[lowest_quantity_index].change_quantity(new_quantity)  # calling the change_quantity method
        print(f"\nThe new quantity value is: {shoe_list[lowest_quantity_index].get_quantity()}")

        f = open('inventory.txt', 'w')  # rewriting and updating the new value
        new_contents = "Country,Code,Product,Cost,Quantity"

        for shoe in range(0, len(shoe_list)):
            new_contents += shoe_list[
                shoe].original_details()
        f.write(new_contents)

        print(f"\nPlease check inventory.txt for the updated details.")
        f.close()

    elif choice == 'n':
        print("\nSure, no problem at all!")
    else:
        print("Please choose only Y or N.")


def search_shoe():  # searching for a specific shoe in the file
    print(f"""
_____________________________ 4. Search for a shoe ____________________________""")
    shoe_list = read_shoes_data()
    code_list = []  # appending the index to the empty code_list

    for i in range(0, len(shoe_list)):
        code_list.append(shoe_list[i].get_code())  # now we have a list of codes

    search_input = input("\nPlease enter the code you would like to search for: ")

    if search_input in code_list:
        for idx in range(0, len(code_list)):
            if code_list[idx] == search_input:
                searched_shoe = shoe_list[idx]  # this finds the index of the code they are searching for
    else:
        print("The code you searched for does not exist. Please try again.")

    print(f"\nThe shoe you searched for was: ")
    searched_shoe.__str__()  # displays searched shoe in table format


def value_per_item():  # this function will calculate the total value for each item.
    print(f"""
_____________________________ 5. Value for all shoes __________________________""")
    shoe_list = read_shoes_data()

    list_of_shoe_values = []  # we first make our two lists which we will zip together
    list_of_shoe_names = []

    for shoe in range(0, len(shoe_list)):  # appending to each list respectively
        list_of_shoe_values.append(int(shoe_list[shoe].get_quantity()) * int(shoe_list[shoe].get_cost()))
        list_of_shoe_names.append(shoe_list[shoe].get_name())

    values_dict = {}  # creating empty dictionary to zip files together

    for i in range(len(list_of_shoe_names)):
        key = list_of_shoe_names[i]
        value = list_of_shoe_values[i]

        print(f"{key    }:\t{str(value)} USD")
        values_dict[key] = value
    # wanting the cost for an individual item
    choice = input(f"""
Would you like to get the price of an individual product, by name? Y/N: """).strip(" ").lower()

    if choice == 'y':
        choice2 = input("Please enter the exact name of the shoe you would like to view the price for: ").strip(" ")
        try:
            print(f"""
    The price of {choice2} is: {values_dict[choice2]}""")
        except KeyError:
            print("Sorry, that shoe was not found. Please try again.")
    elif choice == 'n':
        print("Task complete. Thanks.")
    else:
        print("Please only enter Y/N")


def highest_qty():  # this will determine the maximum quantity in the file
    print()
    list_of_quantities = []  # appending quantities to this empty list to iterate through
    shoe_list = read_shoes_data()

    for i in range(0, len(shoe_list)):  # iterating through lists
        list_of_quantities.append(int(shoe_list[i].get_quantity()))

    index_of_maximum = list_of_quantities.index(max(list_of_quantities))
    shoe_list[index_of_maximum].__str__()  # displays highest quantity in table format

    print("""
************************* FOR SALE! *************************""")


def main():  # created main() function to encapsulate all methods, functions, and classes
    print(f"""
__________________________ Capstone Project IV - OOP __________________________""")
    highest_qty()

    while True:  # created infinite loop
        print(f"""
_______________________________________________________________________________""")
        read_shoes_data()
        options = int(input(f"""\nPlease select one of the following options, ie, 1, 2, 3, etc

1. View all shoes
2. Capture shoes
3. Re-stock shoes
4. Search for a shoe
5. Value for all shoes
6. Highest quantity
7. Exit

Enter your selection here: """))

        if options == 1:  # 1. View all shoes
            view_all()

        elif options == 2:  # 2. Capture shoes
            capture_shoes()

        elif options == 3:  # 3. Re-stock shoes
            re_stock()

        elif options == 4:  # 4. Search for a shoe
            search_shoe()

        elif options == 5:  # 5. Value for all shoes
            value_per_item()

        elif options == 6:  # 6. Highest quantity
            print(f"""
______________________________ 6. Highest quantity ____________________________""")
            highest_qty()

        elif options == 7:  # 7. Exit
            print(f"""\nThank you, and see you soon :)
_______________________________________________________________________________""")
            break

        else:  # Invalid entry
            print("\nYou have made an invalid selection. Try again...")


if __name__ == '__main__':
    main()  # called main() function

# Thank you, Farinaaz :)

# I did get some coding steer from the following URL
# https://github.com/janlwrobel/Capstone-Project-IV-OOP/blob/main/inventory.py
# For the tabulate method I got steer from the following YouTube URL
# https://www.youtube.com/watch?v=Smf68icE_as&t=2s
