import sqlite3
from sqlite3 import Error


def create_connection(path):
    """
    Open a connection to the SQLite DB.

    If there is no existing Database at the entered path one will be created.

    :param path: Absolute path to the location of the Database, or where the Database will be created.
    :return connection: Returns the connection Database object.
    """

    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(r"C:\Users\Tristan\Desktop\school_project\app\db.sqlite")


def execute_query(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        connect.commit()
        print("Query executed successfully")
    except Error as e:
        print(f" The error {e} occurred")


create_students_table = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""


create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES students (id)
);
"""


create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES  users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
)"""

create_students = """
INSERT INTO
    students (name, age, gender, nationality)
VALUES
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 50, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada');
"""

create_posts = """
INSERT INTO
    posts (title, description, user_id)
VALUES
    ("Happy", 'I am feeling very happy today', 1),
    ("Hot Weather", "The weather is very hot today", 2),
    ("Help", "I need some help with my work", 2),
    ("Great News", "I am getting married", 1),
    ("Interesting Game", "It was a fantastic game of tennis", 5),
    ("Party", "anyone up for a late-night party today?", 3);
"""

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_students = "SELECT * from students"
students = execute_read_query(connection, select_students)

# for student in students:
#     print(student)


select_posts = "SELECT * FROM posts"
posts = execute_read_query(connection, select_posts)

# for post in posts:
#     print(post)


select_students_posts = """
SELECT
    students.id,
    students.name,
    posts.description
FROM
    posts
    INNER JOIN students ON students.id = posts.user_id
"""

students_posts = execute_read_query(connection, select_students_posts)

# for students_post in students_posts:
#     print(students_post)


select_posts_comments_students = """
SELECT
    posts.description as post,
    text as comment,
    name
FROM
    posts
    INNER JOIN comments ON posts.id = comments.post_id
    INNER JOIN students on students.id = comments.user_id
"""

posts_comments_students = execute_read_query(connection, select_posts_comments_students)

# for posts_comments_student in posts_comments_students:
#     print(posts_comments_student)


cursor = connection.cursor()
cursor.execute(select_posts_comments_students)
cursor.fetchall()

# column_names = [description[0] for description in cursor.description]
# print(column_names)


select_post_likes = """
SELECT
    description as Post,
    COUNT(likes.id) as Likes
FROM
    likes,
    posts
WHERE
    posts.id = likes.post_id
GROUP BY
    likes.post_id
"""

# post_likes = execute_read_query(connection, select_post_likes)
# for post_like in post_likes:
#     print(post_like)


############## UPDATING ###################

select_post_description = "SELECT description FROM posts WHERE id = 2"

post_description = execute_read_query(connection, select_post_description)

# for description in post_description:
#     print(description)

update_post_description = """
UPDATE
    posts
SET
    description = "The weather has become pleasant now"
WHERE
    id = 2
"""

# execute_query(connection, update_post_description)


################### DELETING ##############

delete_comment = "DELETE FROM comments WHERE id = 5"
execute_query(connection, delete_comment)