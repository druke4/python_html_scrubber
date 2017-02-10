import urllib.request
from bs4 import BeautifulSoup  
import logging  
import string
import csv

logging.basicConfig(level=logging.DEBUG)

class Movie(object):
    def __init__(self, name, totalGross, openingGross):
        self.name = name
        self.totalGross = totalGross
        self.openingGross = openingGross
    
    def __str__(self):
        return(str(self.name)+": "+str(self.totalGross))
    
    def __repr__(self):
        return(str(self.name)+": "+str(self.totalGross))

def get_all_movies():  
    """ returns all the movie urls from boxofficemojo.com in a list"""

    num_of_movies = 25
    # List of movie urls
    movies_list = [Movie(count,0,0) for count in range(num_of_movies)]

    # Loop through the pages within each letter
    url_total_gross = ("http://www.boxofficemojo.com/seasonal/?view=releasedate&yr=2017&season=Winter&sort=gross&order=DESC&p=.htm")
    url_opening = ("http://www.boxofficemojo.com/seasonal/?view=releasedate&yr=2017&season=Winter&sort=opengross&order=DESC&p=.htm")

    total_gross_page = urllib.request.urlopen(url_total_gross)
    opening_gross_page = urllib.request.urlopen(url_opening)

    total_gross_soup = BeautifulSoup(total_gross_page,"html.parser")
    opening_gross_soup = BeautifulSoup(opening_gross_page,"html.parser")

    total_gross_rows = total_gross_soup.find_all("b")
    opening_gross_rows = opening_gross_soup.find_all("b")

    print(total_gross_rows)
    # skip index row
    if len(total_gross_rows) > 1:
        for movies in range(1,num_of_movies+1):
            print( movies )
            total_gross = total_gross_rows[movies*2+10].string
            opening_gross = opening_gross_rows[movies*2+10].string
            movie_name = total_gross_rows[movies*2+9].string
            movies_list[movies-1] = Movie( movie_name, total_gross, opening_gross )

    print("done")
    return movies_list

movie_list = get_all_movies()

with open('Movie_List.csv', 'w') as myfile:
    wr = csv.writer(myfile, dialect='excel')
    wr.writerow(movie_list)

print(*movie_list, sep='\n')











