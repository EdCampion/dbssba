from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField('name of region',max_length=200)
    def __unicode__(self):
        return self.name
    
    @classmethod
    def create(cls,name):
        region = cls(name = name)
        region.save()
        return region
        
 
    #many to many between tweets and topics
class Topic(models.Model):
    name = models.CharField('topic name e.g. Fav Yogurts',max_length = 200) 
    
    def __unicode__(self):
        return self.name

class SearchTerm(models.Model):
    term = models.CharField('Term to search',max_length=20)
    topic = models.ForeignKey(Topic)
    def __unicode__(self):
        return self.term      
        
class Tweet(models.Model):
    
    text = models.CharField('actual tweet',max_length = 140)
   
    reg = models.ForeignKey(Region)
    
    @classmethod
    def create(cls,text,regFK):
        tweet = cls(text = text,reg = regFK)
        tweet.save()
    
    def __unicode__(self):
        length = len(self.text)
        return self.text[0:(length/2)+1] + '...'
    
#A search term can be associated with multiple topics i.e Favourite Ice Cream-> Vanilla Favourite Smell-> Vanilla
# class lnkTopicTerm(models.Model):
#     top = models.ForeignKey(Topic) 
#     term = models.ForeignKey(SearchTerm)
#     
#     def __unicode__(self):
#         return self.top.name + "" + self.term.term
      
# class lnkRegTopic(models.Model):
#     reg = models.ForeignKey(Region)
#     topic = models.ForeignKey(Topic)
#     def __unicode__(self):
#         return self.reg.name + " " + self.topic.name

# class RegionalOccurrence(models.Model):
#     reg = models.ForeignKey(Region)
#     termtop = models.ForeignKey(lnkTopicTerm)
#     occurs = models.IntegerField('how often the term occurred',default = 0)
    

    

       
# Create your models here.
