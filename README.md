
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                           | cn            | cc   | isp             | ip                                 | chatgpt          |
|---:|:---------------------|:-------------------------------|:--------------|:-----|:----------------|:-----------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 107.167.7.22                   | United States | US   | SHARKTECH       | 107.167.18.50                      | Yes (Region: US) |
|  1 | [4](config/4.json)   | 108.166.203.183                | United States | US   | MULTA-ASN1      | 173.82.156.42                      | Yes (Region: US) |
|  2 | [5](config/5.json)   | 64.32.4.44                     | United States | US   | SHARKTECH       | 107.167.13.162                     | Yes (Region: US) |
|  3 | [8](config/8.json)   | hk2.c3bfe79372bi.sanfen006.xyz | Netherlands   | NL   | YISP B.V.       | 154.84.1.197                       | Yes (Region: NL) |
|  4 | [9](config/9.json)   | 156.249.18.161                 | Netherlands   | NL   | YISP B.V.       | 2a02:2a38:1:2796:ae1f:6bff:fef1:e2 | Yes (Region: NL) |
|  5 | [12](config/12.json) | 37.120.193.102                 | Serbia        | RS   | M247 Europe SRL | 146.70.111.194                     | Yes (Region: RS) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTA3LjE2Ny43LjIyIiwgInBvcnQiOiAiNDE2NTQiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJkZWUyMDJjLThmYWUtNDQxZi1hNTg4LTdiYzRkMzg4NzAxOSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAicG9ydCI6IDQ0OTQ1LCAiaWQiOiAiMjY4YTQ5MWItNzY0Yy00NGQxLTgxYTQtMzBkZTE2MTMwODY3IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuNC40NCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJwb3J0IjogNDMxNjYsICJpZCI6ICI4NjUzMDA0Zi1kZTY3LTQ0YzItOWNjZS1lMDgzMDkzM2ZiMDMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTYwZTBcdTY2NmVIUCA4IiwgImFkZCI6ICJoazIuYzNiZmU3OTM3MmJpLnNhbmZlbjAwNi54eXoiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiODIxNmUxZmQtN2Y2Ny00NDBkLTlhNjMtNTFkMGY2YzM4YjEwIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cubWljcm9zb2Z0LmNvbSIsICJwYXRoIjogIi96aC1jbiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4xNjEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlXHU4YzZhXHU3NjdiXHU3NzAxXHU3ZWE2XHU3ZmYwXHU1MTg1XHU2NWFmXHU1ODIxQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDkiLCAicG9ydCI6IDQyMjkyLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMzcuMTIwLjE5My4xMDIiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjU3XHU5YTZjXHU1YzNjXHU0ZTlhICAxMiIsICJwb3J0IjogNTI5MjAsICJpZCI6ICI1NzE3MGZmMC03MTgwLTQ2NjQtOGY2MS04ZGViZGRhMzQ1ZjciLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
```

