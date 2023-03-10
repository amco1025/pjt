import requests
from pprint import pprint


def recommendation(title):
     
    li = []
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=?&language=ko-KR&region=KR&page=1&include_adult=false&query={title}'
    response = requests.get(URL).json()
    
    try:
        id = response['results'][0]['id']
        recomm_URL = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key=?&language=ko-KR&region=KR&page=1'
    except IndexError:
        return None
    
    recomm_response = requests.get(recomm_URL).json()
    result_title = recomm_response['results']
    for i in result_title:
        li.append(i['title'])

    return li


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
