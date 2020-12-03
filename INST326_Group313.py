import pandas
 Calendar:
  """ This is a calendar to keep people organized """

class Calendar:
    """ This class represents a users schedule on a calendar
    
      Attributes: 
          calendar: a list containing other lists that contains events for the days
      Methods:
      		__init__: Initilizes the calander object by parsing a csv
          get_schedule(): Gives the user their schedule for the day
          conflicts: returns a list containing conflicting scheduling appointments
          add_event: Adds an event to your calendar
          remove_event: Removes an event from your calendar
          edit_event: Edits an event in your calendar
    """
    def __init__(self,filename):
      """ Creates a datafram of the schedule using pandas. In addition values for dates and events are assigned as well
          
          Args:
              Self
              Filename: String containing path to CSV schedule file
               """
      fh = pandas.read_csv(filename,sep= ",")
      temp = fh['DATE']
      date_ids=[]
      for i in temp:
        j = datetoid(i)
        date_ids.append(j)
      fh["Date IDs"] = date_ids
      event_ids=[]
      counter = 1
      for i in temp:
        event_ids.append(j)
        j= j+ 1
      fh["Event IDs"] = event_ids
          
          
    def get_schedule(self,day):
      """ Gives the user a list of events for what is scheduled for them
          Args:
              self
              day: What day would the user like to look at their schedule
                  Null case means current date
              
          Return:
              sched: This would be a list of events that the user has scheduled from their calendar
      """



    def conflicts(new_appointment,existing_appointments):
      """
      Returns to the user a list of conflicting scheduling appointments
      
      Args:
        new_appointment(dict): dict of new appointment
        existing_appointment(dict): dict of all appointments
      """


    def add_event(event_id):
      """ Adds an event to the users schedule
      		
          Args:
          	event: the event to be added
      """


    def remove_event(event):
      """ Removes an event from the users schedule
      		
          Args:
          	event: the event to be removed
      """


    def edit_event(event_id,  date_id, event_desc, event_start, event_end)
    	""" Edits the parameters of an event 

            Args:
              date_id: An assigned integer to reference the event to a date on the calendar
            	event_desc: A string that gives a description of the event
            	event_start: A tuple to designate the start time
           		even_end:A tuple to designate the end tim
		"""
    
class Event:
    """ This class represents an event on the calendar

      Attributes: 
          event_id: an assigned integer to refernce the event
          date_id: An assigned integer to reference the event to a date on the calendar
          event_desc: A string that gives a description of the event
          event_start: A tuple to designate the start time
          even_end:A tuple to designate the end time

      Methods:
          __init__: Creates an instance of the event class with given parameters
    """
    

    def __init__(self, event_id, date_id, event_desc, event_start, event_end):
      """Initializes the create of the event object with the given parameters
      
      		Args:
          	event_id: an assigned integer to refernce the event
          date_id: An assigned integer to reference the event to a date on the calendar
          event_desc: A string that gives a description of the event
          event_start: A tuple to designate the start time
          even_end:A tuple to designate the end time
      """
      self.event_id = event_id
      self.date_id = date_id
      self.event_desc = event_desc
      self.event_start = event_start
      self.event_end = event_end

import calendar from Calendar
import event from Event
import argparse
import sys

def main():

if __name__ == "__main__"-
        
    
def datetoid(date):
  """Takes a date as a string and conerts it into a date id
        
        Args:
          date: A string reprentation of a date
          
        Returns:
          temp: An integer with date id
  """

  temp = date.split('/')
  date=''
  for i in temp:
          b = i.split('/')
          if len(b[1]) == 1:
              b[1] = "0" + b[1]
          if len(b[0]) == 1:
              b[0] = "0" + b[0]
          temp = b[2]+b[1]+b[0]
  return int(temp)

def idtodate(id):   
    

        

import calendar from Calendar
import argparse
import sys

def main():

if __name__ == "__main__":
    