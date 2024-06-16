from scrapy.cmdline import _print_branch_coverage, _print_header
from scrapy.settings import BaseSettings

settings = BaseSettings()
_print_header(settings, True)
_print_branch_coverage()
