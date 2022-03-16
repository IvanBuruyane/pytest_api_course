from typing import List, Tuple, Callable


def get_kwargs(identifiers: str, values: List[Tuple[int, int]]):
    list_of_kwargs = []
    for value in values:
        kwargs = {}
        for i, keyword in enumerate(identifiers.split(",")):
            kwargs[keyword] = value[i]
        list_of_kwargs.append(kwargs)
    return list_of_kwargs


def my_parametrize(identifiers: str, values: List[Tuple[int, int]]) -> Callable:
    def my_parametrized_decorator(function: Callable) -> Callable:
        def run_parametrized_func() -> None:
            kwargs_for_function = get_kwargs(identifiers=identifiers, values=values)
            for kwarg in kwargs_for_function:
                print(f"calling function {function.__name__} with {kwarg}")
                function(**kwarg)

        return run_parametrized_func

    return my_parametrized_decorator


def error_generator(param, expected_value, actual_value):
    return f"Expected {param} = {expected_value}, received - {actual_value}"
