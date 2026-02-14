from dataclasses import dataclass
from typing import Optional, Set

@dataclass(frozen=True) #Safer for parallel execution
class TagModel:
    raw: Set[str]
    is_ui: bool
    is_api: bool
    is_hybrid: bool
    is_smoke: bool
    is_regression: bool
    is_critical: bool
    is_quarantine: bool
    browser: Optional[str]
    dataset: Optional[str]
    trace_id: Optional[str]

class TagInterpreter:
    def interpret(self, feature, scenario) -> TagModel:
        # merges Feature-level and Scenario-level tags
        tags = set((feature.tags or []) + (scenario.tags or []))

        def has(t: str) -> bool:
            return t in tags

        browser = _value_for_prefix(tags, "browser=") # @browser=chromium ==> browser = "chromium"
        dataset = _value_for_prefix(tags, "dataset=")
        trace_id = _value_for_prefix(tags, "trace=")

        is_ui = has("ui")
        is_api = has("api")
        is_hybrid = has("hybrid")

        return TagModel(
            raw=tags,
            is_ui=is_ui,
            is_api=is_api,
            is_hybrid=is_hybrid,
            is_smoke=has("smoke"),
            is_regression=has("regression"),
            is_critical=has("critical"),
            is_quarantine=has("quarantine"),
            browser=browser,
            dataset=dataset,
            trace_id=trace_id,
        )

def _value_for_prefix(tags: Set[str], prefix: str) -> Optional[str]:
    for t in tags:
        if t.startswith(prefix):
            return t.split("=", 1)[1].strip() or None
    return None