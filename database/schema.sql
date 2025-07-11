PRAGMA foreign_keys = ON;

-- USERS (all login users, any role)
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('admin','student','teacher','staff','parent','account')),
    created_at TEXT DEFAULT (datetime('now')),
    last_login TEXT
);

-- BATCHES (student batches)
CREATE TABLE IF NOT EXISTS batches (
    batch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_name TEXT UNIQUE NOT NULL,   -- e.g. 'Batch 01'
    year INTEGER,
    description TEXT
);

-- DEPARTMENTS
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT UNIQUE NOT NULL,
    description TEXT
);

-- STUDENTS (core info)
CREATE TABLE IF NOT EXISTS students (
    stu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    batch_id INTEGER NOT NULL,
    dept_id INTEGER,
    photo BLOB,
    name TEXT NOT NULL,
    gender TEXT CHECK (gender IN ('Male', 'Female')),
    dob TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    enroll_date TEXT DEFAULT (date('now')),
    pob TEXT,
    scholarship_flag TEXT DEFAULT 'N' CHECK (scholarship_flag IN ('Y', 'N')),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- STUDENT COURSES (multi-step registration)
CREATE TABLE IF NOT EXISTS student_courses (
    sc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stu_id INTEGER NOT NULL,
    from_school TEXT,
    grade TEXT,
    attach_file BLOB,
    bac2_date TEXT,
    major TEXT,
    study_shift TEXT,
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE
);

-- PARENTS info
CREATE TABLE IF NOT EXISTS parents (
    parent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stu_id INTEGER NOT NULL,
    father_name TEXT,
    father_job TEXT,
    father_phone TEXT,
    mother_name TEXT,
    mother_job TEXT,
    mother_phone TEXT,
    relative_name TEXT,
    relative_job TEXT,
    relative_phone TEXT,
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE
);

-- STUDENT ACHIEVEMENTS
CREATE TABLE IF NOT EXISTS student_achievements (
    achievement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stu_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    date_awarded TEXT,
    file_attachment BLOB,
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE
);

-- TEACHERS
CREATE TABLE IF NOT EXISTS teachers (
    tea_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    dept_id INTEGER,
    photo BLOB,
    name TEXT NOT NULL,
    gender TEXT CHECK (gender IN ('Male', 'Female')),
    dob TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    enroll_date TEXT DEFAULT (date('now')),
    pob TEXT,
    bank_code TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- TEACHER COURSES/QUALIFICATIONS
CREATE TABLE IF NOT EXISTS teacher_courses (
    tc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tea_id INTEGER NOT NULL,
    skill TEXT,
    grade TEXT,
    attach_certificate BLOB,
    job_major TEXT,
    FOREIGN KEY (tea_id) REFERENCES teachers(tea_id) ON DELETE CASCADE
);

-- TEACHER EVALUATIONS
CREATE TABLE IF NOT EXISTS teacher_evaluations (
    evaluation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tea_id INTEGER NOT NULL,
    evaluator TEXT,
    score INTEGER,
    comments TEXT,
    eval_date TEXT,
    FOREIGN KEY (tea_id) REFERENCES teachers(tea_id) ON DELETE CASCADE
);

-- TEACHER REQUESTS
CREATE TABLE IF NOT EXISTS teacher_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tea_id INTEGER NOT NULL,
    request_type TEXT,
    description TEXT,
    status TEXT CHECK(status IN ('Pending', 'Approved', 'Rejected')),
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (tea_id) REFERENCES teachers(tea_id) ON DELETE CASCADE
);

-- STAFFS
CREATE TABLE IF NOT EXISTS staffs (
    sta_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    dept_id INTEGER,
    photo BLOB,
    name TEXT NOT NULL,
    gender TEXT CHECK (gender IN ('Male', 'Female')),
    dob TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    enroll_date TEXT DEFAULT (date('now')),
    pob TEXT,
    bank_code TEXT,
    position TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- STAFF COURSES/QUALIFICATIONS
CREATE TABLE IF NOT EXISTS staff_courses (
    sc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sta_id INTEGER NOT NULL,
    skill TEXT,
    grade TEXT,
    attach_certificate BLOB,
    FOREIGN KEY (sta_id) REFERENCES staffs(sta_id) ON DELETE CASCADE
);

-- COURSES
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_id INTEGER,
    course_name TEXT UNIQUE NOT NULL,
    description TEXT,
    is_local INTEGER DEFAULT 1,   -- 1: local, 0: international
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- STUDENT ENROLLMENTS (Many to Many)
CREATE TABLE IF NOT EXISTS student_enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stu_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- TEACHER ASSIGNMENTS (Many to Many)
CREATE TABLE IF NOT EXISTS teacher_assignments (
    assign_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tea_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (tea_id) REFERENCES teachers(tea_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- LIBRARY BOOKS
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    dept_id INTEGER,
    book_name TEXT NOT NULL,
    author TEXT,
    create_date TEXT,
    published_year INTEGER,
    publisher TEXT,
    language TEXT,
    total_copies INTEGER DEFAULT 1,
    book_image BLOB,
    is_ebook INTEGER DEFAULT 0,   -- 1: E-book, 0: Physical
    file_attachment BLOB,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- LIBRARY BORROW/OWE
CREATE TABLE IF NOT EXISTS book_borrow (
    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    stu_id INTEGER NOT NULL,
    borrow_date TEXT,
    due_date TEXT,
    return_date TEXT,
    status TEXT CHECK(status IN ('Borrowed', 'Returned', 'Owe')),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE
);

-- E-LIBRARY HISTORY
CREATE TABLE IF NOT EXISTS elibrary_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    stu_id INTEGER NOT NULL,
    access_date TEXT DEFAULT (datetime('now')),
    action TEXT,         -- e.g., 'download', 'read', 'preview'
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE
);

-- PAYMENTS
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stu_id INTEGER NOT NULL,
    total_price REAL NOT NULL,
    discount REAL,
    payment_price REAL NOT NULL,
    payment_type TEXT,      -- KHQR, Physical
    invoice_id TEXT,
    payment_date TEXT DEFAULT (datetime('now')),
    payment_for TEXT,       -- tuition, library, parking, etc.
    term TEXT,              -- 3 month, yearly, etc.
    status TEXT DEFAULT 'Paid',
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE
);

-- INCOME TRACKING
CREATE TABLE IF NOT EXISTS income (
    income_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    amount REAL NOT NULL,
    received_date TEXT DEFAULT (datetime('now')),
    remark TEXT
);

-- EXPENSE TRACKING
CREATE TABLE IF NOT EXISTS expense (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    amount REAL NOT NULL,
    paid_date TEXT DEFAULT (datetime('now')),
    remark TEXT
);

-- SCHEDULES (all users)
CREATE TABLE IF NOT EXISTS schedules (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    course_id INTEGER,
    title TEXT,
    description TEXT,
    start_time TEXT,
    end_time TEXT,
    location TEXT,
    type TEXT,           -- class, exam, event, etc.
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- ACTIVITY LOGS
CREATE TABLE IF NOT EXISTS activity_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    action TEXT,
    action_time TEXT DEFAULT (datetime('now')),
    details TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ATTENDANCE
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stu_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    attendance_date TEXT NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late')),
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- EXAMS
CREATE TABLE IF NOT EXISTS exams (
    exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    exam_name TEXT,
    exam_date TEXT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- RESULTS
CREATE TABLE IF NOT EXISTS results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_id INTEGER NOT NULL,
    stu_id INTEGER NOT NULL,
    score REAL,
    grade TEXT,
    gpa REAL,
    term TEXT,
    FOREIGN KEY (exam_id) REFERENCES exams(exam_id) ON DELETE CASCADE,
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE
);

-- ASSIGNMENTS
CREATE TABLE IF NOT EXISTS assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    title TEXT,
    description TEXT,
    due_date TEXT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- SUBMISSIONS
CREATE TABLE IF NOT EXISTS submissions (
    submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL,
    stu_id INTEGER NOT NULL,
    submission_date TEXT,
    file_attachment BLOB,
    grade REAL,
    feedback TEXT,
    FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id) ON DELETE CASCADE,
    FOREIGN KEY (stu_id) REFERENCES students(stu_id) ON DELETE CASCADE
);

-- EXPERIENCE (student & teacher)
CREATE TABLE IF NOT EXISTS experience (
    exp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    role TEXT,
    title TEXT,
    description TEXT,
    start_date TEXT,
    end_date TEXT,
    file_attachment BLOB,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- SURVEY
CREATE TABLE IF NOT EXISTS surveys (
    survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS survey_questions (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    survey_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    FOREIGN KEY (survey_id) REFERENCES surveys(survey_id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS survey_answers (
    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    answer_text TEXT,
    answer_date TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (question_id) REFERENCES survey_questions(question_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Notification (for dashboards)
CREATE TABLE IF NOT EXISTS notifications (
    notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now')),
    is_read INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


-- Indexes for faster search
CREATE INDEX IF NOT EXISTS idx_students_name ON students(name);
CREATE INDEX IF NOT EXISTS idx_teachers_name ON teachers(name);
CREATE INDEX IF NOT EXISTS idx_staffs_name ON staffs(name);
CREATE INDEX IF NOT EXISTS idx_books_name ON books(book_name);
CREATE INDEX IF NOT EXISTS idx_courses_name ON courses(course_name);
CREATE INDEX IF NOT EXISTS idx_students_batch ON students(batch_id);

INSERT INTO users (username, password_hash, role) VALUES ('adm', '123', 'admin');
INSERT INTO users (username, password_hash, role) VALUES ('stu', '123', 'student');
INSERT INTO users (username, password_hash, role) VALUES ('tea', '123', 'teacher');
INSERT INTO users (username, password_hash, role) VALUES ('acc', '123', 'account');
INSERT INTO users (username, password_hash, role) VALUES ('pa', '123', 'parent');
INSERT INTO users (username, password_hash, role) VALUES ('mstu', '123', 'manage_student_parent');
INSERT INTO users (username, password_hash, role) VALUES ('mtea', '123', 'manage_teacher');
INSERT INTO users (username, password_hash, role) VALUES ('eli', '123', 'elibrary');
INSERT INTO users (username, password_hash, role) VALUES ('cou', '123', 'course');

