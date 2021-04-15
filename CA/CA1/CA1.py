import string


def listdoc():
    document_list = []  # for file text to string and splitting
    # Splitting documents into list of strings in lowercase
    document_read = open(r"ap_docs.txt", "r").read()  # open file
    document_read = document_read.replace('\n', ' ')  # remove unnecessary characters
    document_read = document_read.lower()  # prevent not finding word based on case-sensitivity

    for ele in document_read:
        if ele in string.punctuation:
            document_read = document_read.replace(ele, "")  # remove punctuation from strings
    document_list = document_read.split('new document')  # indicate separator between documents
    return document_list


def word_dictionary(document_list):
    word_dict = {}
    for x in range(len(document_list)):  # iterate over documents
        temp = document_list[x].split()  # split documents into words
        for y in range(len(temp)):  # iterate over words in current doc
            word = temp[y]  # current word = key
            if word in word_dict.keys():  # add doc number to word in dict
                word_dict[word].add(x)
            else:  # add word and doc number to dict
                set1 = set()  # initialize to an empty set
                word_dict[word] = set1  # add set to dict
                word_dict[word].add(x)  # add document number to key
    return word_dict


def search_words(word_dict2):
    true = 0
    list1 = []
    search_keyword = input("Enter 2+ search keyword(s) without punctuation\n")
    search_keyword = search_keyword.lower()  # match case of document strings
    search_keywords = search_keyword.split()  # split strings entered into individual words
    for i in range(len(search_keywords)):
        for key in word_dict2:
            if search_keywords[i] == key:  # if search word [i] = word in dict
                true = 1  # match found
                print("Word ", i+1, "in documents:")  # display matches
                print(word_dict2.get(key))  # print document numbers from word key
                list1.append(word_dict2.get(key))  # creates list of sets #set for each word
    intersection1 = set()
    for z in range(1, len(list1)):  # find intersection of adjacent sets and add to set to be returned
        set3 = list1[z].intersection(list1[z-1])  # temporarily store intersect values
        intersection1.update(set3)  # add all values of intersection to master set
    if true != 1:
        print("No matches found...\n")

    return intersection1  # return master set


def search_onekeyword(word_dict3):
    true = 0
    search_keyword = input("Enter search keyword without punctuation\n")
    search_keyword = search_keyword.lower()  # match case of document strings
    for key in word_dict3:
        if search_keyword == key:  # if search word = word in dictionary
            true = 1  # match found
            print("Word found in document(s):")
            print(word_dict3.get(key))  # print document numbers from word key
    if true != 1:
        print("No matches found...\n")


program_menu = 0  # for menu selection
document_num = 0  # for reading a selected document

print("Loading...\n\n")  # setting dict takes a whiile on startup


document_list1 = listdoc()
word_dict1 = word_dictionary(document_list1)  # fill up dictionary


while 1:
    # Main Menu
    print("Please choose an option:")
    print("1.	Search for documents")
    print("2.	Read document")
    print("3.	Exit the program")
    program_menu = int(input())

    if program_menu == 1:  # option1 - search
        print("Press 1 for one word search")
        print("Press 2 for multiple word search")
        option1 = int(input())

        if option1 == 1:
            search_onekeyword(word_dict1)
        elif option1 == 2:
            intersection = search_words(word_dict1)  # run multiple word search
            if len(intersection) > 0:  # only print intersection if there is something in set
                print("Documents in common are:\n", intersection)  # print intersection set
            else:
                print("No documents in common\n")
        else:
            print("ERROR:Invalid option entered\n")
    elif program_menu == 2:  # option2 - read
        document_num = int(input("Enter a document number to read:\n"))
        if document_num <= len(document_list1) - 1 and document_num > 0:  # must be within range
            print("Document selected:", document_num)  # show choice
            print("----------------------------------------------")  # separator
            print(document_list1[document_num])  # display document
        else:
            print("ERROR:Document number not within range... \n")
    elif program_menu == 3:  # option3 - quit
        print("Exiting...")
        break
    else:  # invalid input for menu
        print("Please enter a valid option!\n")
