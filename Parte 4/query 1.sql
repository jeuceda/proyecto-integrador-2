SELECT
	MIN(precio_unitario) AS precio_minimo, MAX(precio_unitario) AS precio_max, AVG(precio_unitario) as precio_avg
FROM producto;