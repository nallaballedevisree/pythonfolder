
class atm():
    def__init__self():
        self.pin=pin
        self.balance=0
        self.menu()
        print("executed")
    def menu(self):
        user_input=input("""
                     hi how can i help you?
                     1.press 1 to create a pin
                     2.press 2 to change a pin
                     3.press 3 to check balance
                     """
                     )   
        if user_input=="1":
            self.create_pin()
        elif user_input=="2"
            self.change_pin()
        elif user_input=="3"
            self.check_balance()
        else:
            exit()
    def create_pin():
        user_input=input("enter a pin")
        self.pin=user_pin
        print("pin created")
        self.menu()
    def change_pin():
        old_pin=input("enter the old pin")
        if old_pin==self.pin:
           new_pin==input("enter the new_pin")
           self.pin==new_pin
           print("pin changed")
           self.menu()
        else:
        print("pin is incorrect")
        self.menu()
    def check_balance():
        check_pin=input("enter the pin")
        if check_pin==self.pin:
           balance=self.check_balance
           print("your balance is ",balance)
        else:
           print("you have entered wrong pin,please enter the correct pin")
           self.menu()    







