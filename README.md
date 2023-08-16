
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp              | ip              | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.21.246    | United States | US   | SHARKTECH        | 107.167.24.162  | Yes (Region: US) |
|  1 | [3](config/3.json)   | 64.32.4.53      | United States | US   | SHARKTECH        | 107.167.13.162  | Yes (Region: US) |
|  2 | [4](config/4.json)   | 64.32.20.97     | United States | US   | SHARKTECH        | 64.32.0.58      | Yes (Region: US) |
|  3 | [5](config/5.json)   | 67.21.64.84     | United States | US   | SHARKTECH        | 67.21.72.34     | Yes (Region: US) |
|  4 | [8](config/8.json)   | 23.95.67.188    | Poland        | PL   | OVH SAS          | 54.36.174.181   | Yes (Region: FR) |
|  5 | [19](config/19.json) | 141.147.153.244 | Japan         | JP   | ORACLE-BMC-31898 | 141.147.153.244 | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuNC41MyIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiODY1MzAwNGYtZGU2Ny00NGMyLTljY2UtZTA4MzA5MzNmYjAzIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDM1NTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiNjQuMzIuMjAuOTciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJjMWJhZDlhNi0xNDgyLTQ5NDEtYTBjNC1lODVmM2NiYmNiNWEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDAwMzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjcuMjEuNjQuODQiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQzMTIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMjMuOTUuNjcuMTg4IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJhNGQ0MWNkMy00YjE3LTQ2YzUtZmViNy1lYzZkNzZiOTY4M2QiLCAibmV0IjogIndzIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiMjA1MiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NzIzMVx1ODM3N1x1NTM0ZVx1NWRkZVx1NWY5N1x1Njg4NVx1NTZlME1pY3Jvc29mdFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA4IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTQxLjE0Ny4xNTMuMjQ0IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNDdkNzEzNS0wOTU0LTQ2YWItYTE5MC0xN2I2Yzg2MzBhODUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDE1NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NzQ1ZVx1NTE3OE9yYWNsZSBDb3Jwb3JhdGlvbiAxOSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

