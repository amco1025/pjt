import requests
from pprint import pprint
import ast

def credits(title):
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=?&language=ko-KR&region=KR&page=1&include_adult=false&query={title}'
    response = requests.get(URL).json()
    answer = {'cast' : [], 'directing': []}
    try:
        id = response['results'][0]['id']
        credict_URL = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key=?&language=ko-KR&region=KR'
    except IndexError:
        return None
    # 여기에 코드를 작성합니다.  
    credict_response = requests.get(credict_URL).json()
    credict_cast = credict_response['cast']
    credict_crew = credict_response['crew']
    for i in credict_cast:
        for j in i.keys():
            if j == 'cast_id':
                if i[j] < 10:
                    answer['cast'].append(i['name'])
                else:
                    continue
    
    for i in credict_crew:
        for j in i.keys():
            if j == 'department':
                if i[j] == 'Directing':
                    answer['directing'].append(i['name'])
    
    return answer
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
