{{ config(materialized='table') }}

with fhv_data as (
    select *, 
    from {{ ref('stg_fhv_tripdata') }}
),

dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)

select *
from fhv_data
inner join dim_zones as pickup_zone
on fhv_data.pickup_locationid = pickup_zone.locationid