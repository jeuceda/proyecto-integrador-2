SELECT
	cliente_id,
	SUM(total) as total_ventas
FROM
	orden
GROUP BY	
    cliente_id