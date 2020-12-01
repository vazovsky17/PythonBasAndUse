class PositiveList(list):
    def append(self, val):
        if val > 0:
            super().append(val)
        else:
            raise NonPositiveError()


class NonPositiveError(Exception):
    pass

