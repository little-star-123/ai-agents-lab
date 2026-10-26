"""A 题补充用例：使用聊天中讲解的数据核对结果。"""


def test_my_summarize_case(summarize_values):
    values = [1, 2, 2, -1]
    result = summarize_values(values)
    assert result == {
        "unique": [1, 2, -1],
        "counts": {1: 1, 2: 2, -1: 1},
        "repeated": {2},
    }
    assert sum(result["counts"].values()) == len(values)
    assert values == [1, 2, 2, -1]
