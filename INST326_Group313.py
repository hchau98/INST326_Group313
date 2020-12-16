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
      self.fh.set_index('Date IDs')
          
          
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


      #new_event = pandas.DataFrame({"DATE": self.event_date, "EVENT DESCRIPTION": self.event, "START TIME": self.start_time, " END TIME": self.end_time})

      #self.fh = self.fh.append([event_date, datetoid(event_date), event, start_time, end_time])
      self.fh.loc[len(self.fh.index)] = [event_date, event, start_time, end_time, datetoid(event_date), len(self.fh.index)+1]
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
          date_id = temp[2]+temp[0]+temp[1]
  return int(date_id)

def idtodate(date_id):  
  """id to date function"""
  pattern = r'(\d\d\d\d)(\d\d)(\d\d)'
  match = re.search(pattern,date_id)
  year = match[1]
  date = match[3]
  month = match[2]
  date = str(month + "/" + date + "/" + year)
  return date

def validatedate(date):
  """Takes a list of the components of a date and ensures the date is valid
        Args:
              date: a list containing the elements of the date
        
        Returns:
              valid: A boolean that is true if the date is valid and false if not
  """
  if int(date[0]) > 12 or int(date[0]) <1:
    return False
  if int(date[1]) <1 or int(date[1]) > 31:
    return False 
  else:
    return True
def parse_args(arglist):
  parser = argparse.ArgumentParser()
  parser.add_argument("filename",help="csv file containing schedule")
  return parser.parse_args(arglist)

if __name__ == "__main__":
  args = parse_args(sys.argv[1:])
  cal = Calendar(args.filename)
  exit = False
  while exit == False:
    action = input("How would you like to use the calendar app today(type help for help)?")
    if action == "help":
      print("schedule: Schedule will give you events for a day\n" +
            "add: Add will alow for you to add an event to you calendar\n" +
            "edit: Edit allows for you to edit an already existing event\n" +
            "remove: Remove will let you remove an event\n" +
            "exit: Will exit the program"
            )
    if action == "schedule":
      day = input("What day would you like to look at your schedule (MM/DD/YYYY):")
      print(cal.get_schedule(day))
    if action == "add":
      day = input("What day will this event occur on (MM/DD/YYYY):")
      desc = input("What is this event:")
      start = input("When does the event start (HH:MM in militaryt time):")
      end_time = input("When does the event end (HH:MM in militaryt time):")
      cal.add_event(day,start, end_time,desc)
      print(desc + " on " + day + " has been added to your calendar.")
    if action == "exit":
      exit = True
    else:
      print("Unknown command")