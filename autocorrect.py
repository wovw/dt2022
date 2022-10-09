from string import punctuation
import language_tool_python
from multiprocessing import shared_memory, Process
import requests
from matplotlib import test
from numba import jit

# check if words exists in dictionary.com
def __is_word(word):
    return requests.get('https://www.dictionary.com/browse/' + word).status_code != 404

# tool object
tool = language_tool_python.LanguageTool('en-US') 

# checks if word is mostly lowercase (all comics are uppercase to if it contains mostly lowercase, its wrong)
def __is_mostly_lowercase(word):
    lower_count = 0
    for char in word:
        if char.islower() or (not char.islower() and not char.isupper()):
           lower_count += 1
    return lower_count >= len(word) / 2

# runs sentence fixer on multiple threads
def __multithread_fix_sentence(arr, index):
    global tool
    arr[index] = arr[index].replace("\n", " ") 
    arr[index].strip()  
    text_list = arr[index].split()
    for i in range(len(text_list)):
        if(any(char.isdigit() for char in text_list[i]) and (text_list[i].isupper() or text_list[i].islower())):
            text_list[i] = "".join(i for i in text_list[i] if not i.isdigit())
        if "..." not in text_list[i] and __is_mostly_lowercase(text_list[i]):
            text_list[i] = ""
    arr[index] = ' '.join(text_list) 
    matches = tool.check(arr[index])
    while(len(matches) != 0):
        offset = matches[0].offset
        errorLength = matches[0].errorLength
        error_word = arr[index][offset:offset + errorLength]
        if not __is_word(error_word):
            if len(matches[0].replacements) != 0:
                arr[index] = arr[index][0:offset] + (matches[0].replacements)[0] + arr[index][offset + errorLength:]
            break
        if len(matches) == 1:
            break
        matches = tool.check(arr[index])
        
# fixes sentences
def fix_sentence(text_list):
    thread_list = []
    threads = len(text_list)
    shared_list = shared_memory.ShareableList(text_list)

    for i in range(threads):
        thread_list.append(Process(target=__multithread_fix_sentence, args=(shared_list,i)))
        thread_list[-1].start()

    for thread in thread_list:
        thread.join()

    text_list = list(shared_list)
    del shared_list

    for i in range(len(text_list)):
        text_list[i] = text_list[i].strip()
        if len(text_list[i]) == 0:
            text_list.remove(text_list[i])
    return text_list

