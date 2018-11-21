###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year,month,day):
    if day < 30:
        return (year, month, day+1)
    else:
        if day ==30:
            if month==12:
               return (year+1, 1, 1)
            else:
               return (year, month+1,1)
print nextDay(2012,12,24)
print nextDay(2012,12,30)
print nextDay(2012,11,30)
