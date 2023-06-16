
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr           | cn          | cc   | isp               | ip             | chatgpt          |
|---:|:-------------------|:---------------|:------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [1](config/1.json) | 156.225.67.76  | Netherlands | NL   | YISP B.V.         | 46.182.107.216 | Yes (Region: US) |
|  1 | [2](config/2.json) | 156.245.8.240  | Netherlands | NL   | YISP B.V.         | 154.84.1.44    | Yes (Region: NL) |
|  2 | [3](config/3.json) | 156.225.67.131 | Netherlands | NL   | YISP B.V.         | 154.84.1.219   | Yes (Region: NL) |
|  3 | [4](config/4.json) | 156.249.18.10  | Netherlands | NL   | YISP B.V.         | 154.84.1.40    | Yes (Region: NL) |
|  4 | [6](config/6.json) | dl.v001sssv.pw | France      | FR   | OVH SAS           | 51.77.213.73   | Yes (Region: FR) |
|  5 | [8](config/8.json) | 104.19.222.252 | Germany     | DE   | AS-GLOBALTELEHOST | 193.108.118.34 | Yes (Region: DE) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzYiLCAicG9ydCI6ICI0MjI0MyIsICJpZCI6ICIzZTAxNmM0ZC05ODZlLTQyZGYtODM4Yy02MDQ2ZjNkODllY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDIiLCAiYWRkIjogIjE1Ni4yNDUuOC4yNDAiLCAicG9ydCI6ICI0OTYzMiIsICJpZCI6ICIyOWE1ZDQ4ZS0yNGYxLTQ4ZmQtYTVlMS05YTQ2Y2IzMTAzMmYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTMxIiwgInBvcnQiOiAiNTU0NDciLCAiaWQiOiAiNTE1YmNiNGQtMGJhMS00Y2FlLTg3Y2YtYTA0NzAwN2VlYzU0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU2LjI0OS4xOC4xMCIsICJwb3J0IjogIjQ2OTIzIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDYiLCAiYWRkIjogImRsLnYwMDFzc3N2LnB3IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiYTRiYjdmOTMtY2VlNi00M2Q3LWIyZGQtZmE5YzcwYjg4MjMzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJkbC52MDAxc3Nzdi5wdyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjEwNC4xOS4yMjIuMjUyIiwgInBvcnQiOiAiMjA4NiIsICJpZCI6ICI0ZDJjYTU4My03ZTJhLTRlZjQtYmExNS1mZmM3ZDkxNDdhMzIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInRvdS52dGNzcy50b3AiLCAicGF0aCI6ICIveWxrczAiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

