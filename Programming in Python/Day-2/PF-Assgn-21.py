#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    daysinmonth = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    if (year%4==0 and year%100!=0) or year%400==0:
        daysinmonth[2] = 29        
    
    if day<daysinmonth.get(month):
        day+=1
    elif day==daysinmonth.get(month):
        month+=1
        day = 1

    if month>12:
        month=1
        year+=1
        
    print(day,"-",month,"-",year)


generate_next_date(30,2,2000)
