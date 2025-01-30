def hoursPassed(time1,time2):
    
    if time1 == time2:
        return "No time passed"
    
    elif (time1.split())[1].lower()=="am" and (time2.split())[1].lower()=="am":
        tup1 = (time1.split())[0].partition(":")
        w,x = int(tup1[0]),int(tup1[2])

        tup2 = (time2.split())[0].partition(":")
        y,z = int(tup2[0]),int(tup2[2])

        return f"{(w-y) if w>y else (y-w)} Hours and {(x-z) if x>z else (z-x)} Minutes"
    
    elif (time1.split())[1].lower()=="pm" and (time2.split())[1].lower()=="pm":
        tup1 = (time1.split())[0].partition(":")
        w,x = int(tup1[0]),int(tup1[2])

        tup2 = (time2.split())[0].partition(":")
        y,z = int(tup2[0]),int(tup2[2])

        return f"{(w-y) if w>y else (y-w)} Hours and {(x-z) if x>z else (z-x)} Minutes"
    else:
        tup1 = (time1.split())[0].partition(":")
        w,x = int(tup1[0]),int(tup1[2])

        tup2 = (time2.split())[0].partition(":")
        y,z = int(tup2[0]),int(tup2[2])

        return f"{(((w-y)))if w>y else (((y-w)))} Hours and {(x-z) if x>z else (z-x)} Minutes"

print(hoursPassed("1:00 AM","3:00 PM"))