from comic_images import detect_text
from comic_autocorrect import fix_sentence
import os
import json
from gtts import gTTS

file_formats = [".jpg", ".gif", ".png", ".jpeg"]

if __name__ == "__main__":
    path = 'IO/'
    filename = ""
    dir_list = os.listdir(path)
    for file in dir_list:
        if os.path.splitext(path + file)[1].lower() in file_formats:
            filename = file

    google_api_text = detect_text(path + filename)
    autocorrected_text = fix_sentence(google_api_text)

    json_output = {}

    largest_length = max(len(google_api_text), len(autocorrected_text))

    for i in range(largest_length):
        json_output[i] = []
        if i >= len(google_api_text):
            json_output[i].append("") 
        else:
            json_output[i].append(str(google_api_text[i])) 

        if i >= len(autocorrected_text):
            json_output[i].append("") 
        else:
            json_output[i].append(str(autocorrected_text[i])) 

    with open(path + "json_file.json", "w") as file1:
        file1.write(json.dumps(json_output, sort_keys=True, indent=4 * ' '))

    myobj = gTTS(text=(" ".join(autocorrected_text)), lang='en', slow=False)
    myobj.save(path + "output.mp3")
