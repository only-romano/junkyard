

class Restaurant:
    """
    Try it yourself 9-1
    Try it yourself 9-4
    """

    def __init__(self, resraurant_name, cuisine_type):
        """Initiazile name and type attributes"""
        self.restaurant = resraurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restraunt(self):
        print("Ресторан называется \"" + self.restaurant.title() + "\".")
        print("Тип кузин в нём: " + self.type + ".")
        print("Кужины обслужили " + str(self.number_served) + " клиентов." +
              "\n")

    def open_restraunt(self):
        print("Ресторан \"" + self.restaurant.title() + "\" открыт!")

    def set_number_seved(self, customers):
        """Set number of served customers"""
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("Don't fuck with me son.")

    def increment_number_served(self, new_customers):
        """Increment of served cusomers"""
        if new_customers >= 0:
            self.number_served += new_customers
        else:
            print("Wise guy, heh? You are nothing but joke.")
