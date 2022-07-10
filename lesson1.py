from typing import Any, Dict, List

origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
]


def filter_by_first_met_value(dataset: List[Dict[str, Any]], keys: List[str]) -> List[Dict[str, Any]]:
    """Filter dataset by first met value in keys"""

    filter_result = []
    selected_values = []
    for entry in dataset:
        select_value = {key: entry[key] for key in keys}
        if select_value not in selected_values:
            selected_values.append(select_value)
            filter_result.append(entry)
    return filter_result


if __name__ == '__main__':
    result = filter_by_first_met_value(origin, ["foo", "bar"])
    print(result)
    result = filter_by_first_met_value(origin, ["foobar"])
    print(result)
    result = filter_by_first_met_value(origin, ["bar", "foobar"])
    print(result)
