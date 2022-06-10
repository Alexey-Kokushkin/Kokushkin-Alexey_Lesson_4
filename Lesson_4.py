#Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

#from random import Random, random


#numbers = [1, 5, 2, 3, 4, 6, 1, 7]

# Первый вариант

#def Nums(numbers):
    #NewList = [numbers[0]]
    #for i in numbers:
        #if i > max(NewList):
            #NewList.append(i)
    #return NewList
    
#print(Nums(numbers))

# Второй вариант

#def SecondNums(numbers):
    #NewList = []
    #for i in range(len(numbers)):
        #if numbers[i] == max(numbers[:i+1:]) and numbers[i] not in NewList:
            #NewList.append(numbers[i])
    #return NewList

#print(SecondNums(numbers))

#_______________________________________________________________________________

#Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.

#import random

#n=int(input('Enter value = '))
#number_list=[]
#with open('File.txt','w') as data:#
    #for i in range(n):
        #number_list.append(random.randint(0, n))
    #data.write(str(number_list))

#with open('File.txt','r') as data:
    #for line in data:
        #for i in number_list:
            #number_list=sorted(number_list)
#print(number_list)
        

#with open('File.txt','a') as data:
    #data.write((f"\n{str(number_list)}"))

#____________________________________________________________________________________________________________

#Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0.
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).

def findTriplets(lst, k):
    triplet_count = 0
    final_temp_list =[]
      
    for i in range(0, len(lst)-1): 
          
        s = set() 
        temp_list = []
  
        # Adding first element
        temp_list.append(lst[i])
  
        curr_k = k - lst[i] 
          
        for j in range(i + 1, len(lst)): 
              
            if (curr_k - lst[j]) in s: 
                triplet_count += 1
                  
                # Adding second element
                temp_list.append(lst[j])
  
                # Adding third element
                temp_list.append(curr_k - lst[j])
                  
                # Appending tuple to the final list
                final_temp_list.append(tuple(temp_list))
                temp_list.pop(2)
                temp_list.pop(1)
            s.add(lst[j])
              
    return final_temp_list
      
# Driver Code
lst = []
with open('1Kints.txt','r') as file:
    for nums in file:
        lst.append(int(nums[:-1]))
    
k = 0
print(findTriplets(lst, k))
  