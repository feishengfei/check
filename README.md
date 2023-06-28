
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn            | cc   | isp     | ip              | chatgpt          |
|---:|:---------------------|:------------------------|:--------------|:-----|:--------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 64.32.20.103            |               |      |         | 64.32.0.58      | Yes (Region: US) |
|  1 | [4](config/4.json)   | 172.247.67.46           |               |      |         | 23.225.9.234    | Yes (Region: US) |
|  2 | [5](config/5.json)   | 67.21.64.84             |               |      |         | 67.21.72.34     | Yes (Region: US) |
|  3 | [6](config/6.json)   | 45.12.144.89            |               |      |         | 45.92.126.90    | Yes (Region: US) |
|  4 | [7](config/7.json)   | 142.4.99.89             |               |      |         | 142.4.99.65     | Yes (Region: US) |
|  5 | [8](config/8.json)   | 192.9.231.146           |               |      |         | 193.108.118.34  | Yes (Region: DE) |
|  6 | [12](config/12.json) | cn-to-hk-443.db-link.in | United States | US   | PONYNET | 205.185.118.164 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMjAuMTAzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYzFiYWQ5YTYtMTQ4Mi00OTQxLWEwYzQtZTg1ZjNjYmJjYjVhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQwMDM5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDb3BlcmF0aW9uIENvbG9jdGlvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgImFkZCI6ICIxNzIuMjQ3LjY3LjQ2IiwgInBvcnQiOiAiNTAwMzUiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjIyNzhlZmU0LWFkMGMtNDdjZS05NDgwLTA2ODYwODM2OGQ3NiIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNjcuMjEuNjQuODQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMxMjMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTIuMTQ0Ljg5IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3MTI3LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZiMjdcdTc2ZGYgIDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTQyLjQuOTkuODkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMzNzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIIDciLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmROb2tpYSA4IiwgImFkZCI6ICIxOTIuOS4yMzEuMTQ2IiwgInBvcnQiOiAiODA4MCIsICJpZCI6ICI4OGM2ZDEyYi02MTRmLTQ4NWYtODNmYy1mYjBjYzU3YzQ4MDEiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmMgIDEyIiwgImFkZCI6ICJjbi10by1oay00NDMuZGItbGluay5pbiIsICJwb3J0IjogNDQzLCAiaWQiOiAiNDBjYmM3NTAtYTE4Mi0zZmUyLTg4MzItOWZhNjAwNjM1NGNmIiwgImFpZCI6IDEsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJmcmVlLXRvLXVzLTAxLmRiLWxpbmsuaW4iLCAicGF0aCI6ICIvZGIiLCAidGxzIjogInRscyJ9
```

