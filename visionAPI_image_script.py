import os
import io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'vision-token.json'

client = vision_v1.ImageAnnotatorClient()

FOLDER_PATH = r'/Users/sakshi/desktop/visionAPI/images'
IMAGE_FILE = 'psych.png'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision_v1.types.Image(content=content)
response = client.document_text_detection(image=image)
docText = response.full_text_annotation.text
print(docText)

f = open("output_file.txt", "a")
f.write(docText)
f.close()

f = open("output_file.txt", "r")
print(f.read())

# Following code is optional
# Prints confidence per letter
# pages = response.full_text_annotation.pages #for page in pages:
#    for block in page.blocks:
#        print('block confidence:', block.confidence)

#        for paragraph in block.paragraphs:
#            print('paragraph confidence:', paragraph.confidence)

#            for word in paragraph.words:
#                word_text = ''.join([symbol.text for symbol in word.symbols])

#                print('Word text: {0} (condifence: {1}'.format(word_text, word.confidence))

#                for symbol in word.symbols:
#                    print('\tSymbol: {0} (confidence: {1}'.format(symbol.text, symbol.confidence))
