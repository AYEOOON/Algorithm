"""
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 
제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

<조건>
- 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
   => 가장 최근에 사용된 알고리즘이라는 뜻으로 "메모리에 남아 있는 캐시 중 가장 오래동안 사용되지 않은 캐시를 새로운 캐시로 교체"한다. 
- cache hit일 경우 실행시간은 1이다.  => CPU가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우
- cache miss일 경우 실행시간은 5이다. => CPU가 참조하고자 하는 메모리가 캐시에 존재하고 있지 않을 경우
"""

# 내 풀이
def solution(cacheSize, cities):
    cache = [cities[0].lower()]
    time = 5
    
    if cacheSize == 0:
        time = len(cities) * 5
    
    for city in cities[1::]:
        city = city.lower()
        if len(cache) < cacheSize:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            else:
                cache.append(city)
                time += 5
        elif len(cache) == cacheSize:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            else:
                cache.pop(0)
                cache.append(city)
                time += 5

    return time


# 다른사람 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)  # 덱에 maxlen이라는 기능 기억!
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
