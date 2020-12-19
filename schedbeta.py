from INST326_Group313 import Calendar
from INST326_Group313 import datetoid




testing_cal = Calendar("test_schedule_js.csv")
print(testing_cal.fh)
testing_cal.remove_event(5)
testing_cal.add_event("12/31/2020", "20:00", "23:59", "New Years Eve Party")
testing_cal.remove_event(2)
print(testing_cal.fh)
#print(testing_cal.fh.index.values[-1])
