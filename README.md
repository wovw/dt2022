## Inspiration
Text recognition has come a long way since the inception of machine learning; however, comics still provide a challenge for a machine. In a world where millions of people read comics and comic books, it is more important than ever to be able to convert these mantels of modern culture into ordered plain text.
## What it does
Comic Convert converts any xkcd comic into plain text and reads it to the user. The website allows the user to upload a cartoon where it will process the image and display two versions of the plain text. The first version is the raw text read from the comic and the second is processed text to autocorrect for errors in the first scan.

## How we built it
Google Vision AI API does the first scan of the comic. Though the API provides "blocks," Comic Convert only extracts the individual sentences. It does this by receiving the block of text from the comic and splitting it with appropriately placed punctuation. In most cases, Vision AI does a good enough job; however, it may detect objects as text when they should've been ignored. 

Comic Autocorrect reads the lists of sentences from Vision AI and filters out nonsense sentences and words. It goes through multiple checks to ensure English readability. First, it removes any new line characters since these would be considered errors when coming from Vision AI. Next, it determines if every word in every sentence makes sense. It first checks if every word is a valid word in www.dictionary.com. If it is not a recognized word, a grammar checker will replace it with the top suggestion. It then converts this text into a speech MP3 file. 

Both of these applications provide a list of sentences for the website to display through a JSON.
## Challenges we ran into
The first challenge we ran into was extracting the text from the comic using Vision AI since our group had no experience with using Google Cloud services. 

The biggest challenge throughout the challenge was to remove the noise from the results provided by Vision AI. In one situation, the API read a window as "38" and the grass as text in Arabic. Our group ventured into two solutions. The first was to use a grammar checker and basic logic of the English language to remove noise. The other was to train a model to take in the image and the list of sentences from Vision AI and output a paragraph of ordered text using PyTorch. Ultimately, the model proved to be too difficult to train so we settled with the grammar check. It is not perfect but works well enough.

Lastly, the creation of the website proved to be challenging; however, all of the issues were ironed out over time. 

## Accomplishments that we're proud of
We are proud of creating a website that can read a comic and show plain text and an audio file for a user to listen to as an audiobook. We are also proud of learning how to use Vision AI and filter out sentences and words that do not make sense in context. 
## What we learned
We learned how to use Google Cloud services and their APIs for python. We also learned how to use python language tools to check for grammar mistakes in any words or sentences in plain text. For the website, we learned how to use Flask to run python with Javascript on a remote machine. Though we never implemented it, we learned quite a bit about PyTorch when trying to create a model for the grammar checker. 
## What's next for Comic Convert
The next major milestone for Comic Convert is to get the machine-trained model for grammar checking up and working. Though the grammar and syntax checker is functional in its current state, it still makes minor mistakes when filtering plain text. We hope that a well-trained model will outperform our current system. 
