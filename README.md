**- 상품 리스트**

상품 전체 리스트
- 상품 전체 리스트를 조회 합니다.
url : (GET) http://localhost:8000/api/products/
결과 :
[
  {
    "id": 1,
    "name": "가구1",
    "description": "1번 가구입니다",
    "price": 1000,
    "category": "가구",
    "coupon_applicable": false,
    "discount_rate": "0.10"
  },
  {
    "id": 2,
    "name": "가구2",
    "description": "2번 가구입니다",
    "price": 5000,
    "category": "가구",
    "coupon_applicable": true,
    "discount_rate": "0.00"
  },
]

상품 카테고리별 리스트 
- 상품을 카테고리별 조회 합니다. 카테고리 id 를 입력 받습니다.
url : (GET) http://localhost:8000/api/products/?category={id}
결과 :
[
  {
    "id": 1,
    "name": "가구1",
    "description": "1번 가구입니다",
    "price": 1000,
    "category": "가구",
    "coupon_applicable": false,
    "discount_rate": "0.10"
  },
]

**- 상품 상세 정보**

상세정보
- 상품 상세 정보를 조회 합니다. 상품 id 를 입력 받습니다.
url : (GET) http://localhost:8000/api/products/{id}/
결과 :
{
  "id": 1,
  "name": "가구1",
  "description": "1번 가구입니다",
  "price": 1000,
  "category": {
    "id": 1,
    "name": "가구"
  },
  "discount_rate": "0.10",  # 상품 자체 할인율
  "coupon_applicable": false,  # 쿠폰 적용 여부
  "discount_price": 900,  # 상품 할인율 적용 금액 price - (price * discount_rate) = discount_price
  "final_price": 900  # 상품 할인율 + 쿠폰할인 discount_price - (discount_price * coupon_discount_rate) = final_price
}


**- 쿠폰 적용**

쿠폰정보
- 쿠폰 정보를 가져옵니다.
url : (GET) http://localhost:8000/api/coupons/
결과 :
[
  {
    "id": 1,
    "code": "sale10",
    "discount_rate": "0.10"
  },
  {
    "id": 2,
    "code": "sale20",
    "discount_rate": "0.20"
  }
]

쿠폰 적용
- 상품에 쿠폰을 적용합니다,
url : (GET) http://localhost:8000/api/products/{id}/?coupon_code=sale10
결과 :
{
  "id": 1,
  "name": "가구1",
  "description": "1번 가구입니다",
  "price": 1000,
  "category": {
    "id": 1,
    "name": "가구"
  },
  "discount_rate": "0.10",
  "coupon_applicable": false,
  "discount_price": 900,
  "final_price": 900
}

