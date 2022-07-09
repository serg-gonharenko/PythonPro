from unittest import TestCase, main
from lesson1 import filter_by_first_met_value

origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    ]


class FilterTest(TestCase):
    def test1(self):
        self.assertEqual(filter_by_first_met_value(origin, ["foo", "bar"]),
                         [
                             {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
                             {"foo": "F", "bar": "BAR", "foobar": "fb"}
                         ]
                         )

    def test2(self):
        self.assertEqual(filter_by_first_met_value(origin, ["foobar"]),
                         [
                             {"foo": "FOO", "bar": "BAR", "foobar": "fb"}
                         ]
                         )

    def test3(self):
        self.assertEqual(filter_by_first_met_value(origin, ["bar", "foobar"]),
                         [
                             {"foo": "FOO", "bar": "BAR", "foobar": "fb"}
                         ]
                         )


if __name__ == '__main__':
    main()
