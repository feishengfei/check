
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr           | cn            | cc   | isp        | ip             | chatgpt          |
|---:|:-------------------|:---------------|:--------------|:-----|:-----------|:---------------|:-----------------|
|  0 | [2](config/2.json) | 142.4.99.90    | United States | US   | PEGTECHINC | 142.4.99.65    | Yes (Region: US) |
|  1 | [3](config/3.json) | 64.32.4.45     | United States | US   | SHARKTECH  | 107.167.13.162 | Yes (Region: US) |
|  2 | [4](config/4.json) | 156.225.67.159 | Netherlands   | NL   | YISP B.V.  | 154.84.1.197   | Yes (Region: NL) |
|  3 | [7](config/7.json) | 156.245.8.158  | Netherlands   | NL   | YISP B.V.  | 154.84.1.138   | Yes (Region: NL) |
|  4 | [8](config/8.json) | 64.32.24.213   | United States | US   | CNSERVERS  | 23.225.9.234   | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuOTkuOTAiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0ggMiIsICJwb3J0IjogNDMzNzksICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuNC40NSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzE2NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNTkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5YzAyNmVmZS02YWYwLTQ2NWYtYjhjMC0zZjU4YzhjMmQ0YzUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDg5MjEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE1OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDciLCAicG9ydCI6IDQ4MTIzLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjEzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA4IiwgInBvcnQiOiA0ODY1OSwgImlkIjogImNmZjlkODYwLTczMzAtNGVlMS1iMDcyLTcxNDJkZGYxNTcxZCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

