
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp              | ip             | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:-----------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 156.225.67.132           | Netherlands   | NL   | YISP B.V.        | 154.84.1.219   | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 156.249.18.16            | Netherlands   | NL   | YISP B.V.        | 154.84.1.193   | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 172.247.67.45            | United States | US   | CNSERVERS        | 23.225.9.234   | Yes (Region: US) |
|  3 | [8](config/8.json)   | cf-lt.sharecentre.online | Netherlands   | NL   | YISP B.V.        | 154.84.1.197   | Yes (Region: NL) |
|  4 | [11](config/11.json) | 156.245.8.83             | Netherlands   | NL   | YISP B.V.        | 154.84.1.161   | Yes (Region: NL) |
|  5 | [15](config/15.json) | 104.20.18.54             | United States | US   | 24.hk global BGP | 163.197.245.87 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTMyIiwgInBvcnQiOiAiNTA4ODQiLCAiaWQiOiAiNTE1YmNiNGQtMGJhMS00Y2FlLTg3Y2YtYTA0NzAwN2VlYzU0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInR3dHcuaGVueW8udXMiLCAicGF0aCI6ICIvaXNhaWZxYWFncGkiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU2LjI0OS4xOC4xNiIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTcyLjI0Ny42Ny40NSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjIyNzhlZmU0LWFkMGMtNDdjZS05NDgwLTA2ODYwODM2OGQ3NiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MDAzNSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2Q29wZXJhdGlvbiBDb2xvY3Rpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjVmNzUxYzZlLTUwYjEtNDc5Ny1iYThlLTZmZmUzMjRhMGJjZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZHAzLnNjcHJveHkudG9wIiwgInBhdGgiOiAiL3NoaXJrZXIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDExIiwgImFkZCI6ICIxNTYuMjQ1LjguODMiLCAicG9ydCI6ICI0ODEyMyIsICJpZCI6ICJkNzczNTA1OC0xZGFjLTQ2MTgtOTlmZi0wYWEwNDQxZWMyZDciLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiXHVkODNjXHVkZGYzXHVkODNjXHVkZGYxTkxcdTgzNzdcdTUxNzAoeW91dHViZVx1OTYzZlx1NGYxZlx1NzlkMVx1NjI4MCkiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjIwLjE4LjU0IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTUiLCAicG9ydCI6IDIwOTUsICJpZCI6ICI4YzRlNWU4My04YmUyLTQ2MzgtZTNmNi1hMDk4ZWU0ODQxOTMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiaGsud3loa2FhMC50ayIsICJwYXRoIjogIi9AaGthYTAiLCAidGxzIjogIiJ9
```

