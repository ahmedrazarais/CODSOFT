from login_class import Login
import json
import random







#  making class for users  inherits with login
class Users(Login):
    def __init__(self):
        super().__init__()

    # make a main page for users
    def main_page(self):
        # fisrt calling login to check if he login then acces our main page
        login=self.login_process()
        if login:
            print("\t\tWelcome to the Task-Tracker \n")
            # display choices
            while True:
                print("\t1.View All Your Goals.")
                print("\t2.Add Any Goal To list.")
                print("\t3.Update Any Goal Details From list.")
                print("\t4.Delete Any Goal From List.")
                print("\t5.Exit: To exit from Task-Tracker\n\n")

                # taking user choice
                user_choice=input("Enter Your Choice In Task-Tracker:").strip()

                # calling respective functions on user choice
                if user_choice=="1":
                   self.user_task_list()
                elif user_choice=="2":
                     self.add_task_process()
                elif user_choice=="3":
                    self.update_task_details()
                elif user_choice=="4":
                    self.remove_tasks()
                elif user_choice=="5":
                    print("Task-Tracker Is now ending...\n\n")
                    return
                else:
                    print("Invalid Choice.Please Enter valid Choice.\n")
                
    def update_user_file(self,task_list):
        with open(self.user_task_file,"w") as file:
            json.dump(task_list,file)


    def read_user_file(self):
        try:
            with open(self.user_task_file) as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Cart file not found.")
        except json.decoder.JSONDecodeError:
            return None

    


    def assign_id(self):
          with open(self.id_file, "r") as file:
            used_ids = file.read()
            used_ids = used_ids.split("\n")
            while True:
                id = random.randint(1000, 9999)
                if str(id) not in used_ids:
                    used_ids.append(str(id))
                    with open(self.id_file, "a") as file:
                        file.write(f"{id}\n")
                    return id
    

    def add_task(self):
        while True:  # taking task name input
            task_name = input("Enter the task name (or enter 0 to go back): ").strip()
            # if he want to go back
            if task_name == '0':
                print("Going back...")
                return None
            # if not get any input
            if not task_name:
                print("Task name cannot be empty. Please try again.\n")
                continue
            # only alphabets and space allowed
            if not task_name.replace(' ', '').isalpha():
                print("Task name can only contain alphabets and spaces. Please try again.\n")
                continue
            # when all successull return taskname
            return task_name
        
    def add_task_description(self):
        while True:
            task_description = input("Enter the task description (or enter 0 to go back): ").strip()
            
            if task_description == '0':
                print("Going back...")
                return None # if want to go back
            
            if not task_description:        # if empty input
                print("Task description cannot be empty. Please try again.")
                continue
            
            # Checking if any alphabet is present in the task description
            if not any(char.isalpha() for char in task_description):
                print("Task description must contain at least one alphabet. Please try again.")
                continue
            
            return task_description
    
                        

 

    def add_task_due_date(self):
        while True:
            due_date = input("Enter the due date (or enter 0 to skip): ").strip()
            
            if due_date == '0':    # if want to go back
                print("Going Back To previous menu...")
                return None
            
            # Checking if the due date contains only digits
            if not all(char.isdigit() for char in due_date):
                print("Please enter the date using digits only.\n")
                continue
            
            return due_date
    
    def add_task_status(self):
        while True:
            status = input("Enter the status of the task (e.g., 'pending', 'Completed'; enter 0 to skip): ").strip().lower()
            
            if status == '0': # if want to go back
                print("Going To previous menu..")
                return None
            # checking for valid word
            if status not in ['pending', 'completed']:
                print("Invalid status. Please enter 'pending' or 'completed'.\n")
                continue
            
            return status
    
    def add_task_process(self):
        task_list = self.read_user_file() or []
        task_id = self.assign_id()

        task_name = self.add_task()
        if task_name:
            task_description = self.add_task_description()
            if task_description:
                task_due_date = self.add_task_due_date()
                if task_due_date:
                    task_status = self.add_task_status()
                    if task_status:
                        # Create dictionary to represent task
                        task = {
                            "id": task_id,
                            "name": task_name,
                            "description": task_description,
                            "date": task_due_date,
                            "status": task_status
                        }
                        # Append task to task_list
                        task_list.append(task)
                        # Update user's task file
                        self.update_user_file(task_list)
                        print("Task added successfully!\n\n")
                        return
                    else:
                        print("No task status provided. Returning to main menu...")
                else:
                    print("No task due date provided. Returning to main menu...")
            else:
                print("No task description provided. Returning to main menu...")
        else:
            print("No task name provided. Returning to main menu...")
    


    
     # this mehtod is to show user task details
    def user_task_list(self):
        data=self.read_user_file()      # calling task details mehtod to access user task details
        if not data:     # checking if file is empty or not
            print("\nDear User Your Task-Tracker List is empty Nothing to Display...Add Some Tasks Then Came back\n\n")
        else:
            
            # if tasks in list
            print("\t\tTask-Details\n\n")
            print("{:<15} {:<25} {:<20} {:<15} {:<15}".format("Id","Task-Name", "Description", "Due-Date", "Status"))
            print("-" * 110)
            # iterate over 2d data format
            for tasks in data:
                print("{:<15} {:<25} {:<20} {:<15} {:<15} ".format(tasks["id"],tasks["name"], tasks["description"], tasks["date"], tasks["status"], ))
            print()


    # remove any product from cart
    def remove_tasks(self):
        data=self.read_user_file()      # calling cart details mehtod to access user cart
        if not data:     # checking if cart is empty or not
            print("\nDear User Your Task-Tracker-List is empty Nothing to Display...Add Some Tasks Then Came back.You can't delete anything at this time\n\n")
            return
        else:
            self.user_task_list()
            while True:
                # taking task id input he want to remove 
                try:
                    id_input = int(input("Enter Task Id You Want to delete (enter 0 to go back):"))
                    if id_input == 0:    # if he wants to go back
                        print("Going back to previous option...\n")
                        return

                    # Find the index of the product with the specified ID
                    index_to_remove = None
                    for index, product in enumerate(data):
                        if product["id"] == id_input:
                            index_to_remove = index
                            break

                    if index_to_remove is not None:           
                        del data[index_to_remove]
                        print(f"Task Having id {id_input} is Deleted Successfully.\n")
                        # calling write details to write updated data
                        self.update_user_file(data)                 
                        return
                    else:
                        print("Invalid Id. No Tasks details Found With That id..\n")
                except ValueError:
                    print("ERROR: Please enter a valid integer.\n")
    

     # mehtod to update product details for admin
    def update_task_details(self):
        contents = self.read_user_file()

        if not contents:
            print("Task-Tracker-List is empty at this time. You can't update anything right now.")
            print("See you soon...")
            return

        self.user_task_list()

        print()

        while True:
            try:
                id_input = int(input("Enter Task Id You Want to update (enter 0 to go back): "))
                if id_input == 0:    # if he want to go9 back 
                    print("Going back to the previous option...\n")
                    return
                # getting next dictionaru=y iteration
                task_to_update = next((task for task in contents if task["id"] == id_input), None)
                # if id found
                if task_to_update:
                    print("Task with that ID found. You can now update its details.")

                    while True:
                        # Display options
                        print("1. Update Task Name")
                        print("2. Update Task Description")
                        print("3. Update Task Due Date")
                        print("4. Update Task Status")
                        print("5. Exit From Update Area\n")
                        # taking choice input
                        update_choice = input("Enter your choice: ").strip()
                        # calling respective mehtods
                        if update_choice == "1":
                            new_name = self.add_task()
                            if new_name:
                                task_to_update["name"] = new_name
                                self.update_user_file(contents)
                                print("Task name updated successfully.\n")
                                self.user_task_list()
                            else:
                                print("Going back to the previous option. No change made yet.\n")

                        elif update_choice == "2":
                            new_description = self.add_task_description()
                            if new_description:
                                task_to_update["description"] = new_description
                                self.update_user_file(contents)
                                print("Task description updated successfully.\n")
                                self.user_task_list()
                            else:
                                print("Going back to the previous option. No change made yet.\n")

                        elif update_choice == "3":
                            new_date = self.add_task_due_date()
                            if new_date:
                                task_to_update["date"] = new_date
                                self.update_user_file(contents)
                                print("Task due date updated successfully.\n")
                                self.user_task_list()
                            else:
                                print("Going back to the previous option. No change made yet.\n")

                        elif update_choice == "4":
                            new_status = self.add_task_status()
                            if new_status:
                                task_to_update["status"] = new_status
                                self.update_user_file(contents)
                                print("Task status updated successfully.\n")
                                self.user_task_list()
                            else:
                                print("Going back to the previous option. No change made yet.\n")

                        elif update_choice == "5":
                            print("Exiting the Task-Tracker update area.\n")
                            return  # if he want to come out of update area

                        else: # if invalid choice
                            print("Invalid choice. Please select from the given options.\n")

                else:
                    print("Invalid ID. No task found with that ID.\n")

            except ValueError:
                print("ERROR: Please enter a valid integer for the task ID.\n")


            
    




    


