f = open("deneme1.ceng", "r")

keywords = ["break","case","char","const","do","else","enum","float","for","if","int","double", "long", "struct", "return", "static", "while"]
operators = ["++","-","*","/","+","--","==", "<", ">", "<=",">=", "="]
stack = []
identifier = "Identifier: "
intConst = "IntConst: "

def printStack(stack):
    type = defination(stack)
    while len(stack) > 0:
        
        typePOP = type.pop()
        stackPOP = stack.pop()
        if typePOP == '' or stackPOP == '':
            continue
        if stackPOP[-1] == ';':
            print(typePOP, stackPOP[:-1])
            print("End of line")
        else:
            print(typePOP, stackPOP) 
            
    

def defination(stack):
    type = []
    for i in stack:
        if i == '':
            type.append('')
        elif i == "/":
            type.append("Comment ")
            stack.clear()
            stack.append(" ")
        elif i in keywords:
            type.append("Keyword: ")
        elif i in operators:
            type.append("Operator: ")
        else:
            type.append("Identifier: ")

    return type


def check(word):
    stack = []
    for operator in operators:
        if operator in word:
            words = word.split(operator)
            stack.append(words[1])
            stack.append(operator)
            #print("words[0]" , words[0])
            array = check(words[0])
            for i in array:
                stack.append(i)
            break
    if not stack:
        stack.append(word)
    return stack



for line in f.readlines():
    words = line.split(" ")
    #print(words)
    arr = []
    for word in words:
        arr = check(word)
        #print(arr)
        printStack(arr)
        '''for i in check(word):
            arr.append(i)'''
    #printStack(arr)
    #printStack(arr)
    #print(arr)


    
#print("words:  " , words)


