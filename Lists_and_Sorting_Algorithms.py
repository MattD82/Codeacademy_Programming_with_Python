### Adding this file to test out GitHub branches

### GREAT RESOURCE ON LISTS https://www.programiz.com/python-programming/list

### GREAT RESOURCE on all things Python (explains sorting algorithms very well) http://interactivepython.org/

# This is a bubble sort algorithm. source for algorithm = http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
# this sort first moves the largest value to the end of the list, then the second larges, etc.
list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(list(range(len(list_1))))

def bubblesort(lst):
	for passnum in range(len(lst)-1):
		for j in range(len(lst) - 1):
			if lst[j+1] < lst[j]:
				lst[j+1], lst[j] = lst[j], lst[j+1]
	return lst

print(bubblesort(list_1))

### This is the same thing without using a simultaneous swap, just as an example, as well as different ranges
def bubblesort_using_temp(lst):
	for passnum in range(len(lst)-1, 0, -1): # need n-1 total passes
		for j in range(passnum): # can use range(passnum) since there will be n-1, n-2, etc pairs left to sort after each pass.
			if lst[j+1] < lst[j]:
				temp = lst[j+1]
				lst[j+1] = lst[j]
				lst[j] = temp
	return lst

print(bubblesort_using_temp(list_1))

# This is an example of a selection sort
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print("This is alist:           " + str(alist))

list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print("This is the insertion sort: " + str(alist))

# This function finds the maximum value in a list
def find_max_in_list(lst):
	list_max = lst[0] # arbitrary element in list. Can't use 0 since could have all negative #'s 
	for i in range(len(lst)):
		if lst[i] > list_max:
			list_max = lst[i]
	return list_max

print(find_max_in_list(list_1))

# This function finds the second highest value in a list
def second_max_in_list(lst):
	list_max = lst[0] # arbitrary element in list. Can't use 0 since could have all negative #'s 
	for i in range(len(lst)):
		if lst[i] > list_max:
			list_max = lst[i]
	second_max = lst[0]
	for i in range(len(lst)):
		if lst[i] < list_max and lst[i] > second_max:
			second_max = lst[i]
	return second_max

print(second_max_in_list(list_1))

# This function reverses the values in a list
def reverse_list(lst):
	reversed_list = []
	for i in range(len(lst)-1, -1, -1):
		reversed_list.append(lst[i])
	return(reversed_list)

print(list_1)
print(reverse_list(list_1))

# alternate way to reverse a list (without using .append)
def reverse(data_list):
	length = len(data_list)
	s = length
	new_list = [None]*length
	for item in data_list:
	    s = s - 1
	    new_list[s] = item
	return new_list

print(reverse(list_1))

# this function reverses the list order within the for loop only!
def reverse_list_forloop(lst):
	new_list = []
	for item in lst[::-1]:
		new_list.append(item)
	return new_list

print(reverse_list_forloop(list_1))


reverse_list_1 = [x for x in list_1[::-1]]
print(reverse_list_1)
