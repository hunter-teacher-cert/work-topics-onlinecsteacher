* Last Name: Wingreen
* First Name: Emma

Mini-lesson 1: https://colab.research.google.com/drive/1FMBkKcnW_xBXcW6gXiESX-_0eOILZskq#scrollTo=aFc0nJKs-7SM \
Mini-lesson 2: https://colab.research.google.com/drive/1Ybmy6EvGM4P1xoYM0FSxkJAHXvoZS-B9#scrollTo=IAexcPP4aXp2 \
Mini-lesson 3: https://colab.research.google.com/drive/10IzBNh9b0uDJWCwSt9bpTaBM40BSeTby

#Homework Query
SELECT s.First, s.Last, s.studentID, s.Grade, s.ScanTime, s.Status, 
Date, CourseSection, Attendance, Teacher, Period
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.studentID=p.studentID AND SUBSTR(s.scanTime, 1, 9)=p.date
WHERE Attendance = "A"
ORDER BY s.Last ASC


