SELECT
  sucursal.nombre,
  SUM(item.monto_venta) AS total_ventas
FROM item
JOIN orden ON item.orden_id = orden.id
JOIN sucursal ON orden.sucursal_id = sucursal.id
GROUP BY sucursal.nombre;
