WITH cte_0 as (
SELECT 
    name as product_name, 
    category,
    REPLACE(price, '.', '') as price,
    date(date_trunc(inserted_at, week)) as inserted_at,
    'viraindo' as source
FROM {{ source('dezoomcamp', 'viraindo_raw') }}
)
SELECT 
    product_name,
    category,
    SAFE_CAST(price as integer) as price,
    inserted_at,
    source
FROM cte_0