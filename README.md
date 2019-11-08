# SE_Measurement

SoftwareMeasurementReport.pdf is a report of the ways in which the software engineering process can be measured

get.py is a try of github api
this python file will genereate three files

for example
I use query user:jaredpalmer (a trending developer)

then the fulljson.json write all data from github
data.json and info.txt write required data in get.py

how to solve the problem of API Rate Limiting
I use order and paging control, as one page of GitHub is limited to 100 message
page=1&per_page=100&sort=stars&order=desc
