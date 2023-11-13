
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                               | ip             | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:----------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | gz3.kiki789.com          | Taiwan        | TW   | Data Communication Business Group | 211.20.21.247  | Yes (Region: TW) |
|  1 | [5](config/5.json)   | 183.233.187.214          | Hong Kong     | HK   | CNSERVERS                         | 172.247.18.74  | Yes (Region: US) |
|  2 | [17](config/17.json) | 198.2.193.152            | China         | CN   | PEG-SV                            | 198.2.193.145  | Yes (Region: US) |
|  3 | [26](config/26.json) | n1699253769.aaigefm.cn   | United States | US   | Alibaba US Technology Co., Ltd.   | 47.76.34.124   | Yes (Region: US) |
|  4 | [33](config/33.json) | n1697685464.aaigefm.cn   | United States | US   | Alibaba US Technology Co., Ltd.   | 47.76.44.192   | Yes (Region: US) |
|  5 | [38](config/38.json) | tg_mfbpn_d4.52vpn.eu.org | Taiwan        | TW   | Data Communication Business Group | 211.20.157.212 | Yes (Region: TW) |

## Valid
```
vmess://eyJob3N0IjogImNtaWhrLmJpbGliaWxpLmNvbSIsICJwYXRoIjogIi84ODU4ZDA0NS02NmZlLTQ0MWEtOGQzNS0xNTA3MjE2ZmJiMmYubGl2ZTIzOC5tM3U4IiwgInRscyI6ICIiLCAidmVyaWZ5X2NlcnQiOiB0cnVlLCAiYWRkIjogImd6My5raWtpNzg5LmNvbSIsICJwb3J0IjogNDUyMTEsICJhaWQiOiAwLCAibmV0IjogIndzIiwgImhlYWRlclR5cGUiOiAibm9uZSIsICJ2IjogIjIiLCAidHlwZSI6ICJub25lIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZTdmXHU0ZTFjXHU3NzAxXHU3OWZiXHU1MmE4IDIiLCAicmVtYXJrIjogIlY0LVx1NTNmMFx1NmU3ZTAxfE5GfFYyUkFZIiwgImlkIjogImE0MjgwY2M4LTgzZTMtM2E4ZC1hMTJhLTU2MjU5YWQ0YWMxYiIsICJjbGFzcyI6IDF9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggNSIsICJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgInBvcnQiOiAiMzg5NjIiLCAiaWQiOiAiNzcwZWU3MzAtMjQ1MC00ZTNjLWE2YzYtMzkzMmJkMzJhZmJkIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAxNyIsICJhZGQiOiAiMTk4LjIuMTkzLjE1MiIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjY4ZDIzOGNlLTNjYTEtNDZkYy1iODMzLWEwOTE2YzgyOWFkMyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4yODI1MTY1OC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5NjI0NzIzMjEzIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMjYiLCAiYWRkIjogIm4xNjk5MjUzNzY5LmFhaWdlZm0uY24iLCAicG9ydCI6IDQ0MywgImlkIjogIjk4MmZhZGQxLTNlNWYtNGFhMy04NTUyLWVkNmZkYTIzNDE0YSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAibjE2OTkyNTM3NjkuYWFpZ2VmbS5jbiIsICJwYXRoIjogIi8iLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAibjE2OTc2ODU0NjQuYWFpZ2VmbS5jbiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMzMiLCAicG9ydCI6IDQ0MywgImlkIjogIjE4NzAwMmZkLWI4YWQtNGQzNi1iNGZiLTFhMzIyNGNjOTllMiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJuMTY5NzY4NTQ2NC5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMzgiLCAiYWRkIjogInRnX21mYnBuX2Q0LjUydnBuLmV1Lm9yZyIsICJwb3J0IjogIjExMDEzIiwgImlkIjogIjg1ZGI2NjUyLWE3NDctM2EwYS1hMTcwLTQyMjczNjA3NjQxMCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

