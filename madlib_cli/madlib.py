import re

def welcome():
    wlcMsg = """
        ****************************************
        ******Welcome to the Madlib Game! ******
        *****Please answer about all question***
        *****To quit at any time, type "quit"***
        ****************************************
    """
    print(wlcMsg)



def read_template(path):
    try:
         file = open(path)
    except FileNotFoundError:
        content = 'The file not found!'
    else:
        content = file.read()
        file.close()

    finally:
        return content


def parse_template(content):
     #    "Adjective"*3, "First_Name", "Large_Animal",
                    #    "Small_Animal",
                    #    "Girls_Name",
                    #    "Past_Verb",
                    #    "Plural_Noun",
                    #    "Number",
    word_list=[  ]
    match_flag = False
    temp = ""
    
    for s in content:
        # find the trigger { for record but we don't want to save { into out output, thus continue
        if s == "{":
            match_flag = True
            continue

        # find the close trigger } so we stop record, append, and re-init
        if s == "}":
            word_list.append(temp)
            match_flag = False
            temp = ""
            continue

        if match_flag:
            temp += s
        

    return word_list




def ask_user(word_list):
    user_story = []
    for word in word_list:
        print("Give me a %s !\n" %word)
        user_story.append(input())
        
    return user_story



def merge(bare, userEnteredList):

 """
     Input:  bare template and a list of user entered language parts
     Output:  a string with the language parts inserted into the template.
 """
 template_words = parse_template(bare)
 user_words = userEnteredList

 for tepm, user in zip(template_words,user_words):
     result = re.replace(tepm,user)
     return result

#   with open(new_file, 'w') as f:
#         f.write(content)   

if __name__ == '__main__':
    welcome()
    content = read_template("/home/eslamakram/python-fun/madlib-cli/madlib_cli/assets/game_template.txt")
    word_list = parse_template(content)
    user_story = ask_user(word_list)
    print(merge(content,user_story))