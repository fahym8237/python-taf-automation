# TAF Tag Policy

## Mandatory tags per Scenario
1) Exactly one execution intent tag:
- @smoke OR @critical OR @regression OR @extended

2) Exactly one technical slice tag:
- @ui OR @api OR @hybrid

## Optional tags
- @owner_<team>
- @quarantine
- @browser=chromium|firefox|edge
- @dataset=<file>

## Traceability
- @trace=REQ-<id> is required for @smoke and @critical

## Examples
@smoke @ui @trace=REQ-AUTH-LOGIN-001
Scenario: Login success ...