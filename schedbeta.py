from INST326_Group313 import Calendar
from INST326_Group313 import datetoid




testing_cal = Calendar("test_schedule_js.csv")
print(testing_cal.fh)
testing_cal.remove_event(5)
testing_cal.add_event("12/31/2020", "20:00", "23:59", "New Years Eve Party")

print(testing_cal.fh)
answer_cal = {"DATE":[]}
