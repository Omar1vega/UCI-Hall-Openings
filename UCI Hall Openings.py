import os

import requests

""" Written By Omar Vega
    https://github.com/Omar1vega/
"""


def get_classes():
    # Downloads Entire Web Schedule of Classes Database, by course code range (1000-99999), saves to a file
    if os.path.exists('WebSocFile.txt'): os.remove('WebSocFile.txt')
    with open('WebSocFile.txt', 'a') as webSocFile:
        for i in range(1, 100):
            range_start = i * 1000
            range_stop = range_start + 999
            ranges = str(range_start) + '-' + str(range_stop)

            url = 'https://www.reg.uci.edu/perl/WebSoc/?YearTerm=2016-14&ShowComments=on&ShowFinals=on&Breadth=ANY' \
                  '&Dept=+ALL&CourseNum=&Division=ANY&CourseCodes=' + ranges + \
                  '&InstrName=&CourseTitle=&ClassType=ALL&Units=&Days=&StartTime=&EndTime=&MaxCap=&FullCourses=ANY' \
                  '&FontSize=100&CancelledCourses=Exclude&Bldg=&Room=&Submit=Display+Text+Results '

            classes = requests.get(url).text
            webSocFile.write(classes)
            print("Done with course codes " + ranges)


def main():
    search_term = input("Enter a Hall/Classroom to search for, e.g. 'HIB 100' , 'SSLH 100' \n").upper()
    times_open_list = []

    #    getClasses()  # Use to update class database
    with open("WebSocFile.txt") as webSoc:
        for line in webSoc:

            if search_term in line and '@' not in line:
                line = line.strip()
                line = line.split()
                if 'M' in line[6] and 'W' not in line[6] and "F" not in line[6]:  # Monday only classes
                    times_open_list.append('Monday' + str(line[7:9]))
                if 'M' not in line[6] and 'W' in line[6] and "F" not in line[6]:  # Wednesday only classes
                    times_open_list.append('Wednesday' + str(line[7:9]))
                if 'M' not in line[6] and 'W' not in line[6] and "F" in line[6]:  # Friday only classes
                    times_open_list.append('Friday' + str(line[7:9]))
                if 'Tu' in line[6] and 'Th' not in line[6]:  # Tuesday only classes
                    times_open_list.append('Tuesday' + str(line[7:9]))
                if 'Tu' not in line[6] and 'Th' in line[6]:  # Thursday only classes
                    times_open_list.append('Thursday' + str(line[7:9]))

                if 'M' in line[6] and 'W' in line[6] and "F" not in line[6]:  # MW classes
                    times_open_list.append('Monday' + str(line[7:9]))
                    times_open_list.append('Wednesday' + str(line[7:9]))
                if 'M' in line[6] and 'W' in line[6] and "F" in line[6]:  # MWF classes
                    times_open_list.append('Monday' + str(line[7:9]))
                    times_open_list.append('Wednesday' + str(line[7:9]))
                    times_open_list.append('Friday' + str(line[7:9]))
                if 'Tu' in line[6] and 'Th' in line[6]:  # TuTh classes
                    times_open_list.append('Tuesday' + str(line[7:9]))
                    times_open_list.append('Thursday' + str(line[7:9]))

        print("These Are The Times The Room Has Class, \nTimes Not Listed Are The Times The Room Is Open")
        times_open_list = sorted(list(set(times_open_list)))

        with open('TimesAvailableFor ' + search_term + '.txt', 'a') as output:
            for item in times_open_list:
                print(item)
                output.write(item)
                output.write("\n")


main()
