import argparse

from scrapy.commands.settings import (
    Command,
    print_branch_coverage_settings_run,
    reset_branch_coverage,
)
from scrapy.settings import BaseSettings, Settings


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
        print(f"Testing coverage with  {test_case}")
        opts = parser.parse_args(list(test_case))
        command.run([], opts)
        print_branch_coverage_settings_run()
        reset_branch_coverage()


if __name__ == "__main__":
    coverage_run_function()
