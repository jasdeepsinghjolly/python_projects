import datetime     # To import built-in datetime module or use from datetime import datetime
user_input = input("Please provide your goal with its colon seperated deadline date\n")
list_of_user_input = user_input.split(":")   # To convert the string inputs from user to list datatype
print(type(list_of_user_input))  # It is list of strings as input function receives
# input from user only in string format.
goal = list_of_user_input[0]
deadline = list_of_user_input[1]
print(type(deadline))
deadline_date = datetime.datetime.strptime(deadline, "%d/%m/%Y")      # to convert the
#string input from user to date datatype. In this first datetime is module name and second datetime
#is the class inside that module and then strptime ( this function is used to convert string to date
# datatype is the function inside that class (datetime).

print(deadline_date)
print(type(deadline_date))
today_date = datetime.datetime.today()
print(f"Today Date: {today_date}")
diff_in_date = deadline_date - today_date   # only dat datatype variables can be added/subtracted from each other
print(type(diff_in_date))
print(f"Time to your Goal {goal} is {diff_in_date.days} days")  # "diff_in_date.days" this is done to print
# only days from the full date like "2021-06-15 20:41:31.397773" and this is available due to datetime module
# and works only with date datatype variables.