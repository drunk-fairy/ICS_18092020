settings = {
    'max_mark_for_individual_task': 50,
    'max_mark_for_one_lab': 10,
    'num_of_labs': 5,
    'mark_for_auto_exam': 90
}

class Student():
    def __init__(self, student_name, settings):
        self.student_name = student_name
        self.settings = settings

        self.lab_tries = 0
        self.last_lab_try_mark = 0

        self.ind_task_tries = 0
        self.last_ind_task_try_mark = 0

        self.lab_1_tries = 0
        self.lab_1_mark = 0

        self.lab_2_tries = 0
        self.lab_2_mark = 0

        self.lab_3_tries = 0
        self.lab_3_mark = 0
        
        self.lab_4_tries = 0
        self.lab_4_mark = 0

        self.lab_5_tries = 0
        self.lab_5_mark = 0

        self.ind_task_tries = 0
        self.ind_task_mark = 0

        self.total_course_mark = 0
      

    def marks_for_lab(self):
        self.lab_1_tries = input('num of lab 1 tries: ')
        self.lab_1_mark = input('mark for lab 1: ')
        self.total_course_mark += int(self.lab_1_mark)

        self.lab_2_tries = input('num of lab 2 tries: ')
        self.lab_2_mark = input('mark for lab 2: ')
        self.total_course_mark += int(self.lab_2_mark)

        self.lab_3_tries = input('num of lab 3 tries: ')
        self.lab_3_mark = input('mark for lab 3: ')
        self.total_course_mark += int(self.lab_3_mark)
        
        self.lab_4_tries = input('num of lab 4 tries: ')
        self.lab_4_mark = input('mark for lab 4: ')
        self.total_course_mark += int(self.lab_4_mark)

        self.lab_5_tries = input('num of lab 5 tries: ')
        self.lab_5_mark = input('mark for lab 5: ')
        self.total_course_mark += int(self.lab_5_mark)


    def mark_for_ind_task(self):
        self.ind_task_tries = input('num of ind task tries: ')
        self.ind_task_mark = input('mark for ind task: ')
        self.total_course_mark += int(self.ind_task_mark)

    def report(self):
        is_exam_auto = False
        if self.total_course_mark >= self.settings['mark_for_auto_exam']:
            is_exam_auto = True
        result_tuple = (self.total_course_mark, is_exam_auto)
        print(f'Total course mark: {result_tuple[0]}\nAuto exam: {result_tuple[1]}')

student = Student('Dima', settings)
student.marks_for_lab()
student.mark_for_ind_task()
student.report()