#2
#firstname = input("Please write your name")
#surname = input("Please write your surname")
#print("hello", firstname,surname)
import random
# from collections.abc import bytes_iterator
from doctest import set_unittest_reportflags
from tkinter.font import names
from tokenize import String

#3
#print("What do you call a bear with no teeth?\nA gummy bear!")
#or
#jouke = input("What do you call a bear with no teeth?\nA gummy bear!")
#or

#4
#num1 = int(input("Please write your first number "))
#num2 = int(input("Please write your second number "))
#answer = num1 + num2
#print(num1,",",num2)
#print("The sum is", answer)

#5
#num1 = int(input("Please write your first number "))
#num2 = int(input("Please write your second number "))
#num3 = int(input("Please write your thrid number "))
#answer = (num1 + num2) * num3
#print("Your number is", num1,",",num2,",", num3)
#print("The result of your action", answer)

#6
#pizza = int(input("How many slices does your pizza have "))
#eat = int(input("how many do you eat pizza slice "))
#answer = pizza - eat
#print("You have",answer,"pizza slice" )

#7
#user = input("Hi whats your name? ")
#print("hi, nice to meet you", user, ",my name is Mateusz")
#age = int(input("How old are you? "))
#print("Nice i have to 28 yerys old ")
#age1 = age + 1
#print("your age to next year is",age1)

#8
#the_bill = int(input("What is the cost of our dinner? "))
#guest = int(input("How many guest is at dinner? "))
#final_the_bill = the_bill / guest
#print("each person must pay",final_the_bill, "$")

#9
#your_numbers_of_day = int(input("Please write your numbers day: "))
#hours = your_numbers_of_day * 24
#minutes = hours * 60
#seconds = minutes * 60
#print("Quantity hours",hours,",","Quantity minutes",minutes,",","Quantity seconds",seconds)

#10
#kilo = int(input("please write your number kilo: "))
#pounds = kilo * 2.204
#print("The number of pounds in the number of kilograms you specified", pounds)

#11
#bigger = int(input("Enter a number greater than 100: "))
#smaller = int(input("enter a number smaller than 10: "))
#quotient = bigger//smaller
#print(quotient)

#-----------------------------------------------------------------------------------
#def if, elif, else:
#num1=10
#if num1 >10:
#    print("Thi is over 10")
#elif num1 == 10:
#    print("This is equal to 10")
#else:
#    print("This is under 10")

#12
#num1= int(input("Please enter first number: "))
#num2= int(input("Please enter second number: "))
#if num1 > num2:
#    print(num2, num1)
#elif num1 == num2:
#    print("Number is identity")
#else:
#    print(num1, num2)

#13
#num1= int(input("Please enter number smaller to 20: "))
#if num1 >= 20:
#    print("To high")
#else:
#    print("thanks")

#14
#num= int(input("Please enter to number from 10 to 20: "))
#if num <= 10:
#    print("Thanks")
#elif num <=20:
#    print("Thanks")
#else:
#    print("Wrong answer")

#or

#num = int(input("Please enter to number from 10 to 20: "))
#if num >= 10 and num <=20:
#    print("Thanks")
#else:
#    print("Wrong answer")

#15
#color = input("Please enter your favorite colour: ")
#if color == "red" or color == "RED" or color == "Red":
#    print("I also like the color red")
#else:
#    print("I dont like", color,"," ,"I prefer red")

#16
#moja próba
#user = input("It is raining?: ")
#if user == "yes" or user =="YES" or user == "Yes":
#    user = input("It is windy?")
#    if user == "yes" or user =="YES" or user == "Yes":
#        print("It's too windy to take an umbrella.")
#    else:
#        print("take umbrella")
#elif user == "no" or user =="NO" or user == "No":
#    print("have a nice day")

#rozwiazanie z zadania
#raining = input("It is raining?: ")
#raining = str.lower(raining)
#if raining == "yes":
#    windy = input("It is windy?")
#    windy = str.lower(windy)
#    if windy == "yes":
#        print("It's too windy to take an umbrella.")
#    else:
#        print("take umbrella")
#else:
#    print("have a nice day")

#17

#age= int(input("How old are you?"))
#if age >= 18:
#    print("you can vote ")
#if age == 17:
#    print("you can learn to drive")
#if age == 16:
#    print("You can buy a lottery ticket")
#elif age < 16:
#    print("you can collect candy ")

#18
#num = int(input("Please enter your number: "))
#if num < 10:
#    print("Too low ")
#elif num >= 10 or num <= 20:
#    print("Correct")
#else:
#    print("to high")

#19

#enter = int(input("Please enter 1,2 or 3: "))
#if enter == 1:
#    print("thank you")
#elif enter == 2:
#    print("Well done")
#elif enter == 3:
#    print("correct")
#else:
#    print("error message")

#20
#name = input("Please enter your name: ")
#lenght = len(name)
#print(lenght)

#21
#name = input("Please enter your name: ")
#lenght_name = len(name)
#surname = input("please enter your surname: ")
#lenght_surname = len(surname)
#print(name ," ",lenght_name)

#22
#name = input("Please enter your name small letter: ")
#surname = input("Please enter your surname small letter: ")
#new_name= name.upper()
#new_surname= surname.upper()
#print(new_name, new_surname)

#23
#phrase = input("Enter the first line of a nursery rhyme")
#lenght = len(phrase)
#print("this has", lenght, "letters in it")
#start = int(input("Enter a starting number: "))
#end = int(input("Enter an end number: "))
#part = (phrase[start:end])
#print(part)

#24
#word= input("Please enter your word: ")
#new_word= word.upper()
#print(new_word)

#25
#name= input("Please enter your name:")
#if len(name)<5:
#    surname = input("please enter your surname")
#    name = name+surname
#    print(name.upper())
#else:
#    print(name.lower())

#26 /przećwiczyć
#word = input("Please enter a word: ")
#first = word[0]
#lenght = len(word)
#rest = word[1:lenght]
#if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
#    new_word = rest + first + "ay"
#else:
#    new_word = word + "way"
#    print(new_word.lower())

#27
#num= float(input("Please enter your number: "))
#print(num*2)

#28 nie do konca dziala
#num = float(input("please enter your number: "))
#answer= num*2
#print(answer)
#print(round(answer,2))

#29
#import math
#num = float(input("Please enter num bigger to 500:"))
#answer = math.sqrt(num)
#print (round(answer,2))

#30
#import math
#print(round(math.pi,5))

#31 poćwiczyc
#import math
#radius = float(input("enter radios of the circus"))
#area = math.pi*(radius**2)
#print(area)

#32 poćwiczyc
#import math
#radius = int(input("Enter the radius of the circle: "))
#depth = int(input("Enter depth: "))
#area= math.pi*(radius**2)
#volume = area*depth
#print(round(volume,3))

#33 dziala!!!!
#num1 = int(input("Enter first number: "))
#num2 = int(input("enter second umber: "))
#ans1 = num1//num2
#ans2 = num1%num2
#print(num1,"divided by", num2, "is", ans1, "with", ans2, "remaining" )

#34
#print("1)Square")
#print("2)Triangle")
#print()
#menu_selection= int(input("Enter a number: "))
#if menu_selection == 1:
#    side= int(input("Enter the lenght of one side: "))
#    area= side*side
#    print("The area of your chosen shape is", area)
#elif menu_selection ==2:
#    base= int(input("Enter the lenght of the base : "))
#    height= int(input("enter of heinht of the triangle: "))
#    area = (base*height)/2
#    print("The area of your chose shape is", area)
#else:
#    print("Incorrect option select")
#----------------------------------------------------------------------------------------------------------
#wiersz = int(input("Podaj wysokość (ilość gwiazdek) prostokąta: "))
#kolumna = int(input("Podaj szerokość (ilość gwiazdek) prostokąta: "))
#for i in range(wiersz):
#    for j in range(kolumna):
#        if i==0 or i==(wiersz -1) or j==0   or j==(kolumna-1):
#            print('*', end=' ')
#        else:
#            print('-', end=' ')
#    print()
#------------------------------------------------------------------------------------------------------------
#52
import random
from xml.sax.saxutils import prepare_input_source


#num = random.randint(1,100)
#print (num)

#53
#fruit = random.choice(["bannana", "apple", "berry", "pineaple"])
#print(fruit)
#54
#coins = random.choice(["h","t"])
#gues = input("podaj h jesli orzel t jesli reszka ")
#if gues == coins:
#    print("wygraleś")
#else:
#    print("pech")
#if coins == "h":
#    print("komputer wybral orla")
#else:
#    print("komputer wybral reszke")

#55
#num = random.randint(1,5)
#user = int(input("podaj swoja liczbe "))
#if num == user:
#    print("trafione")
#if num > user:
#    print("za niski")
#    user = int(input("spróbuj ponownie "))
#    if num == user:
#        print("wygrales")
#    else:
#        print("przegrales")
#if num < user:
#    print("za wysoki")
#    user = int(input("spróbuj ponownie "))
#    if num == user:
#        print("wygrales")
#    else:
#        print("przegrales")

#69 nie dziala
#country_tuple = ("poland", "norway", "france", "ireland", "sweden")
#country_user = input("Please enter country from this list: (poland, norway france, ireland, sweden): ")
#print(country_tuple.index(5,0,4))

#69 alternatywa

#country = ("poland", "norway", "france", "ireland", "sweden")
#print("this is five country:")
#print(country)
#your_country = input("please enter country: ")
#if your_country in country:
#    indeks = country.index(your_country)
#    print(f"Indeks country {your_country} in touple to {indeks}.")
#else:
#    print("It's wrong country")

#70
#country = ("poland", "norway", "france", "ireland", "sweden")
#print("this is five country:")
#print(country)
#your_country = input("please enter country: ")
#if your_country in country:
#    indeks = country.index(your_country)
#    print(f"Indeks country {your_country} in touple to {indeks}.")
#    num = int(input("enter number (index),to see the country in this position: "))
#    if 0 <= num < len(country):
#        print(f"Country under the index {num} this is f{country[num]}. ")
#    else:
#        print("it's wrong number")
#else:
#    print("It's wrong country")
#-------------------------------------------------------------------------
# zad dodatkowe 2

#wiersz = int(input("Podaj wysokość (ilość gwiazdek) prostokąta: "))
#kolumna = int(input("Podaj szerokość (ilość gwiazdek) prostokąta: "))
#for i in range(wiersz):
#    for j in range(kolumna):
#        if i==0 or i==(wiersz -1) or j==0   or j==(kolumna-1):
#            print('*', end=' ')
#        else:
#            print('-', end=' ')
#    print()


#liczba_poczatkowa = 15
#przyrost = 2
#liczba_liczb_wiersza = 5
#ilość_lini = 3

#aktualna_liczba = liczba_poczatkowa

#for _ in range(ilość_lini):
#    for _ in range(liczba_liczb_wiersza):
#        print(aktualna_liczba, end=" ")
#        aktualna_liczba = aktualna_liczba + przyrost
#    print()



#def czesc (imie, miasto, komunikat= "cześć "):
#    print(komunikat + imie +"!")
#    print("widze, ze jestes z miasta", miasto)

#czesc("darek","wroclaw")
#czesc("byniu","wroclaw","milego dnia ")



#def dodawanie(a,b,):
#    z = a + b
#    return z

#wynik = dodawanie (6,7)
#print("wynik: ", wynik)

#def produce_numbers(n):
#    i = 2
#    numbers = []
#    while i < n:
#        numbers.append(i)
#        i = i + 1
#        return numbers
#for i in produce_numbers(10):
#    print("element:", i)


#def czesc (imie, *args):
#    print ("czesc " + imie + "!")
#    for s in args:
#        print("czesc " + s + "!(args)")
#czesc("janusz ", "darek ", "byniu ")

#def czesc(imie, **kwargs):
#    nazwa = imie
#    if "nazwisko" in kwargs:
#        nazwa = nazwa + " " + kwargs["nazwisko"]
#    print("czesc " + nazwa + "!")
#czesc("janusz ")
#czesc("darek ", nazwisko = "kot")

#pliki

#fp = open("tmp.txt", "w")
#fp.close()



#with open("tmp.txt", "r") as plik:
#    dane = [[str(element)
#             for element in linia.split()]
#                for linia in plik.readlines()]
#print(dane)


#80
#first_name = input("Enter your first name: ")
#print(f"Your first name has {len(first_name)} letters.")

#last_name = input("Enter your last name: ")
#print(f"Your last name has {len(last_name)} letters.")

#full_name = first_name + " " + last_name
#print(f"Your full name is: {full_name}")
#print(f"Your full name has {len(full_name)} characters (including the space).")

#81
#subject = input("Enter your favorite school subject: ")
#formatted_subject = "-".join(subject) + "-"
#print(formatted_subject)

#82
#poem_line = "A stranger, as if from another world, From hiding he drives my city."

#print("Poem excerpt:")
#print(poem_line)

#start = int(input("Enter the starting point (character number): "))
#end = int(input("Enter the ending point (character number): "))

#selected_text = poem_line[start:end]
#print(f"Selected fragment: {selected_text}")

#88
#import array
#numbers = array.array('i')
#for i in range(5):
#    num = int(input(f"Enter number {i+1}: "))
#    numbers.append(num)
#numbers = array.array('i', sorted(numbers))
#numbers.reverse()
#print("Sorted array in reverse order:", numbers)

#89
#import array
#import random
#numbers = array.array('i')
#for i in range(5):
#    numbers.append(random.randint(1, 100))
#for num in numbers:
#    print(num)

#90
#import array
#numbers = array.array('i')
#while len(numbers) < 5:
#    user_input = input("Enter a number: ")
#    if user_input.isdigit():
#        user_input = int(user_input)
#        if 10 <= user_input <= 20:
#            numbers.append(user_input)
#        else:
#            print("Out of range")
#    else:
#        print("Please enter a valid positive number")
#print("Thank you!")
#for num in numbers:
#    print(num)

#file = open("countries.txt", "w")
#file.write("italy/n")
#file.write("germany/n")
#file.write("spain/n")
#file.close()
#------------------------------------------------
#file = open("numbers.txt","a" )
#file.write("1,n")
#file.write("2,n")
#file.write("3,n")
#file.write("4,n")
#file.write("5,n")
#file.close()
#file = open("numbers.txt", "r")
#content = file.read()
#file.close()
#print("include file:")
#print(content)
#----------------------------------------------- txt
#file = open("names.txt", "a")
#new_name = input("enter name: ")
#file.write(new_name + "/w")
#file.close()
#file = open("names.txt", "r")
#content = file.read()
#file.close()
#print("include file:")
#print(content)
#___________________________________________________________

#import csv

#file = open("books.csv", mode="w", newline="")
#writer = csv.writer(file)

#writer.writerow(["book", "author", "year of release"])

#new_record = ["To Kill a Mockingbird", "Harper Lee", 1960]
#writer.writerow(new_record)

#new_record = ["The Great Gatsby", "F. Scott Fitzgerald", 1922]
#writer.writerow(new_record)
#file.close()

#------------------------------------------------------------------
#import csv
#num_records = int(input("How many books would you like to add? "))
#file = open("books.csv", "a", newline="")
#writer = csv.writer(file)
#new_record = ["To Kill a Mockingbird", "Harper Lee", 1960]
#writer.writerow(new_record)
#new_record = ["The Great Gatsby", "F. Scott Fitzgerald", 1922]
#writer.writerow(new_record)
#book = input("Enter the title of the book: ")
#author = input("Enter the author's name: ")
#year = input("Enter the year of release: ")
#new_record = [book, author, year]
#writer.writerow(new_record)
#file.close()
#file = open("books.csv", "r", newline="")
#reader = csv.reader(file)
#file.close()
#search_author = input("Enter an author's name to search for their books: ")
#________________________________________________________________________________________________def

#def get_number():
#    num= int(input("enter number: "))
#    return num
#def count_to_number(num):
#    for i in range(1, num+1):
#        print(i)
#number = get_number()
#count_to_number(number)
#------------------------------------------------------------------------------------------------------
#
#                            kolokwium                kolokwium
#
#_____________________________________________________________________________________________________
#109
# print("1) Create a new file")
# print("2) Display the file")
# print("3) Add a new item to the file")
# selection = int(input("Make a selection 1, 2 or 3: "))
#
# if selection == 1:
#     subject = input("Enter a school subject: ")
#     file = open("Subject.txt", "w")
#     file.write(subject + "\n")
#     file.close()
#
# elif selection == 2:
#     file = open("Subject.txt", "r")
#     print(file.read())
#
# elif selection == 3:
#     file = open("Subject.txt", "a")
#     subject = input("Enter a school subject: ")
#     file.write(subject + "\n")
#     file.close()
#     file = open("Subject.txt", "r")
#     print(file.read())
#
# else:
#     print("Invalid option")
#_____________________________________________________________________________________________________________
#1
# 1def transform(text: str) -> str:
#
#     result = []
#     for ch in text:
#         if ch.isalpha():
#             result.append(ch)
#             result.append(ch.swapcase())
#         else:
#             result.append(ch)
#     return ''.join(result)
#
# def main():
#
#     text = input()
#
#     transformed = transform(text)
#     print(transformed)
#
# if __name__ == '__main__':
#     main()
#_--------------------------------__________________________________________-----------------------------
#2
# liczba_poczatkowa = 15
# przyrost = 2
# liczba_liczb_wiersza = 5
# ilość_lini = 3
#
# aktualna_liczba = liczba_poczatkowa
#
# for _ in range(ilość_lini):
#    for _ in range(liczba_liczb_wiersza):
#        print(aktualna_liczba, end=" ")
#        aktualna_liczba = aktualna_liczba + przyrost
#    print()
#____________________________________________________________________________
#3
# text = input("Enter something: ")
#
# # Sprawdź, czy to integer
# if text.isdigit():
#     print("integer")
#
# # Sprawdź, czy to float (czyli zawiera kropkę dziesiętną)
# elif text.replace('.', '', 1).isdigit() and text.count('.') == 1:
#     print("float")
#
# # W przeciwnym razie to string
# else:
#     print("string")
#-------------------------------------------------------------
# def mnozenie(a,b):
#     z = a*b
#     return z
# wynik= mnozenie(2,3)
# print("wynik: ", wynik)
#----------------------------------------------------------------
# def numer_produktow(n):
#     i = 3
#     numery = []
#     while i < n:
#         numery.append(i)
#         i = i + 1
#     return numery
#
# for i in numer_produktow(5):
#     print("element", i)
#---------------------------------------------------------------------
# def porownanie(a,b):
#     if a > b:
#         return "a jest wieksze od b"
#     elif a < b:
#         return "a jest mniejsze od b"
#     else:
#         return "jest rowne"
#
# a = int(input("podaj pierwsza liczbe: "))
# b = int(input("podaj druga liczbe: "))
# print(porownanie(a,b))
#----------------------------------------------------------------------
# print("1)stworz nowy plik")
# print("2)wyswietl plik")
# print("3)dodaj cos nowego do pliku")
# selection = int(input("stworz 1,2 lub 3:"))
# if selection == 1:
#     przedmiot = input("podaj nazwe przedmiotu:")
#     file = open("przedmiot.txt", "w")
#     file.write(przedmiot + "\n")
#     file.close()
# elif selection == 2:
#     file = open("przedmiot.txt", "r")
#     print(file.read())
#     file.close()
# elif selection == 3:
#     file = open("przedmiot.txt", "a")
#     przedmiot = input('podaj nazwe przedmiotu:')
#     file.write(przedmiot +"\n")
#     file.close()
#     file = open("przedmiot.txt", "r")
#     print(file.read())
# else:
#     print("zla opcja")

#---------------------------------sortowanie--------------------------------------------
# ---------------------------------sortowanie--------------------------------------------lista= [4,5,3,6,12,-13,-7,-9]
# def selectionSort(dane):
#     for i in range(len(dane)):
#         for j in range(i + 1 , len (dane)):
#             if dane[i] > dane [j]:
#                 dane[i], dane[j] = dane[j], dane[i]
# print(lista)
# selectionSort(lista)
# print(lista)

# def funkcja(arg1, arg2, arg3 = "Argument 3"):
#
# print(arg1, arg2, arg3)

# def minMaxByLength(lines):
#     min_str = max_str = lines[0]
#     for line in lines:
#         if len(line) < len(min_str):
#             min_str = line
#         if len(line) > len(max_str):
#             max_str = line
#     return min_str, max_str
#
# with open("dane.txt", "r", encoding="utf-8") as file:
#     lines = [line.strip() for line in file.readlines() if line.strip()]
#
# min_str, max_str = minMaxByLength(lines)
# print("Min długość:", len(min_str), "\n", min_str)
# print("Max długość:", len(max_str), "\n", max_str)
# #____________________________________________________________________________________________
# def asciiSum(s):
#     total = 0
#     for ch in s:
#         total += ord(ch)
#     return total
#
# def minMaxByAsciiSum(lines):
#     min_str = max_str = lines[0]
#     for line in lines:
#         if asciiSum(line) < asciiSum(min_str):
#             min_str = line
#         if asciiSum(line) > asciiSum(max_str):
#             max_str = line
#     return min_str, max_str
#
# with open("dane.txt", "r", encoding="utf-8") as file:
#     lines = [line.strip() for line in file.readlines() if line.strip()]
#
# min_str, max_str = minMaxByAsciiSum(lines)
# print("Min ASCII suma:", asciiSum(min_str), "\n", min_str)
# print("Max ASCII suma:", asciiSum(max_str), "\n", max_str)
# #_________________________________________________________________________________________________________
# def minMaxLexicographically(lines):
#     min_str = max_str = lines[0]
#     for line in lines:
#         if line < min_str:
#             min_str = line
#         if line > max_str:
#             max_str = line
#     return min_str, max_str
#
# with open("dane.txt", "r", encoding="utf-8") as file:
#     lines = [line.strip() for line in file.readlines() if line.strip()]
#
# min_str, max_str = minMaxLexicographically(lines)
# print("Min alfabetycznie:", min_str)
# print("Max alfabetycznie:", max_str)
# #---------------------------------------------------------------------------------------------------------------
# import time
#
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - 1):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#
# def selectionSort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#
# def insertionSort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i]); i += 1
#     while j < len(right):
#         result.append(right[j]); j += 1
#     return result
#
# files = ['sort1.txt', 'sort2.txt', 'sort3.txt']
# algorithms = [
#     ('bubble_sort', bubbleSort),
#     ('selection_sort', selectionSort),
#     ('insertion_sort', insertionSort),
#     ('merge_sort', mergeSort),
# ]
#
# for fname in files:
#     file = open(fname, 'r')
#     numbers = []
#     for line in file:
#         numbers.append(int(line.strip()))
#     file.close()
#
#     print('Czasy dla pliku', fname)
#     for name, func in algorithms:
#         print(name)
#         start = time.time()
#         if name == 'merge_sort':
#             func(numbers)
#         else:
#             func(numbers[:])
#         end = time.time()
#         print(end - start)
#     print()
# #----------------------------------------------------------------------------------------------------------------
# def binarySearch(inputList, n):
#     firstIndex = 0
#     lastIndex = len(inputList) - 1
#     while True:
#         midIndex = (firstIndex + lastIndex) // 2
#         if inputList[midIndex] == n:
#             return midIndex
#         if lastIndex == firstIndex + 1:
#             return -1
#         if inputList[midIndex] > n:
#             lastIndex = midIndex
#         else:
#             firstIndex = midIndex
#
# file = open("sort1.txt", "r")
# numbers = []
# for line in file:
#     numbers.append(int(line.strip()))
# file.close()
#
# sortedNumbers = sorted(numbers)
#
# numberToSearch = 0
# foundIndex = binarySearch(sortedNumbers, numberToSearch)
#
# if foundIndex != -1:
#     print(foundIndex)
#     print(sortedNumbers[foundIndex] == numberToSearch)
# else:
#     print("Nie odnaleziono")


#---------------------------------------------01.06.2025 zajecia-------------------------------------------------------------------
# zad 2.1
# def isPalindrome(t):
#     lb = 0
#     ub = len(t) - 1
#     while lb < ub:
#         if t[lb] != t[ub]:
#             return False
#         lb += 1
#         ub -= 1
#     return True
#
# temp = open("palindromy.txt", "r").read().split()
# counter = 0
# for text in temp:
#     if isPalindrome(text):
#         counter += 1
# print("Palindromow:\u001b[34m", counter, "\u001b[0m\n")
#
# # zad 2.2
# def areAnagrams(t1, t2):
#     if len(t1) != len(t2):
#         return False
#     tab = [0 for i in range(128)]
#     for ch in t1:
#         tab[ ord(ch) ] += 1
#     for ch in t2:
#         tab[ ord(ch) ] -= 1
#     # ponizsze uproszczenie wynika z danych, tylko wielkie litery
#     for i in range(65, 91):
#         if tab[i] != 0:
#             return False
#     return True
#
# temp = [line.split() for line in open("anagramy.txt", "r").readlines()]
# counter = 0
# for line in temp:
#     if areAnagrams(line[0], line[1]):
#         counter += 1
# print("Anagramow:\u001b[34m", counter, "\u001b[0m\n")
#
# # zad 2.3
# def mirrorCipher(t):
#     temp = ""
#     i = len(t) - 1
#     while i > -1:
#         temp += t[i]
#         i -= 1
#     return temp
# print("Odbicie lustrzane dla \u001b[32mAla ma kota.\u001b[0m ->\u001b[34m", mirrorCipher("Ala ma kota."), "\u001b[0m\n")
#
# # zad 2.4
# def cipherCeasar(t):
#     temp = ""
#     for ch in t:
#         temp += chr( ord(ch) + 3 )
#     return temp
# print("Proste szyfrowanie Cezara dla \u001b[32mAla ma kota.\u001b[0m ->\u001b[34m", cipherCeasar("Ala ma kota."), "\u001b[0m\n")
#
# # zad 2.5
# def algBruteForceSearch(t, p):
#     n = len(t)
#     m = len(p)
#     i = 0
#     while i < n - m + 1:
#         j = 0
#         while j < m:
#             if p[j] != t[j + i]:
#                 break
#             j += 1
#         if j == m:
#             return True
#         i += 1
#     return False
# print("Czy wzorzec \u001b[32mABA\u001b[0m istnieje w tekscie \u001b[34mABBAAABBBBBAACCCCACBCAA\u001b[0m", algBruteForceSearch("ABBAAABBBBBAACCCCACBCAA", "ABA"))
# print("Czy wzorzec \u001b[32mAA\u001b[0m istnieje w tekscie \u001b[34mABBAAABBBBBAACCCCACBCAA\u001b[0m", algBruteForceSearch("ABBAAABBBBBAACCCCACBCAA", "AA"), "\n")

#-----------------------------------------------------zad 1-------------------------------------------------------
# def znajdzNajdluzszyPalindrom(tekst):
#     n = 0
#     for _ in tekst:
#         n += 1
#
#     maxDlugosc = 0
#     startIndex = 0
#
#     indeks = 0
#     while indeks < n:
#         lewo = indeks
#         prawo = indeks
#         while lewo >= 0 and prawo < n and tekst[lewo] == tekst[prawo]:
#             dlugosc = prawo - lewo + 1
#             if dlugosc >= 2 and dlugosc > maxDlugosc:
#                 maxDlugosc = dlugosc
#                 startIndex = lewo
#             lewo -= 1
#             prawo += 1
#
#         lewo = indeks
#         prawo = indeks + 1
#         while lewo >= 0 and prawo < n and tekst[lewo] == tekst[prawo]:
#             dlugosc = prawo - lewo + 1
#             if dlugosc >= 2 and dlugosc > maxDlugosc:
#                 maxDlugosc = dlugosc
#                 startIndex = lewo
#             lewo -= 1
#             prawo += 1
#
#         indeks += 1
#
#     if maxDlugosc >= 2:
#         wynik = ["" for _ in range(maxDlugosc)]
#         i = startIndex
#         koniec = startIndex + maxDlugosc
#         indeksWynik = 0
#         while i < koniec:
#             wynik[indeksWynik] = tekst[i]
#             i += 1
#             indeksWynik += 1
#
#         zlozony = ""
#         i = 0
#         while i < maxDlugosc:
#             zlozony = zlozony + wynik[i]
#             i += 1
#         return zlozony
#     else:
#         return "brak"
#
# plik = open("palindromy.txt", "r")
#
# linia = plik.readline()
# numer = 1
#
# while linia != "":
#     dlugosc = 0
#     for _ in linia:
#         dlugosc += 1
#
#     ciag = ["" for _ in range(dlugosc)]
#     i = 0
#     j = 0
#     while i < dlugosc:
#         znak = linia[i]
#         if znak != '\n' and znak != '\r':
#             ciag[j] = znak
#             j += 1
#         i += 1
#
#     tekst = ""
#     i = 0
#     while i < j:
#         tekst = tekst + ciag[i]
#         i += 1
#
#     wynik = znajdzNajdluzszyPalindrom(tekst)
#     print(str(numer) + ". " + tekst + " -> " + wynik)
#     numer += 1
#     linia = plik.readline()
#
# plik.close()
#
# #----------------------------------------------------zad 2------------------------------------------------------
# def algorytmBoyerMoore(tekst, wzorzec):
#     n = 0
#     for _ in tekst:
#         n += 1
#
#     m = 0
#     for _ in wzorzec:
#         m += 1
#
#     tablica = [m]
#     i = 1
#     while i < 256:
#         tablica.append(m)
#         i += 1
#
#     i = 0
#     while i < m - 1:
#         kod = ord(wzorzec[i])
#         tablica[kod] = m - 1 - i
#         i += 1
#
#     pozycja = 0
#     while pozycja <= n - m:
#         j = m - 1
#         while j >= 0:
#             if tekst[pozycja + j] != wzorzec[j]:
#                 break
#             j -= 1
#         if j < 0:
#             return True
#         kodZlegoZnaku = ord(tekst[pozycja + m - 1])
#         if kodZlegoZnaku >= 0 and kodZlegoZnaku < 256:
#             przesuniecie = tablica[kodZlegoZnaku]
#         else:
#             przesuniecie = m
#         pozycja += przesuniecie
#
#     return False
#
# tekstTest = "ABBAAABBBBBAACCCCACBCAAAABBAAAABAABCACCCAACACBBABABABCBCBABCAAACBB"
# print("Czy wzorzec ABC występuje w tekście?", algorytmBoyerMoore(tekstTest, "ABC"))
# print("Czy wzorzec ABA występuje w tekście?", algorytmBoyerMoore(tekstTest, "ABA"))
# print("Czy wzorzec AA występuje w tekście?", algorytmBoyerMoore(tekstTest, "AA"))
# print("Czy wzorzec CAF występuje w tekście?", algorytmBoyerMoore(tekstTest, "CAF"))
# print("Czy wzorzec CCCCA występuje w tekście?", algorytmBoyerMoore(tekstTest, "CCCCA"))
# print("Czy wzorzec CAB występuje w tekście?", algorytmBoyerMoore(tekstTest, "CAB"))
# print("Czy wzorzec CCH występuje w tekście?", algorytmBoyerMoore(tekstTest, "CCH"))
# print("Czy wzorzec CBA występuje w tekście?", algorytmBoyerMoore(tekstTest, "CBA"))
#----------------------------------------------------zad 3 hard------------------------------------------------------
#miał być dowolny system ale nie wiedziałem czy dowolny na jaki decyduje sie osoba wpisujaca cyfry czy poprostu
#ja decyduje od razu piszac kod jaki to bedzie system

# def zamien_dziesietna_na_system(liczba, podstawa):
#     # Tworzymy tablicę cyfr: 0–9, A–Z
#     cyfry = []
#     i = 0
#     while i < 36:
#         if i < 10:
#             cyfry.append(chr(48 + i))  # '0' do '9'
#         else:
#             cyfry.append(chr(65 + (i - 10)))  # 'A' do 'Z'
#         i += 1
#
#     # Obsługa przypadku, gdy liczba = 0
#     if liczba == 0:
#         return "0"
#
#     reszty = []  # Tu zapiszemy cyfry systemu docelowego (od końca)
#     while liczba > 0:
#         reszta = liczba % podstawa
#         reszty.append(reszta)
#         liczba = liczba // podstawa
#
#     # Teraz zamieniamy indeksy na znaki i odwracamy kolejność
#     wynik = ""
#     i = len(reszty) - 1
#     while i >= 0:
#         indeks = reszty[i]
#         znak = cyfry[indeks]
#         wynik = wynik + znak
#         i -= 1
#     return wynik
#
# try:
#     liczba = int(input("Podaj liczbę dziesiętną: "))
#     podstawa = int(input("Podaj podstawę systemu docelowego (2–36): "))
#
#     if podstawa < 2 or podstawa > 36:
#         print("Błąd: dozwolony zakres podstawy to od 2 do 36.")
#     elif liczba < 0:
#         print("Błąd: tylko liczby nieujemne.")
#     else:
#         wynik = zamien_dziesietna_na_system(liczba, podstawa)
#         print(f"Liczba w systemie {podstawa}: {wynik}")
# except ValueError:
#     print("Błąd: podano niepoprawne dane.")

#-------------------------------------------zad 4 hard------------------------------------------------------------------
# def zamien_na_dziesietny(tekst, podstawa):
#     # Tworzymy listę cyfr od '0' do '9' oraz 'A' do 'Z'
#     cyfry = []
#     i = 0
#     while i < 20:
#         if i < 10:
#             cyfry.append(chr(48 + i))  # 0-9
#         else:
#             cyfry.append(chr(65 + i - 10))  # A-Z
#         i += 1
#
#     # Zamieniamy tekst na wielkie litery (aby 'g' == 'G')
#     tekst = tekst.upper()
#     wartosc = 0
#     potega = 1  # Zaczynamy od najmniej znaczącej cyfry (podstawa^0)
#
#     i = len(tekst) - 1
#     while i >= 0:
#         znak = tekst[i]
#         indeks = 0
#
#         # Znajdź wartość znaku
#         while indeks < len(cyfry):
#             if cyfry[indeks] == znak:
#                 break
#             indeks += 1
#
#         # Sprawdź, czy znak pasuje do systemu
#         if indeks >= podstawa:
#             return -1  # Błąd: nielegalna cyfra
#
#         wartosc += indeks * potega
#         potega *= podstawa
#         i -= 1
#
#     return wartosc
#
# try:
#     liczba = input("Podaj liczbę w systemie źródłowym (np. 1111): ")
#     podstawa = int(input("Podaj podstawę/rodzaj systemu źródłowego (2–20): "))
#
#     if podstawa < 2 or podstawa > 20:
#         print("Błąd: niepoprawna podstawa.")
#     else:
#         wynik = zamien_na_dziesietny(liczba, podstawa)
#         if wynik == -1:
#             print("Błąd: liczba zawiera niepoprawny znak dla danego systemu.")
#         else:
#             print(f"Liczba dziesiętna: {wynik}")
# except ValueError:
#     print("Błąd: niepoprawna wartość wejściowa.")

#-----------------------------------------------------zad 3------------------------------------------------
# def zamienNaSzesnastkowy(liczba):
#     cyfry = [0] * 16
#     i = 0
#     while i < 16:
#         if i < 10:
#             cyfry[i] = chr(48 + i)
#         else:
#             cyfry[i] = chr(65 + (i - 10))
#         i += 1
#
#     if liczba == 0:
#         return "0"
#
#     reszty = [0] * 100
#     ileReszt = 0
#     while liczba > 0:
#         reszty[ileReszt] = liczba % 16
#         ileReszt += 1
#         liczba = liczba // 16
#
#     wynik = ""
#     i = ileReszt - 1
#     while i >= 0:
#         indeks = reszty[i]
#         znak = cyfry[indeks]
#         wynik = wynik + znak
#         i -= 1
#
#     return wynik
#
# liczbaWejscie = input("Podaj liczbę dziesiętną: ")
#
# czyPoprawna = True
# i = 0
# dlugosc = 0
# for znak in liczbaWejscie:
#     dlugosc += 1
#
# while i < dlugosc:
#     znak = liczbaWejscie[i]
#     if znak < '0' or znak > '9':
#         czyPoprawna = False
#     i += 1
#
# if czyPoprawna:
#     liczba = 0
#     i = 0
#     while i < dlugosc:
#         cyfra = ord(liczbaWejscie[i]) - ord('0')
#         liczba = liczba * 10 + cyfra
#         i += 1
#
#     wynik = zamienNaSzesnastkowy(liczba)
#     print("Liczba w systemie szesnastkowym:", wynik)
# else:
#     print("Błąd: podano niepoprawne dane (to nie jest liczba nieujemna).")
# # ----------------------------------------------------zad 4------------------------------------------------------
#
# def zamienNaDziesietny(szesnastkowa):
#     cyfry = [0] * 16
#     wartosci = [0] * 16
#     i = 0
#     while i < 16:
#         if i < 10:
#             cyfry[i] = chr(48 + i)
#         else:
#             cyfry[i] = chr(65 + (i - 10))
#         wartosci[i] = i
#         i += 1
#
#     tekst = ""
#     i = 0
#     while i < len(szesnastkowa):
#         znak = szesnastkowa[i]
#         kod = ord(znak)
#         if kod >= ord('a') and kod <= ord('f'):
#             znak = chr(kod - 32)
#         tekst = tekst + znak
#         i += 1
#
#     wynik = 0
#     potega = 1
#
#     dlugosc = 0
#     for _ in tekst:
#         dlugosc += 1
#
#     i = dlugosc - 1
#     while i >= 0:
#         znak = tekst[i]
#         wartoscZnaku = -1
#         j = 0
#         while j < 16:
#             if cyfry[j] == znak:
#                 wartoscZnaku = wartosci[j]
#             j += 1
#
#         if wartoscZnaku == -1:
#             return "Błąd: niepoprawny znak w liczbie"
#
#         wynik = wynik + wartoscZnaku * potega
#         potega = potega * 16
#         i -= 1
#
#     return wynik
#
# liczbaHeksadecymalna = input("Podaj liczbę w systemie szesnastkowym: ")
#
# dozwolone = "0123456789ABCDEFabcdef"
# czyPoprawna = True
# i = 0
# dlugosc = 0
# for _ in liczbaHeksadecymalna:
#     dlugosc += 1
#
# while i < dlugosc:
#     znak = liczbaHeksadecymalna[i]
#     j = 0
#     znaleziony = False
#     while j < 22:
#         if znak == dozwolone[j]:
#             znaleziony = True
#         j += 1
#     if znaleziony == False:
#         czyPoprawna = False
#     i += 1
#
# if czyPoprawna and dlugosc > 0:
#     wynik = zamienNaDziesietny(liczbaHeksadecymalna)
#     print("Liczba dziesiętna:", wynik)
# else:
#     print("Błąd: podano niepoprawną liczbę szesnastkową.")

#--------------------------------------------------------------------------------------------------------------
# def dlugosc(L):
#     i = 0
#     while i in L or (i < 10000 and (i < len(L))): i += 1
#     return i
#
# def ascii_na_bity(ascii):
#     bity = []
#     i = 0
#     while i < dlugosc(ascii):
#         a = ascii[i]
#         j = 7
#         while j >= 0:
#             bity += [(a >> j) & 1]
#             j -= 1
#         i += 1
#     return bity
#
# def zlicz_seria(bity):
#     wynik = []
#     i = 0
#     bit = bity[0]
#     licz = 0
#     while i < dlugosc(bity):
#         if bity[i] == bit:
#             licz += 1
#         else:
#             wynik += [licz]
#             bit = bity[i]
#             licz = 1
#         i += 1
#     wynik += [licz]
#     return wynik
#
# def podziel(dane):
#     out = []
#     i = 0
#     while i < dlugosc(dane):
#         val = dane[i]
#         while val > 255:
#             out += [255, 0]
#             val -= 255
#         out += [val]
#         i += 1
#     return out
#
# def wypisz(lista):
#     i = 0
#     while i < dlugosc(lista):
#         print(lista[i], end=' ')
#         i += 1
#
# # --- MAIN ---
# dane = [33, 65, 66, 42]  # "!AB*"
# bity = ascii_na_bity(dane)
# seria = zlicz_seria(bity)
# kompresja = podziel(seria)
#
# wypisz(kompresja)

# #----------------------------------------------------------------------------------------------------------
#
# def dl(L):
#     i = 0
#     while i in L or (i < 9999 and (i < len(L))): i += 1
#     return i
#
# def to_bity(ascii):
#     bity = []
#     i = 0
#     while i < dl(ascii):
#         val = ascii[i]
#         j = 7
#         while j >= 0:
#             bity += [(val >> j) & 1]
#             j -= 1
#         i += 1
#     return bity
#
# def serie(bity):
#     i = 1
#     licz = 1
#     wynik = []
#     bit = bity[0]
#     while i < dl(bity):
#         if bity[i] == bit:
#             licz += 1
#         else:
#             wynik += [licz]
#             licz = 1
#             bit = bity[i]
#         i += 1
#     wynik += [licz]
#     return wynik
#
# def ile_bitow(maxv):
#     n = 1
#     while (1 << n) <= maxv:
#         n += 1
#     return n
#
# def na_n_bitow(lista, n):
#     wynik = []
#     i = 0
#     while i < dl(lista):
#         val = lista[i]
#         j = n - 1
#         while j >= 0:
#             wynik += [(val >> j) & 1]
#             j -= 1
#         i += 1
#     return wynik
#
# def pakuj_bajty(bity):
#     wynik = []
#     i = 0
#     while i + 7 < dl(bity):
#         bajt = 0
#         j = 0
#         while j < 8:
#             bajt = bajt << 1 | bity[i + j]
#             j += 1
#         wynik += [bajt]
#         i += 8
#     if i < dl(bity):
#         brak = 8 - (dl(bity) - i)
#         bajt = 0
#         j = 0
#         while i < dl(bity):
#             bajt = bajt << 1 | bity[i]
#             i += 1
#             j += 1
#         bajt = bajt << (8 - j)
#         wynik += [bajt]
#         return wynik, brak
#     else:
#         return wynik, 0
#
# def kompresja2(ascii):
#     bity = to_bity(ascii)
#     dl_serii = serie(bity)
#     maxv = 0
#     i = 0
#     while i < dl(dl_serii):
#         if dl_serii[i] > maxv:
#             maxv = dl_serii[i]
#         i += 1
#     n = ile_bitow(maxv)
#     bity_danych = na_n_bitow(dl_serii, n)
#     bajty, nadmiar = pakuj_bajty(bity_danych)
#     wynik = [n]
#     wynik[0] = n
#     bajt0 = (nadmiar << 5) | ((bity_danych[0] << 4) if dl(bity_danych) > 0 else 0)
#     wynik += [bajt0]
#     i = 1
#     while i < dl(bajty):
#         wynik += [bajty[i]]
#         i += 1
#     return wynik
#
# # --- Przykład ---
# ascii = [33, 65, 66, 42]  # "!AB*"
# wynik = kompresja2(ascii)
#
# # Wypisz
# i = 0
# while i < dl(wynik):
#     print(wynik[i], end=" ")
#     i += 1

# def dlugosc(L):
#     i = 0
#     while i in L or (i < 10000 and (i < len(L))): i += 1
#     return i
#
# def tekstNaASCII(tekst):
#     ascii = []
#     i = 0
#     while i < len(tekst):
#         znak = tekst[i]
#         kod = 0
#         j = 0
#         while j < 256:
#             if chr(j) == znak:
#                 kod = j
#                 j = 256
#             else:
#                 j += 1
#         ascii += [kod]
#         i += 1
#     return ascii
#
# def asciiNaBity(ascii):
#     bity = []
#     i = 0
#     while i < dlugosc(ascii):
#         a = ascii[i]
#         j = 7
#         while j >= 0:
#             bity += [(a >> j) & 1]
#             j -= 1
#         i += 1
#     return bity
#
# def zliczSeria(bity):
#     wynik = []
#     i = 0
#     bit = bity[0]
#     licz = 0
#     while i < dlugosc(bity):
#         if bity[i] == bit:
#             licz += 1
#         else:
#             wynik += [licz]
#             bit = bity[i]
#             licz = 1
#         i += 1
#     wynik += [licz]
#     return wynik
#
# def podziel(dane):
#     out = []
#     i = 0
#     while i < dlugosc(dane):
#         val = dane[i]
#         while val > 255:
#             out += [255, 0]
#             val -= 255
#         out += [val]
#         i += 1
#     return out
#
# def wypisz(lista):
#     i = 0
#     while i < dlugosc(lista):
#         print(lista[i], end=' ')
#         i += 1
#     print()
#
#
# tekst = "!AB*!"
# dane = tekstNaASCII(tekst)
# bity = asciiNaBity(dane)
# seria = zliczSeria(bity)
# kompresja = podziel(seria)
#
# print("Wejściowy tekst:", tekst)
# print("ASCII (dziesiętnie):", dane)
# print("Bity:", bity)
# print("Wynik (ciąg długości serii):")
# wypisz(kompresja)
#
# #----------------------------------------------------------------------------------------------------------
#
# def dl(L):
#     i = 0
#     while i in L or (i < 9999 and (i < len(L))): i += 1
#     return i
#
# def toBity(ascii):
#     bity = []
#     i = 0
#     while i < dl(ascii):
#         val = ascii[i]
#         j = 7
#         while j >= 0:
#             bity += [(val >> j) & 1]
#             j -= 1
#         i += 1
#     return bity
#
# def serie(bity):
#     i = 1
#     licz = 1
#     wynik = []
#     bit = bity[0]
#     while i < dl(bity):
#         if bity[i] == bit:
#             licz += 1
#         else:
#             wynik += [licz]
#             licz = 1
#             bit = bity[i]
#         i += 1
#     wynik += [licz]
#     return wynik
#
# def ileBitow(maxv):
#     n = 1
#     while (1 << n) <= maxv:
#         n += 1
#     return n
#
# def naNBitow(lista, n):
#     wynik = []
#     i = 0
#     while i < dl(lista):
#         val = lista[i]
#         j = n - 1
#         while j >= 0:
#             wynik += [(val >> j) & 1]
#             j -= 1
#         i += 1
#     return wynik
#
# def pakujBajty(bity):
#     wynik = []
#     i = 0
#     while i + 7 < dl(bity):
#         bajt = 0
#         j = 0
#         while j < 8:
#             bajt = bajt << 1 | bity[i + j]
#             j += 1
#         wynik += [bajt]
#         i += 8
#     if i < dl(bity):
#         brak = 8 - (dl(bity) - i)
#         bajt = 0
#         j = 0
#         while i < dl(bity):
#             bajt = bajt << 1 | bity[i]
#             i += 1
#             j += 1
#         bajt = bajt << (8 - j)
#         wynik += [bajt]
#         return wynik, brak
#     else:
#         return wynik, 0
#
# def liczbaNaBity(val):
#     bity = []
#     j = 7
#     while j >= 0:
#         bity += [(val >> j) & 1]
#         j -= 1
#     return bity
#
# def wypiszBinarne(lista):
#     print("Wynik binarny:")
#     i = 0
#     while i < dl(lista):
#         bity = liczbaNaBity(lista[i])
#         j = 0
#         while j < dl(bity):
#             print(bity[j], end='')
#             j += 1
#         print(" ", end='')
#         i += 1
#     print()
#
# def kompresjaa(ascii):
#     bity = toBity(ascii)
#     dlSerii = serie(bity)
#     maxv = 0
#     i = 0
#     while i < dl(dlSerii):
#         if dlSerii[i] > maxv:
#             maxv = dlSerii[i]
#         i += 1
#     n = ileBitow(maxv)
#     bityDanych = naNBitow(dlSerii, n)
#     bajty, nadmiar = pakujBajty(bityDanych)
#     wynik = [n]
#     bajt0 = (nadmiar << 5) | ((bityDanych[0] << 4) if dl(bityDanych) > 0 else 0)
#     wynik += [bajt0]
#     i = 1
#     while i < dl(bajty):
#         wynik += [bajty[i]]
#         i += 1
#     return wynik
#
# ascii = [33, 65, 66, 42]
# wynik = kompresjaa(ascii)
#
# print("Wynik dziesiętnie:", wynik)
# wypiszBinarne(wynik)

#-------------------------------------------------------------------------------------------------------------------

# tekst = "dupa blada"
#
# #1 Liczba znaków L
# L = 0
# for c in tekst:
#     L += 1
# print("1) Liczba znaków L:", L)
#
# #2 Liczba różnych znaków X
# unikalny = ""
# for c in tekst:
#     znaleziony = False
#     for u in unikalny:
#         if c == u:
#             znaleziony = True
#             break
#     if not znaleziony:
#         unikalny += c
# X = 0
# for _ in unikalny:
#     X += 1
# print("2) Liczba różnych znaków X:", X, "->", unikalny)
#
# #3 Liczba bitów N potrzebnych do maski
# N = 0
# moc = 1
# while moc < X:
#     moc = moc * 2
#     N = N + 1
# print("3) Liczba bitów N:", N)
#
# #4 Zapisz słownik (kolejność unikalnych znaków) do pliku
# # Tu po prostu jako string
# slownik = ""
# for c in unikalny:
#     slownik += c
# print("4) Słownik:", slownik)
#
# #5 Przypisz maski dla znaków
# maski = []
# for i in range(X):
#     m = ""
#     val = i
#     for j in range(N):
#         bit = val % 2
#         if bit == 0:
#             m = "0" + m
#         else:
#             m = "1" + m
#         val = val // 2
#     maski.append(m)
# print("5) Maski:")
# for i in range(X):
#     print(unikalny[i], "->", maski[i])
#
# #6 Oblicz resztę R
# iloczyn = L * N
# R = (8 - (iloczyn + 3) % 8) % 8
# print("6) Reszta R:", R)
#
# #7 Zapisz 3 bity z informacją o reszcie R do ciągu tymczasowego
# tmp = ""
# val = R
# for i in range(3):
#     bit = val % 2
#     if bit == 0:
#         tmp = "0" + tmp
#     else:
#         tmp = "1" + tmp
#     val = val // 2
# print("7) Ciąg tymczasowy po dopisaniu info o R:", tmp)
#
# #8 Dodaj litery zakodowane maską
# for c in tekst:
#     # znajdź indeks w unique
#     idx = 0
#     for i in range(X):
#         if unikalny[i] == c:
#             idx = i
#             break
#     tmp = tmp + maski[idx]
# print("8) Ciąg tymczasowy z dodanymi maskami:", tmp)
#
# #9 Wycinaj po 8 bitów, zamieniaj na liczby i zapisuj
# i = 0
# out = []
# while i + 8 <= len(tmp):
#     bity = ""
#     j = 0
#     while j < 8:
#         bity = bity + tmp[i + j]
#         j += 1
#     # zamiana na liczbę
#     wartosc = 0
#     k = 0
#     while k < 8:
#         wartosc = wartosc * 2
#         if bity[k] == "1":
#             wartosc += 1
#         k += 1
#     out.append(wartosc)
#     i = i + 8
#
# # zostaje mniej niż 8 bitów na końcu
# reszta = ""
# j = i
# while j < len(tmp):
#     reszta = reszta + tmp[j]
#     j += 1
#
# print("9) Wycięte liczby (wartości w bajtach):", out)
# print("Pozostałe bity:", reszta)
#
# #10 Dopisz nadmiarowe bity R i zamień na ostatni bajt
# while len(reszta) < 8:
#     if R > 0:
#         reszta = reszta + "1"
#         R -= 1
#     else:
#         reszta = reszta + "0"
#
# # zamiana na liczbę
# wartosc = 0
# k = 0
# while k < 8:
#     wartosc = wartosc * 2
#     if reszta[k] == "1":
#         wartosc += 1
#     k += 1
# out.append(wartosc)
#
# print("10) Wynik końcowy (wartości bajtów):", out)
#------------------------------------------------------------------------------------------------------------


#def find_union(list_a, list_b):
#    union = []
#    for element in list_a + list_b:
#        if element not in union:
#             union.append(element)
#     return union
#
# class MobilePhone:
#     def __init__(self, display_size, ram, os):
#         self.display_size = display_size
#         self.ram = ram
#         self.os = os
#
# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
#     def change_radius(self, new_radius):
#         self.radius = new_radius
#
# circle = Circle(7)
#
# while True:
#     radius = float(input("Circle radius: "))
#     circle.change_radius(radius)
#     print("Area:", circle.area())
#     print("Circumference:", circle.circumference())
#
# class Elevator:
#     occupancy_limit = 8
#
#     def __init__(self, occupants):
#         if occupants > self.occupancy_limit:
#             print("The maximum occupancy limit has been exceeded."
#                   f" {occupants - self.occupancy_limit} occupants must exit the elevator.")
#         self.occupants = occupants
#
# elevator1 = Elevator(6)
# print("Elevator 1 occupants:", elevator1.occupants)
# elevator2 = Elevator(10)
# print("Elevator 2 occupants:", elevator2.occupants)
#

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.style.use("seaborn-v0_8")
#
#
# # =========================
# # 1. Wczytanie danych
# # =========================
#
# def load_data():
#     try:
#         df = pd.read_csv("Crime_Data_from_2020_to_2024.csv")
#         print("Plik wczytany poprawnie.")
#         return df
#     except FileNotFoundError:
#         print("Nie znaleziono pliku CSV.")
#         exit()
#
#
# # =========================
# # 2. Czyszczenie danych
# # =========================
#
# def clean_data(df):
#
#     df = df.drop_duplicates()
#
#     df["DATE OCC"] = pd.to_datetime(df["DATE OCC"], errors="coerce")
#     df = df.dropna(subset=["DATE OCC"])
#
#     return df
#
#
# # =========================
# # 3. Inżynieria funkcji
# # =========================
#
# def feature_engineering(df):
#
#     df["year"] = df["DATE OCC"].dt.year
#     df["month"] = df["DATE OCC"].dt.month
#     df["day_of_week"] = df["DATE OCC"].dt.day_name()
#
#     return df
#
#
# # =========================
# # 4. Trend przestępczości
# # =========================
#
# def crime_trend(df):
#
#     trend = df.groupby("year").size()
#
#     plt.figure(figsize=(10,6))
#     plt.plot(trend.index, trend.values, marker="o", linewidth=3)
#     plt.title("Crime Trend by Year")
#     plt.xlabel("Year")
#     plt.ylabel("Number of Crimes")
#     plt.grid(True)
#     plt.show()
#
#
# # =========================
# # 5. Top 10 obszarów
# # =========================
#
# def crime_by_area(df):
#
#     area_counts = df["AREA NAME"].value_counts().head(10)
#
#     plt.figure(figsize=(10,6))
#     plt.bar(area_counts.index, area_counts.values)
#     plt.xticks(rotation=45)
#     plt.title("Top 10 Areas by Crime")
#     plt.ylabel("Number of Crimes")
#     plt.tight_layout()
#     plt.show()
#
#
# # =========================
# # 6. Najczęstsze przestępstwa
# # =========================
#
# def top_crime_types(df):
#
#     crime_counts = df["Crm Cd Desc"].value_counts().head(10)
#
#     plt.figure(figsize=(10,6))
#     plt.barh(crime_counts.index, crime_counts.values)
#     plt.title("Top 10 Crime Types")
#     plt.xlabel("Number of Crimes")
#     plt.gca().invert_yaxis()
#     plt.tight_layout()
#     plt.show()
#
#
# # =========================
# # 7. Analiza wieku ofiar
# # =========================
#
# def victim_age_analysis(df):
#
#     df = df[df["Vict Age"] > 0]
#
#     plt.figure(figsize=(8,6))
#     plt.hist(df["Vict Age"], bins=30)
#     plt.title("Victim Age Distribution")
#     plt.xlabel("Age")
#     plt.ylabel("Frequency")
#     plt.show()
#
#
# # =========================
# # 8. Najbardziej niebezpieczny dzień tygodnia
# # =========================
#
# def crime_by_day(df):
#
#     day_counts = df["day_of_week"].value_counts()
#
#     plt.figure(figsize=(8,6))
#     plt.bar(day_counts.index, day_counts.values)
#     plt.xticks(rotation=45)
#     plt.title("Crime by Day of Week")
#     plt.ylabel("Number of Crimes")
#     plt.tight_layout()
#     plt.show()
#
#
# # =========================
# # 9. Prognoza przestępczości
# # =========================
#
# def forecast_crime(df):
#
#     yearly = df.groupby("year").size().reset_index(name="crime_count")
#
#     X = yearly["year"].values
#     y = yearly["crime_count"].values
#
#     a, b = np.polyfit(X, y, 1)
#
#     future_years = np.array([2025, 2026])
#     predictions = a * future_years + b
#
#     plt.figure(figsize=(10,6))
#     plt.plot(X, y, marker="o", linewidth=3, label="History")
#     plt.plot(future_years, predictions, "--o", linewidth=3, label="Forecast")
#     plt.legend()
#     plt.title("Crime Forecast")
#     plt.xlabel("Year")
#     plt.ylabel("Number of Crimes")
#     plt.grid(True)
#     plt.show()
#
#
# # =========================
# # 10. MAIN
# # =========================
#
# def main():
#
#     df = load_data()
#     df = clean_data(df)
#     df = feature_engineering(df)
#
#     crime_trend(df)
#     crime_by_area(df)
#     top_crime_types(df)
#     victim_age_analysis(df)
#     crime_by_day(df)
#     forecast_crime(df)
#
#
# if __name__ == "__main__":
#     main()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import os
#
# plt.style.use("seaborn-v0_8")
#
#
# # =========================
# # 1. Wczytanie danych
# # =========================
#
# def load_data():
#     try:
#         base_path = os.path.dirname(os.path.abspath(__file__))
#         file_path = os.path.join(base_path, "Crime_Data_from_2020_to_2024.csv")
#
#         df = pd.read_csv(file_path)
#         print("Plik wczytany poprawnie.")
#         return df
#
#     except FileNotFoundError:
#         print("Nie znaleziono pliku CSV.")
#         exit()
#
#
# # =========================
# # 2. Czyszczenie danych
# # =========================
#
# def clean_data(df):
#
#     df = df.drop_duplicates()
#
#     df["DATE OCC"] = pd.to_datetime(df["DATE OCC"], errors="coerce")
#     df = df.dropna(subset=["DATE OCC"])
#
#     return df
#
#
# # =========================
# # 3. Feature Engineering
# # =========================
#
# def feature_engineering(df):
#
#     df["year"] = df["DATE OCC"].dt.year
#     df["month"] = df["DATE OCC"].dt.month
#     df["day_of_week"] = df["DATE OCC"].dt.day_name()
#
#     if "TIME OCC" in df.columns:
#         df["hour"] = df["TIME OCC"] // 100
#
#     return df
#
#
# # =========================
# # 4. Trend roczny
# # =========================
#
# def crime_trend(df):
#
#     trend = df.groupby("year").size()
#
#     plt.figure(figsize=(10,6))
#     plt.plot(trend.index, trend.values, marker="o", linewidth=3)
#     plt.title("Crime Trend by Year")
#     plt.xlabel("Year")
#     plt.ylabel("Number of Crimes")
#     plt.grid(True)
#     plt.show()
#
#
# # =========================
# # 5. Sezonowość miesięczna
# # =========================
#
# def crime_by_month(df):
#
#     month_counts = df.groupby("month").size()
#
#     plt.figure(figsize=(10,6))
#     plt.plot(month_counts.index, month_counts.values, marker="o")
#     plt.title("Crime by Month")
#     plt.xlabel("Month")
#     plt.ylabel("Number of Crimes")
#     plt.grid(True)
#     plt.show()
#
#
# # =========================
# # 6. Dzień tygodnia
# # =========================
#
# def crime_by_day(df):
#
#     day_counts = df["day_of_week"].value_counts()
#
#     plt.figure(figsize=(8,6))
#     plt.bar(day_counts.index, day_counts.values)
#     plt.xticks(rotation=45)
#     plt.title("Crime by Day of Week")
#     plt.ylabel("Number of Crimes")
#     plt.tight_layout()
#     plt.show()
#
#
# # =========================
# # 7. Godzina przestępstwa
# # =========================
#
# def crime_by_hour(df):
#
#     if "hour" in df.columns:
#         hour_counts = df.groupby("hour").size()
#
#         plt.figure(figsize=(10,6))
#         plt.plot(hour_counts.index, hour_counts.values, marker="o")
#         plt.title("Crime by Hour")
#         plt.xlabel("Hour of Day")
#         plt.ylabel("Number of Crimes")
#         plt.grid(True)
#         plt.show()
#
#
# # =========================
# # 8. Top 10 obszarów
# # =========================
#
# def crime_by_area(df):
#
#     area_counts = df["AREA NAME"].value_counts().head(10)
#
#     plt.figure(figsize=(10,6))
#     plt.bar(area_counts.index, area_counts.values)
#     plt.xticks(rotation=45)
#     plt.title("Top 10 Areas by Crime")
#     plt.ylabel("Number of Crimes")
#     plt.tight_layout()
#     plt.show()
#
#
# # =========================
# # 9. Top 10 typów przestępstw
# # =========================
#
# def top_crime_types(df):
#
#     crime_counts = df["Crm Cd Desc"].value_counts().head(10)
#
#     plt.figure(figsize=(10,6))
#     plt.barh(crime_counts.index, crime_counts.values)
#     plt.title("Top 10 Crime Types")
#     plt.xlabel("Number of Crimes")
#     plt.gca().invert_yaxis()
#     plt.tight_layout()
#     plt.show()
#
#
# # =========================
# # 10. Wiek ofiar
# # =========================
#
# def victim_age_analysis(df):
#
#     df = df[df["Vict Age"] > 0]
#
#     plt.figure(figsize=(8,6))
#     plt.hist(df["Vict Age"], bins=30)
#     plt.title("Victim Age Distribution")
#     plt.xlabel("Age")
#     plt.ylabel("Frequency")
#     plt.show()
#
#
# # =========================
# # 11. Płeć ofiar
# # =========================
#
# def crime_by_gender(df):
#
#     if "Vict Sex" in df.columns:
#         gender_counts = df["Vict Sex"].value_counts()
#
#         plt.figure(figsize=(6,6))
#         plt.pie(gender_counts.values,
#                 labels=gender_counts.index,
#                 autopct="%1.1f%%")
#         plt.title("Crime by Victim Gender")
#         plt.show()
#
#
# # =========================
# # 12. Heatmapa miesiąc vs rok
# # =========================
#
# def crime_heatmap(df):
#
#     pivot = df.pivot_table(index="month",
#                            columns="year",
#                            aggfunc="size")
#
#     plt.figure(figsize=(10,6))
#     plt.imshow(pivot, aspect="auto")
#     plt.colorbar()
#     plt.title("Crime Heatmap (Month vs Year)")
#     plt.xlabel("Year")
#     plt.ylabel("Month")
#     plt.show()
#
#
# # =========================
# # 13. Prognoza liniowa
# # =========================
#
# def forecast_crime(df):
#
#     yearly = df.groupby("year").size().reset_index(name="crime_count")
#
#     X = yearly["year"].values
#     y = yearly["crime_count"].values
#
#     a, b = np.polyfit(X, y, 1)
#
#     future_years = np.array([2025, 2026])
#     predictions = a * future_years + b
#
#     plt.figure(figsize=(10,6))
#     plt.plot(X, y, marker="o", linewidth=3, label="History")
#     plt.plot(future_years, predictions, "--o", linewidth=3, label="Forecast")
#     plt.legend()
#     plt.title("Crime Forecast")
#     plt.xlabel("Year")
#     plt.ylabel("Number of Crimes")
#     plt.grid(True)
#     plt.show()
#
#
# # =========================
# # MAIN
# # =========================
#
# def main():
#
#     df = load_data()
#     df = clean_data(df)
#     df = feature_engineering(df)
#
#     crime_trend(df)
#     crime_by_month(df)
#     crime_by_day(df)
#     crime_by_hour(df)
#     crime_by_area(df)
#     top_crime_types(df)
#     victim_age_analysis(df)
#     crime_by_gender(df)
#     crime_heatmap(df)
#     forecast_crime(df)
#
#
# if __name__ == "__main__":
#     main()

# import pandas as pd
# import numpy as np
# import
# import matplotlib.pyplot as plt
# import os
#
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, classification_report
#
# plt.style.use("seaborn-v0_8")
#
#
# # =========================
# # LOAD DATA
# # =========================
#
# def load_data():
#     base_path = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_path, "Crime_Data_from_2020_to_2024.csv")
#     df = pd.read_csv(file_path)
#     return df
#
#
# # =========================
# # CLEAN + FEATURE ENGINEERING
# # =========================
#
# def prepare_data(df):
#
#     df = df.drop_duplicates()
#
#     df["DATE OCC"] = pd.to_datetime(df["DATE OCC"], errors="coerce")
#     df = df.dropna(subset=["DATE OCC"])
#
#     df["year"] = df["DATE OCC"].dt.year
#     df["month"] = df["DATE OCC"].dt.month
#     df["day_of_week"] = df["DATE OCC"].dt.day_name()
#
#     if "TIME OCC" in df.columns:
#         df["hour"] = df["TIME OCC"] // 100
#     else:
#         df["hour"] = 0
#
#     weekend_days = ["Saturday", "Sunday"]
#     df["is_weekend"] = df["day_of_week"].isin(weekend_days).astype(int)
#
#     df = df[df["Vict Age"] > 0]
#
#     return df
#
#
# # =========================
# # DASHBOARD EDA
# # =========================
#
# def dashboard(df):
#
#     fig, axs = plt.subplots(3, 3, figsize=(18, 15))
#
#     # 1 Trend roczny
#     yearly = df.groupby("year").size()
#     axs[0,0].plot(yearly.index, yearly.values, marker="o")
#     axs[0,0].set_title("Crime Trend by Year")
#
#     # 2 Miesiące
#     monthly = df.groupby("month").size()
#     axs[0,1].plot(monthly.index, monthly.values)
#     axs[0,1].set_title("Crime by Month")
#
#     # 3 Dzień tygodnia
#     day_counts = df["day_of_week"].value_counts()
#     axs[0,2].bar(day_counts.index, day_counts.values)
#     axs[0,2].tick_params(axis='x', rotation=45)
#     axs[0,2].set_title("Crime by Day")
#
#     # 4 Godzina
#     hour_counts = df.groupby("hour").size()
#     axs[1,0].plot(hour_counts.index, hour_counts.values)
#     axs[1,0].set_title("Crime by Hour")
#
#     # 5 Top obszary
#     top_areas = df["AREA NAME"].value_counts().head(5)
#     axs[1,1].bar(top_areas.index, top_areas.values)
#     axs[1,1].tick_params(axis='x', rotation=45)
#     axs[1,1].set_title("Top 5 Areas")
#
#     # 6 Top przestępstwa
#     top_crimes = df["Crm Cd Desc"].value_counts().head(5)
#     axs[1,2].barh(top_crimes.index, top_crimes.values)
#     axs[1,2].set_title("Top 5 Crime Types")
#
#     # 7 Wiek ofiar
#     axs[2,0].hist(df["Vict Age"], bins=30)
#     axs[2,0].set_title("Victim Age Distribution")
#
#     # 8 Płeć ofiar
#     if "Vict Sex" in df.columns:
#         gender = df["Vict Sex"].value_counts()
#         axs[2,1].pie(gender.values, labels=gender.index, autopct="%1.1f%%")
#         axs[2,1].set_title("Victim Gender")
#
#     # 9 Heatmapa miesiąc vs rok
#     pivot = df.pivot_table(index="month", columns="year", aggfunc="size")
#     im = axs[2,2].imshow(pivot, aspect="auto")
#     axs[2,2].set_title("Heatmap Month vs Year")
#     fig.colorbar(im, ax=axs[2,2])
#
#     plt.tight_layout()
#     plt.show()
#
#
# # =========================
# # MACHINE LEARNING
# # =========================
#
# def machine_learning(df):
#
#     features = df[["hour", "month", "Vict Age"]]
#     target = df["is_weekend"]
#
#     X_train, X_test, y_train, y_test = train_test_split(
#         features, target, test_size=0.3, random_state=42
#     )
#
#     model = LogisticRegression(max_iter=1000)
#     model.fit(X_train, y_train)
#
#     predictions = model.predict(X_test)
#
#     print("\n=== MACHINE LEARNING RESULTS ===")
#     print("Accuracy:", accuracy_score(y_test, predictions))
#     print("\nClassification Report:\n")
#     print(classification_report(y_test, predictions))
#
#
# # =========================
# # MAIN
# # =========================
#
# def main():
#
#     df = load_data()
#     df = prepare_data(df)
#
#     dashboard(df)
#     machine_learning(df)
#
#
# if __name__ == "__main__":
#     main()

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score, mean_absolute_error
# import warnings
# from pmdarima import auto_arima
# from statsmodels.tsa.statespace.sarimax import SARIMAX
#
# plt.style.use("seaborn-v0_8")
#
# # =========================#
# # 1. Wczytanie danych      #
# # =========================#
#
# def load_data():
#     try:
#         df = pd.read_csv("Crime_Data_from_2020_to_2024.csv")
#         print("Plik wczytany poprawnie.")
#         return df
#     except FileNotFoundError:
#         print("Nie znaleziono pliku CSV.")
#         exit()
#
# # =========================#
# # 2. Czyszczenie danych    #
# # =========================#
#
# def clean_data(df):
#     df = df.drop_duplicates()
#     df["DATE OCC"] = pd.to_datetime(
#         df["DATE OCC"],
#         format="%m/%d/%Y %I:%M:%S %p",
#         errors="coerce"
#     )
#     df = df.dropna(subset=["DATE OCC"])
#     return df
#
# # =========================#
# # 3. Feature Engineering   #
# # =========================#
#
# def feature_engineering(df):
#     df["year"] = df["DATE OCC"].dt.year
#     df["month"] = df["DATE OCC"].dt.month
#     df["year_month"] = df["DATE OCC"].dt.to_period("M").astype(str)
#     df["day_of_week"] = df["DATE OCC"].dt.day_name()
#     df["TIME OCC"] = df["TIME OCC"].astype(str).str.zfill(4)
#     df["hour"] = df["TIME OCC"].str[:2].astype(int)
#     return df
#
# # =========================#
# # 4. Trend roczny          #
# # =========================#
#
# def yearly_trend(df):
#     trend = df.groupby("year").size()
#     plt.figure(figsize=(10,6))
#     plt.plot(trend.index, trend.values, marker="o", linewidth=3)
#     plt.title("Trend przestępczości według lat")
#     plt.xlabel("Rok")
#     plt.ylabel("Liczba przestępstw")
#     plt.grid(True)
#     plt.show()
#
# # =========================#
# # 5. Trend miesięczny      #
# # =========================#
#
# def monthly_trend(df):
#     trend = df.groupby("year_month").size()
#     plt.figure(figsize=(12,6))
#     plt.plot(trend.index, trend.values)
#     plt.xticks(rotation=90)
#     plt.title("Trend przestępczości według miesięcy")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Liczba przestępstw")
#     plt.tight_layout()
#     plt.show()
#
# # ===============================#
# # 6. Przestępstwa według godziny #
# # ===============================#
#
# def crime_by_hour(df):
#     hourly = df.groupby("hour").size()
#     full_hours = pd.Series(0, index=range(24))
#     hourly = full_hours.add(hourly, fill_value=0)
#     plt.figure(figsize=(10,6))
#     plt.bar(hourly.index, hourly.values, width=0.6)
#     plt.xticks(range(24))
#     plt.title("Liczba przestępstw w zależności od godziny")
#     plt.xlabel("Godzina (0–23)")
#     plt.ylabel("Liczba przestępstw")
#     plt.grid(axis="y", linestyle="--", alpha=0.5)
#     plt.show()
#     # Początkowo mega nakładały się na siebie godziny i wychodziło jednolite
#
# # =========================#
# # 7. Top 10 obszarów       #
# # =========================#
#
# def crime_by_area(df):
#     area_counts = df["AREA NAME"].value_counts().head(10)
#     plt.figure(figsize=(10,6))
#     plt.bar(area_counts.index, area_counts.values)
#     plt.xticks(rotation=45)
#     plt.title("10 obszarów z największą liczbą przestępstw")
#     plt.xlabel("Obszar")
#     plt.ylabel("Liczba przestępstw")
#     plt.tight_layout()
#     plt.show()
#
# # ============================#
# # 8. Top 10 typów przestępstw #
# # ============================#
#
# def top_crimes(df):
#     crime_counts = df["Crm Cd Desc"].value_counts().head(10)
#     plt.figure(figsize=(10,6))
#     plt.barh(crime_counts.index, crime_counts.values)
#     plt.gca().invert_yaxis()
#     plt.title("10 najczęstszych typów przestępstw")
#     plt.xlabel("Liczba przestępstw")
#     plt.ylabel("Rodzaj przestępstwa")
#     plt.tight_layout()
#     plt.show()
#
# # =====================================#
# # 9. Prognoza miesięczna (SARIMA auto) #
# # =====================================#
#
# def forecast_crime_monthly(df):
#     warnings.filterwarnings("ignore", category=UserWarning)
#
#     monthly = df.groupby("year_month").size()
#     monthly.index = pd.to_datetime(monthly.index)
#     monthly = monthly.asfreq("MS", fill_value=0)
#
#     split_index = int(len(monthly) * 0.8)
#     train = monthly[:split_index]
#     test = monthly[split_index:]
#
#     #  Automatyczny dobór parametrów SARIMA
#     sarima_model = auto_arima(
#         train,
#         seasonal=True,
#         m=12,
#         stepwise=True,
#         suppress_warnings=True,
#         trace=False,
#         error_action='ignore'
#     )
#
#     print(f"Wybrane parametry SARIMA: {sarima_model.order}, {sarima_model.seasonal_order}")
#
#     # Dopasowanie SARIMA z wybranymi parametrami
#     model = SARIMAX(
#         train,
#         order=sarima_model.order,
#         seasonal_order=sarima_model.seasonal_order,
#         enforce_stationarity=False,
#         enforce_invertibility=False
#     )
#     results = model.fit(disp=False)
#
#     # Predykcja testowa (dynamic=False = używa prawdziwych danych)
#     forecast_test = results.get_prediction(start=test.index[0], end=test.index[-1], dynamic=False)
#     forecast_test_mean = forecast_test.predicted_mean
#
#     # Prognoza przyszła 6 miesięcy
#     future_forecast = results.forecast(steps=6)
#     future_index = pd.date_range(
#         start=monthly.index[-1] + pd.offsets.MonthBegin(),
#         periods=6, freq='MS'
#     )
#
#     # Metryki jakości
#     r2 = r2_score(test, forecast_test_mean)
#     mae = mean_absolute_error(test, forecast_test_mean)
#
#     print("\n===== JAKOŚĆ MODELU SARIMA =====")
#     print(f"Współczynnik R2: {r2:.4f}")
#     print(f"Średni błąd bezwzględny (MAE): {mae:.2f}")
#     print("=================================\n")
#     # Jak narazie nie wychodziły dobre dane gorzej przewiduje niż średnia chyba mało danych.
#     # Biblioteka Prophet tez nie pomogła
#
#
#
#     # Wykres chronologiczny
#     plt.figure(figsize=(14,6))
#     plt.plot(monthly, label="Dane historyczne", color="blue")
#     plt.plot(forecast_test_mean, label="Predykcja testowa", color="orange")
#     plt.plot(future_index, future_forecast, label="Prognoza na 6 miesięcy", color="green")
#     plt.xlabel("Data")
#     plt.ylabel("Liczba przestępstw")
#     plt.title("Prognoza liczby przestępstw (model SARIMA auto)")
#     plt.legend()
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
#
#
# # =========================#
# # MAIN                     #
# # =========================#
#
# def main():
#     df = load_data()
#     df = clean_data(df)
#     df = feature_engineering(df)
#
#     yearly_trend(df)
#     monthly_trend(df)
#     crime_by_hour(df)
#     crime_by_area(df)
#     top_crimes(df)
#     forecast_crime_monthly(df)
#
# if __name__ == "__main__":
#     main()

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score, mean_absolute_error
# import warnings
# from pmdarima import auto_arima
# from statsmodels.tsa.statespace.sarimax import SARIMAX
#
# plt.style.use("seaborn-v0_8")
#
# # =========================#
# # 1. Wczytanie danych      #
# # =========================#
#
# def load_data():
#     try:
#         df = pd.read_csv("Crime_Data_from_2020_to_2024.csv")
#         print("Plik wczytany poprawnie.")
#         return df
#     except FileNotFoundError:
#         print("Nie znaleziono pliku CSV.")
#         exit()
#
# # =========================#
# # 2. Czyszczenie danych    #
# # =========================#
#
# def clean_data(df):
#     df = df.drop_duplicates()
#     df["DATE OCC"] = pd.to_datetime(
#         df["DATE OCC"],
#         format="%m/%d/%Y %I:%M:%S %p",
#         errors="coerce"
#     )
#     df = df.dropna(subset=["DATE OCC"])
#     return df
#
# # =========================#
# # 3. Feature Engineering   #
# # =========================#
#
# def feature_engineering(df):
#     df["year"] = df["DATE OCC"].dt.year
#     df["month"] = df["DATE OCC"].dt.month
#     df["year_month"] = df["DATE OCC"].dt.to_period("M").astype(str)
#     df["year_month_dt"] = df["DATE OCC"].dt.to_period("M").dt.to_timestamp()
#     df["day_of_week"] = df["DATE OCC"].dt.day_name()
#     df["TIME OCC"] = df["TIME OCC"].astype(str).str.zfill(4)
#     df["hour"] = df["TIME OCC"].str[:2].astype(int)
#     df["is_weekend"] = df["DATE OCC"].dt.weekday >= 5
#     return df
#
# # =========================#
# # 4. Trend roczny (TOP 5)  #
# # =========================#
#
# def yearly_trend(df):
#     top_types = df["Crm Cd Desc"].value_counts().head(5).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#     yearly_type = df_top.groupby(["year", "Crm Cd Desc"]).size().unstack(fill_value=0)
#
#     yearly_type.plot(kind="bar", stacked=True, figsize=(12,7))
#     plt.title("Trend roczny przestępczości (TOP 5 typów)")
#     plt.xlabel("Rok")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(title="Typ przestępstwa", bbox_to_anchor=(1.05, 1))
#     plt.xticks(rotation=0)
#     plt.tight_layout()
#     plt.show()
#
# # =========================#
# # 5. Trend miesięczny      #
# # =========================#
#
# def monthly_trend(df):
#     top_types = df["Crm Cd Desc"].value_counts().head(3).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#
#     monthly_type = df_top.groupby(["year_month_dt", "Crm Cd Desc"]).size().unstack(fill_value=0)
#
#     plt.figure(figsize=(14,6))
#     for col in monthly_type.columns:
#         plt.plot(monthly_type.index, monthly_type[col], label=col)
#
#     plt.title("Trend miesięczny (TOP 3 typy przestępstw)")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend()
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
#
#     # Porównanie miesiąc do miesiąca
#     monthly_total = df.groupby("year_month_dt").size()
#     mom_change = monthly_total.diff()
#
#     plt.figure(figsize=(14,6))
#     plt.bar(mom_change.index, mom_change.values)
#     plt.title("Zmiana liczby przestępstw miesiąc do miesiąca")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Różnica względem poprzedniego miesiąca")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
#
# # ===============================#
# # 6. Godzina + weekend vs robocze#
# # ===============================#
#
# def crime_by_hour(df):
#     hourly_week = df[df["is_weekend"] == False].groupby("hour").size()
#     hourly_weekend = df[df["is_weekend"] == True].groupby("hour").size()
#
#     full_hours = pd.Series(0, index=range(24))
#     hourly_week = full_hours.add(hourly_week, fill_value=0)
#     hourly_weekend = full_hours.add(hourly_weekend, fill_value=0)
#
#     plt.figure(figsize=(12,6))
#     plt.plot(hourly_week.index, hourly_week.values, label="Dni robocze")
#     plt.plot(hourly_weekend.index, hourly_weekend.values, label="Weekend")
#
#     plt.title("Przestępstwa według godziny (dni robocze vs weekend)")
#     plt.xlabel("Godzina")
#     plt.ylabel("Liczba przestępstw")
#     plt.xticks(range(24))
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
# # =========================#
# # 7. Porównanie rok do roku#
# # =========================#
#
# def crime_by_area(df):
#     yearly = df.groupby("year").size()
#     yoy = yearly.pct_change() * 100
#
#     fig, ax1 = plt.subplots(figsize=(10,6))
#
#     ax1.bar(yearly.index, yearly.values)
#     ax1.set_xlabel("Rok")
#     ax1.set_ylabel("Liczba przestępstw")
#
#     ax2 = ax1.twinx()
#     ax2.plot(yoy.index, yoy.values, marker="o")
#     ax2.set_ylabel("Zmiana % rok do roku")
#
#     plt.title("Porównanie rok do roku (YoY)")
#     plt.tight_layout()
#     plt.show()
#
# # ============================#
# # 8. Główne kategorie         #
# # ============================#
#
# def top_crimes(df):
#     def categorize(crime):
#         crime = str(crime).lower()
#         if "burglary" in crime:
#             return "Burglary"
#         elif "theft" in crime:
#             return "Theft"
#         elif "assault" in crime:
#             return "Assault"
#         elif "vehicle" in crime:
#             return "Vehicle Crime"
#         else:
#             return "Other"
#
#     df["Category"] = df["Crm Cd Desc"].apply(categorize)
#     category_counts = df["Category"].value_counts()
#
#     plt.figure(figsize=(10,6))
#     plt.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%")
#     plt.title("Główne kategorie przestępstw")
#     plt.show()
#
# # =====================================#
# # 9. Prognoza miesięczna (SARIMA auto) #
# # =====================================#
#
# def forecast_crime_monthly(df):
#     warnings.filterwarnings("ignore", category=UserWarning)
#
#     monthly = df.groupby("year_month").size()
#     monthly.index = pd.to_datetime(monthly.index)
#     monthly = monthly.asfreq("MS", fill_value=0)
#
#     split_index = int(len(monthly) * 0.8)
#     train = monthly[:split_index]
#     test = monthly[split_index:]
#
#     sarima_model = auto_arima(
#         train,
#         seasonal=True,
#         m=12,
#         stepwise=True,
#         suppress_warnings=True,
#         trace=False,
#         error_action='ignore'
#     )
#
#     print(f"Wybrane parametry SARIMA: {sarima_model.order}, {sarima_model.seasonal_order}")
#
#     model = SARIMAX(
#         train,
#         order=sarima_model.order,
#         seasonal_order=sarima_model.seasonal_order,
#         enforce_stationarity=False,
#         enforce_invertibility=False
#     )
#
#     results = model.fit(disp=False)
#
#     forecast_test = results.get_prediction(start=test.index[0], end=test.index[-1], dynamic=False)
#     forecast_test_mean = forecast_test.predicted_mean
#
#     future_forecast = results.forecast(steps=6)
#     future_index = pd.date_range(
#         start=monthly.index[-1] + pd.offsets.MonthBegin(),
#         periods=6, freq='MS'
#     )
#
#     r2 = r2_score(test, forecast_test_mean)
#     mae = mean_absolute_error(test, forecast_test_mean)
#
#     print("\n===== JAKOŚĆ MODELU SARIMA =====")
#     print(f"Współczynnik R2: {r2:.4f}")
#     print(f"Średni błąd bezwzględny (MAE): {mae:.2f}")
#     print("=================================\n")
#
#     plt.figure(figsize=(14,6))
#     plt.plot(monthly, label="Dane historyczne")
#     plt.plot(forecast_test_mean, label="Predykcja testowa")
#     plt.plot(future_index, future_forecast, label="Prognoza na 6 miesięcy")
#     plt.xlabel("Data")
#     plt.ylabel("Liczba przestępstw")
#     plt.title("Prognoza liczby przestępstw (model SARIMA auto)")
#     plt.legend()
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
#
# # =========================#
# # MAIN                     #
# # =========================#
#
# def main():
#     df = load_data()
#     df = clean_data(df)
#     df = feature_engineering(df)
#
#     yearly_trend(df)
#     monthly_trend(df)
#     crime_by_hour(df)
#     crime_by_area(df)
#     top_crimes(df)
#     forecast_crime_monthly(df)
#
# if __name__ == "__main__":
#     main()

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score, mean_absolute_error
# import warnings
# from pmdarima import auto_arima
# from statsmodels.tsa.statespace.sarimax import SARIMAX
# import numpy as np
#
# plt.style.use("seaborn-v0_8")
#
# # =========================#
# # 1. Wczytanie danych      #
# # =========================#
#
# def load_data():
#     try:
#         df = pd.read_csv("Crime_Data_from_2020_to_2024.csv")
#         print("Plik wczytany poprawnie.")
#         return df
#     except FileNotFoundError:
#         print("Nie znaleziono pliku CSV.")
#         exit()
#
# # =========================#
# # 2. Czyszczenie danych    #
# # =========================#
#
# def clean_data(df):
#     df = df.drop_duplicates()
#     df["DATE OCC"] = pd.to_datetime(
#         df["DATE OCC"],
#         format="%m/%d/%Y %I:%M:%S %p",
#         errors="coerce"
#     )
#     df = df.dropna(subset=["DATE OCC"])
#     return df
#
# # =========================#
# # 3. Feature Engineering   #
# # =========================#
#
# def feature_engineering(df):
#     df["year"] = df["DATE OCC"].dt.year
#     df["month"] = df["DATE OCC"].dt.month
#     df["month_name"] = df["DATE OCC"].dt.strftime("%b")
#     df["year_month"] = df["DATE OCC"].dt.to_period("M").astype(str)
#     df["year_month_dt"] = df["DATE OCC"].dt.to_period("M").dt.to_timestamp()
#     df["TIME OCC"] = df["TIME OCC"].astype(str).str.zfill(4)
#     df["hour"] = df["TIME OCC"].str[:2].astype(int)
#     df["is_weekend"] = df["DATE OCC"].dt.weekday >= 5
#     return df
#
# # =========================#
# # 4. Trend roczny (TOP 15) #
# # =========================#
#
# def yearly_trend(df):
#     top_types = df["Crm Cd Desc"].value_counts().head(15).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#     yearly_type = df_top.groupby(["year", "Crm Cd Desc"]).size().unstack(fill_value=0)
#
#     colors = plt.cm.tab20.colors[:15]
#
#     yearly_type.plot(kind="bar", stacked=True, figsize=(14,8), color=colors)
#     plt.title("Trend roczny (TOP 15 typów)")
#     plt.xlabel("Rok")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(bbox_to_anchor=(1.05,1))
#     plt.xticks(rotation=0)
#     plt.tight_layout()
#     plt.show()
#
# # =========================#
# # 5. Trend miesięczny (TOP 7)
# # =========================#
#
# def monthly_trend(df):
#     top_types = df["Crm Cd Desc"].value_counts().head(7).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#     monthly_type = df_top.groupby(["year_month_dt", "Crm Cd Desc"]).size().unstack(fill_value=0)
#
#     colors = plt.cm.Set2.colors
#
#     plt.figure(figsize=(15,7))
#     for i, col in enumerate(monthly_type.columns):
#         plt.plot(monthly_type.index, monthly_type[col],
#                  label=col, color=colors[i], linewidth=2)
#
#     plt.title("Trend miesięczny (TOP 7)")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(bbox_to_anchor=(1.05,1))
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
#
# # =========================#
# # 6. Miesiąc do miesiąca  #
# # =========================#
#
# def month_comparison(df):
#     monthly_year = df.groupby(["year", "month"]).size().unstack(fill_value=0)
#     monthly_year = monthly_year.reindex(columns=range(1,13))
#
#     months = ["Sty","Lut","Mar","Kwi","Maj","Cze",
#               "Lip","Sie","Wrz","Paź","Lis","Gru"]
#
#     plt.figure(figsize=(14,7))
#
#     for year in monthly_year.index:
#         plt.plot(months,
#                  monthly_year.loc[year],
#                  marker="o",
#                  linewidth=2,
#                  label=str(year))
#
#     plt.title("Porównanie miesięcy z podziałem na lata")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(title="Rok")
#     plt.grid(True)
#     plt.show()
#
# # ===============================#
# # 7. Przestępstwa na godzinę    #
# # ===============================#
#
# def crime_by_hour(df):
#     hourly_year = df.groupby(["year", "hour"]).size().unstack(fill_value=0)
#     hourly_year = hourly_year.reindex(columns=range(24), fill_value=0)
#
#     plt.figure(figsize=(14,7))
#
#     for year in hourly_year.index:
#         plt.plot(hourly_year.columns,
#                  hourly_year.loc[year],
#                  linewidth=2,
#                  label=str(year))
#
#     plt.title("Rozkład godzinowy przestępstw z podziałem na lata")
#     plt.xlabel("Godzina")
#     plt.ylabel("Liczba przestępstw")
#     plt.xticks(range(24))
#     plt.legend(title="Rok")
#     plt.grid(True)
#     plt.show()
#
# # =========================#
# # 8. Kategorie (4 kołowe) #
# # =========================#
#
# def top_crimes(df):
#     top10 = df["Crm Cd Desc"].value_counts().head(10)
#
#     subsets = [
#         top10.iloc[0:3],
#         top10.iloc[3:6],
#         top10.iloc[6:8],
#         top10.iloc[8:10]
#     ]
#
#     fig, axes = plt.subplots(2, 2, figsize=(16,12))
#
#     for ax, subset in zip(axes.flatten(), subsets):
#
#         # skrócenie nazw do 30 znaków
#         labels = [label[:30] + "..." if len(label) > 30 else label
#                   for label in subset.index]
#
#         colors = plt.cm.Set3(np.linspace(0, 1, len(subset)))
#
#         wedges, texts, autotexts = ax.pie(
#             subset.values,
#             autopct='%1.1f%%',
#             startangle=90,
#             colors=colors,
#             wedgeprops=dict(width=0.4),
#             pctdistance=0.75
#         )
#
#         # większe procenty
#         for autotext in autotexts:
#             autotext.set_size(11)
#             autotext.set_weight("bold")
#
#         # legenda zamiast etykiet na kole
#         ax.legend(
#             wedges,
#             labels,
#             title="Kategorie",
#             loc="center left",
#             bbox_to_anchor=(1, 0.5)
#         )
#
#         ax.set_title("Struktura kategorii", fontsize=13, weight="bold")
#
#     plt.tight_layout()
#     plt.show()
#
# # =========================#
# # 9. Jeden wykres kołowy  #
# # =========================#
#
# def top_categories_single(df):
#     top15 = df["Crm Cd Desc"].value_counts().head(15)
#
#     colors = plt.cm.tab20(np.linspace(0, 1, len(top15)))
#
#     explode = [0.08 if i == 0 else 0 for i in range(len(top15))]
#
#     plt.figure(figsize=(12,10))
#     wedges, texts, autotexts = plt.pie(
#         top15,
#         labels=top15.index,
#         autopct="%1.1f%%",
#         startangle=140,
#         colors=colors,
#         explode=explode,
#         wedgeprops=dict(width=0.45),
#         pctdistance=0.75
#     )
#
#     for autotext in autotexts:
#         autotext.set_size(11)
#         autotext.set_weight("bold")
#
#     plt.title("TOP 15 kategorii przestępstw", fontsize=16, weight="bold")
#     plt.tight_layout()
#     plt.show()
#
# # =====================================#
# # 10. SARIMA (bez zmian)              #
# # =====================================#
#
# def forecast_crime_monthly(df):
#     warnings.filterwarnings("ignore", category=UserWarning)
#
#     monthly = df.groupby("year_month").size()
#     monthly.index = pd.to_datetime(monthly.index)
#     monthly = monthly.asfreq("MS", fill_value=0)
#
#     split_index = int(len(monthly) * 0.8)
#     train = monthly[:split_index]
#     test = monthly[split_index:]
#
#     sarima_model = auto_arima(train, seasonal=True, m=12,
#                               stepwise=True, suppress_warnings=True)
#
#     model = SARIMAX(train,
#                     order=sarima_model.order,
#                     seasonal_order=sarima_model.seasonal_order,
#                     enforce_stationarity=False,
#                     enforce_invertibility=False)
#
#     results = model.fit(disp=False)
#
#     forecast_test = results.get_prediction(start=test.index[0],
#                                            end=test.index[-1],
#                                            dynamic=False)
#
#     forecast_test_mean = forecast_test.predicted_mean
#     future_forecast = results.forecast(steps=6)
#     future_index = pd.date_range(
#         start=monthly.index[-1] + pd.offsets.MonthBegin(),
#         periods=6, freq='MS'
#     )
#
#     r2 = r2_score(test, forecast_test_mean)
#     mae = mean_absolute_error(test, forecast_test_mean)
#
#     print("\n===== JAKOŚĆ MODELU SARIMA =====")
#     print(f"Współczynnik R2: {r2:.4f}")
#     print(f"Średni błąd bezwzględny (MAE): {mae:.2f}")
#     print("=================================\n")
#
#     plt.figure(figsize=(14,6))
#     plt.plot(monthly, label="Dane historyczne")
#     plt.plot(forecast_test_mean, label="Predykcja testowa")
#     plt.plot(future_index, future_forecast, label="Prognoza na 6 miesięcy")
#     plt.legend()
#     plt.title("Prognoza liczby przestępstw (SARIMA)")
#     plt.grid(True)
#     plt.show()
#
# # =========================#
# # MAIN                     #
# # =========================#
#
# def main():
#     df = load_data()
#     df = clean_data(df)
#     df = feature_engineering(df)
#
#     yearly_trend(df)
#     monthly_trend(df)
#     month_comparison(df)
#     crime_by_hour(df)
#     top_crimes(df)
#     top_categories_single(df)
#     forecast_crime_monthly(df)
#
# if __name__ == "__main__":
#     main()

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score, mean_absolute_error
# import warnings
# from pmdarima import auto_arima
# from statsmodels.tsa.statespace.sarimax import SARIMAX
# import numpy as np
#
# plt.style.use("seaborn-v0_8")
#
# # =========================#
# # 1. Wczytanie danych      #
# # =========================#
#
# def load_data():
#     try:
#         df = pd.read_csv("Crime_Data_from_2020_to_2024.csv")
#         print("Plik wczytany poprawnie.")
#         return df
#     except FileNotFoundError:
#         print("Nie znaleziono pliku CSV.")
#         exit()
#
# # =========================#
# # 2. Czyszczenie danych    #
# # =========================#
#
# def clean_data(df):
#     df = df.drop_duplicates()
#     df["DATE OCC"] = pd.to_datetime(
#         df["DATE OCC"],
#         format="%m/%d/%Y %I:%M:%S %p",
#         errors="coerce"
#     )
#     df = df.dropna(subset=["DATE OCC"])
#     return df
#
# # =========================#
# # 3. Feature Engineering   #
# # =========================#
#
# def feature_engineering(df):
#     df["year"] = df["DATE OCC"].dt.year
#     df["month"] = df["DATE OCC"].dt.month
#     df["month_name"] = df["DATE OCC"].dt.strftime("%b")
#     df["year_month"] = df["DATE OCC"].dt.to_period("M").astype(str)
#     df["year_month_dt"] = df["DATE OCC"].dt.to_period("M").dt.to_timestamp()
#     df["TIME OCC"] = df["TIME OCC"].astype(str).str.zfill(4)
#     df["hour"] = df["TIME OCC"].str[:2].astype(int)
#     df["is_weekend"] = df["DATE OCC"].dt.weekday >= 5
#     return df
#
# # =========================#
# # 4. Trend roczny (TOP 15) #
# # =========================#
#
# def yearly_trend(df):
#     top_types = df["Crm Cd Desc"].value_counts().head(15).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#     yearly_type = df_top.groupby(["year", "Crm Cd Desc"]).size().unstack(fill_value=0)
#
#     colors = plt.cm.tab20.colors[:15]
#
#     yearly_type.plot(kind="bar", stacked=True, figsize=(14,8), color=colors)
#     plt.title("Trend roczny (TOP 15 typów)")
#     plt.xlabel("Rok")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(bbox_to_anchor=(1.05,1))
#     plt.xticks(rotation=0)
#     plt.tight_layout()
#     plt.show()
#
# # =========================#
# # 5. Trend miesięczny (TOP 7)
# # =========================#
#
# def monthly_trend(df):
#     top_types = df["Crm Cd Desc"].value_counts().head(7).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#     monthly_type = df_top.groupby(["year_month_dt", "Crm Cd Desc"]).size().unstack(fill_value=0)
#
#     colors = plt.cm.Set2.colors
#
#     plt.figure(figsize=(15,7))
#     for i, col in enumerate(monthly_type.columns):
#         plt.plot(monthly_type.index, monthly_type[col],
#                  label=col, color=colors[i], linewidth=2)
#
#     plt.title("Trend miesięczny (TOP 7)")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(bbox_to_anchor=(1.05,1))
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
#
# # =========================#
# # 6. Miesiąc do miesiąca  #
# # =========================#
#
# def month_comparison(df):
#     monthly_year = df.groupby(["year", "month"]).size().unstack(fill_value=0)
#     monthly_year = monthly_year.reindex(columns=range(1,13))
#
#     months = ["Sty","Lut","Mar","Kwi","Maj","Cze",
#               "Lip","Sie","Wrz","Paź","Lis","Gru"]
#
#     plt.figure(figsize=(14,7))
#
#     for year in monthly_year.index:
#         plt.plot(months,
#                  monthly_year.loc[year],
#                  marker="o",
#                  linewidth=2,
#                  label=str(year))
#
#     plt.title("Porównanie miesięcy z podziałem na lata")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(title="Rok")
#     plt.grid(True)
#     plt.show()
#
# # ===============================#
# # 7. Dni robocze vs weekend     #
# # ===============================#
#
# def crime_by_hour(df):
#     hourly_week = df[df["is_weekend"] == False].groupby("hour").size()
#     hourly_weekend = df[df["is_weekend"] == True].groupby("hour").size()
#
#     full_hours = pd.Series(0, index=range(24))
#     hourly_week = full_hours.add(hourly_week, fill_value=0)
#     hourly_weekend = full_hours.add(hourly_weekend, fill_value=0)
#
#     plt.figure(figsize=(12,6))
#     plt.plot(hourly_week.index, hourly_week.values, label="Dni robocze", linewidth=3)
#     plt.plot(hourly_weekend.index, hourly_weekend.values, label="Weekend", linewidth=3)
#
#     plt.title("Dni robocze vs weekend (godzinowo)")
#     plt.xlabel("Godzina")
#     plt.ylabel("Liczba przestępstw")
#     plt.xticks(range(24))
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
#
# # =========================#
# # 9. Jeden wykres kołowy  #
# # =========================#
#
# def top_categories_single(df):
#     top10 = df["Crm Cd Desc"].value_counts().head(10)
#
#     colors = plt.cm.tab10(np.linspace(0, 1, len(top10)))
#
#     explode = [0.08 if i == 0 else 0 for i in range(len(top10))]
#
#     plt.figure(figsize=(10,8))
#     wedges, texts, autotexts = plt.pie(
#         top10,
#         labels=top10.index,
#         autopct="%1.1f%%",
#         startangle=140,
#         colors=colors,
#         explode=explode,
#         wedgeprops=dict(width=0.45),
#         pctdistance=0.75
#     )
#
#     for autotext in autotexts:
#         autotext.set_size(11)
#         autotext.set_weight("bold")
#
#     plt.title("TOP 10 kategorii przestępstw", fontsize=16, weight="bold")
#     plt.tight_layout()
#     plt.show()
#
# # =====================================#
# # 10. SARIMA              #
# # =====================================#
#
# def forecast_crime_monthly(df):
#     warnings.filterwarnings("ignore", category=UserWarning)
#
#     monthly = df.groupby("year_month").size()
#     monthly.index = pd.to_datetime(monthly.index)
#     monthly = monthly.asfreq("MS", fill_value=0)
#
#     split_index = int(len(monthly) * 0.8)
#     train = monthly[:split_index]
#     test = monthly[split_index:]
#
#     sarima_model = auto_arima(train, seasonal=True, m=12,
#                               stepwise=True, suppress_warnings=True)
#
#     model = SARIMAX(train,
#                     order=sarima_model.order,
#                     seasonal_order=sarima_model.seasonal_order,
#                     enforce_stationarity=False,
#                     enforce_invertibility=False)
#
#     results = model.fit(disp=False)
#
#     forecast_test = results.get_prediction(start=test.index[0],
#                                            end=test.index[-1],
#                                            dynamic=False)
#
#     forecast_test_mean = forecast_test.predicted_mean
#     future_forecast = results.forecast(steps=6)
#     future_index = pd.date_range(
#         start=monthly.index[-1] + pd.offsets.MonthBegin(),
#         periods=6, freq='MS'
#     )
#
#     r2 = r2_score(test, forecast_test_mean)
#     mae = mean_absolute_error(test, forecast_test_mean)
#
#     print("\n===== JAKOŚĆ MODELU SARIMA =====")
#     print(f"Współczynnik R2: {r2:.4f}")
#     print(f"Średni błąd bezwzględny (MAE): {mae:.2f}")
#     print("=================================\n")
#
#     plt.figure(figsize=(14,6))
#     plt.plot(monthly, label="Dane historyczne")
#     plt.plot(forecast_test_mean, label="Predykcja testowa")
#     plt.plot(future_index, future_forecast, label="Prognoza na 6 miesięcy")
#     plt.legend()
#     plt.title("Prognoza liczby przestępstw (SARIMA)")
#     plt.grid(True)
#     plt.show()
#
# # =========================#
# # MAIN                     #
# # =========================#
#
# def main():
#     df = load_data()
#     df = clean_data(df)
#     df = feature_engineering(df)
#
#     yearly_trend(df)
#     monthly_trend(df)
#     month_comparison(df)
#     crime_by_hour(df)
#     top_categories_single(df)
#     forecast_crime_monthly(df)
#
# if __name__ == "__main__":
#     main()
# ------------------------------------------------------------------------------------------
# import threading
# import time
# import tkinter as tk
# import math
#
# NUM_PHILOSOPHERS = 5
# RADIUS = 200
# CENTER = 300
# DELAY = 1  # czas w sekundach między etapami
#
# # Semafory (widelce)
# forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]
#
# # Stany filozofów
# states = ["MYŚLI"] * NUM_PHILOSOPHERS
# state_lock = threading.Lock()
#
# # Kolory stanów
# COLORS = {
#     "MYŚLI": "#6CA0DC",
#     "GŁODNY": "#FFA500",
#     "JE": "#90EE90"
# }
#
# # Flagi sterujące
# simulation_running = False
# simulation_paused = False
#
# # Historia stanów do cofania
# history = []
#
#
# def philosopher(index, canvas, philosopher_items):
#     left_fork = index
#     right_fork = (index + 1) % NUM_PHILOSOPHERS
#
#     while simulation_running:
#         while simulation_paused:
#             time.sleep(0.1)
#         step(index, "MYŚLI", canvas, philosopher_items)
#         if not simulation_running: break
#
#         while simulation_paused:
#             time.sleep(0.1)
#         step(index, "GŁODNY", canvas, philosopher_items)
#         if not simulation_running: break
#
#         fork1, fork2 = min(left_fork, right_fork), max(left_fork, right_fork)
#         with forks[fork1]:
#             with forks[fork2]:
#                 while simulation_paused:
#                     time.sleep(0.1)
#                 step(index, "JE", canvas, philosopher_items)
#                 if not simulation_running: break
#
#         while simulation_paused:
#             time.sleep(0.1)
#         step(index, "MYŚLI", canvas, philosopher_items)
#         if not simulation_running: break
#
#
# def step(index, state, canvas, philosopher_items):
#     with state_lock:
#         states[index] = state
#         history.append(states.copy())
#         canvas.after(0, update_visual, index, canvas, philosopher_items)
#         time.sleep(DELAY)
#
#
# def update_visual(index, canvas, philosopher_items):
#     circle, text = philosopher_items[index]
#     canvas.itemconfig(circle, fill=COLORS[states[index]])
#     canvas.itemconfig(text, text=f"{index}\n{states[index]}")
#
#
# def start_simulation(canvas, philosopher_items, start_btn, pause_btn, play_btn, back_btn):
#     global simulation_running, simulation_paused
#     simulation_running = True
#     simulation_paused = False
#     start_btn.config(state="disabled")
#     pause_btn.config(state="normal")
#     play_btn.config(state="disabled")
#     back_btn.config(state="normal")
#
#     for i in range(NUM_PHILOSOPHERS):
#         threading.Thread(target=philosopher, args=(i, canvas, philosopher_items), daemon=True).start()
#
#
# def pause_simulation(pause_btn, play_btn):
#     global simulation_paused
#     simulation_paused = True
#     pause_btn.config(state="disabled")
#     play_btn.config(state="normal")
#
#
# def resume_simulation(pause_btn, play_btn):
#     global simulation_paused
#     simulation_paused = False
#     pause_btn.config(state="normal")
#     play_btn.config(state="disabled")
#
#
# def step_back(canvas, philosopher_items):
#     global history, states
#     if len(history) > 1:
#         history.pop()  # usuń bieżący stan
#         states = history[-1].copy()
#         for i in range(NUM_PHILOSOPHERS):
#             update_visual(i, canvas, philosopher_items)
#
#
# def create_ui():
#     root = tk.Tk()
#     root.title("Ucztujący Filozofowie")
#
#     canvas = tk.Canvas(root, width=600, height=600, bg="#F5F5F5")
#     canvas.pack()
#
#     philosopher_items = []
#
#     for i in range(NUM_PHILOSOPHERS):
#         angle = 2 * math.pi * i / NUM_PHILOSOPHERS
#         x = CENTER + RADIUS * math.cos(angle)
#         y = CENTER + RADIUS * math.sin(angle)
#         circle = canvas.create_oval(x - 40, y - 40, x + 40, y + 40, fill=COLORS["MYŚLI"], outline="black", width=2)
#         text = canvas.create_text(x, y, text=f"{i}\nMYŚLI", font=("Arial", 12, "bold"), fill="black")
#         philosopher_items.append((circle, text))
#
#     for i in range(NUM_PHILOSOPHERS):
#         angle1 = 2 * math.pi * i / NUM_PHILOSOPHERS
#         angle2 = 2 * math.pi * ((i + 1) % NUM_PHILOSOPHERS) / NUM_PHILOSOPHERS
#         x1 = CENTER + (RADIUS - 60) * math.cos(angle1)
#         y1 = CENTER + (RADIUS - 60) * math.sin(angle1)
#         x2 = CENTER + (RADIUS - 60) * math.cos(angle2)
#         y2 = CENTER + (RADIUS - 60) * math.sin(angle2)
#         canvas.create_line(x1, y1, x2, y2, width=4, fill="#333333")
#
#     btn_frame = tk.Frame(root)
#     btn_frame.pack(pady=10)
#
#     start_btn = tk.Button(btn_frame, text="Start", font=("Arial", 12, "bold"))
#     pause_btn = tk.Button(btn_frame, text="Stop", font=("Arial", 12, "bold"), state="disabled")
#     play_btn = tk.Button(btn_frame, text="Play", font=("Arial", 12, "bold"), state="disabled")
#     back_btn = tk.Button(btn_frame, text="Cofnij", font=("Arial", 12, "bold"), state="disabled")
#
#     start_btn.config(command=lambda: start_simulation(canvas, philosopher_items, start_btn, pause_btn, play_btn, back_btn))
#     pause_btn.config(command=lambda: pause_simulation(pause_btn, play_btn))
#     play_btn.config(command=lambda: resume_simulation(pause_btn, play_btn))
#     back_btn.config(command=lambda: step_back(canvas, philosopher_items))
#
#     start_btn.grid(row=0, column=0, padx=5)
#     pause_btn.grid(row=0, column=1, padx=5)
#     play_btn.grid(row=0, column=2, padx=5)
#     back_btn.grid(row=0, column=3, padx=5)
#
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     create_ui()

# import time
# import multiprocessing as mp
# import os
#
# # =========================
# # Wczytywanie danych
# # =========================
# def load_data(filename):
#     if not os.path.exists(filename):
#         print(f"Błąd: plik {filename} nie istnieje!")
#         exit(1)
#
#     with open(filename, "r") as f:
#         return [int(line.strip()) for line in f]
#
#
# # =========================
# # Bubble Sort
# # =========================
# def bubble_sort(arr):
#     a = arr.copy()
#     n = len(a)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a
#
#
# # =========================
# # Merge (scalanie)
# # =========================
# def merge(left, right):
#     result = []
#     i = j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
#
# # =========================
# # Merge wielu części
# # =========================
# def merge_all(parts):
#     while len(parts) > 1:
#         new_parts = []
#         for i in range(0, len(parts), 2):
#             if i + 1 < len(parts):
#                 new_parts.append(merge(parts[i], parts[i + 1]))
#             else:
#                 new_parts.append(parts[i])
#         parts = new_parts
#     return parts[0]
#
#
# # =========================
# # Sortowanie równoległe
# # =========================
# def parallel_sort(data, num_processes):
#     chunk_size = len(data) // num_processes
#     chunks = []
#
#     for i in range(num_processes):
#         start = i * chunk_size
#         end = (i + 1) * chunk_size if i != num_processes - 1 else len(data)
#         chunks.append(data[start:end])
#
#     with mp.Pool(processes=num_processes) as pool:
#         sorted_chunks = pool.map(sorted, chunks)
#
#     return merge_all(sorted_chunks)
#
#
# # =========================
# # Pomiar czasu
# # =========================
# def measure_time(func, *args):
#     start = time.perf_counter()
#     result = func(*args)
#     end = time.perf_counter()
#     return result, end - start
#
#
# # =========================
# # MAIN
# # =========================
# if __name__ == "__main__":
#     mp.freeze_support()  # ważne dla Windows
#
#     filename = "numbers.txt"  # plik musi być w tym samym folderze
#     data = load_data(filename)
#     data = data[:10000] #testy
#
#     print(f"Liczba elementów: {len(data)}")
#
#     # -------- Bubble Sort --------
#     print("\n--- Bubble Sort ---")
#     _, t1 = measure_time(bubble_sort, data)
#     print(f"Czas: {t1:.4f} s")
#
#     # -------- 2 procesy --------
#     print("\n--- 2 procesy ---")
#     _, t2 = measure_time(parallel_sort, data, 2)
#     print(f"Czas: {t2:.4f} s")
#
#     # -------- 3 procesy --------
#     print("\n--- 3 procesy ---")
#     _, t3 = measure_time(parallel_sort, data, 3)
#     print(f"Czas: {t3:.4f} s")
#
#     # -------- 4 procesy --------
#     print("\n--- 4 procesy ---")
#     _, t4 = measure_time(parallel_sort, data, 4)
#     print(f"Czas: {t4:.4f} s")

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score, mean_absolute_error
# import warnings
# from pmdarima import auto_arima
# from statsmodels.tsa.statespace.sarimax import SARIMAX
# import numpy as np
#
# plt.style.use("seaborn-v0_8")
#
# # =========================#
# # 1. Wczytanie danych      #
# # =========================#
#
# def load_data():
#     try:
#         df = pd.read_csv("Crime_Data_from_2020_to_2024.csv")
#         print("Plik wczytany poprawnie.")
#         return df
#     except FileNotFoundError:
#         print("Nie znaleziono pliku CSV.")
#         exit()
#
# # =========================#
# # 2. Czyszczenie danych    #
# # =========================#
#
# def clean_data(df):
#     df = df.drop_duplicates()
#     df["DATE OCC"] = pd.to_datetime(
#         df["DATE OCC"],
#         format="%m/%d/%Y %I:%M:%S %p",
#         errors="coerce"
#     )
#     df = df.dropna(subset=["DATE OCC"])
#     return df
#
# # =========================#
# # 3. Feature Engineering   #
# # =========================#
#
# def feature_engineering(df):
#     df["year"] = df["DATE OCC"].dt.year
#     df["month"] = df["DATE OCC"].dt.month
#     df["month_name"] = df["DATE OCC"].dt.strftime("%b")
#     df["year_month"] = df["DATE OCC"].dt.to_period("M").astype(str)
#     df["year_month_dt"] = df["DATE OCC"].dt.to_period("M").dt.to_timestamp()
#     df["TIME OCC"] = df["TIME OCC"].astype(str).str.zfill(4)
#     df["hour"] = df["TIME OCC"].str[:2].astype(int)
#     df["is_weekend"] = df["DATE OCC"].dt.weekday >= 5
#     return df
#
# # =========================#
# # 4. Trend roczny (TOP 15) #
# # =========================#
#
# def yearly_trend(df):
#     top_types = df["Crm Cd Desc"].value_counts().head(15).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#     yearly_type = df_top.groupby(["year", "Crm Cd Desc"]).size().unstack(fill_value=0)
#
#
#     yearly_percent = yearly_type.div(yearly_type.sum(axis=1), axis=0) * 100
#
#     colors = plt.cm.tab20.colors[:15]
#
#     ax = yearly_type.plot(kind="bar", stacked=True, figsize=(14,8), color=colors)
#
#
#     for i, year in enumerate(yearly_type.index):
#         cumulative = 0
#         for j, col in enumerate(yearly_type.columns):
#             value = yearly_type.loc[year, col]
#             percent = yearly_percent.loc[year, col]
#
#             if value > 0:
#                 for i, year in enumerate(yearly_type.index):
#                     cumulative = 0
#                     for j, col in enumerate(yearly_type.columns):
#                         value = yearly_type.loc[year, col]
#
#                         if value > 0:
#                             ax.text(i, cumulative + value / 2,
#                                     f"{int(value)}",
#                                     ha="center", va="center", fontsize=7)
#
#                         cumulative += value
#
#     plt.title("Trend roczny (TOP 15 typów)")
#     plt.xlabel("Rok")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(bbox_to_anchor=(1.05,1))
#     plt.xticks(rotation=0)
#     plt.tight_layout()
#     plt.show()
#
# # ===========================#
# # 5. Trend miesięczny (SUMA) #
# # ===========================#
#
# def monthly_trend(df):
#     top_types = df["Crm Cd Desc"].value_counts().head(7).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#
#     monthly_type = df_top.groupby(["month", "Crm Cd Desc"]).size().unstack(fill_value=0)
#     monthly_type = monthly_type.reindex(range(1, 13))
#
#     months = ["Sty","Lut","Mar","Kwi","Maj","Cze",
#               "Lip","Sie","Wrz","Paź","Lis","Gru"]
#
#     colors = plt.cm.Set2.colors
#
#     plt.figure(figsize=(14,7))
#
#     for i, col in enumerate(monthly_type.columns):
#         plt.plot(months,
#                  monthly_type[col],
#                  label=col,
#                  color=colors[i],
#                  linewidth=2)
#
#     plt.title("Trend miesięczny (suma ze wszystkich lat)")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
#
# # ======================================#
# # 5b. Trend miesięczny dla każdego roku #
# # ======================================#
#
# def monthly_trend_by_year(df):
#
#     years = [2020, 2021, 2022, 2023, 2024]
#
#     top_types = df["Crm Cd Desc"].value_counts().head(7).index
#     df_top = df[df["Crm Cd Desc"].isin(top_types)]
#
#     months = ["Sty","Lut","Mar","Kwi","Maj","Cze",
#               "Lip","Sie","Wrz","Paź","Lis","Gru"]
#
#     colors = plt.cm.Set2.colors
#
#
#     for year in years:
#         df_year = df_top[df_top["year"] == year]
#
#         print(f"Rok {year} -> rekordy:", len(df_year))
#
#         if df_year.empty:
#             print(f"Brak danych dla {year}")
#             continue
#
#         monthly_type = df_year.groupby(["month", "Crm Cd Desc"]).size().unstack(fill_value=0)
#         monthly_type = monthly_type.reindex(range(1, 13), fill_value=0)
#
#         plt.figure(figsize=(14,7))
#
#         for i, col in enumerate(monthly_type.columns):
#             plt.plot(
#                 months,
#                 monthly_type[col],
#                 label=col,
#                 color=colors[i % len(colors)],
#                 linewidth=2
#             )
#
#         plt.title(f"Trend miesięczny - {year}")
#         plt.xlabel("Miesiąc")
#         plt.ylabel("Liczba przestępstw")
#         plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
#         plt.grid(True)
#         plt.tight_layout()
#
#         plt.show(block=True)
#
# # =========================#
# # 6. Miesiąc do miesiąca   #
# # =========================#
#
# def month_comparison(df):
#     monthly_year = df.groupby(["year", "month"]).size().unstack(fill_value=0)
#     monthly_year = monthly_year.reindex(columns=range(1,13))
#
#     months = ["Sty","Lut","Mar","Kwi","Maj","Cze",
#               "Lip","Sie","Wrz","Paź","Lis","Gru"]
#
#     plt.figure(figsize=(14,7))
#
#     for year in monthly_year.index:
#         plt.plot(months,
#                  monthly_year.loc[year],
#                  marker="o",
#                  linewidth=2,
#                  label=str(year))
#
#     plt.title("Porównanie miesięcy z podziałem na lata")
#     plt.xlabel("Miesiąc")
#     plt.ylabel("Liczba przestępstw")
#     plt.legend(title="Rok")
#     plt.grid(True)
#     plt.show()
#
# # ===============================#
# # 7. Dni robocze vs weekend      #
# # ===============================#
#
# def crime_by_hour(df):
#     hourly_week = df[df["is_weekend"] == False].groupby("hour").size()
#     hourly_weekend = df[df["is_weekend"] == True].groupby("hour").size()
#
#     full_hours = pd.Series(0, index=range(24))
#     hourly_week = full_hours.add(hourly_week, fill_value=0)
#     hourly_weekend = full_hours.add(hourly_weekend, fill_value=0)
#
#     plt.figure(figsize=(12,6))
#     plt.plot(hourly_week.index, hourly_week.values, label="Dni robocze", linewidth=3)
#     plt.plot(hourly_weekend.index, hourly_weekend.values, label="Weekend", linewidth=3)
#
#     plt.title("Dni robocze vs weekend (godzinowo)")
#     plt.xlabel("Godzina")
#     plt.ylabel("Liczba przestępstw")
#     plt.xticks(range(24))
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
#
# # =========================#
# # 8. Jeden wykres kołowy   #
# # =========================#
#
# def top_categories_single(df):
#     top10 = df["Crm Cd Desc"].value_counts().head(10)
#
#     colors = plt.cm.tab10(np.linspace(0, 1, len(top10)))
#
#     explode = [0.08 if i == 0 else 0 for i in range(len(top10))]
#
#     plt.figure(figsize=(10,8))
#     wedges, texts, autotexts = plt.pie(
#         top10,
#         labels=top10.index,
#         autopct="%1.1f%%",
#         startangle=140,
#         colors=colors,
#         explode=explode,
#         wedgeprops=dict(width=0.45),
#         pctdistance=0.75
#     )
#
#     for autotext in autotexts:
#         autotext.set_size(11)
#         autotext.set_weight("bold")
#
#     plt.title("TOP 10 kategorii przestępstw", fontsize=16, weight="bold")
#     plt.tight_layout()
#     plt.show()
#
# # =====================================#
# # 9. SARIMA                            #
# # =====================================#
#
# def forecast_crime_monthly(df):
#     warnings.filterwarnings("ignore", category=UserWarning)
#
#     monthly = df.groupby("year_month").size()
#     monthly.index = pd.to_datetime(monthly.index)
#     monthly = monthly.asfreq("MS", fill_value=0)
#
#     split_index = int(len(monthly) * 0.8)
#     train = monthly[:split_index]
#     test = monthly[split_index:]
#
#     sarima_model = auto_arima(train, seasonal=True, m=12,
#                               stepwise=True, suppress_warnings=True)
#
#     model = SARIMAX(train,
#                     order=sarima_model.order,
#                     seasonal_order=sarima_model.seasonal_order,
#                     enforce_stationarity=False,
#                     enforce_invertibility=False)
#
#     results = model.fit(disp=False)
#
#     forecast_test = results.get_prediction(start=test.index[0],
#                                            end=test.index[-1],
#                                            dynamic=False)
#
#     forecast_test_mean = forecast_test.predicted_mean
#     future_forecast = results.forecast(steps=6)
#     future_index = pd.date_range(
#         start=monthly.index[-1] + pd.offsets.MonthBegin(),
#         periods=6, freq='MS'
#     )
#
#     r2 = r2_score(test, forecast_test_mean)
#     mae = mean_absolute_error(test, forecast_test_mean)
#
#     print("\n===== JAKOŚĆ MODELU SARIMA =====")
#     print(f"Współczynnik R2: {r2:.4f}")
#     print(f"Średni błąd bezwzględny (MAE): {mae:.2f}")
#     print("=================================\n")
#
#     plt.figure(figsize=(14,6))
#     plt.plot(monthly, label="Dane historyczne")
#     plt.plot(forecast_test_mean, label="Predykcja testowa")
#     plt.plot(future_index, future_forecast, label="Prognoza na 6 miesięcy")
#     plt.legend()
#     plt.title("Prognoza liczby przestępstw (SARIMA)")
#     plt.grid(True)
#     plt.show()
#
# # =========================#
# # MAIN                     #
# # =========================#
#
# def main():
#     df = load_data()
#     df = clean_data(df)
#     df = feature_engineering(df)
#
#     yearly_trend(df)
#     monthly_trend(df)
#     monthly_trend_by_year(df)
#     month_comparison(df)
#     crime_by_hour(df)
#     top_categories_single(df)
#     forecast_crime_monthly(df)
#
# if __name__ == "__main__":
#     main()


import threading
import time
import random
import sys
import os

LICZBA = 5

widelce = [threading.Lock() for _ in range(LICZBA)]

lewy = [False] * LICZBA
prawy = [False] * LICZBA
stan = ["m"] * LICZBA
licznik = [0] * LICZBA

print_lock = threading.Lock()


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()


def rysuj():
    with print_lock:
        clear_screen()

        col_w = 6

        def row(cells):
            return "||" + "".join(f"{c:^{col_w}}" for c in cells) + "||"

        naglowek = [f"Fil{i}" for i in range(LICZBA)]

        widok_widelcow = []
        for i in range(LICZBA):
            l = "|" if lewy[i] else "_"
            p = "|" if prawy[i] else "_"
            widok_widelcow.append(f"{l}{p}")

        stany = stan[:]
        liczniki = [str(x) for x in licznik]

        width = 2 + col_w * LICZBA + 2
        linia = "=" * width


        print(linia)
        print(row(naglowek))
        print(row(widok_widelcow))
        print(row(stany))
        print(row(liczniki))
        print(linia, flush=True)

class Filozof(threading.Thread):
    def __init__(self, i):
        super().__init__(daemon=True)
        self.i = i
        self.l = i
        self.p = (i + 1) % LICZBA

    def run(self):
        while True:

            stan[self.i] = "m"
            rysuj()
            time.sleep(random.uniform(0.8, 1.6))


            stan[self.i] = "c"
            with widelce[self.l]:
                lewy[self.i] = True
                rysuj()

                time.sleep(random.uniform(0.2, 0.6))


                with widelce[self.p]:
                    prawy[self.i] = True
                    stan[self.i] = "j"
                    licznik[self.i] += 1
                    rysuj()

                    time.sleep(random.uniform(0.8, 1.6))


                    prawy[self.i] = False


                lewy[self.i] = False
                stan[self.i] = "m"
                rysuj()


for i in range(LICZBA):
    Filozof(i).start()


while True:
    time.sleep(1)