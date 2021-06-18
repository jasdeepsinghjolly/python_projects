import requests
response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")   # This is the Gitlab API for
# users account to get all projects under the user.
print(response.text)
print(type(response.text))   # This provide the list but its datatype is str instead of list so for this reason we use json format.
print(response.json())    # This will give output in list datatype which is compatible with python and also
# response is list of dictionaries each project will be element for list and and each element is a dictionary containing
# all values with keys.
print(type(response.json()))
project_list = response.json()
print(project_list[0])

for dictionary in project_list:    # Each element in the project_list is a dictionary having all details of a project
    # for "FOR" loop each element from the list is put inside the dictionary variable.
    print(f"Project name: {dictionary['name']}\nProject URL: {dictionary['web_url']}\n")  # We have used single quotes for key (name) in the dictionary as we
    # cannot use "" inside ""

