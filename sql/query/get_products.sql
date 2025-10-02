SELECT
    product_id AS "ID",
    product_name AS "Tên sản phẩm",
    material AS "Chất liệu",
    product_size AS "Size",
    printf("%,d", base_price) AS "Giá",
    description AS "Mô tả"
FROM Products