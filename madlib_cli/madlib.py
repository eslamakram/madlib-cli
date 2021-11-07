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
    """Read path and return the data as a giant string."""

    with open(path) as f:
         return f.read()
        

    # try:
    #      file = open(path, 'r')
    #      content = file.read()
    #      file.close()
         
    # except FileNotFoundError:
    #     content = 'The file not found!'

    # finally:
    #     return content

def write_file(path, responses):
    """Write a file back to the given path."""
    with open(path, 'w') as wf:
        return wf.write(responses)


def parse_template(content):

    """
    Parse input for further processing.
        get_keys is called to get the parts of speech to be modified
        remove_keys is called to strip the parts of speech to be replaced
    """
          
    # Get parts of speech to be modified.
    key_list = []
    end = 0

    repetitions = content.count('{')
    for i in range(repetitions):
        start = content.find('{', end) + 1
        end = content.find('}', start)
        key = content[start:end]
        key_list.append(key)

    prompts = key_list

    # Remove the parts of speech from the text for modification.
    regex = r"\{.*?\}"
    stripped = re.sub(regex, '{}', content)

    return prompts, stripped

    # another way by flag
    # word_list=[  ]
    # match_flag = False
    # temp = ""
    
    # for s in content:
    #     # find the trigger { for record but we don't want to save { into out output, thus continue
    #     if s == "{":
    #         match_flag = True
    #         continue

    #     # find the close trigger } so we stop record, append, and re-init
    #     if s == "}":
    #         word_list.append(temp)
    #         match_flag = False
    #         temp = ""
    #         continue

    #     if match_flag:
    #         temp += s

    # return word_list

# def ask_user(word_list):
#     user_story = []
#     for word in word_list:
#         print("Give me a %s !\n" %word)
#         user_story.append(input())
        
#     return user_story



def merge(bare, responses):

    """
     Input:  bare template and a list of user entered language parts
     Output:  a string with the language parts inserted into the template.

    Call the above helper functions to bring it all together.
    First, the prompts are parsed into a more usable format.
    Next, the prompts are presented the user to gather parts of speech.
    Finally, the story is recombined and prepared for display to the user.
    """
    # responses = get_responses(prompts)
    prompts, stripped = parse_template(bare)
    story = stripped.format(*responses)
    return story



def get_responses(prompts):
  # Responses are gathered by the helper function above."""
    responses = []

    for prompt in prompts:
        # User is prompted for specific input based on previously gathered keys.
        # As each response is entered, it is appended into a list to be used later.
    
        if prompt[0] == 'A' or 'I':
        # In case the user is asked for an adjective or interjection
        # Can't help but fix grammar whenever possible
            response = input(f'Enter an {prompt}: ')
            responses.append(response)
        else:
             response = input(f'Enter a {prompt}: ')

    return responses

 
if __name__ == '__main__':
    welcome()
    content = read_template("assets/game_template.txt")
    prompts, stripped = parse_template(content)
    responses = get_responses(prompts)
    story = merge(content,responses)
    write_file('assets/game_story.txt',story) 