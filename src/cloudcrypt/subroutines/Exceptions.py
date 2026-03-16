import warnings

class WarningAndExceptions:
    class CustomExceptions:
        class InvalidArgumentException(BaseException):
            pass


    class CustomWarnings:
        def no_access_warning(self, filepath: str):
            warnings.warn("No Access on: "+filepath, RuntimeWarning)

