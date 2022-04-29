# -*- coding: utf-8 -*-
"""
This progam is a webscrapper for HACKERNEWS. Allows user to set a minimum cut-off for
the votes that each article must have inorder to be to displayed.
Returns a list of dictionaries that contain the title, link and votes of articles on the site that meet the criteria.

Created on Mon May 17 02:13:12 2021

@author: Bruce Mvubele
"""
#make a comment

## Beautiful soups allows to grab html to get data
## Requests helps us download the html
import requests
from bs4 import BeautifulSoup
import pprint

min_points = int(input('Enter the minimum points you would like to see on each post: \n'))

res = requests.get('https://news.ycombinator.com/')  #grabs the page as a string, 200 response is positive response
soup = BeautifulSoup(res.text, 'html.parser') # converts string to useful html format (html.oarser)
                                              # allows for extraction of data from html
                                              #soup.select('obj') grabs data
                                              
links = soup.select('.storylink')  #grabs all elements that have class storylink (list)
subtext = soup.select('.subtext') #grabs all the text on the webpage front page

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'])

                                              
def create_custom_site(links, subtext):
    
    hn = [] #new hackerrank
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.get('href',None) #gets the link of the article
        vote = subtext[idx].select('.score') # gets the votes of the acrticle as array
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points >= min_points:
                
                hn.append({'title': title, 'link': href, 'votes': points})
          
            
    return sort_stories_by_votes(hn) 

pprint.pprint(create_custom_site(links, subtext))
