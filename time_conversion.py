# Convert time to 24 hour clock

if (time[-2:] == 'PM'):
    if time[:2] == "12":
        hour = "12"
    else: 
        hour =  str(12 + int(time[:2]))
else:
    if time[:2] == "12":
        hour = "00"
    else:
        hour = time[:2]

print ":".join([hour, time[3:5], time[6:8]])
