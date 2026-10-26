"""可修改的小测试示例：另选输入，保留自己的预期与解释。

测试通过参数接收课程 fixture，--impl 才能切换候选实现。
不要直接 from operations import pop_last 绕过这个开关。
"""


def test_my_pop_example(pop_last):
    items = [7, 4]

    result = pop_last(items)

    assert result == 4
    assert items == [7]


def test_mixed_values_keep_repeats_and_input(positive_squares):
    values = [0, -4, 5, 5, 2]
    result = positive_squares(values)
    assert result == [25, 25, 4]
    assert values == [0, -4, 5, 5, 2]


def test_map_keeps_keys_and_input(positive_square_map):
    record = {"zero": 0, "negative": -4, "first": 5, "repeat": 5}
    result = positive_square_map(record)
    assert result == {"first": 25, "repeat": 25}
    assert list(result) == ["first", "repeat"]
    assert record == {"zero": 0, "negative": -4, "first": 5, "repeat": 5}
    assert result is not record
