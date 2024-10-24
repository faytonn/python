beginningYear=0
endingYear=0
totalDays = 0


while True:
   if beginningYear < 1600 or beginningYear > 2100:
    beginningYear = int(input())
    endingYear = int(input())
   else:
        break

while True:
    if endingYear < 1600 or endingYear > 2100:
            endingYear = int(input())


    for year in range(beginningYear, endingYear + 1):
            totalDays += 365
            if (year - 1600) % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    continue
                totalDays += 1
    break

print(totalDays)
        
