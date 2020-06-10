# web-scrapper
This is web scrapper.
To run this file you need to install python 3.8 on your system,
then open cmd or terminal in your system and run the following commands:
'pip install requests'
'pip install bs4'
'pip install pandas'
after running these commands one by one
now locate the file directory where web_scrapper.py is downloaded/created
now in cmd go to that directory
now type the following command:
'python (file name - in your case it is web_scrapper.py)' example:-'python web_scrapper.py'
hit enter and wait till 'done' message prints out
then check out same directory in which file includes and find a file named 'data.csv'


if running this code taking longer time than expected
you can change the 8th line in the code that is range(1,253) to range(1,2) and save the file
run again in your cmd and check file in your directory named 'data.csv'
this time you will get result earlier than expected but this data contain only from one page.


Note: Make sure that there must no file exist in the same directory named 'data.csv', else you will get an error.
