
class People():
    def __init__(self, name, age, job, jobname):
        self.name = name
        self.age = age
        self.job = job
        self.jobname = jobname
    def displayInfo(self):
        print(f"My name is {self.name}!")
        print(f"I am {self.age} years old!")
        print(f"I am an {self.job}!")
        print(f"I work at {self.jobname}!")
    

p1 = People("Lily", 20, "Engineer", "Google")
p2 = People("Joe", 21, "Doctor", "Choc")

p1.displayInfo()
p2.displayInfo()