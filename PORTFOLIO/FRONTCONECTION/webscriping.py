from .models import posts

import requests
from bs4 import BeautifulSoup
import os
import re


def get_posts():

    url = 'https://news.mit.edu/topic/machine-learning'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    # add string
    x='https://news.mit.edu'


    # find the title
    artical = soup.find_all('h3', class_="term-page--news-article--item--title")
    # title in span tag
    title = [t.find('span').text for t in artical if t.find('span') is not None]

    # link in artical variable is in a tag
    link = [x+str(l.find('a')['href']) for l in artical if l.find('a') is not None]



    # find image
    image = soup.find_all('img')
    # fiter only link which is present in data-src attribute
    image = [x+str(img['data-src']) for img in image if 'data-src' in img.attrs]


    post = soup.find_all('p', class_='term-page--news-article--item--dek')
    # description in post variable span tag
    description = [p.find('span').text for p in post if p.find('span') is not None]

    # date time of the post

    date = soup.find_all('time')
    date = [d.text for d in date]

    # save to the model posts
    # check if the post is already present in the database
    # if not then save the post to the database
    # if present then update the post


    # apply candition on the defference of the length of arrays

    if len(title) != len(description) or len(title) != len(link) or len(title) != len(image) or len(title) != len(date):
        print('Error: The length of the arrays are not equal')
        return
    for i in range(len(title)):
        posts.objects.get_or_create(title=title[i],
            description=description[i],
            html_url=link[i],
            image=image[i],
            date=date[i]
        )
