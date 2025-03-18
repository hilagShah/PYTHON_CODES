def ispangram(sentence):
    testString = "abcdefghijklmnopqrstuvwxyz"
    x = sentence.lower()
    sentenceSet = set(x)
    for i in testString:
        if i not in sentenceSet:
            return False
            break
    return True
def anotherMethod(sentence):
    z = set()
    a = sentence.lower()
    testString = "abcdefghijklmnopqrstuvwxyz"
    x = set(testString)
    y = set(a)
    z = x-y
    if not z :
        print("IS P")
    else:
        print("IS NOT P")
        
    
sentence = (input("ENTER THE SENTENCE TO BE CHECKED: "))
print(ispangram(sentence))
anotherMethod(sentence)