
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp          | ip                                 | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:-------------|:-----------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 140.99.49.58        | United States | US   | DEDIPATH-LLC | 45.83.21.242                       | Yes (Region: US) |
|  1 | [3](config/3.json)   | 23.225.211.21       | United States | US   | CNSERVERS    | 23.225.57.210                      | Yes (Region: US) |
|  2 | [5](config/5.json)   | 107.167.16.102      | United States | US   | SHARKTECH    | 2610:150:c011:6:ec4:7aff:fe4a:b00a | Yes (Region: US) |
|  3 | [8](config/8.json)   | amszxc.66666654.xyz | Netherlands   | NL   | YISP B.V.    | 154.84.1.230                       | Yes (Region: NL) |
|  4 | [14](config/14.json) | 45.58.186.81        | United States | US   | SHARKTECH    | 64.32.2.26                         | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTQwLjk5LjQ5LjU4IiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI1NTYwMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZERhdGFiaWxpdHkgMiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDZXJhTmV0d29ya3NcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMjMuMjI1LjIxMS4yMSIsICJwb3J0IjogIjQyOTQxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTA3LjE2Ny4xNi4xMDIiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImI3NGY0YWZhLTFhNTctNGFmZi1iN2U1LThhZDVlYTMzNTY2ZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjQ3MDc0IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImFtc3p4Yy42NjY2NjY1NC54eXoiLCAicG9ydCI6IDIwOTUsICJpZCI6ICI0MTdkMjdmYi1jYjkzLTNiZDgtOWJmNy03MWNkOTEzMTk4MjEiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImFtc3p4LjY2NjY2NjU0Lnh5eiIsICJwYXRoIjogIi9oZ2NlZm9tbiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAiYWRkIjogIjQ1LjU4LjE4Ni44MSIsICJwb3J0IjogIjUxMTQwIiwgImlkIjogIjRhMTM4ZTE5LTA1OTUtNGQ1MS04M2M2LWZkMjc2Y2Y3ZDMwNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvZm9vdGVycyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
```

