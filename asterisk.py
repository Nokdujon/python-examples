"""Usage of Asterisks in Python"""

from functools import reduce


def multiplication_and_power_operations() -> None:
    """1. multiplication and power operations."""
    multiplication = 2 * 3  # 6
    power = 2**3  # 8

    print(multiplication)
    print(power)


def extend_list_type_containers() -> None:
    """2. repeatedly extending the list-type containers."""
    zeros_list = [0] * 5  # [0, 0, 0, 0, 0]
    zeros_tuple = (0,) * 5  # (0, 0, 0, 0, 0)

    print(zeros_list)
    print(zeros_tuple)

    vector_list = [[1, 2, 3]]
    for i, vector in enumerate(vector_list * 3):
        # vector_list * 3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        print([(i + 1) * e for e in vector])  # [1, 2, 3], [2, 4, 6], [3, 6, 9]


def packing() -> None:
    """3. using the variadic arguments. (so-called “packing”)"""

    numbers = [1, 2, 3, 4, 5, 6]
    # left side should be a tuple or a list.
    (*a,) = numbers  # a = [1, 2, 3, 4, 5, 6]
    print(a)

    *a, b = numbers  # a = [1, 2, 3, 4, 5],  b = 6
    (
        a,
        *b,
    ) = numbers  # a = 1, b = [2, 3, 4, 5, 6]
    print(a, b)

    a, *b, c = numbers  # a = 1, b = [2, 3, 4, 5], c = 6
    print(a, b, c)


def unpacking() -> None:
    """4. unpacking the containers."""
    # Unpacking a function using positional argument.
    # This method is very useful while printing your data in a raw format
    # (without any comma and brackets ). Many of the programmer try to remove
    # comma and bracket by using a convolution of functions, Hence this simple
    # prefix asterisk can solve your problem in unpacking them.

    def positional_args() -> None:
        """*args(positional arguments): tuple"""

        def product(*numbers: int) -> int:
            return reduce(lambda x, y: x * y, numbers)

        primes = [2, 3, 5, 7, 11, 13]
        print(product(*primes))  # 30030
        print(product(primes))  # an only argument [2, 3, 5, 7, 11, 13]

        args = [3, 6]
        print(
            "sum(number for number in range(3, 6)) = ",
            sum(number for number in range(3, 6)),
        )
        print(
            "sum(number for number in range(*args)) = ",
            sum(number for number in range(*args)),
        )  # range(*args) == range(3, 6)

    def keyword_args() -> None:
        """**kwargs(keyword arguments): dict"""

        def pre_process(**headers):
            content_length = headers["Content-Length"]
            print("content length: ", content_length)

            host = headers["Host"]
            if "https" not in host:
                raise ValueError("You must use SSL for http communication")

        headers = {
            "Accept": "text/plain",
            "Content-Length": 348,
            "Host": "http://mingrammer.com",
        }
        pre_process(**headers)

    positional_args()
    keyword_args()
