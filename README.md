# SE_Measurement

SoftwareMeasurementReport.pdf is a report of the ways in which the software engineering process can be measured

get.py is a try of github api.
This python file will genereate three files

For example
I use query user:jaredpalmer (a trending developer)

Then the fulljson.json write all data from github.
data.json and info.txt write required data in get.py.

how to solve the problem of API Rate Limiting?
I use order and paging control, as one page of GitHub is limited to 100 message
page=1&per_page=100&sort=stars&order=desc


Data Visualisation:
Firstly, get languages.json with programming language stastics by get.py
(Which repo do I use? repo:jumpserver/jumpserver    https://api.github.com/repos/jumpserver/jumpserver/languages)
Then visualization.html can use this json file and d3js

Final result: https://github.com/scyqa1/SE_Measurement/blob/master/data.png
![Image text]( https://github.com/scyqa1/SE_Measurement/blob/master/data.png)
