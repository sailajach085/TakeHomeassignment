DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS student_submission;
DROP TABLE IF EXISTS roster;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS course_work;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);


CREATE TABLE student_submission (
    submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_work_id INTEGER,
    course_id INTEGER,
    student_id INTEGER,
    _status TEXT CHECK( _status IN ('NEW','TURNED_IN')),
    assigned_points Float,
    max_points Float
);

CREATE TABLE roster (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER
);

CREATE TABLE student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    school TEXT NOT NULL,
    grade_level INTEGER
);

CREATE TABLE course (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER,
    name TEXT NOT NULL
);

CREATE TABLE course_work (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    due TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);