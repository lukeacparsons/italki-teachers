import json
import pathlib
import fnmatch
import csv
import dateutil.parser
from datetime import date



def get_teacher_attributes(page_file):
    test = json.load(page_file)
    data = test.get('data')
    for teacher in data:
        session_count = teacher.get('teacher_info').get('session_count')
        user_id = teacher.get('user_info').get('user_id')
        is_pro = teacher.get('user_info').get('is_pro')
        sign_up_date = teacher.get('teacher_info').get('first_valid_time')
        yourdate = dateutil.parser.parse(sign_up_date).date()
        today = date.today()
        days_since_sign_up = (today-yourdate).days
        student_count = teacher.get('teacher_info').get('student_count')
        session_to_student_ratio = session_count / student_count if int(student_count) != 0 else 0  
        url = 'https://www.italki.com/teacher/'+str(user_id)+'/russian'
        min_price = teacher.get('course_info').get('min_price')
        print(user_id, session_to_student_ratio, sign_up_date, days_since_sign_up, session_count, url, is_pro, min_price)

#with open('teachers.csv', mode='w') as teacher_file:
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
for path in pathlib.Path("pages").iterdir():
#for path in glob.glob("pages/page*.json").iterdir():
    if fnmatch.fnmatch(path, 'page*.json'):
        if path.is_file():
            current_file = open(path, "r")
            get_teacher_attributes(current_file)
            current_file.close()

#current_file = open("pages/page_43.json", "r")
#get_teacher_attributes(current_file)

# first crawl and update the pages.

# then loop through the pages.

# extract the values required from each page.

# output the values to a file/db/airtable?? somewhere.
