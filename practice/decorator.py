def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("decorator begin")
        func(*args, **kwargs)
        print("decorator end")

    return wrapper


def say_hello(name):
    print(f"greeting, {name}!")


@simple_decorator
def say_hello_with_decorator(*args, **kwargs):
    say_hello(*args, **kwargs)


if __name__ == "__main__":
    say_hello_with_decorator_func = simple_decorator(say_hello)
    say_hello_with_decorator_func("John")

    say_hello_with_decorator("Boris")
