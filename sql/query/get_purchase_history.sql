SELECT
  purchase_id AS 'ID',
  purchase_date AS 'Ngày',
  printf('%,d', subtotal)  AS 'Tổng tiền',
  supplier_name AS 'Nhà cung cấp',
  product_name AS 'Tên sản phẩm',
  notes AS 'Ghi chú'
FROM Purchases
LEFT JOIN Suppliers ON Purchases.supplier_id = Suppliers.supplier_id
JOIN Products ON Purchases.product_id = Products.product_id
