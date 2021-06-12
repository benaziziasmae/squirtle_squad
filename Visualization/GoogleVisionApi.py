import os
import re
from google.cloud import vision

class UnableToDecodeImageError(Exception):
    pass

def ImgToStringOCR(imageURL=None):

    # apply credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath('valued-bastion-303823-bf54c21ee612.json')

    # detect text from image file fxn
    def detect_text_uri(uri):
        """Detects text in the file located in Google Cloud Storage or on the Web."""
        client = vision.ImageAnnotatorClient()
        image = vision.Image()
        image.source.image_uri = uri

        response = client.text_detection(image=image)
        texts = response.text_annotations
        return texts[0].description

    # initialize image as address
    ## replace imageURL with S3 bucket
    imageURL = imageURL or "https://cdn.discordapp.com/attachments/573601042147704862/849067497600188426/IMG_3084.JPG"

    # run fxn to get photo's text (card's text)
    card_text = detect_text_uri(imageURL)

    # regex filtration
    regexReg = '\d{2,3}\/\d{2,3}'
    regexPromo = '\W{0,4}\d{2,3}'

    # try regular card collector_number regex
    try:
        collector_number = re.findall(regexReg, card_text)[0]
    except IndexError:
        # try promo card collector_number regex
        try:
            collector_number = re.findall(regexPromo, card_text)[0]
        except IndexError:
            print('Cannot find collector number')
            raise UnableToDecodeImageError('Cannot find collector number')

    return collector_number

# pass collector_number to query
