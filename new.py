import math
def permute(word):
    words = []
    for x in range(math.factorial(len(word))):
        words.append([word[0]])
    
    for x in range(len(words)):
        for y in range(len(word)):
            words[x][x // (y + 1)] = word[x // (y + 1)]
        

        


    
    print(words)

permute("dog")