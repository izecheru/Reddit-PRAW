import praw
import requests
import os



# Folderul in care se salveaza pozele daca nu sunt deja descarcate
download_folder = ''

# Subreddit-ul de pe care vrei sa iei pozele
subreddit_target = ''

# Numarul de poze pe care vrei sa le descarci
limit_ = 5




def log_in():
    reddit = praw.Reddit(client_id = '',
                         client_secret = '',
                         username = '',
                         password = '',
                         user_agent = '')
    return reddit

created = []

def create_image(path, link):
    response = requests.get(str(link), stream = True)
    file = open(str(download_folder)+str(link).split('/')[-1],'wb')
    file.write(response.content)
    file.close()


def to_create(up, name):
    for i in range(len(up)):
        created.append(str(up[i])+'-'+str(name[i]).split('/')[-1])
    return created




reddit = log_in()
subreddit = reddit.subreddit(subreddit_target)
hot_sub = subreddit.hot(limit = limit_)

up =[]
name = []


for submission in hot_sub:
    if str(submission.url).find('jpg')!=-1:
        name.append(submission.url)
        up.append(submission.ups)



def sort(lista):
    for j in range(0, len(lista)):
            for i in range(0, len(lista)-1):
                if lista[i] > lista[i+1]:
                    lista[i+1], lista[i] = lista[i], lista[i+1]
                    name[i+1], name[i] = name[i], name[i+1]
def init():

    if len(name)>2:
        sort(up)

    for i in range(len(name)):
        try:
            if exists(str(name[i]).split("/")[-1]):
                print('{} already exists'.format(str(name[i]).split("/")[-1]))
            else:
                create_image(str(download_folder), name[i])
                print("image: {} UPS: {}".format(str(name[i]).split('/')[-1],
                                                                        up[i]))
        except:
            print("Cel mai probabil are ceva cacat de emoji.")



def exists(to_look_for):
    path_ =  str(download_folder)+str(to_look_for)
    if os.path.exists(path_)==True:
        return True
    return False


init()
