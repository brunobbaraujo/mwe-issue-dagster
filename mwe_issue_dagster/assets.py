from dagster import (
    AssetSelection,
    asset,
    build_schedule_from_partitioned_job,
    define_asset_job,
)

from mwe_issue_dagster.partitions import multi_partition


@asset(partitions_def=multi_partition)
def asset1():
    return


job = define_asset_job(
    name="Asset1_job",
    selection=AssetSelection.assets(asset1),
)

scheduler = build_schedule_from_partitioned_job(job=job)
