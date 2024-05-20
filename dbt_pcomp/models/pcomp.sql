
select * from (select * from {{ ref('enterkomputer') }}
union all
select * from {{ ref('viraindo') }})
QUALIFY ROW_NUMBER() OVER (PARTITION BY product_name, category, price, `source` ORDER BY inserted_at ASC nulls last) = 1