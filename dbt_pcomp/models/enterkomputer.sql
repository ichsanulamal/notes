WITH cte_0 as (
SELECT 
    PNAME as product_name, 
    case KNAME
    when 'Keyboard' then 'keymouse'
    when 'Processor' then 'proc'
    when 'Hard Drive' then 'storage'
    when 'RAM' then 'memory'
    when 'SSD' then 'storage'
    else KNAME end as category,
    JSON_EXTRACT_ARRAY(PPRCZ)[SAFE_OFFSET(0)] as price, 
    date(date_trunc(inserted_at, week)) as inserted_at,
    'enterkomputer' as source
FROM {{ source('dezoomcamp', 'enterkomputer_raw') }}
)
SELECT 
    product_name,
    lower(category) as category,
    SAFE_CAST(price as integer) as price,
    inserted_at,
    source
FROM cte_0



-- lcd
-- psu
-- vga
-- proc
-- audio
-- tinta
-- casing
-- cooler
-- gadget
-- memory
-- office
-- server
-- printer
-- storage
-- keymouse
-- notebook
-- software
-- aksesoris
-- pcbranded
-- projector
-- networking
-- rackserver
-- motherboard
-- partnotebook
-- mcardflashdisk
-- ups-stabilizer

-- KNAME
-- PSU
-- Casing
-- LCD
-- Keyboard
-- Processor
-- Hard Drive
-- Cooler
-- RAM
-- SSD
-- VGA
-- Motherboard





