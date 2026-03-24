from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from playwright.sync_api import sync_playwright, APIRequestContext, Playwright

from tas.interaction.api.api_response import ApiResponse
from tas.interaction.api.api_capture import ApiLastExchange


@dataclass(frozen=True)
class ApiSessionConfig:
    base_url: str
    timeout_ms: int = 30_000
    default_headers: Optional[Dict[str, str]] = None
    ignore_https_errors: bool = False


class ApiSession:
    def __init__(self, cfg: ApiSessionConfig):
        self._cfg = cfg
        self._pw: Optional[Playwright] = None
        self._ctx: Optional[APIRequestContext] = None
        self._last: Optional[ApiLastExchange] = None

    @property
    def last_exchange(self) -> Optional[ApiLastExchange]:
        return self._last

    def start(self) -> None:
        if not self._cfg.base_url:
            raise RuntimeError("ApiSessionConfig.base_url is empty")

        self._pw = sync_playwright().start()
        self._ctx = self._pw.request.new_context(
            base_url=self._cfg.base_url,
            extra_http_headers=self._cfg.default_headers or {},
            timeout=self._cfg.timeout_ms,
            ignore_https_errors=self._cfg.ignore_https_errors,  # ✅ critical
        )



    def close(self) -> None:
        try:
            if self._ctx:
                self._ctx.dispose()
        finally:
            if self._pw:
                self._pw.stop()

    def get(self, path: str, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("GET", path, json=None, headers=headers)

    def post(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("POST", path, json=json, headers=headers)

    def put(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("PUT", path, json=json, headers=headers)

    def patch(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("PATCH", path, json=json, headers=headers)

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self._request("DELETE", path, json=None, headers=headers)

    def _request(
        self,
        method: str,
        path: str,
        json: Optional[Dict[str, Any]],
        headers: Optional[Dict[str, str]],
    ) -> ApiResponse:
        if not self._ctx:
            raise RuntimeError("ApiSession used before start()")

        import json as _json

        req_headers = dict(headers or {})

        # If we are sending JSON, encode it manually and ensure content-type
        data = None
        if json is not None:
            data = _json.dumps(json)
            if not any(k.lower() == "content-type" for k in req_headers.keys()):
                req_headers["Content-Type"] = "application/json"

        resp = self._ctx.fetch(
            path,
            method=method,
            headers=req_headers,
            data=data,   # <-- Playwright accepts data=, not json=
        )

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

        self._last = ApiLastExchange(
            method=method,
            url=resp.url,
            request_headers=dict(req_headers),
            request_json=json,
            status=resp.status,
            response_headers=dict(resp.headers),
            response_text=body_text,
            response_json=parsed_json,
        )

        return ApiResponse(
            url=resp.url,
            status=resp.status,
            headers=dict(resp.headers),
            body_text=body_text,
            json=parsed_json,
        )