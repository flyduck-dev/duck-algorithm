SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS
LIKE '강원도%'
# '%강원도%' 대한민국 강원도 정선군, 강원도 정선군 (o)
# '강원도%' 강원도 정선군 (o)
# '%강원도' 대한민국 강원도 (o)