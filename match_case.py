"""The Match-Case Statement"""


def match_case() -> None:
    """
    The match statement In Python was introduced in version 3.10 using
    the match statement you can achieve cleaner more readable code that allows
    all the same functionality as the if controlled statement.

    The match statement compares a value to several different conditions
    until one of these conditions is met.
    """

    def print_http_status(http_status: int) -> None:
        """Function printing http sttus."""

        match http_status:
            case 200 | 201:  # Combining
                print("Success")
            case 400:
                print("Bad request")
            case 500 | 501:
                print("Server Error")
            case _:  # Default if nothing is found in the case
                print("Unkown status")

        print_http_status(200)
