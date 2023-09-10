SELECT 
	sucursal_id,
	SUM(cantidad) AS cantidad_total
FROM
	stock
GROUP BY	
    sucursal_id 