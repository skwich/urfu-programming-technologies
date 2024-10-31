def apply_filter(func):
    def wrapper(*args, **kwargs):
        print("=====")
        print(args[0])
        print("=====")
    return wrapper

@apply_filter
def print_text(text, abc):
    print(text, abc)

print_text("aboba", 123)