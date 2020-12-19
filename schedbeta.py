from INST326_Group313 import Calendar
from INST326_Group313 import datetoid
import pandas as pd



testing_cal = Calendar("test_schedule_js.csv")
#print(testing_cal.fh)
testing_cal.add_event("12/31/2020", "20:00", "23:59", "New Years Eve Party")
testing_cal.remove_event(2)
print(testing_cal.get_schedule("3/17/2021"))
result_sched = {"DATE": ['3/17/2021',"3/17/2021"], 'EVENT DESCRIPTION' : ["Dads Birthday Dinner", "St Patricks Day Party"], 'START TIME' : ["18:00", "21:00"], 'END TIME': ["20:00", "23:59"], 'Date IDs' : [20210317, 20210317], "Event IDs" : [4, 5]}    
pf = pd.DataFrame(data=result_sched)
right_ans =[]
for index, row in pf.iterrows():
        right_ans.append(row)
print(right_ans)
print(right_ans[0].equals(testing_cal.get_schedule("3/17/2021")[0]))
print(right_ans[1].equals(testing_cal.get_schedule("3/17/2021")[1]))
#print(testing_cal.get_schedule("3/17/2021").equals(right_ans))   
                  
