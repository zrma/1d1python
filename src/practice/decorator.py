from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def simple_decorator(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"decorator start: {func.__name__} {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"decorator end: {func.__name__}")
        return result

    return wrapper


def say_hello(name: str) -> None:
    print(f"greeting, {name}!")


@simple_decorator
def say_hello_with_decorator(*args: Any, **kwargs: Any) -> None:
    if len(args) == 1 and isinstance(args[0], str) and not kwargs:
        return say_hello(*args, **kwargs)

    raise ValueError(f"Invalid arguments: {args} {kwargs}")
