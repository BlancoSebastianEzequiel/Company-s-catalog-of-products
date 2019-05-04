class StatusException(Exception):
    def __init__(self, message, status=None):
        super(StatusException, self).__init__(message)
        self.status = status
