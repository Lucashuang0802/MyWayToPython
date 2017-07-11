
# variable
spam = 1
text = "# This is not a comment because it's inside quotes."

# number
num = 8 / 5 # division always return a floating point number
num1 = 8 // 5 # floor divison discards the fractional part
num2 = 5 ** 2 # 5 squared

# string
word = 'does\'t'
word1 = "does't"
s = 'First line.\nSecond line.'  # \n means newline
print(s)
s1 = 3 * 'un' + 'ium' # 3 times 'un', followed by 'ium'
text = ('Put several strings within parentheses ' 'to have them joined together.')
print(text)

s = 'supercalifragilisticexpialidocious'
length = len(s)

# list
cubes = [1, 8, 27, 65, 125]
cubes[3] = 4 ** 3
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
letters[0:2] = [] # remove values
print(letters)

# while-loop
a, b = 0, 1
while b < 10:
	print(b)
	a, b = b, a + b

x = 10
if x < 0:
	x = 0
	print("Negative changed to zero")
elif x == 0:
	print("Zero")
elif x == 1:
	print("Single")
else:
	print('More')



