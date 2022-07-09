from typing import Any, Dict, List

origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
]


def filter_by_first_met_value(dataset: List[Dict[str, Any]], keys: List[str]) -> List[Dict[str, Any]]:
    """Filter dataset by first met value in keys"""
    filter_result = []
    for entry in dataset:
        if all(key in entry for key in keys):
            if not filter_result:
                filter_result.append(entry)
            for check_entry in filter_result:
                if all(entry[key] == check_entry[key] for key in keys):
                    break
                else:
                    filter_result.append(entry)
    return filter_result


if __name__ == '__main__':
    result = filter_by_first_met_value(origin, ["foo", "bar"])
    print(result)
    result = filter_by_first_met_value(origin, ["foobar"])
    print(result)
    result = filter_by_first_met_value(origin, ["bar", "foobar"])
    print(result)