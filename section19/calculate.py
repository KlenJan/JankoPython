'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**kwargs):
    result = 0
    if kwargs["operation"] == "add":
        result = kwargs["first"] + kwargs["second"]
    if kwargs["operation"] == "subtract":
        result = kwargs["first"] - kwargs["second"]
    if kwargs["operation"] == "multiply":
        result = kwargs["first"] * kwargs["second"]
    if kwargs["operation"] == "divide":
        result = kwargs["first"] / kwargs["second"]
    if not kwargs["make_float"]:
        result = int(result)
    if "message" in kwargs:
        return f"{kwargs['message']} {result}"
    return f"The result is {result}"


print(calculate(make_float=False, operation='add', message='You just added',
                first=2, second=4))  # "You just added 6"

print(calculate(make_float=True, operation='divide',
      first=3.5, second=5))  # "The result is 0.7"
