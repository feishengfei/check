
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                | cn   | cc   | isp   | ip             | chatgpt          |
|---:|:-------------------|:--------------------|:-----|:-----|:------|:---------------|:-----------------|
|  0 | [3](config/3.json) | 64.32.21.241        |      |      |       | 107.167.24.162 | Yes (Region: US) |
|  1 | [5](config/5.json) | 45.199.138.125      |      |      |       | 154.84.1.127   | Yes (Region: NL) |
|  2 | [6](config/6.json) | 108.166.203.183     |      |      |       | 173.82.156.42  | Yes (Region: US) |
|  3 | [7](config/7.json) | 156.249.18.127      |      |      |       | 154.84.1.138   | Yes (Region: NL) |
|  4 | [8](config/8.json) | scaleway.696960.xyz |      |      |       | 154.84.1.197   | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjQuMzIuMjEuMjQxIiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9xd2VyIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMjUiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIzN2MyOWY0Mi1iN2M3LTQwYzctOWRhOS03NDNkY2M0ODk1YmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDc3NzgsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgzIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNjhhNDkxYi03NjRjLTQ0ZDEtODFhNC0zMGRlMTYxMzA4NjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0NDk0NSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDYiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTU2LjI0OS4xOC4xMjciLCAicG9ydCI6ICI0ODEwMCIsICJpZCI6ICIxMTExN2Q0Yy0zYjZhLTRlNzYtOGJjYy0yYjQxYjNlOWNhOTMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAic2NhbGV3YXkuNjk2OTYwLnh5eiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZTM1N2NkNjMtZjFhNS00YzhlLWM0MmUtMjZkYTExMjA3ZmVlIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9yb290LyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

