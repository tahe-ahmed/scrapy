from scrapy.cmdline import _print_branch_coverage_cmd, _print_header
from scrapy.settings import BaseSettings


def test_coverage_print_header():
    settings = BaseSettings({"BOT_NAME": "coverage_bot", "TEST_BOT_False": "coverage"})
    _print_header(settings, False)
    _print_branch_coverage_cmd()


if __name__ == "__main__":
    test_coverage_print_header()
