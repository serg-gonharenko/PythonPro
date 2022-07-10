from unittest import TestCase, main
from lesson1 import filter_by_first_met_value

origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    ]


class FilterTestMy(TestCase):
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


class FilterTest(TestCase):
    FIXTURE = [
        {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
        {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
        {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
        {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
        {"name": "Serhii", "company": "A-Level", "job": "Python Trainer"},
    ]

    def test_filter_by_name(self):
        test_value = [
            {"name": "Serhii", "company": "SoftServe",
             "job": "Software Engineer"},
            {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
        ]
        keys = ["name"]
        result = filter_by_first_met_value(FilterTest.FIXTURE, keys)
        self.assertListEqual(test_value, result)

    def test_filter_name_company(self):
        test_value = [
            {"name": "Serhii", "company": "SoftServe",
             "job": "Software Engineer"},
            {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
            {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
            {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
            {"name": "Serhii", "company": "A-Level", "job": "Python Trainer"},
        ]
        keys = ["name", "company"]
        result = filter_by_first_met_value(FilterTest.FIXTURE, keys)
        self.assertListEqual(test_value, result)


if __name__ == '__main__':
    main()
