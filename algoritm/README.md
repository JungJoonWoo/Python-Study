# Python-Study
N 범위에 따른 시간복잡도(1초 기준)

N < 500인 경우: O(N^3)

N < 2,000인 경우: O(N^2)

N < 100,000인 경우: O(NlogN)

N < 10,000,000인 경우: O(N)

## String

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| len(s) | 문자열의 길이를 반환 | O(1) |
| s[i] | 인덱스를 통한 접근 | O(1) |
| s[i:j] | 슬라이싱 | O(k) |
| s[i:j:k] | k-간격 슬라이싱 | O(k) |
| s + t | 문자열 연결 | O(n + m) |
| s.strip() | 양쪽 공백 제거 | O(n) |
| s.lstrip() | 왼쪽 공백 제거 | O(n) |
| s.rstrip() | 오른쪽 공백 제거 | O(n) |
| s.startswith(prefix) | 특정 문자열로 시작하는지 검사 | O(len(prefix)) |
| s.endswith(suffix) | 특정 문자열로 끝나는지 검사 | O(len(suffix)) |
| s.find(sub) | 부분 문자열의 위치 검색 | O(n) |
| s.rfind(sub) | 부분 문자열의 위치 검색(오른쪽부터) | O(n) |
| s.replace(old, new) | 문자열의 일부를 다른 문자열로 치환 | O(n) |
| s.split(sep) | 문자열을 특정 문자열로 나눔 | O(n) |
| s.join(iterable) | 문자열들을 특정 문자열로 연결 | O(n) |
| s.count(sub) | 부분 문자열의 개수 반환 | O(n) |

## List

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| len(s) | 리스트의 길이를 반환 | O(1) |
| s[i] | 인덱스를 통한 접근 | O(1) |
| s[i:j] | 슬라이싱 | O(k) |
| s[i:j] = t | 슬라이싱을 통한 대체 | O(n) |
| s[i:j:k] | k-간격 슬라이싱 | O(k) |
| s.append(x) | 리스트의 끝에 요소 추가 | O(1) |
| s.pop() | 리스트의 마지막 요소 제거 후 반환 | O(1) |
| s.pop(i) | 특정 인덱스 요소 제거 후 반환 | O(n) |
| s.insert(i, x) | 특정 위치에 요소 추가 | O(n) |
| s.remove(x) | 리스트에서 값 x 제거 | O(n) |
| s.count(x) | x의 개수 반환 | O(n) |
| s.index(x) | x의 인덱스 반환 | O(n) |
| s.sort() | 리스트 정렬 | O(n log n) |
| min(s), max(s) | 최소값, 최대값 반환 | O(n) |
| s.reverse() | 리스트를 역순으로 뒤집음 | O(n) |

## Tuple

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| len(t) | 튜플의 길이를 반환 | O(1) |
| t[i] | 인덱스를 통한 접근 | O(1) |
| t[i:j] | 슬라이싱 | O(k) |
| t[i:j:k] | k-간격 슬라이싱 | O(k) |
| min(t), max(t) | 최소값, 최대값 반환 | O(n) |
| t.index(x) | x의 인덱스 반환 | O(n) |
| t.count(x) | x의 개수 반환 | O(n) |

## Dictionary

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| len(d) | 사전의 길이를 반환 | O(1) |
| d[key] | 키를 통한 접근 | O(1) |
| d[key] = value | 키를 통한 값 할당 | O(1) |
| key in d | 사전에 특정 키가 있는지 검사 | O(1) |
| key not in d | 사전에 특정 키가 없는지 검사 | O(1) |
| del d[key] | 특정 키와 그에 대응하는 값을 삭제 | O(1) |
| d.clear() | 사전의 모든 항목 삭제 | O(1) |
| d.copy() | 사전의 얕은 복사 | O(n) |
| d.get(key) | 특정 키에 대응하는 값을 반환 (없을 경우 None) | O(1) |
| d.items() | 사전의 모든 (키, 값) 쌍을 반환 | O(n) |
| d.keys() | 사전의 모든 키를 반환 | O(n) |
| d.values() | 사전의 모든 값을 반환 | O(n) |
| d.update(d2) | 다른 사전 d2의 (키, 값) 쌍을 d에 추가 | O(len(d2)) |

## Set

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| len(s) | 집합의 길이를 반환 | O(1) |
| x in s | 집합에 특정 원소가 있는지 검사 | O(1) |
| x not in s | 집합에 특정 원소가 없는지 검사 | O(1) |
| s.issubset(t) | s가 t의 부분집합인지 검사 | O(len(s)) |
| s.issuperset(t) | s가 t의 상위집합인지 검사 | O(len(t)) |
| s.union(t) | s와 t의 합집합 반환 | O(len(s) + len(t)) |
| s.intersection(t) | s와 t의 교집합 반환 | O(min(len(s), len(t))) |
| s.difference(t) | s와 t의 차집합 반환 | O(len(t)) |
| s.symmetric_difference(t) | s와 t의 대칭차집합 반환 | O(len(s)) |
| s.copy() | s의 얕은 복사본을 반환 | O(len(s)) |
| s.add(x) | s에 원소 x 추가 | O(1) |
| s.remove(x) | s에서 원소 x 제거 | O(1) |
| s.discard(x) | s에서 원소 x 제거(없어도 에러 발생하지 않음) | O(1) |
| s.pop() | s에서 임의의 원소 제거 후 반환 | O(1) |
| s.clear() | s의 모든 원소 제거 | O(1) |

## 내장 함수

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| abs(x) | 숫자의 절대값 반환 | O(1) |
| all(iterable) | 모든 요소가 참이면 True 반환 | O(n) |
| any(iterable) | 어떤 요소가 참이면 True 반환 | O(n) |
| ascii(object) | 객체를 ascii 형태로 반환 | O(n) |
| bin(x) | 정수를 이진 문자열로 변환 | O(log n) |
| bool([x]) | 불리언 값을 반환 | O(1) |
| chr(i) | 유니코드 코드 포인트가 정수 i인 문자 반환 | O(1) |
| divmod(a, b) | a를 b로 나눈 몫과 나머지를 튜플로 반환 | O(1) |
| enumerate(iterable[, start]) | 열거 객체 반환 | O(1) |
| eval(expression[, globals[, locals]]) | 표현식의 문자열을 평가하고 결과 반환 | O(n) |
| filter(function, iterable) | iterable의 요소 중 function이 참인 것들로 이루어진 이터레이터 반환 | O(n) |
| hex(x) | 정수를 16진수 문자열로 변환 | O(log n) |
| len(s) | 길이(요소의 수) 반환 | O(1) |
| map(function, iterable, ...) | 각 요소가 함수에 의해 수행된 결과를 반환 | O(n) |
| max(iterable, *[, key, default]) | 가장 큰 항목 반환 | O(n) |
| min(iterable, *[, key, default]) | 가장 작은 항목 반환 | O(n) |
| pow(base, exp[, mod]) | base의 exp승을 반환, mod가 주어지면 base의 exp승을 mod로 나눈 나머지 반환 | O(1) |
| range([start,] stop[, step]) | 연속된 정수를 가진 객체 반환 | O(1) |
| round(number[, ndigits]) | 숫자를 가장 가까운 정수로 반올림 | O(1) |
| sorted(iterable, *, key=None, reverse=False) | 새로 정렬된 리스트 반환 | O(n log n) |
| sum(iterable[, start]) | 합계 반환 | O(n) |
| type(object) | 객체의 타입 반환 | O(1) |

## itertools

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| chain(*iterables) | 여러 시퀀스를 연결하여 반환 | O(n) |
| combinations(iterable, r) | 입력 iterable에서 요소의 길이 r 서브 시퀀스를 생성 | O(nCr) |
| combinations_with_replacement(iterable, r) | 입력 iterable에서 요소의 길이 r 서브 시퀀스를 생성(중복 허용) | O((n+r-1)Cr) |
| count(start=0, step=1) | start부터 시작하여 step만큼 더하는 무한 이터레이터 | O(∞) |
| cycle(iterable) | 입력 iterable을 무한히 반복하는 이터레이터 | O(∞) |
| islice(iterable, start, stop[, step]) | 시퀀스 s를 s[start:stop:step]와 유사하게 슬라이싱 | O(n) |
| permutations(iterable, r=None) | 입력 iterable에서 요소의 길이 r 순열을 생성 | O(nPr) |
| product(*iterables, repeat=1) | 입력 iterable의 데카르트 곱을 생성 | O(n^r) |
| repeat(object[, times]) | 주어진 횟수만큼 객체를 반복하여 반환 | O(n) |

## heapq

| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| heapify(x) | 리스트 x를 선형 시간에 유효한 힙으로 변환 | O(n) |
| heappush(heap, item) | item을 heap에 추가 | O(log n) |
| heappop(heap) | heap에서 가장 작은 항목을 제거하고 반환 | O(log n) |
| heappushpop(heap, item) | heap에 item을 푸시한 다음, heap에서 가장 작은 항목을 제거하고 반환 | O(log n) |
| heapreplace(heap, item) | heap에서 가장 작은 항목을 제거하고 반환한 다음, item을 heap에 추가 | O(log n) |
| nlargest(n, iterable[, key]) | iterable에서 가장 큰 n 개의 항목을 반환 | O(n log n) |
| nsmallest(n, iterable[, key]) | iterable에서 가장 작은 n 개의 항목을 반환 | O(n log n) |

## bisect
| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| bisect_left(a, x, lo=0, hi=len(a)) | 정렬된 리스트 a에 x를 삽입할 위치를 찾아 반환(이미 x와 같은 값이 있으면 그 앞의 위치 반환) | O(log n) |
| bisect_right(a, x, lo=0, hi=len(a)), bisect(a, x, lo=0, hi=len(a)) | 정렬된 리스트 a에 x를 삽입할 위치를 찾아 반환(이미 x와 같은 값이 있으면 그 뒤의 위치 반환) | O(log n) |
| insort_left(a, x, lo=0, hi=len(a)) | 정렬된 리스트 a에 x를 삽입(이미 x와 같은 값이 있으면 그 앞에 삽입) | O(n) |
| insort_right(a, x, lo=0, hi=len(a)), insort(a, x, lo=0, hi=len(a)) | 정렬된 리스트 a에 x를 삽입(이미 x와 같은 값이 있으면 그 뒤에 삽입) | O(n) |

## Counter

| 메서드 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| elements() | Counter 객체에서 원소를 반복적으로 반환 | O(n) |
| most_common([n]) | 가장 많이 나타나는 n 개의 요소와 그들의 수를 반환 | O(n log n) |
| subtract([iterable-or-mapping]) | 반복가능한 객체 또는 매핑에서 Counter 객체를 뺌 | O(n) |

## deque

| 메서드 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| append(x) | 데크의 오른쪽에 x 추가 | O(1) |
| appendleft(x) | 데크의 왼쪽에 x 추가 | O(1) |
| pop() | 데크의 오른쪽 요소 제거 후 반환 | O(1) |
| popleft() | 데크의 왼쪽 요소 제거 후 반환 | O(1) |
| rotate(n) | 데크의 요소를 n만큼 오른쪽으로 회전 | O(n) |

## math
| 함수 | 설명 | 시간 복잡도 |
| --- | --- | --- |
| ceil(x) | x보다 크거나 같은 가장 작은 정수를 반환 | O(1) |
| floor(x) | x보다 작거나 같은 가장 큰 정수를 반환 | O(1) |
| fabs(x) | x의 절대값을 반환 | O(1) |
| factorial(x) | x의 팩토리얼을 반환 | O(n) |
| fmod(x, y) | x를 y로 나눈 나머지를 반환 | O(1) |
| frexp(x) | x를 맨티사와 지수로 분리하여 반환 | O(1) |
| fsum(iterable) | iterable의 합계를 반환 | O(n) |
| gcd(a, b) | a와 b의 최대공약수를 반환 | O(log min(a, b)) |
| isfinite(x) | x가 유한한지 검사 | O(1) |
| isinf(x) | x가 무한대인지 검사 | O(1) |
| isnan(x) | x가 NaN인지 검사 | O(1) |
| pow(x, y) | x의 y승을 반환 | O(1) |
| sqrt(x) | x의 제곱근을 반환 | O(1) |
| log(x[, base]) | 로그 값을 계산하여 반환 | O(1) |
| sin(x) | 사인 값을 계산하여 반환 | O(1) |
| cos(x) | 코사인 값을 계산하여 반환 | O(1) |
| tan(x) | 탄젠트 값을 계산하여 반환 | O(1) |
