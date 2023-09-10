SELECT
  categoria.nombre,
  SUM(stock.cantidad) AS cantidad_total
FROM stock
JOIN producto ON stock.producto_id = producto.id
JOIN categoria ON producto.categoria_id = categoria.id
GROUP BY categoria.nombre;