# Light Nates -- Theodore Peters, Ryan Aday
# SoftDev1 pd7
# k17 -- Average (If you know what I mean...)
# 2018-10-09

import sqlite3
from random import choice, randint


db = sqlite3.connect('datta.db') #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

c.execute("CREATE TABLE peeps_avg(id INTEGER PRIMARY KEY, average REAL);")

def get_avgs():
    c.execute("DELETE FROM peeps_avg;")
    c.execute("SELECT id FROM nerds;")
    students = c.fetchall()[:]
    for i in students:
        c.execute("SELECT mark FROM teacher_reviews WHERE teacher_reviews.id={};".format(i[0]))
        grades = c.fetchall()
        avg = 0.0
        for j in grades:
            avg += j[0]
        avg /= len(grades)
        c.execute("INSERT INTO peeps_avg VALUES({}, {});".format(i[0], avg))
def add_course(code, mark, sid):
    c.execute('INSERT INTO teacher_reviews VALUES("{}", {}, {});'.format(code, mark, sid))

get_avgs()
c.execute("SELECT * FROM peeps_avg;")
print('averages of starting courses: \n\n', c.fetchall(), '\n\n\n')
new_classes = ('bazinga school', 'large dum nerd head face school', 'the computer interaction club', 'woodworking', 'making epic posters to advertise the stuyvesant computer interactin club in gimp', 'thinking up good classes to add to stuyvesant highschoool', 'elvis impersonation', 'AP lunch', 'doing the robot', 'art appretiation but with a cirriculum thats good')
for i in range(40):
    add_course(choice(new_classes), randint(25, 99), randint(1, 10))
c.execute("SELECT * FROM teacher_reviews;")
print('new courses:\n\n', c.fetchall(),'\n\n\n')
get_avgs()
c.execute("SELECT * FROM peeps_avg;")
print('new avgs: \n\n', c.fetchall(), '\n\n\n')
db.commit()
db.close()
