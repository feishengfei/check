
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                 | cn            | cc   | isp             | ip             | chatgpt          |
|---:|:---------------------|:-------------------------------------|:--------------|:-----|:----------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.173                       | Netherlands   | NL   | YISP B.V.       | 154.84.1.129   | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 156.245.8.241                        | Netherlands   | NL   | YISP B.V.       | 154.84.1.44    | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 108.166.203.181                      | United States | US   | MULTA-ASN1      | 173.82.156.42  | Yes (Region: US) |
|  3 | [6](config/6.json)   | 156.225.67.73                        | Netherlands   | NL   | YISP B.V.       | 154.84.1.19    | Yes (Region: NL) |
|  4 | [7](config/7.json)   | 64.32.21.246                         | United States | US   | SHARKTECH       | 107.167.24.162 | Yes (Region: US) |
|  5 | [8](config/8.json)   | gamespeed-gateway-1.numastergame.com | Poland        | PL   | OVH SAS         | 54.36.174.181  | Yes (Region: FR) |
|  6 | [9](config/9.json)   | 37.120.193.102                       | Serbia        | RS   | M247 Europe SRL | 146.70.111.194 | Yes (Region: RS) |
|  7 | [11](config/11.json) | 156.225.67.242                       | Netherlands   | NL   | YISP B.V.       | 154.84.1.37    | Yes (Region: NL) |
|  8 | [15](config/15.json) | 142.4.100.202                        | China         | CN   | PEG-SV          | 142.4.100.193  | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3MyIsICJwb3J0IjogIjQzMDc0IiwgImlkIjogIjIwYjMwOTE2LWUyMDMtNDEyZS04ZWMwLTkwMGYzYWNkNTEyOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNzk5NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNjhhNDkxYi03NjRjLTQ0ZDEtODFhNC0zMGRlMTYxMzA4NjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0NDk0NSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICIzMTkwOSIsICJpZCI6ICIyMTE1NWVmZC04ZTI5LTQzZDItOTViYy1mZTMxOTBlY2IxYzYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwOTEzYjFhYy0xZjZjLTQzNmItOTliNC1hNWQ2ZTM0M2QwMjUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTE4NzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMzcuMTIwLjE5My4xMDIiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1NzE3MGZmMC03MTgwLTQ2NjQtOGY2MS04ZGViZGRhMzQ1ZjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjUyOTIwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjU3XHU5YTZjXHU1YzNjXHU0ZTlhICA5IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3LjI0MiIsICJwb3J0IjogIjQzMzcwIiwgImlkIjogIjk5MDAwNmJkLWNiMjAtNDgyZi05Yzk3LWY1ZmM2NTM1OTYwNSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAxNSIsICJhZGQiOiAiMTQyLjQuMTAwLjIwMiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMjI1Njc0NzEueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5MTgzNzQwMjA3MyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICJ3d3cuMjI1Njc0NzEueHl6In0=
```

