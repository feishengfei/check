
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn            | cc   | isp                    | ip                             | chatgpt          |
|---:|:---------------------|:-------------------|:--------------|:-----|:-----------------------|:-------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 64.32.24.222       | United States | US   | SHARKTECH              | 170.178.189.58                 | Yes (Region: US) |
|  1 | [6](config/6.json)   | 39.kccic2pa.xyz    | United States | US   | OVH SAS                | 51.81.211.205                  | Yes (Region: US) |
|  2 | [8](config/8.json)   | 156.225.67.153     | Poland        | PL   | OVH SAS                | 54.36.174.181                  | Yes (Region: FR) |
|  3 | [9](config/9.json)   | 03.kccic2pa.xyz    | United States | US   | OVH SAS                | 15.204.10.95                   | Yes (Region: US) |
|  4 | [12](config/12.json) | 19.kccic2pa.xyz    | Japan         | JP   | Akamai Connected Cloud | 2400:8902::f03c:93ff:fe8a:d61d | Yes (Region: JP) |
|  5 | [26](config/26.json) | wi.saintink.eu.org |               |      |                        | 109.74.202.203                 | Yes (Region: GB) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiNjQuMzIuMjQuMjIyIiwgInBvcnQiOiAiNDQzIiwgImlkIjogImNmZjlkODYwLTczMzAtNGVlMS1iMDcyLTcxNDJkZGYxNTcxZCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy44MjYxNTM1NS54eXoiLCAicGF0aCI6ICIvcGF0aC8wODA4MjIyNzI5MTQiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggNiIsICJhZGQiOiAiMzkua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMzkiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJhZWZjMzg5LTcyYjEtNGYyMy1iYmFkLTNhODVjZjUxZmU4YSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIjM5LmtjY2ljMnBhLnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNTMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJhN2ZhOGYxNC00ZmI2LTQyODAtOTAwNS1kNmJiZTk5YzVkYTkiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5Mzk5MjgyMTc3NiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggOSIsICJhZGQiOiAiMDMua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMDMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjVkNGRhNDA1LTUxZTYtNGZjOS05MDZmLWU1ZmRkNjZlZjcyYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIjFnemR4Mi4xNTY3ODYueHl6IiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjE5LmtjY2ljMnBhLnh5eiIsICJwb3J0IjogIjUwMDE5IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJiYWVmYzM4OS03MmIxLTRmMjMtYmJhZC0zYTg1Y2Y1MWZlOGEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIxOS5rY2NpYzJwYS54eXoiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWEgIDI2IiwgImFkZCI6ICJ3aS5zYWludGluay5ldS5vcmciLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzdWIyLnNhaW50aW5rLmV1Lm9yZyIsICJwYXRoIjogIi92dWsyLjBiYWQuY29tL2NoYXQiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

