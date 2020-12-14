import pandas
import argparse
import sys
import re

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
      self.filename = filename
      self.fh = pandas.read_csv(filename,sep= ",")
      temp = self.fh['DATE']
      date_ids=[]
      #Datemethod
      for i in temp:
        j = datetoid(i)
        date_ids.append(j)
      self.fh["Date IDs"] = date_ids
      event_ids=[]
      counter = 1
      for i in temp:
        event_ids.append(counter)
        counter = counter + 1
      self.fh["Event IDs"] = event_ids
          
          
    def get_schedule(self,day):
      """ Gives the user a list of events for what is scheduled for them
          Args:
              self
              day: What day would the user like to look at their schedule
                  Null case means current date
              
          Return:
              sched: This would be a list of events that the user has scheduled from their calendar
      """
      self.day = day 
      date_id = datetoid(self.day)
      scheds = []
      temp = self.fh 
      for index, row in temp.iterrows():
        if row['Date IDs'] == date_id:
          scheds.append(row)
      return (scheds)


    def conflicts(self):
      """
      Returns to the user a list of conflicting scheduling appointments
      
      Args:
        new_appointment(dict): dict of new appointment
        existing_appointment(dict): dict of all appointments
      """

      
      
      


    def add_event(self, event_date, start_time, end_time, event):
      """ Adds an event to the users schedule
      		
          Args:
              event_date: the day of the event to be added
              start_time: the time event starts
              end_time: the time the event ends
              event(str): description of the event to be added 
      """

      self.event_date = datetoid(event_date)
      self.start_time = start_time
      self.end_time = end_time
      self.event = event

      new_event = pandas.DataFrame({"DATE": self.event_date, "EVENT DESCRIPTION": self.event, "START TIME": self.start_time, " END TIME": self.end_time})

      self.fh = self.fh.append(new_event, ignore_index=True)
      return self.fh

    def remove_event(self):
      """ Removes an event from the users schedule
      		
          Args:
          	event: the event to be removed
      """


    def edit_event(event_id,  date_id, event_desc, event_start, event_end):
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
    def create_event(self):
      date = idtodate(self.date_id)
      data = {'Date': [date],'Event Description':[self.event_desc],'Start Time':[self.event_start],'End Time':[self.event_end],'Date IDs':[self.date_id],'Event IDs':[self.event_id]}
      event = pd.Dataframe(data, columns =['Date','Event Description','Start Time','End Time','Data IDs','Event IDs'])
      return(event)



def datetoid(date):
  """Takes a date as a string and converts it into a date id
        
        Args:
          date: A string representation of a date
          
        Returns:
          date_id: An integer with date id
  """

  temp = date.split("/")
  date_id=''
  for i in temp:
          if len(temp[1]) == 1:
              temp[1] = "0" + temp[1]
          if len(temp[0]) == 1:
              temp[0] = "0" + temp[0]
          date_id = temp[2]+temp[1]+temp[0]
  return date_id

def idtodate(date_id):  
  """id to date function"""
  pattern = r'(\d\d\d\d)(\d\d)(\d\d)'
  match = re.search(pattern,date_id)
  year = match[1]
  date = match[3]
  month = match[2]
  date = str(month + "/" + date + "/" + year)
  return date
  
  
def parse_args(arglist):
  parser = argparse.ArgumentParser()
  parser.add_argument("filename",help="csv file containing schedule")
  return parser.parse_args(arglist)

if __name__ == "__main__":
  args = parse_args(sys.argv[1:])
  print(Calendar(args.filename).get_schedule("12/13/2020"))