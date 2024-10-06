INSERT INTO millie.t_product (name, description, price, discount_rate, coupon_applicable, category_id) VALUES ('가구1', '1번 가구입니다', 1000, 0.10, 0, 1);
INSERT INTO millie.t_product (name, description, price, discount_rate, coupon_applicable, category_id) VALUES ('가구2', '2번 가구입니다', 5000, 0.00, 1, 1);
INSERT INTO millie.t_product (name, description, price, discount_rate, coupon_applicable, category_id) VALUES ('식품1', '1번 식품입니다', 3000, 0.20, 0, 2);
INSERT INTO millie.t_product (name, description, price, discount_rate, coupon_applicable, category_id) VALUES ('가구3', '3번 가구입니다', 2000, 0.20, 1, 1);

INSERT INTO millie.t_coupon (code, discount_rate) VALUES ('sale10', 0.10);
INSERT INTO millie.t_coupon (code, discount_rate) VALUES ('sale20', 0.20);

INSERT INTO millie.t_category (id, name) VALUES (1, '가구');
INSERT INTO millie.t_category (id, name) VALUES (2, '식품');
