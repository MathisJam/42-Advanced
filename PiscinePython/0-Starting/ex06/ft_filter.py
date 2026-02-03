def ft_filter(function, iterable):
    """Applique une fonction sur chaque element dun iterable
    et retourne une liste des elements pour lesquels"""
    try:
        if function:
            return [item for item in iterable if function(item)]
    except Exception:
        return []
    return [item for item in iterable if item]
