import requests


def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=b75123c6e5d59d8072f7aeb3cabcf263&language=ko-KR'

    response = requests.get(URL).json()
    cnt = 0

    for _ in response['results']:
        cnt += 1
        
    return cnt
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
