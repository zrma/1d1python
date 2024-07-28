from functools import singledispatch, wraps
from typing import Any, Callable, Concatenate


def simple_decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"decorator start: {func.__name__} {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"decorator end: {func.__name__}")
        return result

    return wrapper


def simple_decorator_with_args[**P, R](*dargs: Any, **dkwargs: Any) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            print(f"decorator start: {func.__name__} {args} {kwargs} {dargs} {dkwargs}")
            result = func(*args, **kwargs)
            print(f"decorator end: {func.__name__}")
            return result

        return wrapper

    return decorator


@singledispatch
def convert_to_list(value: Any) -> list[Any]:
    raise NotImplementedError(f"Cannot convert {value} to list")


@convert_to_list.register
def _(value: str) -> list[str]:
    return [value]


@convert_to_list.register
def _(value: int) -> list[str]:
    return ["unknown" for _ in range(value)]


def simple_decorator_with_first_args[**P, R](
    func: Callable[Concatenate[list[str], P], R],
) -> Callable[Concatenate[str | int, P], R]:
    @wraps(func)
    def wrapper(name: str | int, /, *args: P.args, **kwargs: P.kwargs) -> R:
        print(f"decorator start: {func.__name__} {args} {kwargs}")
        print(f"got {name=}")
        result = func(convert_to_list(name), *args, **kwargs)
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


@simple_decorator_with_args("hello", "world", hello="world")
def say_hello_with_decorator_args(*args: Any, **kwargs: Any) -> None:
    if len(args) == 1 and isinstance(args[0], str) and not kwargs:
        return say_hello(*args, **kwargs)

    raise ValueError(f"Invalid arguments: {args} {kwargs}")


@simple_decorator_with_first_args
def say_hello_list(name: list[str], n: int) -> None:
    for i, s in enumerate(name):
        print(f"greeting, {i=} {s=}!")
    print(f"{n=}")
