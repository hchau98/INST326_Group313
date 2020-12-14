from INST326_Group313 import Calendar
from INST326_Group313 import datetoid
cal = datetoid("11/22/2020")
cal_test = Calendar("SCHDULE_CSV.csv")
print(cal_test.fh)
cal_test.add_event("12/13/2020", "12:00", "14:00", "Party")
print(cal_test.fh)
