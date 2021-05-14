
"""
This program will calculate the input of class average of the test scores
It will start(counter) with a accumlator(sum) and set it to zero
loop through the list of test scores
add all test scores
then increment or add by 1
as the loop ends there are no more scores to add
divide the scores(sum) by the number of test scores(counter)
print the output to the user

output will print the average of the class scores

"""


"""

scores
interator, sum =0
loop through test scores
 accumlator = sum + scores
 iterator = interator + 1
output = sum / total scores

print output

"""

scores = [100, 80, 90, 70, 50, 95]
iterator = 0
accumulator = 0
student_count = len(scores)
print("Length is: ", len(scores))

while iterator < len(scores):
    print(f"item at index {iterator} is: ", scores[iterator])
    accumulator = accumulator + scores[iterator]
    iterator = iterator + 1

print("Sum is: ", accumulator)
average = accumulator / student_count
print("The average of total scores in the class is: ", average)
