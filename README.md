
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp        | ip                                 | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------|:-----------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 107.167.29.93   | United States | US   | SHARKTECH  | 107.167.9.234                      | Yes (Region: US) |
|  1 | [3](config/3.json)   | 107.167.29.229  | United States | US   | SHARKTECH  | 170.178.180.90                     | Yes (Region: US) |
|  2 | [4](config/4.json)   | 67.21.84.216    | United States | US   | SHARKTECH  | 67.21.85.2                         | Yes (Region: US) |
|  3 | [5](config/5.json)   | 173.82.55.92    | United States | US   | MULTA-ASN1 | 23.234.230.34                      | Yes (Region: US) |
|  4 | [6](config/6.json)   | 23.234.198.83   | United States | US   | MULTA-ASN1 | 2607:f130:109:0:225:90ff:fe79:7d34 | Yes (Region: US) |
|  5 | [8](config/8.json)   | 23.234.198.86   | United States | US   | MULTA-ASN1 | 2607:f130:109:0:225:90ff:fe79:7d34 | Yes (Region: US) |
|  6 | [9](config/9.json)   | 183.232.249.189 | Hong Kong     | HK   | CNSERVERS  | 172.247.175.42                     | Yes (Region: US) |
|  7 | [31](config/31.json) | 139.99.245.164  |               |      |            | 139.99.130.144                     | Yes (Region: AU) |
|  8 | [35](config/35.json) | 54.36.174.181   |               |      |            | 54.36.174.181                      | Yes (Region: FR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTA3LjE2Ny4yOS45MyIsICJwb3J0IjogIjQ1NTg1IiwgImlkIjogIjQ2NWRlYzFhLWUwOWItNGJiNi05OTA1LTcwZjc1ZDYwMzVjOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTA3LjE2Ny4yOS4yMjkiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjQ2MzIxIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE2IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgInBvcnQiOiA0NzA4OCwgImlkIjogImI5YTMwNWE5LTFmZjItNGVjMS1iMzM4LTkzMzU1NTgzM2JhYSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTczLjgyLjU1LjkyIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUiLCAicG9ydCI6IDM0NDEyLCAiaWQiOiAiODI2MjBhNmUtZGJmZC00ZDU3LThhNTktOTAwNGE0YmI5ZTkyIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44MyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2IiwgInBvcnQiOiAzNDg4OCwgImlkIjogImE5YWJmM2U3LTg3ZjQtNDczZC04ZDAzLTJmMjZjYTRiMzU4MyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44NiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA4IiwgInBvcnQiOiAzNDg4OCwgImlkIjogImE5YWJmM2U3LTg3ZjQtNDczZC04ZDAzLTJmMjZjYTRiMzU4MyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggOSIsICJhZGQiOiAiMTgzLjIzMi4yNDkuMTg5IiwgInBvcnQiOiAiNTk5MDIiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9wYXRoLzE2OTAzNjkyNTAwMDgiLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTM5Ljk5LjI0NS4xNjQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NmZiM1x1NTkyN1x1NTIyOVx1NGU5YVx1NjA4OVx1NWMzY09WSCAzMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@54.36.174.181:6679#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2035
```

