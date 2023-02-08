from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """Download trip data from GCS"""
    gcs_path = f"/home/abdulwahab/data-engineering-zoomcamp/week_2_workflow_orchestration/03_deployments/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("zoom-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path="/home/abdulwahab/data-engineering-zoomcamp/week_2_workflow_orchestration/03_deployments/")
    return Path(gcs_path)



@task()
def transform(path: Path) -> pd.DataFrame:
    """Data cleaning example"""
    df = pd.read_parquet(path)
    df.drop(df.columns[0], axis=1, inplace=True)
    return df


@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("zoom-gcp-creds")

    df.to_gbq(
        destination_table="trips_data_all.yellow_rides",
        project_id="igneous-ethos-375619",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
    )


@flow(log_prints=True)
def etl_gcs_to_bq(color: str, year: int, months: list[int]):
    """Main ETL flow to load data into Big Query"""

    paths = []
    for month in months:
        path = extract_from_gcs(color, year, month)
        paths.append(path)

    dfs = [transform(path) for path in paths]
    df = pd.concat(dfs, axis=0)
    write_bq(df)

if __name__ == "__main__":
    etl_gcs_to_bq(color="yellow", year=2019, months=[2, 3])

