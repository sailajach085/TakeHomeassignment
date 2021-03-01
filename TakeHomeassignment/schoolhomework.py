#!/usr/bin/python3
from flask import Flask, render_template, jsonify, request, json
from app import *
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret_key'

"""
Entry point of the app
Author: Sailaja
"""


@app.route('/')
def home():
    """
    Simple message as home page
    """
    return render_template('index.html')


@app.route('/<name>')
def dynamic_api(name):

    conn = get_db_connection()
    data = []
    if name == 'student':
        data = conn.execute('SELECT student_id, _status FROM student_submission Where _status = "TURNED_IN" group by student_id').fetchall()
    elif name == 'course':
        # data = conn.execute('SELECT st.course_id, avg(s.grade_level) FROM student_submission st, student s Where st.student_id = s.student_id group by st.course_id').fetchall()
        data = conn.execute('SELECT course_id, avg(assigned_points) FROM student_submission group by course_id').fetchall()
    elif name == 'teacher':
        data = conn.execute('SELECT c.teacher_id, count(cw.title) FROM course_work cw, course c Where cw.course_id = c.course_id group by c.teacher_id').fetchall()
    elif name == 'school':
        _data = conn.execute('SELECT s.school, count(distinct(sb.student_id)) FROM student_submission sb, student s Where sb.student_id = s.student_id and sb._status = "TURNED_IN" group by s.school having count(sb.student_id)>1').fetchall()
        _data1 = conn.execute('SELECT s.school, count(s.student_id) FROM student s group by s.school').fetchall()

        rowaDict = {}
        rowaDict1 = {}
        
        for row in _data:
            t = (row[0], row[1])
            rowaDict[row[0]] = row[1]

        for row in _data1:
            t = (row[0], row[1])
            rowaDict1[row[0]] = row[1]

        for key,value in rowaDict.items():
            if rowaDict1[key] :
                rowaDict1[key] = (value*100)/rowaDict1[key]
                s = (key, rowaDict1[key])
                data.append(s)
        

    rowarray_list = []
    for row in data:
        t = (row[0], row[1])
        rowarray_list.append(t)

    results = json.dumps(rowarray_list)
    conn.close()

    return results



    

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
