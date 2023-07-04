
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr           | cn             | cc   | isp        | ip            | chatgpt          |
|---:|:-------------------|:---------------|:---------------|:-----|:-----------|:--------------|:-----------------|
|  0 | [2](config/2.json) | 107.167.7.12   | United States  | US   | SHARKTECH  | 107.167.18.50 | Yes (Region: US) |
|  1 | [3](config/3.json) | 156.225.67.73  | Netherlands    | NL   | YISP B.V.  | 154.84.1.19   | Yes (Region: NL) |
|  2 | [4](config/4.json) | 137.175.9.205  | United States  | US   | PEGTECHINC | 142.4.118.225 | Yes (Region: US) |
|  3 | [7](config/7.json) | 154.85.1.245   | Netherlands    | NL   | YISP B.V.  | 154.84.1.206  | Yes (Region: NL) |
|  4 | [8](config/8.json) | 41.215.242.126 | United States  | US   | CNSERVERS  | 23.225.9.234  | Yes (Region: US) |
|  5 | [9](config/9.json) | 51.195.125.16  | United Kingdom | GB   | OVH SAS    | 51.89.42.212  | Yes (Region: GB) |

## Valid
```
vmess://eyJhZGQiOiAiMTA3LjE2Ny43LjEyIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJiZGVlMjAyYy04ZmFlLTQ0MWYtYTU4OC03YmM0ZDM4ODcwMTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0MTY1NCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlx1NWUwMlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1MzEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDQiLCAiYWRkIjogIjEzNy4xNzUuOS4yMDUiLCAicG9ydCI6ICI1NzkwMiIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ1IiwgInBvcnQiOiAiNDc3MzEiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDEuMjE1LjI0Mi4xMjYiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJlZTQ0MmY0My1iMDdhLTQxOWQtYmQyNy0yZDM0NTYzOTNhYmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzU2NzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTdjM1x1NTNjYSAgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNTEuMTk1LjEyNS4xNiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1NDkwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4MmYxXHU1NmZkXHU3OTNlXHU0ZjFhXHU0ZmRkXHU5NjY5XHU1Yjg5XHU1MTY4XHU5MGU4IDkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

