n = int(input('Enter the number of student records: '))
                             # Initialize an empty dictionary to store student marks
dictionary = {}
                             # Input student records
for _ in range(n):
    name, *marks = input('Enter the name and grades separated by space: ').split()
    dictionary[name] = list(map(float, marks))
                             # Input the student name for which the average needs to be calculated
query_name = input('Enter the student name to query: ')
                             # Calculate and print the average if the student is found, otherwise print a message
average = sum(dictionary.get(query_name, [])) / len(dictionary.get(query_name, []))
print("Average marks for the name chosen is {:.2f}".format(average))'''
