from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from playwright.sync_api import sync_playwright, APIRequestContext, Playwright

from tas.interaction.api.api_response import ApiResponse


@dataclass(frozen=True)
class ApiSessionConfig:
    base_url: str
    timeout_ms: int = 30_000
    default_headers: Optional[Dict[str, str]] = None


class ApiSession:
    def __init__(self, cfg: ApiSessionConfig):
        self._cfg = cfg
        self._pw: Optional[Playwright] = None
        self._ctx: Optional[APIRequestContext] = None

    def start(self) -> None:
        self._pw = sync_playwright().start()
        self._ctx = self._pw.request.new_context(
            base_url=self._cfg.base_url,
            extra_http_headers=self._cfg.default_headers or {},
            timeout=self._cfg.timeout_ms,
        )

    def close(self) -> None:
        try:
            if self._ctx:
                self._ctx.dispose()
        finally:
            if self._pw:
                self._pw.stop()

    def get(self, path: str, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("GET", path, headers=headers)

    def post(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("POST", path, json=json, headers=headers)

    def put(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("PUT", path, json=json, headers=headers)

    def patch(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("PATCH", path, json=json, headers=headers)

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("DELETE", path, headers=headers)

    def _request(self, method: str, path: str, json: Optional[Dict[str, Any]] = None,
                 headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        if not self._ctx:
            raise RuntimeError("ApiSession used before start()")

        resp = self._ctx.fetch(path, method=method, json=json, headers=headers or {})
        body_text = None
        parsed_json = None
        try:
            body_text = resp.text()
        except Exception:
            body_text = None
        try:
            parsed_json = resp.json()
        except Exception:
            parsed_json = None

        return ApiResponse(
            url=resp.url,
            status=resp.status,
            headers=dict(resp.headers),
            body_text=body_text,
            json=parsed_json,
        )
