from INST326_Group313 import Calendar
from INST326_Group313 import datetoid
cal = datetoid("11/22/2020")
cal_test = Calendar("SCHDULE_CSV.csv")
print(cal)
print(cal_test.fh)
sched_test = cal_test.get_schedule("1/1/2021")
print(sched_test)