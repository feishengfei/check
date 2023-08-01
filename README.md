
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp              | ip                        | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------|:--------------------------|:-----------------|
|  0 | [2](config/2.json)   | 173.82.55.92    | United States | US   | MULTA-ASN1       | 23.234.230.34             | Yes (Region: US) |
|  1 | [3](config/3.json)   | 64.32.21.246    | United States | US   | SHARKTECH        | 107.167.24.162            | Yes (Region: US) |
|  2 | [4](config/4.json)   | 156.245.8.241   | Netherlands   | NL   | YISP B.V.        | 154.84.1.44               | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 107.167.29.93   | United States | US   | SHARKTECH        | 107.167.9.234             | Yes (Region: US) |
|  4 | [6](config/6.json)   | 156.245.8.128   | Netherlands   | NL   | YISP B.V.        | 154.84.1.164              | Yes (Region: NL) |
|  5 | [11](config/11.json) | 139.99.245.164  | Australia     | AU   | OVH SAS          | 139.99.130.144            | Yes (Region: AU) |
|  6 | [13](config/13.json) | 183.232.249.189 | Hong Kong     | HK   | CNSERVERS        | 172.247.175.42            | Yes (Region: US) |
|  7 | [14](config/14.json) | Shopify.com     | France        | FR   | CLOUDFLARENET    | 2a09:bac5:3264:be::13:298 | Yes (Region: FR) |
|  8 | [23](config/23.json) | 146.190.106.128 | Singapore     | SG   | DIGITALOCEAN-ASN | 146.190.106.128           | Yes (Region: SG) |
|  9 | [27](config/27.json) | 107.167.29.229  | United States | US   | SHARKTECH        | 170.178.180.90            | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTczLjgyLjU1LjkyIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAicG9ydCI6IDM0NDEyLCAiaWQiOiAiODI2MjBhNmUtZGJmZC00ZDU3LThhNTktOTAwNGE0YmI5ZTkyIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9wYXRoLzE2ODk1ODg0OTc3NjUiLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NTEwOCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiMTA3LjE2Ny4yOS45MyIsICJwb3J0IjogIjQ1NTg1IiwgImlkIjogIjQ2NWRlYzFhLWUwOWItNGJiNi05OTA1LTcwZjc1ZDYwMzVjOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjEyOCIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNDgxMjMiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDYiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTM5Ljk5LjI0NS4xNjQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NmZiM1x1NTkyN1x1NTIyOVx1NGU5YVx1NjA4OVx1NWMzY09WSCAxMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggMTMiLCAiYWRkIjogIjE4My4yMzIuMjQ5LjE4OSIsICJwb3J0IjogIjU5OTAyIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvcGF0aC8xNjkwMzY5MjUwMDA4IiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDE0IiwgImFkZCI6ICJTaG9waWZ5LmNvbSIsICJwb3J0IjogIjIwODYiLCAiaWQiOiAiMjUwZjQzMzEtOGMzZS00Yjg3LWE4NmItNWM1ZmJmOWRkYmE4IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJGci5jbG91ZGZsYXJlLnF1ZXN0IiwgInBhdGgiOiAiL2FyaWVzIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTQ2LjE5MC4xMDYuMTI4IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogInpvb20udXMiLCAiaWQiOiAiNWE1ZWM2NGQtYmFmZi00OWJiLWFiNmEtZDU5NzhkYzUzZTRhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi90aGFydXdhZnJlZSIsICJwb3J0IjogIjEyMjgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAyMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTA3LjE2Ny4yOS4yMjkiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjQ2MzIxIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDI3IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
```

