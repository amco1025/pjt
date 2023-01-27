# problem_a
```
인기있는 영화 목록을 응답 받아 개수를 출력하라.
 ```

 ### 어려웠던 점
 ```
 API key를 처음 사용해보아 데이터를 불러오는 과정이 어려웠다.
 ```

 ### 해결과정
 ```
 사이트 검색과 교수님 설명을 통하여 조금은 API key사용법에 대하여 알게 되었다.
 ```

 ### 만든 함수 
 ```
 def popular_count():  # 함수 선언
    URL = 'https://api.themoviedb.org/3/movie/popular?  api_key=b75123c6e5d59d8072f7aeb3cabcf263&language=ko-KR' 
    # popular데이터를 한국어와 한국지역에서 불러옴

    response = requests.get(URL).json() 
    cnt = 0 
    # 반환해야 할 값인 수를 cnt라는 변수를 통하여 선언하고 초기 값으로 0할당.

    for _ in response['results']: # results의 길이만큼 단순 반복
        cnt += 1 # 반복문을 돌 떄 마다 cnt의 값을 1증가
        
    return cnt # cnt 반환
```

### 풀이 과정
```
1. url에 tmdb에서 현재 인기 있는 영화를 API key를 통하여 불러옴
2. 반환할 값인 인기 있는 영화 개수를 나타내주는 변수 cnt를 생성하고 0 할당.
3. 인기있는 영화의 개수만큼 반복문을 돌면서 cnt의 값을 1씩 증가.

```

# problem_b
```
인기 영화 목록 중 평점이 8점 이상인 영화를 출력하라
```

### 어려웠던 점
```
처음 출력할 평점이 8점 이상인 영화를 보여줄 리스트를 만들지 않고 반복문을 돌리며 출력할려 하여 1나의 영화만 반환되었다.
```

### 해결과정
```
평점이 8점 이상인 영화를 보여줄 리스트를 만들고 반복문을 돌며 위 문제의 조건인 평점이 8점 넘는 영화만을 리스트에 append하며 저장한 후 출력하였다.
```

### 만든 함수
```
def vote_average_movies():  # 함수 선언
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=b75123c6e5d59d8072f7aeb3cabcf263&language=ko-KR&region=KR'
    # 인기있는 영화를 API key를 사용하여 불러옴
    response = requests.get(URL).json()
    answer = [] # 평점이 8점 넘는 영화만 저장할 리스트 생성

    for i in response['results']: # 인기 있는 영화들을 넣어가며 반복문 진행
      for j in i.keys(): # 그 영화에 대한 key들을 넣어가며 반복문 진행
        if j == 'vote_average': # 만약 그 값이 평점이라면
          if i[j] >= 8: # 그리고 그 평점이 8점 이상이라면
            answer.append(i) # 반환할 리스트에 append

    return(answer) # 평점이 8점 이상인 영화들을 반환

```

### 풀이 과정
```
1. url에 tmdb에서 현재 인기 있는 영화를 API key를 통하여 불러옴
2. 평점이 8점 이상인 영화들만 저장할 리스트 생성
3. 반복문을 돌며 조건을 만족하는 영화들을 반환할 리스트에 저장
4. 리스트 반환
```

# problem_c
```
인기 영화 목록을 평점이 높은 순으로 5개의 영화 데이터 목록 출력합니다.
```

### 어려웠던 점
```
sorted()에 대하여 정확히 몰라 처음 .sort()처럼 사용하여 값에 따라 정렬이 안되었다.
리스트 안에 있는 딕셔너리의 특정 값에 따라 정렬하는 방법에 대하여 몰라 어려웠다.
```

### 해결 과정
```
sort와 달리 sorted는 변수에 정렬된 값을 할당하여야 그 값이 저장된다는 것을 찾아보고 그렇게 하였더니 되었다.
정렬 방법은 구글을 찾아보다 sorted안에서 람다 함수를 사용 가능하다는 것을 알게 되어 그 방법으로 해결하였다.
```

### 만든 함수
```
def ranking():      # 함수 선언
    ranking = []    # 평점이 높은 순서로 5개의 영화를 저장할 리스트 생성
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=b75123c6e5d59d8072f7aeb3cabcf263&language=ko-KR&region=KR'
    # 인기 있는 영화를 API key를 사용하여 불러옴
    response = requests.get(URL).json()
    li = response['results'] # li에 response중 results에 있는 값을 저장
    li = sorted(li , key= lambda x: x['vote_average'], reverse = True)
    # 평점이 높은 순서로 정렬
    for i in range(5):
      ranking.append(li[i])
      # 반복문을 5번 돌며 차례대로 ranking 리스트에 저장
    return ranking # ranking 리스트 반환
    
```

### 풀이 과정
```
1. url에 tmdb에서 현재 인기 있는 영화를 API key를 통하여 불러옴
2. 새로 만든 리스트에 response['results]를 저장
3. 리스트에 저장된 값들을 평점 순서로 정렬
4. 평점이 가장 높은 영화 5개만을 저장할 리스트에 반복문을 돌며 영화 저장
5. 반환
```

# problem_d
```
제공된 영화 제목을 검색하여 추천 영화 목록을 출력
```

### 어려웠던 점
```
url을 통하여 정보를 가져오는 과정에서 한번만 사용하는 것이 아닌 계속하여 타고 들어 갈 수 있다는 것을 처음에는 모르고 알게된 후에는 익숙하지 않아 어려웠다.
```

### 해결 과정
```
처음에는 질문을 통하여 url을 여러번 사용 가능하다는 것을 알게 되고 어떻게 사용하는지 알게 되었다.
```

### 만든 함수
```
def recommendation(title):
     
    li = []
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=b75123c6e5d59d8072f7aeb3cabcf263&language=ko-KR&region=KR&page=1&include_adult=false&query={title}'
    response = requests.get(URL).json()
    # 입력한 영화 제목에 맞추어 값을 가져옴
    try:
        id = response['results'][0]['id'] # 가져온 값에서 id값을 id라는 변수에 저장
        recomm_URL = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key=b75123c6e5d59d8072f7aeb3cabcf263&language=ko-KR&region=KR&page=1' # 그 id 값에 맞추어 추천영화 반환
    except IndexError: # 만약 없다면 None 반환
        return None
    
    recomm_response = requests.get(recomm_URL).json()
    result_title = recomm_response['results']  # 출력할 변수에 recomm_response['results'] 저장
    for i in result_title: # 반복문을 돌며 
        li.append(i['title']) # 반환할 li에 append

    return li # li 반환

```
# problem_e
```
제공된 영화 제목을 검색하여 해당 영화의 출연진과 스태프 중 연출진 반환
```

### 어려웠던 점
```
데이터를 전체적으로 볼 수 없어서 앞에 문제들과 같이 results인줄 알고 cast와 crew가 따로 있는지 몰라서 어려웠다.
```

### 해결 과정
```
사이트에서 example을 통하여 데이터를 볼 수 있다는 것을 알게 되어 보니 results가 아닌 cast와 crew로 나누어 저장 되어 있다는 것을 알게 되어 해결할 수 있었다.
```

### 만든 함수 
```
def credits(title):
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=b75123c6e5d59d8072f7aeb3cabcf263&language=ko-KR&region=KR&page=1&include_adult=false&query={title}' # 입력한 영화 제목에 맞는 정보를 불러옴
    response = requests.get(URL).json()
    answer = {'cast' : [], 'directing': []} # 문제에서 요구하는 출력 값에 맞추는 변수 생성
    try:
        id = response['results'][0]['id'] # 입력한 값의 id값을 id라는 변수에 할당
        credict_URL = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key=b75123c6e5d59d8072f7aeb3cabcf263&language=ko-KR&region=KR'
    except IndexError:
        return None # id값에 맞는 영화의 credict 정보를 가져옴
    # 여기에 코드를 작성합니다.  
    credict_response = requests.get(credict_URL).json()
    credict_cast = credict_response['cast'] # credict_cast에 cast의 정보만 저장
    credict_crew = credict_response['crew'] # credict_crew에 crew의 정보만 저장
    for i in credict_cast: # cast의 정보만 넣으면 반복문 진행
        for j in i.keys():
            if j == 'cast_id':
                if i[j] < 10:
                    answer['cast'].append(i['name'])
                else:
                    continue
    # 문제의 조건을 충족하면 반환할 변수에서 cast 칸에 이름은 append
    for i in credict_crew: # crew의 정보만 넣으며 반복문 진행
        for j in i.keys(): 
            if j == 'department':
                if i[j] == 'Directing':
                    answer['directing'].append(i['name'])
    # 문제의 조건을 만족하면 반환할 변수에서 directing 칸에 이름을 append
    return answer
```
### 풀이 과정
```
1. 영화의 정보 가져오기
2. 문제의 조건에 맞추어 반환할 자료구조 선언
3. 입력한 영화에 맞는 credict 정보를 가져옴
4. cast와 crew에 따라 정보 저장
5. cast와 crew를 각각 반복문에 넣으며 반복문 진행
6. 조건을 충족하는 값만 반환할 변수에 저장
7. 변수 반환
```


