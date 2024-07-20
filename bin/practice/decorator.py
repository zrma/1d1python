from src.practice.decorator import say_hello, say_hello_with_decorator, simple_decorator

if __name__ == "__main__":
    say_hello_with_decorator_func = simple_decorator(say_hello)
    say_hello_with_decorator_func("John")

    say_hello_with_decorator("Boris")
