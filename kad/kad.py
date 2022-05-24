def to_kad(dictionary: dict) -> object:
    kad = object()
    for key in dictionary.keys():
        setattr(kad, key, dictionary[key])
    return kad
    
