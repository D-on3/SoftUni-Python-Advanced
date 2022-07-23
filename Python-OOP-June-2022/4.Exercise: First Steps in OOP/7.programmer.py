class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        self.course_name = course_name
        self.new_language = language
        self.skills_earned = skills_earned
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        self.new_language = new_language
        self.skills_needed = skills_needed
        self.old_language = self.language

        if skills_needed <= self.skills and new_language != self.language:
            self.language = new_language
            return f"{self.name} switched from {self.old_language} to {new_language}"
        elif skills_needed <= self.skills and new_language == self.language:
            return f"{self.name} already knows {self.language}"
        elif skills_needed > self.skills:
            return f"{self.name} needs {abs(skills_needed - self.skills)} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
