from dagster import Definitions

from mwe_issue_dagster.assets import asset1, job, scheduler

defs = Definitions(assets=[asset1], jobs=[job], schedules=[scheduler])
