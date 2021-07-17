#capitalize()	Converts the first character to upper case

x = "Alphábet"
print(x.capitalize())

#casefold()	Converts string into lower case

print(x.casefold())

#center()	Returns a centered string

print(x.center(100))

#count()	Returns the number of times a specified value occurs in a string

print(x.count("a"))

#encode()	Returns an encoded version of the string

print(x.encode())

#endswith()	Returns true if the string ends with the specified value

print(x.endswith("t"))

#expandtabs()	Sets the tab size of the string

y="A\tl\tp\th\ta"
print(y.expandtabs(2))

#find()	Searches the string for a specified value and returns the position of where it was found

print(x.find("b"))

#format()	Formats specified values in a string

txt = "For only {price:.0f} dollars!"
print(txt.format(price = 49.49))

#format_map()	Formats specified values in a string

a = {'x':'John', 'y':'Wick'} 
print("{x}'s last name is {y}".format_map(a)) 

#index()	Searches the string for a specified value and returns the position of where it was found

print(x.index("A"))

#isalnum()	Returns True if all characters in the string are alphanumeric

print(x.isalnum())

#isalpha()	Returns True if all characters in the string are in the alphabet

print(x.isalpha())

#isdecimal()	Returns True if all characters in the string are decimals

print(x.isdecimal())

#isdigit()	Returns True if all characters in the string are digits

print(x.isdigit())

#isidentifier()	Returns True if the string is an identifier

print(x.isidentifier())

#islower()	Returns True if all characters in the string are lower case

print(x.islower())

#isnumeric()	Returns True if all characters in the string are numeric

print(x.isnumeric())

#isprintable()	Returns True if all characters in the string are printable

print(x.isprintable())

#isspace()	Returns True if all characters in the string are whitespaces

print(x.isspace())

#istitle()	Returns True if the string follows the rules of a title

print(x.istitle())

#isupper()	Returns True if all characters in the string are upper case

print(x.isupper())

#join()	Joins the elements of an iterable to the end of the string

list1 = ['1','2','3','4']  
s = "-"
s = s.join(list1) 
print(s) 

#ljust()	Returns a left justified version of the string

sample_string="Ant"
print(sample_string.ljust(9,"b"))

#lower()	Converts a string into lower case

print(x.lower())

#lstrip()	Returns a left trim version of the string

print(sample_string.lstrip("A"))

#maketrans()	Returns a translation table to be used in translations

str1 = "wy"
str2 = "gf"
str3 = "u"
trg = "weeksyourweeks"
table = trg.maketrans(str1, str2, str3)
print (trg)

#print (trg.translate(table)) 
#partition()	Returns a tuple where the string is parted into three parts

x = sample_string.partition("n")
print(x)

#replace()	Returns a string where a specified value is replaced with a specified value

print(sample_string.replace("t","a"))

#rfind()	Searches the string for a specified value and returns the last position of where it was found

print(sample_string.rfind("n"))

#rindex()	Searches the string for a specified value and returns the last position of where it was found

print(sample_string.rindex("n"))

#rjust()	Returns a right justified version of the string

print(sample_string.rjust(50," "))

#rpartition()	Returns a tuple where the string is parted into three parts

x = sample_string.rpartition("n")
print(x)

#rsplit()	Splits the string at the specified separator, and returns a list

y = "qwerty"
z = y.rsplit('e')
print(z)

#rstrip()	Returns a right trim version of the string

z = "Mark"
print(z.rstrip("ark"))

#split()	Splits the string at the specified separator, and returns a list

print(z.strip("M"))

#splitlines()	Splits the string at line breaks and returns a list

c = "asdfg\nghjkl"
print(c.splitlines())

#startswith()	Returns true if the string starts with the specified value

print(z.startswith("M"))

#strip()	Returns a trimmed version of the string

q = " 2 ab tyre 68   "
print(q.strip())

#swapcase()	Swaps cases, lower case becomes upper case and vice versa

print(sample_string.swapcase())

#title()	Converts the first character of each word to upper case

print(sample_string.title())

#translate()	Returns a translated string

table = { 119 : 103, 121 : 102, 117 : None } 
  
# target string  

trg = "weeksyourweeks"
print (trg) 
print (trg.translate(table)) 

#upper()	Converts a string into upper case

print(q.upper())

#zfill()	Fills the string with a specified number of 0 values at the beginning

print(z.zfill(10))