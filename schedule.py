import random
import re

f = open("output.txt", "w")
# g = open("names.txt", "r")
u = open("unavailable.txt", "r")
s = open("schedule.txt", "r")
rand = open("random.txt", "w")

midweek = [0, 1, 2, 3]
treasures = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
gems = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
closing = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13]
living = list(range(13))
living2 = list(range(13))

random.shuffle(midweek)
random.shuffle(treasures)
random.shuffle(gems)
random.shuffle(closing)
random.shuffle(living)
random.shuffle(living2)

rand.write(str(midweek))
rand.write(str(treasures))
rand.write(str(gems))
rand.write(str(closing))
rand.write(str(living))
rand.write(str(living2))

smidweek = [3, 1, 0, 2]
streasures = [0, 6, 7, 3, 8, 2, 5, 1, 9, 4]
sgems = [8, 3, 7, 12, 5, 4, 2, 10, 6, 9, 11, 0, 1]
sclosing = [6, 8, 2, 3, 9, 7, 5, 0, 4, 1, 10, 13]
sliving = [2, 5, 9, 6, 10, 3, 12, 1, 11, 0, 7, 8, 4]
sliving2 = [8, 1, 0, 4, 10, 7, 2, 12, 3, 6, 5, 9, 11]

week = 0

smidweekcount = 0
studycount = 0
streasurescount = 0
sgemscount = 0
sclosingcount = 0
slivingcount = 0
slivingcount2 = 0

midweeklist = []
studylist = []
treasureslist = []
gemslist = []
closinglist = []
livinglist = []
livinglist2 = []

schedulelines = s.read().splitlines()

unavailablelines = u.read().splitlines()
numberofppl = len(unavailablelines)

unavailable = []
for i in range(numberofppl):
    temp = []
    unavailable.append(temp)

names = []

for i in unavailablelines:
    if i == "":
        unavailablelines.remove(i)

for i in range(len(unavailablelines)):
    split = unavailablelines[i].split()
    if len(split) > 2:
        for j in range(len(split)-2):
            unavailable[i].append(split[j+2])
    names.append("(" + split[0] + " " + split[1] + ")")
#print(unavailable)

weekname = []
livingcount = []
for i in schedulelines:
    weekname.append((i.split())[0])
    livingcount.append((i.split())[1])

#(livingcount)

count1 = 0
count2 = 0
for i in unavailable:
    for j in i:
        for k in weekname:
            if j == k:
                #print(weekname.index(k))
                unavailable[count1][count2] = str(weekname.index(k))
        count2 += 1
    count1 += 1

#(unavailable)

for i in schedulelines:
    midweeklist.append(midweek[(smidweekcount + week) % len(midweek)])
    while str(week) in unavailable[midweeklist[week]]:
        midweeklist.pop(week)
        smidweekcount += 1
        midweeklist.append(midweek[(week + smidweekcount) % len(smidweek)])

    studylist.append(midweek[(studycount + week) % len(midweek)])
    while str(week) in unavailable[studylist[week]] or midweeklist[week] == studylist[week]:
        studylist.pop(week)
        studycount += 1
        studylist.append(midweek[(week + studycount) % len(midweek)])

    treasureslist.append(treasures[week % len(treasures)])
    while midweeklist[week] == treasureslist[week] or studylist[week] == treasureslist[week] or str(week) in unavailable[treasureslist[week]]:
        treasureslist.pop(week)
        treasureslist.append(streasures[(streasurescount - 1) % len(streasures)])
        streasurescount += 1

    gemslist.append(gems[week % len(gems)])
    while gemslist[week] == midweeklist[week] or studylist[week] == gemslist[week] or gemslist[week] == treasureslist[week] or str(week) in unavailable[gemslist[week]]:
        gemslist.pop(week)
        gemslist.append(sgems[(sgemscount-1) % len(sgems)])
        sgemscount += 1

    livinglist.append(living[week % len(living)])
    print(livinglist)
    while livinglist[week] == midweeklist[week] or livinglist[week] == studylist[week] or livinglist[week] == treasureslist[week] or livinglist[week] == gemslist[week] or str(week) in unavailable[livinglist[week]]:
        livinglist.pop(week)
        livinglist.append(sliving[(slivingcount-1) % len(sliving)])
        slivingcount += 1
    print(livingcount)
    if livingcount[week] == str(1):
        print("here")
        livinglist2.append(False)
    elif livingcount[week] == str(2):
        print("here")
        livinglist2.append(living2[week % len(living2)])
        while livinglist2[week] == midweeklist[week] or livinglist2[week] == studylist[week] or livinglist2[week] == treasureslist[week] or livinglist2[week] == gemslist[week] or livinglist2[week] == livinglist[week] or str(week) in unavailable[livinglist[week]]:
            livinglist2.pop(week)
            livinglist2.append(sliving2[(slivingcount2 - 1) % len(sliving2)])
            slivingcount2 += 1

    closinglist.append(closing[week % len(closing)])
    print(livinglist2)
    while closinglist[week] == midweeklist[week] or closinglist[week] == studylist[week] or closinglist[week] == treasureslist[week] or closinglist[week] == gemslist[week] or closinglist[week] == livinglist[week] or closinglist[week] == livinglist2[week] or str(week) in unavailable[closinglist[week]]:
        closinglist.pop(week)
        closinglist.append(sclosing[(sclosingcount - 1) % len(sclosing)])
        sclosingcount += 1

    week += 1
# print(midweeklist)
# print(treasureslist)
# print(gemslist)
# print(closinglist)

for i in range(week):
    if livinglist2[i] == False:
        f.write(weekname[i] + " " + names[midweeklist[i]] + " " + names[treasureslist[i]] + " "
                + names[gemslist[i]] + " " + names[studylist[i]] + " " + names[livinglist[i]] + " / " + names[closinglist[i]])
        f.write("\n")
    else:
        f.write(weekname[i] + " " + names[midweeklist[i]] + " " + names[treasureslist[i]] + " "
                + names[gemslist[i]] + " " + names[studylist[i]] + " " + names[livinglist[i]] + " "
                + names[livinglist2[i]] + " " + names[closinglist[i]])
        f.write("\n")

f.close()

validatemidweek = []
validatetreasures = []
validategems = []
validateclosing = []

for i in range(max(midweek)+1):
    validatemidweek.append(midweeklist.count(i))

for i in range(max(treasures)+1):
    validatetreasures.append(treasureslist.count(i))

for i in range(max(gems)+1):
    validategems.append(gemslist.count(i))

for i in range(max(closing)+1):
    validateclosing.append(closinglist.count(i))

print(validatemidweek)
print(validatetreasures)
print(validategems)
print(validateclosing)

u.close()

import csv

names = []

for i in range(len(unavailablelines)):
    split = unavailablelines[i].split()
    if len(split) > 2:
        for j in range(len(split)-2):
            unavailable[i].append(split[j+2])
    names.append(split[0] + " " + split[1])


with open('output.csv', mode='w') as output:
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([' ','midweek chairman','treasures','gems','living','living2','bible study','closing'])
    for i in range(week):
        if livinglist2[i] == False:
            writer.writerow([weekname[i],names[midweeklist[i]],names[treasureslist[i]],names[gemslist[i]],names[livinglist[i]],' ',names[studylist[i]],names[closinglist[i]]])
        else:
            writer.writerow([weekname[i],names[midweeklist[i]],names[treasureslist[i]],names[gemslist[i]],names[livinglist[i]],names[livinglist2[i]],names[studylist[i]],names[closinglist[i]]])

