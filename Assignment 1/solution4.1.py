def reverse(string):
    #split the input string into list of words
    words = string.split()
    #reverse the words and join them
    output = " ".join(reversed(words))
    return output

input=input("Enter the sentence: ")
output = reverse(input)
print(output)