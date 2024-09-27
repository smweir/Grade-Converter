import math, tkinter

window = tkinter.Tk()
window.geometry("500x300")

def grade_con(grade):
    if grade >= 90:
        return("A")
    elif grade >= 80 and grade <= 89:
        return("B")
    elif grade >= 70 and grade <= 79:
        return("C")
    elif grade >= 65 and grade <= 69:
        return("D")
    else:
        return("F")

def average(testscore):
    testsum = 0
    for i in testscore:
        testsum += i
    average = testsum / len(testscore)
    print("your test average is " + grade_con(average))

def median(testscore):
    testscore.sort()
    print(testscore)
    if len(testscore) % 2 == 0: #even
        mid = len(testscore) / 2
        median = (testscore[mid] + testscore[mid - 1]) / 2
    else:
        mid = int(math.ceil(len(testscore) / 2))
        median = testscore[mid]
    print("your test median is " + str(median))

median([9,87,93,72,84])

def entrybox(button):
    if button["text"] == 2:
        entry1 = tkinter.Entry(window, text = "")
        entry1.pack()
        entry2 = tkinter.Entry(window, text = "")
        entry2.pack()
    if button["text"] == 3:
        entry3 = tkinter.Entry(window, text = "")
        entry3.pack()
        entry4 = tkinter.Entry(window, text = "")
        entry4.pack()
        entry5 = tkinter.Entry(window, text = "")
        entry5.pack()
    if button["text"] == 4:
        entry6 = tkinter.Entry(window, text = "")
        entry6.pack()
        entry7 = tkinter.Entry(window, text = "")
        entry7.pack()
        entry8 = tkinter.Entry(window, text = "")
        entry8.pack()
        entry9 = tkinter.Entry(window, text = "")
        entry9.pack()



print("welcome to the grade converter, input your test scores here ")
Label1 = tkinter.Label(window, text = "how many test scores are there?")
Label1.pack()
button1 = tkinter.Button(window, text = "2", command = lambda:entrybox(button1))
button1.pack()
button2 = tkinter.Button(window, text = "3", command = lambda:entrybox(button2))
button2.pack()
button3 = tkinter.Button(window, text = "4", command = lambda:entrybox(button3))
button3.pack()
numtest = int(input("how many test scores are there? "))
tests = []
for i in range(numtest):
    numscore = int(input("what is your test score for " + str(i + 1) + " "))
    tests.append(numscore)
    print(grade_con(numscore))


average(tests)
testrem = int(input("How many tests do you have left? "))
A = 90
B = 80
C = 70
D = 65
F = 0
desgrade = input("What grade do you want to get? ")
if desgrade == "A":
    desgrade = 90
elif desgrade == "B":
    desgrade = 80
elif desgrade == "C":
    desgrade = 70
elif desgrade == "D":
    desgrade = 65
totalsum = desgrade * (testrem + numtest)
oldsum = 0 
for score in tests:
    oldsum += score
newsum = totalsum - oldsum
newavg = newsum / testrem
if desgrade == 90:
    desgrade = "A"
elif desgrade == 80:
    desgrade = "B"
elif desgrade == 70:
    desgrade = "C"
elif desgrade == 65:
    desgrade = "D"
print("To get a score of " + str(desgrade) + " you need " + str(newavg) + " on the remaining " + str(testrem) + " tests")


window.mainloop()




