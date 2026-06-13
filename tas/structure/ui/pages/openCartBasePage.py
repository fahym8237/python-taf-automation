from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PageContext:
    page: Any
    base_url: str = ""


class OpenCartBasePage:
    def __init__(self, ctx: PageContext):
        self._ctx = ctx
    @property
    def page(self):
        return self._ctx.page
    def goto(self, url: str) -> None:
        self.page.goto(url)
    def click(self, selector: str) -> None:
        el = self.page.locator(selector).first
        el.click()

        # Post-click wait 
        try:
            # wait for network idle (good for AJAX-heavy apps)
            self.page.wait_for_load_state("networkidle")

            # wait for a specific element to appear
            # self.page.locator("#result").wait_for(state="visible")

            # wait for spinner to disappear
            # self.page.locator(".spinner").wait_for(state="hidden")

        except Exception as e:
            print(f"Post-click wait condition not met: {e}")
    def fill(self, selector: str, value: str) -> None:
        self.page.locator(selector).first.fill(value)
    def is_visible(self, selector: str, timeout: int = 500) -> bool:
        locator = self.page.locator(selector).first
        try:
            # Wait until the element is visible (up to timeout ms)
            locator.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False
    def text_content(self, selector: str) -> str | None:
        locator = self.page.locator(selector).first
        return locator.text_content() if locator.is_visible() else None
    def get_attribute(self, selector: str, attribute: str) -> str | None:
        return self.page.locator(selector).first.get_attribute(attribute)
    def current_url(self) -> str:
        return self.page.url
    def set_viewport(self, width: int, height: int) -> None:
        self.page.set_viewport_size({
            "width": width,
            "height": height
        })
    def clear_and_fill(self, selector: str, value: str) -> None:
        locator = self.page.locator(selector).first
        locator.clear()
        locator.fill(value)
    def url_contains(self, value: str) -> bool:
        return value in self.page.url
    def get_input_validation_message(self, selector: str) -> str:
        return self.page.locator(selector).first.evaluate(
            "element => element.validationMessage"
        )
    def is_input_valid(self, selector: str) -> bool:
        return self.page.locator(selector).first.evaluate(
            "element => element.validity.valid"
        )
    def refresh_page(self) -> None:
        self.page.reload()
    def browser_back(self) -> None:
        self.page.go_back()
    def browser_forward(self) -> None:
        self.page.go_forward()
    def input_value(self, selector: str) -> str:
        return self.page.locator(selector).first.input_value()
    def set_viewport(self, width: int, height: int) -> None:
        self.page.set_viewport_size({
            "width": width,
            "height": height
        })
    def current_url(self) -> str:
        return self.page.url
    def clear_cookies(self) -> None:
        self.page.context.clear_cookies()
    def refresh_page(self) -> None:
        self.page.reload()
    def input_value(self, selector: str) -> str:
        return self.page.locator(selector).first.input_value()
    def clear_and_fill(self, selector: str, value: str) -> None:
        locator = self.page.locator(selector).first
        locator.clear()
        locator.fill(value)
    def is_input_valid(self, selector: str) -> bool:
        return self.page.locator(selector).first.evaluate(
            "element => element.validity.valid"
        )
    def get_attribute(self, selector: str, attribute: str) -> str | None:
        return self.page.locator(selector).first.get_attribute(attribute)
    def refresh_page(self) -> None:
        self.page.reload()
    def browser_back(self) -> None:
        self.page.go_back()
    def input_value(self, selector: str) -> str:
        return self.page.locator(selector).first.input_value()
    def url_contains(self, value: str) -> bool:
        return value in self.page.url


            