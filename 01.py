strengths = [10, 26, 30, 55, 75, 85, 100]
# Do the following:

#Print the length of the list
#Print the first and last element
#Print only the elements from index 2 to index 4 (inclusive)
print('#Ex 1')
print(len(strengths))
print(strengths[0],strengths[-1])
print(strengths[2:4])

#Use a for loop to print each value, but only if it's greater than 50
print('')
print('#Ex 2')
count =0
for s in strengths:
  if s > 50:
    print(s)
    count+=1
print(count)
