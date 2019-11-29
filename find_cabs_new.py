
class Trip:
    def __init__(self,driver_name,driver_rating,customer_name,customer_rating):
        self.customer_dict = {customer_name:[driver_name]}
        self.customer_rating_dict = {customer_name:[customer_rating]}
        self.driver_rating_dict = {driver_name:[driver_rating]}
        self.driver_name = driver_name
        self.driver_rating = driver_rating
        self.customer_name = customer_name
        self.customer_rating = customer_rating

    def add_values(self,driver_name,driver_rating,customer_name,customer_rating):
        new_obj = Trip(driver_name,driver_rating,customer_name,customer_rating)
        if new_obj.customer_name not in self.customer_rating_dict:
            self.customer_rating_dict[new_obj.customer_name] = [int(new_obj.customer_rating)]
        else:
            self.customer_rating_dict[new_obj.customer_name].append(int(new_obj.customer_rating))
        if new_obj.driver_name not in  self.driver_rating_dict:
            self.driver_rating_dict[new_obj.driver_name] = [int(new_obj.driver_rating)]
        else:
            self.driver_rating_dict[new_obj.driver_name].append(int(new_obj.driver_rating))
        if int(driver_rating) > 1:
            #print(driver_rating)
            if new_obj.customer_name not in self.customer_dict:
                self.customer_dict[new_obj.customer_name] = [new_obj.driver_name]
            else:
                self.customer_dict[new_obj.customer_name].append(new_obj.driver_name)
        else:
            self.customer_dict[new_obj.customer_name] = []

    def get_customer_rating(self,customer_name):
        avg = 0
        l = 0
        if customer_name in self.customer_rating_dict:
            l = len(self.customer_rating_dict[customer_name])
            for j in self.customer_rating_dict[customer_name]:
                avg += j
        else:
            print("Please create add the values for that customer")
            exit(1)
        return avg / l

    def get_driver_rating(self):
        avg_rating_driver = {}
        for i in self.driver_rating_dict.keys():
            avg = 0
            l = len(self.driver_rating_dict[i])
            for j in self.driver_rating_dict[i]:
                avg += j
                avg_rating_driver[i] = (avg / l)
        return avg_rating_driver

    def print_names(self):
        print(self.customer_dict)
        print(self.customer_rating_dict)
        print(self.driver_rating_dict)
        print(self.get_driver_rating())

    def check_eligible_driver(self,customer_name):
        print("Average customer rating:", self.get_customer_rating(customer_name))
        for i in self.get_driver_rating():
            if self.get_driver_rating()[i] >= self.get_customer_rating(customer_name):
                print(i, end=' ')
                flag = 1
        if flag == 1:
            exit(0)
        else:
            if self.customer_dict[customer_name] is not None:
                print(self.customer_dict[customer_name])
            else:
                print("No driver asscociated")

customer_name = input("Enter customer name : ")
obj = Trip("Raghu",4,"Amar",5)
obj.add_values("Raghu",5,"Akbar",4)
obj.add_values("Raghu",1,"Anthony",2)
obj.add_values("Ram",5,"Amar",1)
obj.add_values("Ram",4,"Anthony",5)
obj.add_values("Ram",5,"Akbar",5)
obj.add_values("Ranjan",3,"Amar",2)
obj.add_values("Ranjan",4,"Akbar",5)
obj.add_values("Ranjan",3,"Anthony",3)
obj.check_eligible_driver(customer_name)