{{ config(materialized='view') }}

select

    dispatching_base_num,
   -- identifiers
    cast(pulocationid as integer) as  pickup_locationid,
    cast(dolocationid as integer) as dropoff_locationid,
    
    -- timestamps
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,
    
    -- trip info
    cast(SR_Flag as integer) as share_ride_flag,
    Affiliated_base_number

from {{source('staging', 'fhv_tripdata')}}
-- dbt build --m <model.sql> --var 'is_test_run: false'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}