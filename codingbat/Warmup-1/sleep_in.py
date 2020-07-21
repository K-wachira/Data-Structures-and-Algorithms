"""

The parameter weekday is True if it is a weekday,
and the parameter vacation is True if we are on vacation.
 We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


"""


def sleep_in(weekday, vacation):
    # vacation is True if
    # weekdat is True

    if not weekday and not vacation:
        return True
    elif weekday and not vacation:
        return False
    elif not weekday and vacation:
        return True
    elif weekday and vacation:
        return True
