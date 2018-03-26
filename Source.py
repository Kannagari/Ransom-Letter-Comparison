from collections import Counter
#Counter keeps track of how many times equivalent elements are added.
#By comparing the values of Counter(Ransom) to Counter(magazine)
#we can see if the magazine contained all the needed words to create
#a ransom letter, hence, if its empty, the magazine had what it needed.
#If its not empty. the ransom letter could not be made.
def ransom_note(magazine, ransom):
    return(Counter(ransom) - Counter(magazine)) == {}

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
