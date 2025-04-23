import datetime
d1=(18,2,2025)
d2=(18,2,2024)
date1=datetime.date(d1[2],d1[1],d1[0])
date2=datetime.date(d2[2],d2[1],d2[0])
print(date1,date2,sep='\n')
print(abs((date1-date2).days))