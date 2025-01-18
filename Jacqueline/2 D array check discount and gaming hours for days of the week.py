##def checkdiscount(price,u_code):
##    code= \
##        [["PVFC7", 10],
##        ["CPU5", 5],
##        ["BGF", 15]]# python does not support mulitple datatypes in an array
##    
##    for x in code:
##        
##        newprice = price
####        size=len(code)
##        for x in code:
##            if (x[0])==u_code:
##                 discount =(x[1])
##                 newprice =price-discount
##                 print("the new price is", newprice, " pounds and the discount was", discount)
##                 return newprice
##price =int(input(" enter a price"))
##u_code= input(" enter a discount code")
##checkdiscount(price, u_code)

time=\
       [
        ["Monday",   60,  30, 45, 0],
        ["Tuesday",  180, 60, 0,  60],
        ["Wednesday",200, 30, 0,  20],
        ["Thursday", 60,  10, 15, 15],
        ["Friday",   100, 35, 30, 45],
        ["Saturday", 200, 45, 0,   35]
        ]


#write the code to print out how many minutes student billy played games on Wedneday

print("Student 0 played for " , time[2][1], " minutes on ", time[2][0])
print("")
    
#print ( " student", time[0], " plays for a total of ", total)

time2=\
        [
        ["Billy", 60,180, 200, 60, 100],
        [ "Chin", 30, 60, 30,  10, 35],
        ["Henry", 45, 0, 0, 15, 30],
        ["Inaya", 0, 60, 20, 15, 45]
        ]


total2 =0
for min in time2:
    total =0
    total = total +min[1]+min[2]+min[3]+min[4]+min[5]
    total2=total2+total
    print ( " Student", min[0], "has a total of ", total)
print("")
print("In total all pupils played for ", total2)
print ("")

total2 =0
time=\
       [
        ["Monday",    60,  30, 45, 0],
        ["Tuesday",   180, 60, 0,  60],
        ["Wednesday", 200, 30, 0,  20],
        ["Thursday",  60,  10, 15, 15],
        ["Friday",    100, 35, 30, 45],
        ]



for day in time:
    total = 0
    total = total +day[1]+day[2]+day[3]+day[4]
    total2=total2+total
    print ( "Day", day[0], "played for ", total)
print("")
print("In total all pupils days had ", total2)
    
