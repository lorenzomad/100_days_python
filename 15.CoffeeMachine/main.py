"""this module will emulate a coffee machine behaviour
according to the requirements of the project in the 
attached file"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


class CoffeeMachine():
    """class to simulate a coffemachine"""
    def __init__(self):
        self.water = resources["water"]
        self.milk = resources["milk"]
        self.coffee = resources["coffee"]
        self.money = 0


    def __repr__(self):
        report = f"Water: {str(self.water)}ml"
        report += f"\nMilk: {str(self.milk)}ml"
        report += f"\nCoffee: {str(self.coffee)}g"
        report += f"\nMoney: ${str(self.money)}"
        return report

    def check_resources(self, choice):
        """check if the resources are sufficient for the requested product
        and returns a boolean accordingly"""
        if (MENU[choice]["ingredients"]["water"] > self.water):
            print("sorry there is not enough water")
            return False
        if (MENU[choice]["ingredients"]["coffee"] > self.coffee):
            print("sorry there is not enough coffee")
            return False
        if (choice != "espresso"):
            if (MENU[choice]["ingredients"]["milk"] > self.milk):
                print("sorry there is not enough milk")
                return False
        return True


    def insert_coins(self):
        """requests number of each type of coins as input and provides
        the total as output"""
        quarters = int(input("how many quarters?"))
        dimes = int(input("how many dimes?"))
        nickles = int(input("how many nickles?"))
        pennies = int(input("how many pennies?"))
        total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
        return total

    def check_cost(self, money, choice):
        """check that the cost is lower than the amount of money provided"""
        if (MENU[choice]["cost"] > money):
            print("Sorry that's not enough money. Money refunded")
            return False
        return True


    def provide_coffee(self, money, choice):
        """provide the coffee choice and udpate the resources and return the change"""
        # provide change
        change = money - MENU[choice]["cost"]
        print(f"Here is ${change} in change")
        #make coffee
        print(f"Here is your ${choice}")
        #update resources
        self.water -= MENU[choice]["ingredients"]["water"]
        if choice != "espresso":
            self.milk -= MENU[choice]["ingredients"]["milk"]
        self.coffee -= MENU[choice]["ingredients"]["coffee"]
        self.money += MENU[choice]["cost"]




def get_input():
    """receive input from the user"""
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    return choice


def main():
    """coffeemachine loop"""
    coffee_machine = CoffeeMachine()
    coffee_choice = get_input()

    while coffee_choice != "off":
        if coffee_choice == "report":
            print(coffee_machine)

        elif coffee_choice in MENU.keys():
            if coffee_machine.check_resources(coffee_choice):
                money = coffee_machine.insert_coins()
                if coffee_machine.check_cost(money, coffee_choice):
                    coffee_machine.provide_coffee(money, coffee_choice)
        else:
            print("please provide a valid choice")

        coffee_choice = get_input()

      
if __name__ == "__main__":
    main()