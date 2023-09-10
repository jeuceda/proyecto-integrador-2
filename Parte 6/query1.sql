SELECT
  categoria.nombre,
  AVG(producto.precio_unitario) AS precio_promedio
FROM producto
JOIN categoria ON producto.categoria_id = categoria.id
GROUP BY categoria.nombre;