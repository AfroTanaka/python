class SchoolReport:
    school_name = 'Sample middle school'
    def __init__(self, student_name,
                 math_score, jp_score, en_score):
        self.student_name = student_name
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score
    
    def calc_avg_score(self):
        sum_score = (self.math_score + self.jp_score
                     + self.en_score)
        avg_score = sum_score / 3
        return avg_score

sr = SchoolReport('Tanaka A', 100, 30, 50)
print(sr.school_name)
SchoolReport.school_name = 'Sample High School'
print(sr.school_name)

sr_a = SchoolReport('tanaka A', 100, 30, 50)
avg_a = sr_a.calc_avg_score()
print(f'The three subjects average for A: {avg_a}')



sr_b = SchoolReport('suzuki B', 20, 59, 20)
avg_b = sr_b.calc_avg_score()
print(f'The three subjects average for B: {avg_b}')

sr_c = SchoolReport('saito C', 19, 22, 19)
avg_c = sr_c.calc_avg_score()
print(f'The three subjects average for C: {avg_c}')
