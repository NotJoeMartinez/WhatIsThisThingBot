import io
import os
import praw
import urllib.request
from google.cloud import vision
from config import reddit

# Reddit praw authentication




# adds message id to replied to array
# returnes submission url
def get_image_uri():
    for message in reddit.inbox.mentions(limit=1):
        replied_to.append(message.id)
        return message.submission.url


def detect_labels(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations

    # list of lables
    all_lables = []

    for label in labels:
        all_lables.append(label.description)
    # print(all_lables)
    return all_lables

# coverts the array returned by detect_labels into a string with each lable sitting on a new line
def convert(list):
    s = [str(i) for i in list]
    res = "\n".join(s)
    return res

attrs = detect_labels(get_image_uri())

# replies to comments with attrs 
for x in reddit.inbox.unread(limit=None):
    x.reply("Lables: \n" + convert(attrs))
    print("replied to comment")
    # mark mention as read 
    x.mark_read()



