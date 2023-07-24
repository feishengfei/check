
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr              | cn            | cc   | isp              | ip                        | chatgpt          |
|---:|:---------------------|:------------------|:--------------|:-----|:-----------------|:--------------------------|:-----------------|
|  0 | [1](config/1.json)   | 45.58.186.81      | United States | US   | SHARKTECH        | 64.32.2.26                | Yes (Region: US) |
|  1 | [2](config/2.json)   | 64.32.21.246      | United States | US   | SHARKTECH        | 107.167.24.162            | Yes (Region: US) |
|  2 | [3](config/3.json)   | 23.225.211.21     |               |      |                  | 23.225.57.210             | Yes (Region: US) |
|  3 | [8](config/8.json)   | cf.dalazhi.eu.org | Netherlands   | NL   | YISP B.V.        | 154.84.1.230              | Yes (Region: NL) |
|  4 | [9](config/9.json)   | Shopify.com       | France        | FR   | CLOUDFLARENET    | 2a09:bac5:3264:be::13:298 | Yes (Region: FR) |
|  5 | [10](config/10.json) | 23.108.100.103    |               |      |                  | 23.108.100.101            | Yes (Region: US) |
|  6 | [17](config/17.json) | 104.20.18.54      | United States | US   | 24.hk global BGP | 163.197.245.87            | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJhZGQiOiAiNDUuNTguMTg2LjgxIiwgInBvcnQiOiAiNTExNDAiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi9mb290ZXJzIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9wYXRoLzE2ODk1ODg0OTc3NjUiLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDZXJhTmV0d29ya3NcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMjMuMjI1LjIxMS4yMSIsICJwb3J0IjogIjQyOTQxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLmRhbGF6aGkuZXUub3JnIiwgInBvcnQiOiA0NDMsICJpZCI6ICI2NDQ4MGY0Yy02MWMyLTRkODgtODljMy1mYzAwNDUyMjliZmMiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInVzLmRhbGF6aGkuZXUub3JnIiwgInBhdGgiOiAiL2twbHh2d3MiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDkiLCAiYWRkIjogIlNob3BpZnkuY29tIiwgInBvcnQiOiAiMjA4NiIsICJpZCI6ICIyNTBmNDMzMS04YzNlLTRiODctYTg2Yi01YzVmYmY5ZGRiYTgiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIkZyLmNsb3VkZmxhcmUucXVlc3QiLCAicGF0aCI6ICIvYXJpZXMiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRMZWFzZVdlYlx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxMCIsICJhZGQiOiAiMjMuMTA4LjEwMC4xMDMiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQwNTg3MzMzLnh5eiIsICJwYXRoIjogIi9mb290ZXJzIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE3IiwgImFkZCI6ICIxMDQuMjAuMTguNTQiLCAicG9ydCI6ICIyMDk1IiwgImlkIjogIjhjNGU1ZTgzLThiZTItNDYzOC1lM2Y2LWEwOThlZTQ4NDE5MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiaGsud3loa2FhMC50ayIsICJwYXRoIjogIi9AaGthYTAiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

