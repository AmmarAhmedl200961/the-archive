# Question 3:
# For each student find the percentage of time spent by the student in a course in Spring 2020. Write an efficient MapReduce
# algorithm to perform above task.
# Percentage of the time spend by a student A in course B = (Time spend by the student A in a course B classroom / Total time spent by all students in course B classroom) * 100

# Output format for above Question
# (Student rollnumber, course -> Percentage of the time spend by a student A in course B (sem C))
# Output for given input
# L20-4305, BigData -> 100%
# L20-4305, DataMining -> 60%
# L20-1111, DataMining -> 40%

# Hint: This problem is similar to relative frequency word co-occurrence problem discussed in the class.


import re
from mrjob.job import MRJob

reg_login = re.compile(r'Login:\d{2}-\d{2}-\d{2}-\d{1,2}:\d{2}')
reg_logout = re.compile(r'Logout:\d{2}-\d{2}-\d{2}-\d{1,2}:\d{2}')

def convert_to_seconds(time_str):
    hours, minutes = map(int, time_str.split(':'))
    seconds = hours * 3600 + minutes * 60
    return seconds

class CourseAccess(MRJob):

    def mapper(self, _, line):
        # Extract relevant information from the record
        student_rollnumber, course = line.split(' ')[0], line.split(' ')[1]
        login = reg_login.search(line).group()
        logout = reg_logout.search(line).group()
        # access time only
        login = login.split('-')[-1]
        logout = logout.split('-')[-1]
        # convert to 24-hour format
        login_seconds = convert_to_seconds(login)
        logout_seconds = convert_to_seconds(logout)
        if logout_seconds < login_seconds:
            logout_seconds += 86400  # add 24 hours
        time_spent = logout_seconds - login_seconds
        # Emit intermediate key-value pair
        yield (student_rollnumber, course), time_spent
                
    def reducer(self, key, course_time_spent):
        student, course = key
        # course_time = 0
        # for course, _ in key:
        #     course_time += course_time_spent
        total_time_spent = sum(course_time_spent)
        yield (student, course), total_time_spent
        
if __name__ == '__main__':
    CourseAccess.run()
