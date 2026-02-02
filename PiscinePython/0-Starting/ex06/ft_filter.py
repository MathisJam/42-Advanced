def ft_filter(function, iterable):
    if function:
        return [item for item in iterable if function(item)]
    return [item for item in iterable if item]
