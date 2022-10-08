import base64
import json
import os

from google.cloud import vision
import io

vision_client = vision.ImageAnnotatorClient()

#project_id = os.environ["GCP_PROJECT"]


def detect_text(filename):
    print("Looking for text in image {}".format(filename))

    futures = []

    with io.open(filename, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    
    text_detection_response = vision_client.text_detection(image=image)
    annotations = text_detection_response.text_annotations
    if len(annotations) > 0:
        text = annotations[0].description
    else:
        text = ""
    print("Extracted text {} from image ({} chars).".format(text, len(text)))
    
    for future in futures:
        future.result()
        
print(detect_text("cartoon1.png"))