def log(logger):
    def Inner(func):
        def wrapper(*args, **kwargs):
            package=func.__module__
            position=func.__qualname__
            try:
                logger.info(f"package : {package} --> position : {position}")
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"package : {package} --> position : {position} --> exception : {str(e)}")
                return func(*args, **kwargs)
        return wrapper
    return Inner