import pytest
import INST326_Group313 as cal
#Jake
def test_jake():
    assert cal.datetoid("9/13/1999") == 19990913
    assert cal.validatedate(["13","13", "1999"]) == False
    assert cal.validatedate(["09","45", "2020"]) == False
    
    assert cal.validatedate(["12","25", "2020"]) == True
    testing_cal = cal.Calendar("test_schedule_js.csv")
    print("hi")

   