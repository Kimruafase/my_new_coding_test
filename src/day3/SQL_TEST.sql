-- 천재지변으로 인해 일부 데이터가 유실되었습니다.
-- 입양을 간 기록은 있는데,
-- 보호소에 들어온 기록이 없는
-- 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.

SELECT o.animal_id, o.name
from animal_outs as o
left join animal_ins as i on o.animal_id = i.animal_id
where i.animal_id is null

-- 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다.
-- 보호 시작일보다 입양일이 더 빠른 동물의
-- 아이디와 이름을 조회하는 SQL문을 작성해주세요.
-- 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.

SELECT i.animal_id, i.name
from animal_ins as i
inner join animal_outs as o on i.animal_id = o.animal_id
where i.datetime > o.datetime
order by i.datetime asc

-- 아직 입양을 못 간 동물 중,
-- 가장 오래 보호소에 있었던 동물
-- 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요.
-- 이때 결과는 보호 시작일 순으로 조회해야 합니다.

SELECT i.name, i.datetime
from animal_ins as i
left join animal_outs as o on i.animal_id = o.animal_id
where o.animal_id is null
order by i.datetime asc
limit 3

-- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다.
-- 보호소에 들어올 당시에는 중성화1되지 않았지만,
-- 보호소를 나갈 당시에는 중성화된 동물의
-- 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.

SELECT i.animal_id, i.animal_type, i.name
from animal_ins as i
inner join animal_outs as o on i.animal_id = o.animal_id
where i.sex_upon_intake like "intact%" and o.sex_upon_outcome not like "intact%"

-- USER_INFO 테이블과 ONLINE_SALE 테이블에서 2021년에 가입한 전체 회원들 중
-- 상품을 구매한 회원수와 상품을 구매한 회원의 비율
-- (=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을
-- 년, 월 별로 출력하는 SQL문을 작성해주세요.
-- 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림하고,
-- 전체 결과는 년을 기준으로 오름차순 정렬해주시고
-- 년이 같다면 월을 기준으로 오름차순 정렬해주세요.

SELECT date_format(o.sales_date, '%Y') as YEAR,
month(o.sales_date) as MONTH,
count(distinct u.user_id) as PURCHASED_USERS,
round((count(distinct u.user_id)/
       (select count(user_id)
        from user_info
        where joined like "2021%")), 1) as PURCHASED_RATIO
from user_info as u
inner join online_sale as o on u.user_id = o.user_id
where u.joined like "2021%"
group by YEAR, MONTH
order by YEAR asc, MONTH asc