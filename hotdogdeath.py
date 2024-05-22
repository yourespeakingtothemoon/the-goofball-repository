minutesinyear = 525600
currentage = 33.6
maxage = 73.2
##for the purposes of the hypotheical, we will assume you are consuming hot dogs for all minutes you are awake.
##if you would like to specfiy a small number like 1 or 3, you can use fractions of time awake
hotdogsperminute = 1
timeawake = 16
minutesremovedfromhotdogconsumption = 36
minutesawake = timeawake * 60


timeremaining = (maxage - currentage) * minutesinyear

totalhotdogs = 0
minutesspent=0
livedminutes = currentage * minutesinyear
while timeremaining > 0:
    if minutesspent == minutesawake:
        minutesspent = 0
        timeremaining -= (24 - timeawake)*60
        livedminutes += (24 - timeawake)*60
    minutesspent += 1
    totalhotdogs += hotdogsperminute
    timeremaining -= (minutesremovedfromhotdogconsumption * hotdogsperminute) + 1
    livedminutes += 1
   
   

print('hot dogs wolfed: '+ str(totalhotdogs-hotdogsperminute))
print(timeremaining)
if timeremaining < 0 and timeremaining > -37:
    print('you died while partially eating a hot dog')
    portion = abs(timeremaining) / (minutesremovedfromhotdogconsumption + 1)
    portionPercent = portion * 100
    print('you died while through '+str(portionPercent)+'% of a hot dog')
elif timeremaining < -37:
    print('you died peacefully in your sleep')
else:
    print('you died after eating a complete hot dog')
print ('your age at death: '+ str(livedminutes / minutesinyear))



