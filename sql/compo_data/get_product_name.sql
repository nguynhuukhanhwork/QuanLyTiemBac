SELECT
    product_name AS "Tên sản phẩm",
    material AS "Chất liệu",
    product_size AS "Size",
    printf('%,d', base_price) AS "Giá"
FROM Products;
