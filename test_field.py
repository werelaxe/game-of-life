from copy import copy
from field import Field


def test_field(dim_count, size, rule):
    f = Field(dim_count, size, rule)
    old_field = copy(f)
    f.update()

    f.print_field()


test_field(2, 3, (2, 3))
