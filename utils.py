import time
import datetime

class Days():

    def __init__(self,name,day,month):
        self.name = name
        self.day = day
        self.month = month

    def calculation(self):
        current_year = "2023"
        next_year = "2024"
        form = "%Y%B%d"
        current_date = datetime.datetime.now().date()

        date_1 = current_year+self.month+self.day
        std_date_1 = datetime.datetime.strptime(date_1,form).date()

        date_2 = next_year+self.month+self.day
        std_date_2 = datetime.datetime.strptime(date_2,form).date()
        if std_date_1 >= current_date:
            days = std_date_1-current_date
            print("remaing_days :",days)
            return days.days
        
        else:
            days = std_date_2-current_date
            print("remaing_days :",days)
            return days.days


if __name__ == "__main__":
    name = "Amol"
    day = "03"
    month = "june"
    
    
    obj = Days(name,day,month)
    days = obj.calculation()
