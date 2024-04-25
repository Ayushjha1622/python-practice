from datetime import datetime 

def days_since_birth(birthdate):
    today=datetime.now(),date()
    diff=today-birthdate
    return diff.days

birth = input("enter in YYYY-MM-DD format: ")
birth=datetime.strptime(birth,"%Y-%m-%d").date()
days_elapsed=days_since_birth(birth)
print(days_elapsed)