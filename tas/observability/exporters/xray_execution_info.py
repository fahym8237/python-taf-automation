from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List


@dataclass(frozen=True)
class XrayExecutionInfo:
    project_key: str
    summary: str
    issuetype_name: str = "Test Execution"
    description: Optional[str] = None
    labels: Optional[List[str]] = None
    test_plan_key: Optional[str] = None
    environment: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        fields: Dict[str, Any] = {
            "project": {"key": self.project_key},
            "summary": self.summary,
            "issuetype": {"name": self.issuetype_name},
        }

        if self.description:
            fields["description"] = self.description

        if self.labels:
            fields["labels"] = self.labels

        # Keep environment in description for portability unless you have
        # a dedicated Jira custom field configured for it.
        if self.environment:
            env_line = f"\nEnvironment: {self.environment}"
            fields["description"] = (fields.get("description", "") + env_line).strip()

        payload: Dict[str, Any] = {"fields": fields}

        # Xray multipart imports support passing the Test Plan key alongside
        # the execution creation flow. Xray’s docs/examples call out Test Plan
        # linkage as a multipart use case. :contentReference[oaicite:1]{index=1}
        if self.test_plan_key:
            payload["testPlanKey"] = self.test_plan_key

        return payload


def build_default_execution_info(
    project_key: str,
    run_kind: str,
    issuetype_name: str,
    git_ref: Optional[str] = None,
    build_id: Optional[str] = None,
    labels: Optional[List[str]] = None,
    test_plan_key: Optional[str] = None,
    environment: Optional[str] = None,
) -> XrayExecutionInfo:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    parts = [f"TAS {run_kind}"]
    if git_ref:
        parts.append(git_ref)
    if build_id:
        parts.append(f"build {build_id}")

    summary = " | ".join(parts)
    description = f"Automated execution uploaded by TAS on {now}"

    return XrayExecutionInfo(
        project_key=project_key,
        summary=summary,
        issuetype_name=issuetype_name,
        description=description,
        labels=labels,
        test_plan_key=test_plan_key,
        environment=environment,
    )