def write():
    try:
        file=open(r'points','r')
    except FileNotFoundError:
        return {}
    else:
        pass
