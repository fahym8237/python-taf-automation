from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from pathlib import Path

from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page, Playwright


@dataclass(frozen=True)
class UiSessionConfig:
    browser: str = "chromium"         # chromium|firefox|webkit
    headless: bool = True
    trace_mode: str = "off"           # off|on-failure|always
    artifacts_dir: Optional[Path] = None


class UiSession:
    def __init__(self, cfg: UiSessionConfig):
        self._cfg = cfg
        self._pw: Optional[Playwright] = None
        self._browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None
        self._trace_started: bool = False

    @property
    def page(self) -> Page:
        if not self._page:
            raise RuntimeError("UiSession.page accessed before start()")
        return self._page

    def start(self) -> None:
        self._pw = sync_playwright().start()

        browser_name = self._cfg.browser.lower().strip()
        if browser_name == "chromium":
            launcher = self._pw.chromium
        elif browser_name == "firefox":
            launcher = self._pw.firefox
        elif browser_name == "webkit":
            launcher = self._pw.webkit
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        self._browser = launcher.launch(headless=self._cfg.headless)
        self._context = self._browser.new_context()
        self._page = self._context.new_page()

        if self._cfg.trace_mode in ("always", "on-failure"):
            # trace will be saved by orchestration on failure or always at scenario end
            self._context.tracing.start(screenshots=True, snapshots=True, sources=True)
            self._trace_started = True

    def goto(self, url: str) -> None:
        self.page.goto(url)

    def screenshot(self, path: Path, full_page: bool = True) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.page.screenshot(path=str(path), full_page=full_page)
        return path

    def stop_trace(self, path: Path) -> Optional[Path]:
        if not self._context or not self._trace_started:
            return None
        path.parent.mkdir(parents=True, exist_ok=True)
        self._context.tracing.stop(path=str(path))
        self._trace_started = False
        return path

    def close(self) -> None:
        # Close in safe order
        try:
            if self._context:
                self._context.close()
        finally:
            try:
                if self._browser:
                    self._browser.close()
            finally:
                if self._pw:
                    self._pw.stop()
