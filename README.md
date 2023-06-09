
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                      | cn            | cc   | isp                               | ip             | chatgpt          |
|---:|:---------------------|:--------------------------|:--------------|:-----|:----------------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 45.58.186.81              | United States | US   | SHARKTECH                         | 64.32.2.26     | Yes (Region: US) |
|  1 | [4](config/4.json)   | 64.32.4.39                | United States | US   | SHARKTECH                         | 107.167.13.162 | Yes (Region: US) |
|  2 | [8](config/8.json)   | ns1.v2-vip.fun            | Germany       | DE   | AS-GLOBALTELEHOST                 | 193.108.118.34 | Yes (Region: DE) |
|  3 | [9](config/9.json)   | tw99-hinet.mynodes001.one | Taiwan        | TW   | Data Communication Business Group | 61.224.76.224  | Yes (Region: TW) |
|  4 | [10](config/10.json) | 120.241.117.55            | Singapore     | SG   | G-Core Labs S.A.                  | 91.243.81.99   | Yes (Region: SG) |
|  5 | [12](config/12.json) | 8.v2-ray.cyou             | Japan         | JP   | AMAZON-02                         | 18.179.36.139  | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuNTguMTg2LjgxIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDUxMTQwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiNjQuMzIuNC4zOSIsICJwb3J0IjogIjQzMTY2IiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAibnMxLnYyLXZpcC5mdW4iLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiaG9zdCI6ICJkZTUuaXJ0ZWguZnVuIiwgImlkIjogIjhhYmU5NDk2LTVlMjQtNGU0OS1iNTY2LWRjZjg2MTE2MDE3ZCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvaTk5TGd2U2FzbGJzUExMUVE3ajZaIiwgInBvcnQiOiAiODAiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAidHc5OS1oaW5ldC5teW5vZGVzMDAxLm9uZSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNWYwNGRlODQtNmI3ZS0zNTY0LTgyYzItZDJhOTk4MDAyNjI5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTIwLjI0MS4xMTcuNTUiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjc4OGU2NTc3LWVlOTktM2IyNy1iOGUzLTgxMTQxMWFlMzJhOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNzExMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZTdmXHU0ZTFjXHU3NzAxXHU3OWZiXHU1MmE4IDEwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

