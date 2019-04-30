import praw
import urllib.request

# Praw authentication


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

get_images()
