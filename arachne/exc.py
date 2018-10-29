

class ArachneError(Exception):
    def __init__(self, message, details):
        super().__init__(message)
        self.message = message
        self.details = details

    def as_obj(self):
        return {
            "message": self.message,
            "details": self.details,
        }


class ValidationError(ArachneError):
    def __str__(self):
        return ";".join(["{} {}".format(k, v) for k, v in self.details.items()])


class VarNotFountError(ArachneError):
    pass


class VarAlreadyDefinedError(ArachneError):
    pass


class ConfigurationError(ArachneError):
    pass
