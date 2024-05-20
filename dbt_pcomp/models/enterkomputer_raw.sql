{{
  config(
    materialized = 'table'
  )
}}

select * 
from {{ source('dezoomcamp', 'enterkomputer_raw') }}
QUALIFY ROW_NUMBER() OVER (PARTITION BY PNAME, KNAME, PPRCZ ORDER BY inserted_at ASC nulls last) = 1 -- dedup