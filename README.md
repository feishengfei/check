
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp            | ip                       | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:---------------|:-------------------------|:-----------------|
|  0 | [2](config/2.json)   | 154.84.1.113    | Netherlands   | NL   | YISP B.V.      | 154.84.1.40              | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.225.67.73   | Netherlands   | NL   | YISP B.V.      | 154.84.1.19              | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.225.67.206  | Netherlands   | NL   | YISP B.V.      | 154.84.1.161             | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 156.245.8.128   | Netherlands   | NL   | YISP B.V.      | 154.84.1.164             | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 142.4.99.77     | United States | US   | PEGTECHINC     | 142.4.99.65              | Yes (Region: US) |
|  5 | [7](config/7.json)   | 156.249.18.61   | Netherlands   | NL   | YISP B.V.      | 154.84.1.178             | Yes (Region: NL) |
|  6 | [8](config/8.json)   | cf2.992688.xyz  | United States | US   | CNSERVERS      | 23.225.9.234             | Yes (Region: US) |
|  7 | [10](config/10.json) | 154.85.1.245    | Netherlands   | NL   | YISP B.V.      | 154.84.1.206             | Yes (Region: NL) |
|  8 | [12](config/12.json) | 94.177.25.209   | Estonia       | EE   | Astrec Data OU | 2a05:1cc0:10:4::222:fffe | Yes (Region: EE) |
|  9 | [19](config/19.json) | dl8.v001sssv.pw | France        | FR   | OVH SAS        | 51.178.24.58             | Yes (Region: FR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTU0Ljg0LjEuMTEzIiwgInBvcnQiOiAiNDc4NTIiLCAiaWQiOiAiNWE0ZDY5YWQtMjBhOS00OTQxLWIyMjMtODdiYmQwOWY1ZjUyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1MzEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjA2IiwgInBvcnQiOiAiNDA5MzkiLCAiaWQiOiAiZDc3MzUwNTgtMWRhYy00NjE4LTk5ZmYtMGFhMDQ0MWVjMmQ3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAiYWRkIjogIjE1Ni4yNDUuOC4xMjgiLCAicG9ydCI6ICI0ODEyMCIsICJpZCI6ICIzY2E5MTJkYS02YWMyLTQxOGYtYjljZi00NWI2ZjY5NDU3OWIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTQyLjQuOTkuNzciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMzNzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIIDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTU2LjI0OS4xOC42MSIsICJwb3J0IjogIjU0MTIzIiwgImlkIjogIjkzNTAzZGQ1LTI0NWEtNGViMS1hZTJhLTU3YWI5ZjJiM2MyOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiY2YyLjk5MjY4OC54eXoiLCAiYWlkIjogIjAiLCAiZW5jcnlwdGlvbiI6ICJhdXRvIiwgImhvc3QiOiAibzIuOTkyNjg4Lnh5eiIsICJpZCI6ICI3ZmRkZGIyYS0xNDAzLTQwZTEtOTQ2Ni1lODJkZDMzOGYwYTAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjgwODAiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogZmFsc2UsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInVybF9ncm91cCI6ICJ2MnJheSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjE1NC44NS4xLjI0NSIsICJwb3J0IjogIjQ3NzMxIiwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTcyMzFcdTZjOTlcdTVjM2NcdTRlOWEgIDEyIiwgImFkZCI6ICI5NC4xNzcuMjUuMjA5IiwgInBvcnQiOiAiNDQzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI3NTdiZDNiMS0xMmY1LTQ5ZTMtYjgxYi0xMDQwZjc1YWFlZDciLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjI0LjE2OS4yMzgiLCAiYWlkIjogMCwgImhvc3QiOiAic3Rhci1vbmUuY2ZkIiwgImlkIjogIjFhMjVkY2U0LTlkMjctNGU4ZC1lNDZlLTE2MTk5YmU1NGY4MSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcG9ydHMvNDUzMTQiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxNiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE5IiwgImFkZCI6ICJkbDgudjAwMXNzc3YucHciLCAicG9ydCI6ICI4MCIsICJpZCI6ICIzZmVjNzE4Mi0wMmZiLTQ3MzAtOWI5Ny00YzlhZWU1NjNlZjYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImRsOC52MDAxc3Nzdi5wdyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

