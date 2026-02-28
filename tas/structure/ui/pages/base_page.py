from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class PageContext:
    # In Layer 6 Imp, `page` will be Playwright Page
    page: Any
    base_url: str

class BasePage:
    def __init__(self, ctx: PageContext):
        self._ctx = ctx

    @property
    def page(self):
        return self._ctx.page

    def goto(self, url: str) -> None:
        self.page.goto(url)

    def goto_path(self, path: str) -> None:
        if self._ctx.base_url.endswith("/") and path.startswith("/"):
            url = self._ctx.base_url[:-1] + path
        elif not self._ctx.base_url.endswith("/") and not path.startswith("/"):
            url = self._ctx.base_url + "/" + path
        else:
            url = self._ctx.base_url + path
        self.page.goto(url)

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).first.is_visible()
