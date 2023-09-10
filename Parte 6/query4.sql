SELECT cliente.nombre,
       SUM(orden.total) AS total_compras
FROM orden
INNER JOIN cliente ON orden.cliente_id = cliente.id
GROUP BY cliente.nombre
ORDER BY total_compras DESC
LIMIT 1;