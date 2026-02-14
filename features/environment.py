from tas.orchestration.lifecycle import LifecycleManager

_lifecycle = LifecycleManager()

# -Load configuration (environment, browser, secrets) -Initialize logging/reporting -Prepare global resources -Setup execution context.
# Entry point of the Context Lifecycle
def before_all(context):
    _lifecycle.before_all(context)

# -Create browser instance (or API session) -Reset test data context -Attach metadata (tags, trace IDs) -Prepare isolated scenario context
def before_scenario(context, scenario):
    _lifecycle.before_scenario(context, scenario)

# -Capture screenshot on failure -Capture Playwright trace -Log step result -Attach artifacts to Allure report. 
def after_step(context, step):
    _lifecycle.after_step(context, step)

# -Close browser -Cleanup test data -Release API tokens -Attach scenario-level artifacts.
def after_scenario(context, scenario):
    _lifecycle.after_scenario(context, scenario)

# -Close global sessions -Generate consolidated reports -Release shared resources -Final logging
def after_all(context):
    _lifecycle.after_all(context)