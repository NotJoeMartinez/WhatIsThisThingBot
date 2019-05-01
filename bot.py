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


# Path to local things folder
things_folder = 'Path to folder with unkown images'

# download image
def download_images(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


# pull images from reddit
def get_images():
    for submission in reddit.subreddit('whatisthisthing').rising(limit=5):
        download_images(submission.url, things_folder, submission.id)
        print("submission with id " + submission.id + " saved to things folder")

# detects lables in file and prints them to console
def detect_labels(path):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)


# calls detect_lables function on local directory
for image in os.listdir(things_folder):
    detect_labels(things_folder + image)
