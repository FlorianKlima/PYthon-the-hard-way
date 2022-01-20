message = str.capitalize("hello world")
print(message)

message = "hello world".capitalize()
print(message)

message = "hello world"
print(message.capitalize())

message = "hello world"
print(message.upper())
print(message.lower())
message = message.title()
print(message)
print(message.swapcase())

location = 'Mississippi'
print(location.count('s'))
print(len(location))

message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))
print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

message = 'Morgan is so cute!'
print(message.find('cute'))
print(message.find('M'))
print(message.find('!'))

message = '       SHEEP!       '
print(message.lstrip() + '!')
print(message.rstrip() + '!')
print(message.strip() + '!')

message = 'Morgan is so dumb!'
message = message.replace('dumb', 'cute')
print(message)

message = 'Fuck ya!'
print(message.rjust(20))
print(message.ljust(20))
print(message.center(20))
print(message.rjust(20, '*'))
print(message.ljust(20, '*'))
