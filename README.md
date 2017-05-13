# maisie-info

## 나를 소개하는 페이지를 만들자

### 머리말
지금 있는 [maisie.site](https://maisie.site)에는 그냥 index.html 파일 달랑 있어서 업데이트 하려면 html을 손대야 하지만 저는 그것이 너무너무 귀찮고 힘든 의지 박약 사람이기 때문에 절대 이렇게 놓아선 안된다고 판단, 새로운 홈페이지를 만들기로 했습니다.

조금 유용하게 만들기 위해서, pinned repository를 보여주거나 최근 github 활동 등을 API로 가져와서 보여줄 생각입니다. 그리고 이걸 오픈소스로 공개하는 것까지 하면 완벽하겠지요. 다른 사람들도 잘 쓰면 좋겠다는 생각에서 만들기로 했습니다. x_x 잘 될지 안될지는 모르지만요.

새로운 Web 환경을 공부한다는 생각으로 처음에는 계획을 장황하게 잡았지만, 뭐 일단 아는 것과 새로운 것의 비율을 잘 맞춰서 만든 다음에 업데이트 하면 좋지 않을까? 하는 생각을 합니다.

### 목표
- 홈페이지 안에서 github 활동도 보고 github repository로 이동도 되고 아무튼 내 개발 이력을 볼 수 있게 하면 좋겠다
- 다른 사람도 보고 쉽게 만들 수 있게 주석을 많이 달자
- 수시로 업데이트 하자

### 스펙
- Python 3

### 라이브러리
- [Flask](https://github.com/pallets/flask)
- [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)
- [Github API](https://developer.github.com/v3/) - [GutHub-Flask](https://github-flask.readthedocs.io/en/latest/)

### TODO
- [ ] Python - SQLAlchemy
- [ ] + HTML/CSS
- [ ] + Flask
- [ ] + Github API
- [ ] + Publish & Final Debug
