import pytest
import INST326_Group313 as cal
import pandas as pd
#Jake
def test_jake():
    assert cal.datetoid("9/13/1999") == 19990913
    assert cal.validatedate(["13","13", "1999"]) == False
    assert cal.validatedate(["09","45", "2020"]) == False
    
    assert cal.validatedate(["12","25", "2020"]) == True
    testing_cal = cal.Calendar("test_schedule_js.csv")
    testing_cal.add_event("12/31/2020", "20:00", "23:59", "New Years Eve Party")
    testing_cal.remove_event(2)
    result = testing_cal.get_schedule("3/17/2021")
    answer_sched = {"DATE": ['3/17/2021',"3/17/2021"], 'EVENT DESCRIPTION' : ["Dads Birthday Dinner", "St Patricks Day Party"], 'START TIME' : ["18:00", "21:00"], 'END TIME': ["20:00", "23:59"], 'Date IDs' : [20210317, 20210317], "Event IDs" : [4, 5]}    
    pf = pd.DataFrame(data=answer_sched)
    right_ans =[]
    for index, row in pf.iterrows():
            right_ans.append(row)
    assert right_ans[0].equals(result[0]) == True
    assert right_ans[1].equals(result[1]) == True
   

   