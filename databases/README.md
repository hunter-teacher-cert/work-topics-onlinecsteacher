* Last Name: Wingreen
* First Name: Emma

## Google Colabs

Mini-lesson 1: https://colab.research.google.com/drive/1FMBkKcnW_xBXcW6gXiESX-_0eOILZskq#scrollTo=aFc0nJKs-7SM \
Mini-lesson 2: https://colab.research.google.com/drive/1Ybmy6EvGM4P1xoYM0FSxkJAHXvoZS-B9#scrollTo=IAexcPP4aXp2 \
Mini-lesson 3: https://colab.research.google.com/drive/10IzBNh9b0uDJWCwSt9bpTaBM40BSeTby

## Homework Query

SELECT s.First, s.Last, s.studentID, s.Grade, s.ScanTime, s.Status, \
Date, CourseSection, Attendance, Teacher, Period \
FROM scan AS s \
INNER JOIN periodAtt AS p \
ON s.studentID=p.studentID AND SUBSTR(s.scanTime, 1, 9)=p.date \
WHERE Attendance = "A" \
ORDER BY s.Last ASC

## Async Query 1
### A list of all teachers whose classes are cut most often

SELECT teacher, COUNT(*) AS total FROM \
(SELECT s.First, s.Last, s.studentID, s.Grade, s.ScanTime, s.Status, \
Date, CourseSection, Attendance, Teacher, Period \
FROM scan AS s \
INNER JOIN periodAtt AS p \
ON s.studentID=p.studentID AND SUBSTR(s.scanTime, 1, 9)=p.date \
WHERE Attendance = "A" \
ORDER BY s.Last ASC) \
GROUP BY teacher \
ORDER BY total DESC 

## Async Query 2
### All students who have cut class and parent contact info where available

SELECT * FROM (SELECT s.First, s.Last, s.studentID, s.Grade, s.ScanTime, s.Status, \
Date, CourseSection, Attendance, Teacher, Period \
FROM scan AS s \
INNER JOIN periodAtt AS p \
ON s.studentID=p.studentID AND SUBSTR(s.scanTime, 1, 9)=p.date \
WHERE Attendance = "A" \
ORDER BY s.Last ASC) \
AS allCuts \
INNER JOIN bio AS b \
ON allCuts.studentID=b.studentID \
ORDER BY allCuts.Teacher ASC, allCuts.ScanTime 
