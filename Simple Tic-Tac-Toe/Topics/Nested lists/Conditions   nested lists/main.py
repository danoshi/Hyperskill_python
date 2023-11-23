# the list "students" is already defined
#students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]

my_list = [studen[0] for studen in students if studen[1].startswith("A")]

print(my_list)
