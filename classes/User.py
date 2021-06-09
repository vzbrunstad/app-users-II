
class User:
    def __init__(self, name, email, drivers_license):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license

    def __str__(self):
        return f"Name: {self.name}, Email Address: {self.email}, Driver's License: {self.drivers_license}"

    def get_license(self):
        return self.drivers_license 










# import csv 
# import os.path

# my_path = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join(my_path, "../data/user_info.csv")

# class User():

#     def __init__ (self):

#     # def __init__ (self, name=None, email=None, license=None):
#     #     self.name= name
#     #     self.email= email
#     #     self.license= license
#         # user_1 = User('vince, 'vzb@msn.com, R12345)
#         pass

#     # @classmethod
#     # def get_all_users(cls):
       
#     #     with open(path, 'r') as csvfile:
#     #         users = csv.DictReader(csvfile) 
#     #         users_list = []
#     #         for user in users:
#     #             users_list.append(User(user['name'],user ['email'], user['license']))
#     #             print(user['name'])
#     #         return users_list

#     # def list_users (self):
#     #     print(User.get_all_users)
#     #     # self.users_list = self.get_all_users()
#     #     # for i, obj in enumerate(users_list):
#     #     #     print (f"{i+1}. {obj.name} {obj.employee_id}")
    

    
#     def add_user (self):
#         user_data = {'name': 'user'}

#         user_data['name'] = input('please enter your name: \n')
#         user_data['email'] = input('please enter your email: \n')
#         user_data["license"] = input('Please enter your drivers lisence number: \n')


#         print(f"congradulations {user_data['name']} you have successfully created an account!")

#         User.add_to_csv(self, user_data)


#     user = []    
#     def add_to_csv(self, user_data):
#         with open(path, 'a', newline='') as csv_file:
#             csv_writer = csv.DictWriter(csv_file, fieldnames = ['name','email','license'])
#             csv_writer.writerow(user_data)
#             print(user_data)
#             self.user.append(User(**user_data))


#     # def delete_user(self):
#     #     print("delete user")


