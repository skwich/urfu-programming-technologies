import time

def log(is_get_time: bool):
    def decorator(input_func):
        def output_func(*args):
            result = input_func(*args)
            date = f"[{time.ctime()}] " if is_get_time else ""
            print(f"{date}Func: {input_func.__name__}, Text: {result}")
            return result
        return output_func
    return decorator

@log(True)
def print_text_with_time(text):
    print(text)
    return text

@log(False)
def print_text(text):
    print(text)
    return text

print_text("POCOX3PRO")
print_text_with_time("AKYLA")