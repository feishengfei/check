
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp                                      | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.112.132  | United States | US   | PEG-SV                                   | 38.54.250.33   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 45.199.138.161 | Netherlands   | NL   | YISP B.V.                                | 46.182.107.129 | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 198.2.215.114  | China         | CN   | PEG-SV                                   | 142.4.107.246  | Yes (Region: US) |
|  3 | [5](config/5.json)   | 45.199.138.169 | Netherlands   | NL   | YISP B.V.                                | 154.84.1.145   | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 107.167.30.83  | United States | US   | SHARKTECH                                | 107.167.24.162 | Yes (Region: US) |
|  5 | [8](config/8.json)   | 67.21.90.5     | Poland        | PL   | OVH SAS                                  | 54.36.174.181  | Yes (Region: FR) |
|  6 | [15](config/15.json) | 130.162.158.81 | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 23.26.239.241  | Yes (Region: US) |
|  7 | [18](config/18.json) | 162.159.60.89  | Spain         | ES   | NIXVAL                                   | 213.162.210.42 | Yes (Region: ES) |
|  8 | [29](config/29.json) | 104.25.227.40  | United States | US   | Akamai Connected Cloud                   | 50.116.14.153  | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC4xMTIuMTMyIiwgInBvcnQiOiA0NDMsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuODAxMjg2OTMueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDUxNjA2NDIxNSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5NTQ5YTJjZi0xMjliLTQzYTEtODhkYi1lZjdmNjQ4ZGU3NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA0IiwgImFkZCI6ICIxOTguMi4yMTUuMTE0IiwgInBvcnQiOiA0NDMsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNzI3OTUwMjUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDUxNjA2NDIxNSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI2ZTc5ZWVhNC01ZjcyLTQ2ODMtYWQwZS01MzM5ZjAxMzQyMWIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDc3ODUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTA3LjE2Ny4zMC44MyIsICJwb3J0IjogNDQzLCAiaWQiOiAiNTdmOTNlOTItZWJiOS00ZjE2LTliZGMtODIyNWQyMDEwOTk1IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjMyOTMyNjcxLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiNjcuMjEuOTAuNSIsICJwb3J0IjogNDQzLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDE1IiwgImFkZCI6ICIxMzAuMTYyLjE1OC44MSIsICJwb3J0IjogODAsICJpZCI6ICIyMWQ2MGI4Yy1jZDlkLTRjYmMtOWE2OC1iMjljZTdkMjhlZDgiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogIjE4Lnd5aGthYTAuZ3EiLCAicGF0aCI6ICIvVEc6QGhrYWEwIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE4IiwgImFkZCI6ICIxNjIuMTU5LjYwLjg5IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiN2E2MGMxNWUtY2JjZC00ODZkLWFlZTYtMDdhNDk0ZjQwM2UzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ4YnkuZGFvemhhbmcubGluayIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTA0LjI1LjIyNy40MCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJzdWIuc2FpbnRpbmsuZXUub3JnIiwgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvdnVzMy4wYmFkLmNvbS9jaGF0IiwgInBvcnQiOiAiNDQzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAyOSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAic3ViLnNhaW50aW5rLmV1Lm9yZyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
```

