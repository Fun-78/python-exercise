'''
def reverse_str(input_sting):
    fragment = [input_sting[i:i+5]for i in range(0, len(input_sting))]
    fragment.reverse()
    reversestr = ''.join(fragment)
    return reversestr
input_sting = 'hello how are you doing'
print(reverse_str(input_sting))
'''

'''
def countCar(string, char):
    return string.count(char)


print(countCar("pineapple juice", "a"))  # Output: 4
print(countCar("Gédéon is already here", "é"))  
'''

'''
def find(string, char):
    try:
        return string.index(char)
    except ValueError:
        return -1

# Test the function with some strings
print(find("Juliet & Romeo", "&"))  # Output: 7
'''


prefixes = 'JKLMNOP'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)