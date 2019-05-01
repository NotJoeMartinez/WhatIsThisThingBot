import io
import os
import praw
import urllib.request
from google.cloud import vision


# Reddit praw authentication
reddit = praw.Reddit(client_id='my client id',
                     client_secret='my client secret',
                     user_agent='my user agent')


# Google vision authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'path to local json file'


# pull images from reddit
def get_uri():
    for message in reddit.inbox.mentions():
        return message.parent().url


# detect image lables
def detect_labels(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    for label in labels:
        print(label.description)

# todo: reply to the comment with the lables


detect_labels(get_uri())
