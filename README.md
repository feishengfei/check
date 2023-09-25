
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp       | ip                                   | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:----------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 154.85.1.244   | Netherlands   | NL   | YISP B.V. | 154.84.1.206                         | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 45.199.138.209 | Netherlands   | NL   | YISP B.V. | 2a02:2a38:1:2796:ae1f:6bff:fe24:8940 | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.225.67.25  | Netherlands   | NL   | YISP B.V. | 154.84.1.193                         | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 156.245.8.146  | Netherlands   | NL   | YISP B.V. | 154.84.1.134                         | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 45.199.138.180 | Netherlands   | NL   | YISP B.V. | 154.84.1.229                         | Yes (Region: NL) |
|  5 | [8](config/8.json)   | 156.225.67.48  | Poland        | PL   | OVH SAS   | 54.36.174.181                        | Yes (Region: FR) |
|  6 | [9](config/9.json)   | 67.21.64.84    | United States | US   | SHARKTECH | 67.21.72.34                          | Yes (Region: US) |
|  7 | [13](config/13.json) | 107.167.16.85  | United States | US   | SHARKTECH | 170.178.189.50                       | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU0OTgyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4yMDkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhNDY5MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTA0NDcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjUiLCAicG9ydCI6ICI1MTM4MSIsICJpZCI6ICIzNzVlNzBmMC01ZDQ2LTQ3NmYtOGQ2OS0wZmIzNWM1NTQ4YTkiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYzYjRiODI5LTdmMDEtNGUyNi1iMDM3LWYwNGIxZjA5ODc2NSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Mjk1MiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4MCIsICJwb3J0IjogIjU0ODg1IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJkMzEzMzQ4NC1mMmJmLTRiMGMtOGQzOC1mOGU2NDViNjU2ODciLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny40OCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NTQ5MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjcuMjEuNjQuODQiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQzMTIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDkiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogIjEwNy4xNjcuMTYuODUiLCAicG9ydCI6IDQ0MywgImlkIjogIjc2NDBhMWU3LTk3MDEtNDI4ZS1hNGIyLTE5YjNlN2RkNmY5ZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41MTEwOTA1Ny54eXoiLCAicGF0aCI6ICIvcGF0aC8wODA4MjIyNzI5MTQiLCAidGxzIjogInRscyJ9
```

