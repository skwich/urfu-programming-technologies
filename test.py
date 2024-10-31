def apply_filter(func):
    def wrapper(*args):
        text = func(*args)
        text = "biboba"
        return text
    return wrapper

def apply_sort(func):
    def wrapper(*args):
        text = func(*args)
        text = "didoda"
        return text
    return wrapper

def print_formatted_text(func):
    def wrapper(*args):
        print(func(*args))
    return wrapper

@print_formatted_text
@apply_sort
@apply_filter
def print_text(text):
    return text

# print_text("aboba")

#---

students = [
    {
        "alex": 20,
        "vitya": 19
    },
    {
        "petya": 23,
        "vova": 24
    }
]

# for item in students:
#     for e in item.items():
#         print(e)

for student in students:
    for (key,value) in student.items():
        student[key] = "2000"

# for item in students:
#     for e in item.items():
#         print(e)












