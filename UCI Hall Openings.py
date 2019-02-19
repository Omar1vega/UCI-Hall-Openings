import requests

""" Written By Omar Vega
    https://github.com/Omar1vega/
"""


def getClasses():
    # Downloads Entire Web Schedule of Classes Database, by course code range (1000-99999), saves to a file
    with open('WebSocFile.txt', 'a') as webSocFile:
        for i in range(1, 100):
            rangeStart = i * 1000
            rangeStop = rangeStart + 999
            ranges = str(rangeStart) + '-' + str(rangeStop)

        url = 'https://www.reg.uci.edu/perl/WebSoc/?YearTerm=2016-14&ShowComments=on&ShowFinals=on&Breadth=ANY&Dept=+ALL&CourseNum=&Division=ANY&CourseCodes=' + ranges + '&InstrName=&CourseTitle=&ClassType=ALL&Units=&Days=&StartTime=&EndTime=&MaxCap=&FullCourses=ANY&FontSize=100&CancelledCourses=Exclude&Bldg=&Room=&Submit=Display+Text+Results'

            classes = requests.get(url).text
            webSocFile.write(classes)
            print("Done with course codes " + ranges)


def main():
    searchTerm = input("Enter a Hall/Classroom to search for, e.g. 'HIB 100' , 'SSLH 100' \n").upper()
    timesOpenList = []

    ##    getClasses()  ##Use to update class database
    with open("WebSocFile.txt") as webSoc:
        for line in webSoc:

            if (searchTerm in line and '@' not in line):
                line = line.strip()
                line = line.split()
                if 'M' in line[6] and 'W' not in line[6] and "F" not in line[6]:  ##Monday only classes
                    timesOpenList.append('Monday' + str(line[7:9]))
                if 'M' not in line[6] and 'W' in line[6] and "F" not in line[6]:  ##Wednesday only classes
                    timesOpenList.append('Wednesday' + str(line[7:9]))
                if 'M' not in line[6] and 'W' not in line[6] and "F" in line[6]:  ##Friday only classes
                    timesOpenList.append('Friday' + str(line[7:9]))
                if 'Tu' in line[6] and 'Th' not in line[6]:  ##Tuesday only classes
                    timesOpenList.append('Tuesday' + str(line[7:9]))
                if 'Tu' not in line[6] and 'Th' in line[6]:  ##Thursday only classes
                    timesOpenList.append('Thursday' + str(line[7:9]))

                if 'M' in line[6] and 'W' in line[6] and "F" not in line[6]:  ##MW classes
                    timesOpenList.append('Monday' + str(line[7:9]))
                    timesOpenList.append('Wednesday' + str(line[7:9]))
                if 'M' in line[6] and 'W' in line[6] and "F" in line[6]:  ##MWF classes
                    timesOpenList.append('Monday' + str(line[7:9]))
                    timesOpenList.append('Wednesday' + str(line[7:9]))
                    timesOpenList.append('Friday' + str(line[7:9]))
                if 'Tu' in line[6] and 'Th' in line[6]:  ##TuTh classes
                    timesOpenList.append('Tuesday' + str(line[7:9]))
                    timesOpenList.append('Thursday' + str(line[7:9]))
        print("These Are The Times The Room Has Class, \nTimes Not Listed Are The Times The Room Is Open")
        timesOpenList = sorted(list(set(timesOpenList)))
        output = open('TimesAvailablefor ' + searchTerm + '.txt', 'a')

        with open('TimesAvailableFor ' + searchTerm + '.txt', 'a') as output:
            for item in timesOpenList:
                print(item)
                output.write(item)
                output.write("\n")


main()
