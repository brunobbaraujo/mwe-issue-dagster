# Setup

1. Create a virtualenv
2. Run `pip install -e .`
<br>

# Dagster issue with schedule

1. Run the command `dagster dev`
2. Open the UI
3. Go to Overview -> Schedules -> Asset1_job_schedule -> Test Schedule.

Please use `date = today` when testing the schedule.

# Where the error is

In `dagster._core.definitions.schedule_definition.py`, at [line 866](https://github.com/dagster-io/dagster/blob/master/python_modules/dagster/dagster/_core/definitions/schedule_definition.py#L866):
```py
item = check.inst(result[0], (SkipReason, RunRequest))
```

When checking what caused it, I've come across line 857
```py
result = list(ensure_gen(execution_fn(context)))
```

When running Test Schedule for this repository, type of result is a `list[list[RunRequest]]`.<br>
So its length is 1, but result[0] is of type `list[RunRequest]`, causing the check to fail.

# Proposed Solution

Add the following lines to convert from `list[list[T]]` to `list[T]`:

```py
result = list(ensure_gen(execution_fn(context)))
if all(isinstance(elem, list) for elem in result):
    result = sum(result, [])
```
