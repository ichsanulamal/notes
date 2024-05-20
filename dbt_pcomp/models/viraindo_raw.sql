{{
  config(
    materialized = 'table'
  )
}}

select * 
from {{ source('dezoomcamp', 'viraindo_raw') }}
QUALIFY ROW_NUMBER() OVER (PARTITION BY name, category, price ORDER BY inserted_at ASC nulls last) = 1 -- dedup