
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                 | cn            | cc   | isp       | ip              | chatgpt          |
|---:|:-------------------|:---------------------|:--------------|:-----|:----------|:----------------|:-----------------|
|  0 | [1](config/1.json) | 137.175.1.13         |               |      |           | 107.148.193.115 | Yes (Region: US) |
|  1 | [2](config/2.json) | 64.32.24.213         |               |      |           | 170.178.189.58  | Yes (Region: US) |
|  2 | [4](config/4.json) | 156.225.67.152       |               |      |           | 154.84.1.194    | Yes (Region: NL) |
|  3 | [6](config/6.json) | 156.245.8.158        |               |      |           | 154.84.1.138    | Yes (Region: NL) |
|  4 | [7](config/7.json) | cfcdn2.sanfencdn.net |               |      |           | 104.237.159.122 | Yes (Region: US) |
|  5 | [8](config/8.json) | 104.18.110.194       | United States | US   | CNSERVERS | 23.225.9.234    | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDEiLCAiYWRkIjogIjEzNy4xNzUuMS4xMyIsICJwb3J0IjogIjUzNDAzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjEzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInBvcnQiOiA0ODY1OSwgImlkIjogImNmZjlkODYwLTczMzAtNGVlMS1iMDcyLTcxNDJkZGYxNTcxZCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTUyIiwgInBvcnQiOiAiNDYzMzMiLCAiaWQiOiAiYTdmYThmMTQtNGZiNi00MjgwLTkwMDUtZDZiYmU5OWM1ZGE5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE1OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDYiLCAicG9ydCI6IDQ4MTIzLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDciLCAiYWRkIjogImNmY2RuMi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjIyNzBmNDQ4LTM4ZjAtNGVlZi1hOTAzLTBlMGJlZjc0N2E4NCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXM2LnNhbmZlbmNkbjEuY29tIiwgInBhdGgiOiAiL3poLWNuIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjE4LjExMC4xOTQiLCAiYWlkIjogMCwgImhvc3QiOiAieWxrcy52dGNzcy50b3AiLCAiaWQiOiAiZGFjOWNmMzYtZmY0Yy00ZDkwLWQ1NDktZDM5MDg2ZTc1MDg4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9xd2VyIiwgInBvcnQiOiAyMDg2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

