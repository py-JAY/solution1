def hoursPassed(time1,time2):
    def changeFormat(time):
        hours,minutes = map(int, time[:-3].split(":"))
        meridian = time[-2:].lower()

        if meridian == "am":
            if hours == 12:
                hours = 0
        else:
            if hours != 12:
                hours += 12
        
        return (hours * 60)+minutes
    
    min1 = changeFormat(time1)
    min2 = changeFormat(time2)

    diff = min2 - min1

    if diff<0:
        diff += (24*60)
    
    hours = diff // 60
    minutes = diff % 60

    return f"{hours} Hours and {minutes} Minutes" if diff>0 else "No time passed"
