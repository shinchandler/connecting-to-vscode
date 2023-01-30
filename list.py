# list : ordered, mutable, allows duplicate,crud

numbers = [10,20,30,40,50]

print(numbers)
print(numbers[0])

print("length of list = ",len(numbers))
print("last_element = ",numbers[-1])

print("before deletion = ",numbers)
del numbers[2]                     # del fncn
print("after deletion = ",numbers) # deleting through index no
numbers.remove(40)                 # remove fncn
print("after deletion = ",numbers) # deleting through element name

#pop
print("before pop = ", numbers)
numbers.pop()                      # pop fncn
print("after pop = ", numbers)

#insert
numbers.insert(2,500)
print(numbers)

#multiply elements
zeros = [0]*10
print(zeros)

#reversing
numbers.reverse()
print(numbers)

#copy list
numbers_2 = numbers
numbers.append(2000)
print(numbers)
print(numbers_2)

#min max fncn

#enumerate 
#takes 2 values