CREATE TABLE sales (
  id          bigserial,
  uuid        uuid,
  total       numeric(7, 2) DEFAULT 0.0,
  sale_date   timestamp with time zone NOT NULL,
  created_at  timestamp with time zone NOT NULL DEFAULT NOW(),
  city        text,
  country     text,
  latitude    float,
  longitude   float
);
CREATE TABLE fraud (
  id          bigserial,
  uuid        uuid,
  created_at  timestamp with time zone NOT NULL,
  fraud_type  numeric
);
CREATE TABLE products (
  productId   bigserial,
  productName text,
  description text
);
CREATE TABLE contrats(
  uuid        uuid,
  productId   bigserial,
  startDate   timestamp with time zone NOT NULL,
  endDate     timestamp with time zone NOT NULL
);