from string import punctuation
import language_tool_python
from multiprocessing import shared_memory, Process
import requests
from matplotlib import test

def is_word(word):
    return requests.get('https://www.dictionary.com/browse/' + word).status_code != 404

tool = language_tool_python.LanguageTool('en-US') 

def is_mostly_lowercase(word):
    lower_count = 0
    for char in word:
        if char.islower() or (not char.islower() and not char.isupper()):
           lower_count += 1
    return lower_count >= len(word) / 2

def multithread_fix_sentence(arr, index):
    global tool
    arr[index] = arr[index].replace("\n", " ") 
    arr[index].strip()  
    text_list = arr[index].split()
    for i in range(len(text_list)):
        if(any(char.isdigit() for char in text_list[i]) and (text_list[i].isupper() or text_list[i].islower())):
            text_list[i] = ''.join(i for i in text_list[i] if not i.isdigit())
        if "..." not in text_list[i] and is_mostly_lowercase(text_list[i]):
            text_list[i] = ''
    arr[index] = ' '.join(text_list) 
    matches = tool.check(arr[index])
    while(len(matches) != 0):
        offset = matches[0].offset
        errorLength = matches[0].errorLength
        error_word = arr[index][offset:offset + errorLength]
        if not is_word(error_word):
            if len(matches[0].replacements) != 0:
                arr[index] = arr[index][0:offset] + (matches[0].replacements)[0] + arr[index][offset + errorLength:]
            break
        if len(matches) == 1:
            break
        matches = tool.check(arr[index])
text_list = ["TO SOLVE THIS EQUATION, WE INVOKE GAUSS'S OPERATOR TO TRANSFORM IT INTO A DRAGON.", "THEN WE SLAY THE DRAGON WITH HILBERT'S ARROW, AND TRANSFORM ITS CORPSE BACK INTO THE SOLUTION.", 'JUST TO BE CLEAR, THIS IS A METAPHOR, RIGHT?', 'DOES THIS LOOK LIKE ENGLISH CLASS?', '!\n\nALL ADVANCED MATH TECHNIQUES']
if __name__ == '__main__':
    thread_list = []
    threads = len(text_list)
    test_list = shared_memory.ShareableList(text_list)
    for i in range(threads):
        thread_list.append(Process(target=multithread_fix_sentence, args=(test_list,i)))
        thread_list[-1].start()

    for thread in thread_list:
        thread.join()
    test_list = list(test_list)
    for item in test_list:
        if len(item) == 0:
            test_list.remove(item)
    print(test_list)