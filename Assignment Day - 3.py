#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Movienode:
    def __init__(self, moviename, releasedate):
        self.moviename = moviename
        self.releasedate = releasedate
        self.next = None
        return
    
class Netflixmovielist:
    def __init__(self):
        self.head = None
    
    def addmovie(self, moviename, releasedate):
        new = Movienode(moviename, releasedate)
        if self.head == None:
            self.head = new
            return
        new.next = self.head
        self.head = new
        return
    
    def removeLastNode(self):
        if self.head == None:
            return None
        if next == None: 
            self = None
            return None
        second_last = self.head 
        while(second_last.next.next): 
            second_last = second_last.next
        second_last.next = None
        return self        
    
    def displaymovies(self):
        if self.head == None:
            print ("No movies to show")
            return
        temp = self.head
        
        while(temp != None):
            print(temp.moviename, temp.releasedate, "->", end = " ")
            temp = temp.next
        print("None")
        return
        
movie_list = Netflixmovielist()
movie_list.addmovie('Iron Man', '10th june 2010')
movie_list.addmovie('Singham', '12th marchh 2016')
movie_list.addmovie('Bajirao Singham', '11th may 2016')
movie_list.addmovie('K3G', '23rd Jan 2005')
movie_list.removeLastNode()
movie_list.displaymovies()


# In[ ]:




