def val(variable):
    return to_boolean(strip(integer(variable)))

def integer(variable):
    if type(variable)==float:
        return int(variable)
    return variable

def strip(variable):
    if type(variable)==int or type(variable)==type(None):
        return variable
    return variable.strip()

def to_boolean(variable):
    if variable == 'Yes':
        return True
    elif variable == 'No':
        return False
    return variable
