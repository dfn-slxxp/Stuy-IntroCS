def isEmpty(dict):
    return not dict

def highest3(dict):
    ts = list(dict.values())
    ts.sort(reverse=True)
    try:
        return [ts[0], ts[1], ts[2]]
    except IndexError:
        return ts