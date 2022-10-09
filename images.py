
from google.cloud import vision
import io
from typing import Sequence
from google.api_core.client_options import ClientOptions
from google.cloud import documentai

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image, image_context={"language_hints": ["en"]})
    # texts = response.text_annotations
    # print('Texts:')
    # print("block" in texts)
    # for text in texts:
    #     print('\n"{}"'.format(text.description))

    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                 for vertex in text.bounding_poly.vertices])

    #     print('bounds: {}'.format(','.join(vertices)))
    # if len(texts) > 0:
    #     pgs = texts[0]
    #     print(pgs)
    
    txtStrings = []
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            # print('\nBlock confidence: {}\n'.format(block.confidence))
            # print(block.description)
            
            blk = []
            for paragraph in block.paragraphs:
                para = []
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    word_text = word_text.strip()
                    para.append(word_text)
                
                para = ''.join([
                        p + " " for p in para
                    ])
                para = para.strip()
                blk.append(para)
                
            blk = ''.join([
                        b + "\n" for b in blk
                    ])
            para = para.strip()
            txtStrings.append(blk)
    while None in txtStrings:
        txtStrings.remove(None)
        
    txtStrings = ''.join([
                        ñ + "\n" for ñ in txtStrings
                    ])
    txtStrings = txtStrings.strip()
    
    txtStrings = txtStrings.replace(' ?', "?ඞ")
    txtStrings = txtStrings.replace(' ,', ",")
    txtStrings = txtStrings.replace(' !', "!ඞ")
    txtStrings = txtStrings.replace(' . ', ".ඞ ")
    txtStrings = txtStrings.replace(' ... ', "...ඞ\n")
    txtStrings = txtStrings.replace('... ', "ඞ\n...")
    txtStrings = txtStrings.replace(' .', ".ඞ")

    txtStrings = txtStrings.split("ඞ")
    txtStrings = [s.strip() for s in txtStrings]

    return txtStrings
    
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))





#------------------------------------------------------------------------------------------------

#filename = "C:/Users/upads/Documents/escuela_drive/Misc/Datathon 2022/training-strips/cartoon4.png"
filename = "given_dataset/cartoon15.png"
#filename = "new_dataset/advanced_techniques.png"
#img = cv2.imread('training-strips\\' + filename)
#text = pytesseract.image_to_string(img)
print(detect_text(filename))









