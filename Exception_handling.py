# class CustomError(Exception):
#     """Base class for other custom exceptions"""
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
class ValueTooHighError(Exception):
 pass

class ValueTooLowError(Exception):
    pass


def check_value(value):
    if value > 100:
        raise ValueTooHighError(f"Value {value} is too high. Maximum allowed is 100.")
    # elif value < 0:
    #     raise ValueTooLowError(f"Value {value} is too low. Minimum allowed is 0.")
    else:
        print(f"Value {value} is within the acceptable range.")

values = [150]

try:
    for value in values:
        check_value(value)
except ValueTooHighError as e:
    print(f"Caught an error: {e}")
except ValueTooLowError as e:
    print(f"Caught an error: {e}")
except Exception as e:
    print(f"Caught an unexpected error: {e}")
