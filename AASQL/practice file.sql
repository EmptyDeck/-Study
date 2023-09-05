
-- WHERE mem_id = 'blk' or mem_id = 'mmu'
-- WHERE mem_id IN ('blk','mmu') -- @this line is same as the upper one@ IN operator is good for many conditions
-- WHERE price > 20 AND price < 500
-- WHERE price BETWEEN 20 AND 500 -- @same as upper one
-- WHERE mem_id LIKE '%U' -- LIKE 'M%' means starts with M // '%M%' means M anywhere // '%M' means M at the end
-- LIKE aloso has 'B__U' to count the chr before the letter


-- EXER print SQL prices with + 50% more price

-- SELECT num,mem_id,prod_name,price,price* 1.5 AS 'price up 50%'
-- FROM buy
-- WHERE prod_name LIKE '%SQL%'




