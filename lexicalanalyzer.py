f = open("code_file.ceng", "r")

keywords = ["break","case","char","const","do","else","enum","float","for","if","int","double", "long", "struct", "return", "static", "while"]
operators = ["/*", "*/", "++","-","*","/","+","--","==", "<", ">", "<=",">=", "=", "(", ")", "{", "}"]
brackets = ["(", ")", "{", "}"]
stack = []
identifier = "Identifier: "
intConst = "IntConst: "
commentflag = False

def printStack(stack): #prints the stack
    global commentflag
    f = open("code.lex", "a")
    type = defination(stack)
    while len(stack) > 0:
        global comment
        typePOP = type.pop()
        stackPOP = stack.pop()
        if stackPOP == "/*":
            print("Commentline started")
            commentflag = True
            continue
        if commentflag == True:
            if stackPOP == "*/":
                commentflag = False
                print("Commentline finished")
                continue
            continue
        if stackPOP == "Comment":
            print(typePOP, stackPOP)
            f.write(typePOP + stackPOP + "\n")
            comment = True
        if typePOP == '' or stackPOP == '' or stackPOP == '\n':
            continue
        if len(stackPOP) > 1:
            if stackPOP[-1:] == '\n':
                stackPOP = stackPOP[:-1]
        if stackPOP[-1] == ';':
            if typePOP == " ":
                stackPOP = stackPOP[:-1] + "End Of line" 
            else:   
                stackPOP = stackPOP[:-1]
                stack.append("end of line")
                type.append(" ")
                
        if comment is not True:
            f.write(typePOP + stackPOP + "\n")
            print(typePOP, stackPOP)
            
    

def defination(stack): #returns the type of the word
    type = []
    for i in stack:
        if i == '':
            type.append('')
        elif i == "Comment":
            type.append(" ")
        elif i == ';' or i == ";\n":
            type.append(" ")
        elif i in keywords:
            type.append("Keyword: ")
        elif i in operators:
            if i in brackets:
                if i == "(":
                    type.append("leftPar: ")
                elif i == ")":
                    type.append("rightPar: ")
                elif i == "{":
                    type.append("leftCurlyBracket: ")
                elif i == "}":
                    type.append("rightCurlyBracket: ")
            else:
                type.append("Operator: ")
        else:
            if i.isdigit():
                type.append("IntConst: ")
                if len(str(i)) > 10:
                    type.append("ERROR: IntConst is too long")
            else:
                type.append("Identifier: ")
                if len(i) > 25:
                    print("ERROR:  Identifier is too long")

    return type


def check(word): #checks if the word is a keyword or an operator
    stack = []
    if word == '//':
        stack.append("Comment")
        return stack
    for operator in operators:
        if operator in word:
            words = word.split(operator)
            stack.append(words[1])
            stack.append(operator)
            array = check(words[0])
            for i in array:
                stack.append(i)
            break
    if not stack:
        stack.append(word)
    return stack



for line in f.readlines():
    comment = False
    words = line.split(" ") # words dosyadaki her satırının kelime ve operatorlerini ayırıyoruz
    arr = []
    for word in words:
        arr = check(word) # her kelimeyi kontrol ediyoruz
        printStack(arr) # stack'i print ediyoruz



