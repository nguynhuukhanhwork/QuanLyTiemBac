-- =======================
-- DỮ LIỆU DEMO
-- =======================

-- Products
INSERT INTO Products (product_name, material, product_size, base_price, description) VALUES
('Nhẫn vàng 24K', 'Vàng', 'Vừa', 7200000 , 'Nhẫn vàng 24K trơn, thiết kế cổ điển'),
('Lắc tay bạc 925', 'Bạc', 'Nhỏ', 100000, 'Lắc tay bạc sáng bóng cho nữ'),
('Dây chuyền ruby', 'Vàng', 'Lớn', 7400000, 'Dây chuyền vàng đính đá ruby');

-- Customers
INSERT INTO Customers (customer_name, phone, address) VALUES
('Nguyễn Văn A', '0909123456', '123 Lê Lợi, Quận 1, TP.HCM'),
('Trần Thị B', '0988222333', '456 Nguyễn Trãi, Quận 5, TP.HCM');

-- Suppliers
INSERT INTO Suppliers (supplier_name, phone, address) VALUES
('Công ty SJC', '0289998888', '1 Nguyễn Huệ, Quận 1, TP.HCM'),
('Bạc Hà Jewelry', '0287776666', '789 CMT8, Quận 10, TP.HCM');

-- Purchases
INSERT INTO Purchases (supplier_id, purchase_date, product_id, quantity, unit_price, subtotal, notes) VALUES
(1, '19-7-2025', 1, 10.0, 6800000, 10.0 * 6800000, 'Mua nhẫn vàng 24K từ SJC'),
(2, '19-7-2025', 2, 20.0, 75000, 20.0 * 75000, 'Nhập lắc tay bạc từ Bạc Hà');

-- Sales
INSERT INTO Sales (customer_id, total_amount, notes) VALUES
(1, 11000000, 'Bán nhẫn vàng và bạc cho khách A'),
(2, 7400000, 'Bán dây chuyền ruby cho khách B');

-- SaleItems
INSERT INTO SaleItems (sale_id, product_id, quantity, unit_price, subtotal) VALUES
-- Bán nhẫn vàng (1.5 chỉ x 7.2 triệu)
(1, 1, 1.5, 7200000, 1.5 * 7200000),
-- Bán lắc bạc (5 chiếc x 100k)
(1, 2, 5, 100000, 5 * 100000),
-- Bán 1 dây chuyền ruby theo đúng base_price
(2, 3, 1, 7400000, 1 * 7400000);