<h1 align="center">Hi 👋, I'm Ionut Zecheru</h1>
<h3 align="center">A handicapat who has internet from erce esi.</h3>

# Reddit PRAW

This script can be used to download the images from a specific subreddit.

# Installation


### Install from Visual Studio package manager.
![Alt text](https://i.imgur.com/EBh6hMR.png)

```bash
pip install praw
or just praw and it will give you the option with pip
```

### Before you go knee deep in the code, you must register in [reddit apps](https://www.reddit.com/prefs/apps)
#### ![alt text](https://i.imgur.com/p6ZUIOe.png)
You must get those values for the script to work.
# Do not make them public!!!
```python
def log_in():
    reddit = praw.Reddit(client_id = 'the code under personal use script',
                         client_secret = 'the secret is the longer code',
                         username = 'obvious',
                         password = 'pass',
                         user_agent = 'your username')
```
# Usage

```python
import praw
import requests
import os

download folder = '' # here you must specify the download folder where the images will go

subreddit_target = '' # here you must specify the subreddit that you want to take images from

limit_ = '' # this is simply the number of images that will be downloaded
```
#### Note that the script won't download the same image twice.
#### It will give a certain message in the console.

## Changes i have in mind for future updates
* Filter subreddit posts by New/ Top
* Download images uploaded on a specific date
* Check if subreddit exists
* Donwload images with certain number of upvotes
* Many more...


