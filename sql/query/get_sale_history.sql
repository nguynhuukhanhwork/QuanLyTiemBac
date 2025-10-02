SELECT
    Sales.sale_id AS 'Mã hóa đơn',
    Sales.sale_date AS 'Ngày bán',
    Customers.customer_name AS 'Khách hàng',
    GROUP_CONCAT(Products.product_name || ' (' || SaleItems.quantity || ')', ', ') AS 'Sản phẩm mua',
    printf("%,d", Sales.total_amount) AS 'Tổng tiền',
    Sales.notes AS 'Ghi chú'
FROM Sales
LEFT JOIN Customers ON Sales.customer_id = Customers.customer_id
LEFT JOIN SaleItems ON Sales.sale_id = SaleItems.sale_id
LEFT JOIN Products ON SaleItems.product_id = Products.product_id
GROUP BY Sales.sale_id
ORDER BY Sales.sale_date DESC;