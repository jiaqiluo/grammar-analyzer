#Jiaqi Luo
#CS311, Program 2

import os, json

def load_in_file():
    filename = raw_input("Enter the filename(eg. test1.json): ")
    if not os.path.isfile(filename):
        print "Error: no such file in current dirctory."
        return load_in_file()
    f = open(filename)
    content = json.load(f)    
    return content
    
def get_description(content):
    if content:
        return content['description']
    else:
        return False
        
def get_grammar(content):
    if content:
        return content['rule']
    else:
        return False

def get_test_string():
    test_string = ''
    while not test_string:
        test_string = raw_input("\nEnter string: ")
    return test_string

def parser(grammar, test_string):
    stack = [] # Ready? 
    stack.append('S') # Go! 
    while len(test_string) != 0:
        if len(stack) == 0:
            return False
        element = stack.pop() 
        if element in grammar:
            index = find(grammar[element], test_string[0])
            if index < 0: 
                return False
            else:
                for i in reversed(grammar[element][index]):
                    stack.append(i)
        else:
            if element == test_string[0]:
                # marked off first char of the testing string
                test_string = test_string[1:len(test_string)]
            else:
                return False
    if len(stack) != 0:
        return False
    else:
        return True

def find(rules, letter):
        index = -1
        for i in range(len(rules)):
            if rules[i][0] == letter:
                index = i
        return index


def main():
    sample = load_in_file()
    print "The grammar is: \n\t\t" + get_description(sample)
    again = True
    while again:
        test_string = get_test_string()
        if parser(get_grammar(sample), test_string):
            print "ACCEPT"
        else:
            print "REJECT"
        response = raw_input("Again(y/n)? ")
        while response not in ['Y', 'y', 'n', 'N']:
            print "Enter 'y' or 'Y' or 'n' or 'N'"
            response = raw_input("Again(y/n)? ") 
        if response in ['n', 'N']:
            again = False
    
if __name__ == "__main__":
    main()
    
