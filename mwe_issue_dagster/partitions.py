from datetime import date, timedelta

from dagster import (
    DailyPartitionsDefinition,
    MultiPartitionsDefinition,
    StaticPartitionsDefinition,
)

YESTERDAY = (date.today() - timedelta(days=1)).isoformat()

daily_partitions_def = DailyPartitionsDefinition(start_date=YESTERDAY)
static_partitions_def = StaticPartitionsDefinition(["a", "b", "c"])

multi_partition = MultiPartitionsDefinition(
    {
        "time": daily_partitions_def,
        "static": static_partitions_def,
    }
)
