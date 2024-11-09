-- CAR_RENTAL_COMPANY_CAR 테이블과
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과
-- CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서
-- 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중
-- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
-- 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서
-- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요.
-- 결과는 대여 금액을 기준으로 내림차순 정렬하고,
-- 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬,
-- 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.

SELECT c1.CAR_ID as CAR_ID,
c1.CAR_TYPE as CAR_TYPE,
round(c1.DAILY_FEE * 30 * (100 - c3.DISCOUNT_RATE) / 100) as FEE
from CAR_RENTAL_COMPANY_CAR as c1
inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY as c2 on c1.CAR_ID = c2.CAR_ID
inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as c3 on c1.CAR_TYPE = c3.CAR_TYPE
where c1.CAR_ID not in (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where END_DATE >= "2022-11-01 00:00:00" and START_DATE <= "2022-12-01 00:00:00")
and c3.DURATION_TYPE like "30%"
group by c1.CAR_ID
having c1.CAR_TYPE in ("세단", "SUV") and (FEE >= 500000 and FEE < 2000000)
order by FEE desc, CAR_TYPE asc, CAR_ID desc

-- FOOD_PRODUCT와 FOOD_ORDER 테이블에서
-- 생산일자가 2022년 5월인 식품들의
-- 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요.
-- 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고
-- 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.

SELECT P.PRODUCT_ID, P.PRODUCT_NAME, (P.PRICE * SUM(O.AMOUNT)) as TOTAL_SALES
from FOOD_PRODUCT as P
inner join FOOD_ORDER as O on P.PRODUCT_ID = O.PRODUCT_ID
where O.PRODUCE_DATE > "2022-04-30" and O.PRODUCE_DATE <= "2022-05-31"
group by P.PRODUCT_ID
order by TOTAL_SALES desc, P.PRODUCT_ID asc

-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이
-- 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

SELECT F.FLAVOR
from FIRST_HALF as F
inner join JULY as J on F.FLAVOR = J.FLAVOR
group by F.FLAVOR
order by sum(F.TOTAL_ORDER) + sum(J.TOTAL_ORDER) desc
limit 3

-- DEVELOPERS 테이블에서 Front End 스킬을 가진 개발자의 정보를 조회하려 합니다.
-- 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요.
-- 결과는 ID를 기준으로 오름차순 정렬해 주세요.

select distinct D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
from DEVELOPERS as D
inner join SKILLCODES as S on S.CODE = S.CODE & D.SKILL_CODE
where S.CATEGORY like "Front End"
order by D.ID

-- '경제' 카테고리에 속하는 도서들의
-- 도서 ID(BOOK_ID), 저자명(AUTHOR_NAME), 출판일(PUBLISHED_DATE) 리스트를 출력하는 SQL문을 작성해주세요.
-- 결과는 출판일을 기준으로 오름차순 정렬해주세요.

SELECT b.BOOK_ID, A.AUTHOR_NAME,
date_format(B.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK as b
inner join AUTHOR as a on b.AUTHOR_ID = a.AUTHOR_ID
where b.CATEGORY like "경제"
order by B.PUBLISHED_DATE asc

-- MEMBER_PROFILE와 REST_REVIEW 테이블에서
-- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성해주세요.
-- 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고,
-- 결과는 리뷰 작성일을 기준으로 오름차순,
-- 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬해주세요.

SELECT m.member_name as MEMBER_NAME,
r.review_text as REVIEW_TEXT,
date_format(r.review_date, '%Y-%m-%d') as REVIEW_DATE
from member_profile as m
inner join rest_review as r on m.member_id = r.member_id
where m.member_id =
(select member_id
from rest_review
group by member_id
order by count(member_id) desc
limit 1)
order by REVIEW_DATE asc, REVIEW_TEXT asc