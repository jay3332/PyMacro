class SpeedError(Exception):
    pass


class TaskEndError(Exception):
    pass


class TaskException(Exception):
    def __init__(self, original):
        self.error = original
        super().__init__(
            "{0.__class__.__name__}: "
            "{0}".format(original)
        )
