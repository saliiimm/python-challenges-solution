import math
#palindrome checker

def is_palindrome(s):
    if (s == s[::-1]):
        return True
    else:
        return False

result = is_palindrome('test')
print(result)
result2 = is_palindrome('radar')
print(result2)


#are anagram
def are_anagram(s1,s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    else:
        return False

result3 = are_anagram('listen', 'silent')
print(result3)
result4 = are_anagram('hello', 'world')
print(result4)

#is_prime
def is_prime(n):
    for i in range(2,math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

result5 = is_prime(17)
print(result5)
result6 = is_prime(15)
print(result6)

#sortedlist
def merge_sorted_list(l1,l2):
    return sorted(l1 + l2)

list1 = [1, 3, 5]
list2 = [2, 4, 6]
result7 = merge_sorted_list(list1,list2)
print(result7)

#reverse string
def reverse_string(s):
    return s[::-1]

result8 = reverse_string("Hello, World!")
print(result8)

#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result9 = factorial(5)
print(result9)
    
    
#sum of even numbers     
def sum_of_even_numbers(l):
    result = 0
    for i in range(len(l)):
        if (l[i] % 2 == 0):
            result += l[i]
    return result

result10 = sum_of_even_numbers([1,2,3,4,5,6,7])
print(result10)

#num of words in a sentence
def words_count(s):
    return len(s.split())
result11 = words_count('hey there is five words')
print(result11)