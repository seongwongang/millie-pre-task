-- auto-generated definition
create table t_category
(
    id   bigint auto_increment
        primary key,
    name varchar(100) not null
);


-- auto-generated definition
create table t_coupon
(
    id            bigint auto_increment
        primary key,
    code          varchar(50)   not null,
    discount_rate decimal(5, 2) not null,
    constraint code
        unique (code)
);

-- auto-generated definition
create table t_product
(
    id                bigint auto_increment
        primary key,
    name              varchar(255)         not null,
    description       longtext             not null,
    price             int                  not null,
    discount_rate     decimal(4, 2)        null,
    coupon_applicable tinyint(1) default 0 not null,
    category_id       bigint               not null,
    constraint t_product_category_id_dc613a56_fk
        foreign key (category_id) references t_category (id)
);