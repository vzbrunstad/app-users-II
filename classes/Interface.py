import csv 
import os.path

from classes.User import User

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/user_info.csv")

class Interface():
    def __init__(self):
        self.users = []
        self.run()

    def run(self):

        while True:
            input = self.menu()
            if input == 1:
                self.add_user()
            elif input == 2:
                self.delete_user()
            elif input == 3:
                self.view_users()
            elif input == 4:
                self.add_post()
            elif input == 5:
                break

    def menu(self):
        return int(input("1. Add user\n2. Delete User\n3. View Users\n4. Quit\n> "))

    def add_user(self):

        user_data = {'name': 'user'}

        user_data['name'] = input('please enter your name: \n')
        user_data['email'] = input('please enter your email: \n')
        user_data["license"] = input('Please enter your drivers lisence number: \n')

        print(f"congradulations {user_data['name']} you have successfully created an account!")

        self.users.append(User(user_data['name'], user_data['email'], user_data["license"]))
 
    #     self.write_to_csv(self, user_data)


    # def write_to_csv(self, user_data):
    #     with open(path, 'a', newline='') as csv_file:
    #         csv_writer = csv.DictWriter(csv_file, fieldnames = ['name','email','license'])
    #         csv_writer.writerow(user_data)
    #         print(user_data)
    #         self.user.append(User(**user_data))

    def delete_user(self):
        license = input("Enter the driver's license number of the user you would like to delete: ")
        for i, user in enumerate(self.users):
            if license == user.get_license():
                self.users.pop(i)
                print(f"User with license {license} deleted.")
                return

        print(f"No user with that license {license}.4")

    def view_users(self):
        for user in self.users:
            print(user)

    def add_post(self):
        post = input("")












# import csv 
# import os.path

# from classes.User import User

# my_path = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join(my_path, "../data/user_info.csv")

# class Interface():

#     def run (self):

#         while True:
#             mode = input("\nWhat would you like to do?\nOptions:\n1. List All Users\n2. Add a User\n3. Delete User\n4. Quit\n")

#             if mode == '1':
#                 self.get_all_users()
#                 # User.list_users()
#             elif mode == '2':
#                 User.add_user(self)
#             elif mode == '3':
#                 self.delete_user()
#             elif mode == '4':
#                 break

#     @classmethod
#     def get_all_users(cls):
       
#         with open(path, 'r') as csvfile:
#             users = csv.DictReader(csvfile) 
#             users_list = []
#             for user in users:
#                 users_list.append(User(user['name'],user ['email'], user['license']))
#                 print(user['name'])
#             return users_list


