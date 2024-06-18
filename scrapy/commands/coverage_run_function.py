import argparse

from scrapy.settings import BaseSettings, Settings

from .settings import Command, _print_branch_coverage, reset_branch_coverage


def coverage_run_function():
    command = Command()
    command.settings = Settings(command.default_settings)
    command.crawler_process = type("", (), {})()
    command.crawler_process.settings = Settings(
        {
            "testBaseSetting": BaseSettings({"test_nested_key": "test_nested_value"}),
            "testNotBaseSetting": "test_Value",
            "testBoolSetting": True,
            "testIntSetting": 5,
            "testFloatSetting": 5.5,
            "testListSetting": ["one", "two", "three"],
        }
    )

    parser = argparse.ArgumentParser()
    command.add_options(parser)

    test_cases = [
        ("--get", "testBaseSetting"),
        ("--get", "testNotBaseSetting"),
        ("--getbool", "testBoolSetting"),
        ("--getint", "testIntSetting"),
        ("--getfloat", "testFloatSetting"),
        ("--getlist", "testListSetting"),
        (),
    ]

    for test_case in test_cases:
        if test_case:
            print(f"Testing coverage with  {test_case}")
        else:
            print("Testing coverage on default settings")

        opts = parser.parse_args(list(test_case))
        command.run([], opts)

        _print_branch_coverage()
        reset_branch_coverage()


if __name__ == "__main__":
    coverage_run_function()
