from cmdline import _print_header, _print_branch_coverage
from scrapy.settings import BaseSettings, Settings

settings = BaseSettings()

_print_header(settings, True)

_print_branch_coverage()