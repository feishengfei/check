
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp       | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:----------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.134 | Netherlands   | NL   | YISP B.V. | 154.84.1.206   | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 45.199.138.139 | Netherlands   | NL   | YISP B.V. | 154.84.1.128   | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.245.8.240  | Netherlands   | NL   | YISP B.V. | 154.84.1.44    | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 64.32.21.247   | United States | US   | SHARKTECH | 107.167.24.162 | Yes (Region: US) |
|  4 | [8](config/8.json)   | 173.245.49.236 | Netherlands   | NL   | YISP B.V. | 154.84.1.44    | Yes (Region: NL) |
|  5 | [12](config/12.json) | 64.32.24.211   | United States | US   | SHARKTECH | 170.178.189.58 | Yes (Region: US) |
|  6 | [15](config/15.json) | 45.199.138.158 | Netherlands   | NL   | YISP B.V. | 154.84.1.231   | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMzQiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIxZDQ3NGYwYi1lNzhkLTRhZjktYmM0YS1hNDY3NDY3YmM3YTciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQ0MzkzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgMiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMzkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmZTVmNjllNy1lMTgzLTQzOWItOTUwYi05NjYxZWYwNjUxZjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMzNDIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC4yNDAiLCAicG9ydCI6ICI0NTMyNiIsICJpZCI6ICIyOWE1ZDQ4ZS0yNGYxLTQ4ZmQtYTVlMS05YTQ2Y2IzMTAzMmYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiXHVkODNjXHVkZGYzXHVkODNjXHVkZGYxTkxcdTgzNzdcdTUxNzAoeW91dHViZVx1OTYzZlx1NGYxZlx1NzlkMVx1NjI4MCkiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuMjEuMjQ3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNTdmOTNlOTItZWJiOS00ZjE2LTliZGMtODIyNWQyMDEwOTk1IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0MzEzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTVmMTdcdTU0MDlcdTVjM2NcdTRlOWFcdTVkZGVcdTk2M2ZcdTRlYzBcdTY3MmNOViBORVhUXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDgiLCAiYWRkIjogIjE3My4yNDUuNDkuMjM2IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiNWY3NTFjNmUtNTBiMS00Nzk3LWJhOGUtNmZmZTMyNGEwYmNlIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJjYS5pbG92ZXNjcC5jb20iLCAicGF0aCI6ICIvc2hpcmtlciIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjExIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxMiIsICJwb3J0IjogNDg2NTksICJpZCI6ICJjZmY5ZDg2MC03MzMwLTRlZTEtYjA3Mi03MTQyZGRmMTU3MWQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNTgiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJmNTI1MGM0ZS1mODU1LTRlZmYtYjczYy1hMDIyMjZkNDJmZTciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQ5MTgzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgMTUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
```

