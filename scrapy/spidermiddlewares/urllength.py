"""
Url Length Spider Middleware

See documentation in docs/topics/spider-middleware.rst
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, AsyncIterable, Iterable

from scrapy import Spider
from scrapy.exceptions import NotConfigured
from scrapy.http import Request, Response
from scrapy.settings import BaseSettings

if TYPE_CHECKING:
    # typing.Self requires Python 3.11
    from typing_extensions import Self

logger = logging.getLogger(__name__)


class UrlLengthMiddleware:
    def __init__(self, maxlength: int):
        self.maxlength: int = maxlength

    @classmethod
    def from_settings(cls, settings: BaseSettings) -> Self:
        maxlength = settings.getint("URLLENGTH_LIMIT")
        if not maxlength:
            from_settings_branch_coverage["branch1"] = True
            write_from_settings_branch_coverage_to_file()
            raise NotConfigured
        else:
            from_settings_branch_coverage["branch2"] = True
            write_from_settings_branch_coverage_to_file()
        return cls(maxlength)

    def process_spider_output(
        self, response: Response, result: Iterable[Any], spider: Spider
    ) -> Iterable[Any]:
        return (r for r in result if self._filter(r, spider))

    async def process_spider_output_async(
        self, response: Response, result: AsyncIterable[Any], spider: Spider
    ) -> AsyncIterable[Any]:
        async for r in result:
            if self._filter(r, spider):
                yield r

    def _filter(self, request: Any, spider: Spider) -> bool:
        if isinstance(request, Request) and len(request.url) > self.maxlength:
            logger.info(
                "Ignoring link (url length > %(maxlength)d): %(url)s ",
                {"maxlength": self.maxlength, "url": request.url},
                extra={"spider": spider},
            )
            assert spider.crawler.stats
            spider.crawler.stats.inc_value(
                "urllength/request_ignored_count", spider=spider
            )
            return False
        return True

def write_from_settings_branch_coverage_to_file():
    project_dir = Path(__file__).resolve().parent.parent.parent
    output_file = os.path.join(project_dir, "branch_coverage_from_settings.txt")
    coverage_percentage = (
                                  sum(from_settings_branch_coverage.values()) / len(from_settings_branch_coverage)
                          ) * 100
    with open(output_file, "w", encoding="utf-8") as f:
        for branch, executed in from_settings_branch_coverage.items():
            f.write(f"{branch} has been {'executed' if executed else 'missed'}\n")
        f.write(f"Branch coverage: {coverage_percentage:.2f}%\n")

from_settings_branch_coverage = {
    "branch1" : False,
    "branch2" : False
}
