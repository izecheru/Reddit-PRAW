
# Reddit PRAW
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FzecheruIonut%2FReddit-PRAW&count_bg=%239DAC91&title_bg=%23555555&icon=&icon_color=%23DD0000&title=Views&edge_flat=false)](https://hits.seeyoufarm.com)

# This script can be used to download the images from a specific subreddit.

# Installation


### Install from Visual Studio package manager.
![Alt text](https://i.imgur.com/EBh6hMR.png)

```bash
pip install praw
or just praw and it will give you the option with pip
```

### Before you use the code, you must register in [reddit apps](https://www.reddit.com/prefs/apps)
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



