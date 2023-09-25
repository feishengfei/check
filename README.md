
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                           | cn            | cc   | isp                               | ip                  | chatgpt          |
|---:|:---------------------|:-------------------------------|:--------------|:-----|:----------------------------------|:--------------------|:-----------------|
|  0 | [2](config/2.json)   | 1.164.147.203                  | Taiwan        | TW   | Data Communication Business Group | 1.164.147.203       | Yes (Region: TW) |
|  1 | [3](config/3.json)   | ci.outline-vpn.cloud           | United States | US   | SHARKTECH                         | 67.21.72.34         | Yes (Region: US) |
|  2 | [4](config/4.json)   | 156.225.67.25                  | Netherlands   | NL   | YISP B.V.                         | 154.84.1.193        | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 156.245.8.146                  | Poland        | PL   | OVH SAS                           | 54.36.174.181       | Yes (Region: FR) |
|  4 | [31](config/31.json) | vxyfa-1080-v2-2.d-kcd.tuil.xyz | Japan         | JP   | Eons Data Communications Limited  | 2404:c140:221:4c::a | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTUzZjBcdTUzMTdcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMiIsICJhZGQiOiAiMS4xNjQuMTQ3LjIwMyIsICJwb3J0IjogIjIzMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0OTBkOWZlYi1kNjc5LTNhZDEtYTM1OC03ZWJkZjA5ZTMwYTEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8_ZWQ9MjA0OCIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiY2kub3V0bGluZS12cG4uY2xvdWQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAicG9ydCI6IDQzMTIzLCAiaWQiOiAiMjU2NmQwMGYtMjE4Yy00OGY3LTlhMzYtMTNkM2Q2ZjFhNzI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjUiLCAicG9ydCI6ICI1MTM4MSIsICJpZCI6ICIzNzVlNzBmMC01ZDQ2LTQ3NmYtOGQ2OS0wZmIzNWM1NTQ4YTkiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYzYjRiODI5LTdmMDEtNGUyNi1iMDM3LWYwNGIxZjA5ODc2NSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Mjk1MiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggMzEiLCAiYWRkIjogInZ4eWZhLTEwODAtdjItMi5kLWtjZC50dWlsLnh5eiIsICJwb3J0IjogIjM5OTI4IiwgImlkIjogImE1OTBlNjkyLTRjOGQtNDJkZC1iYTgwLWIxNzY1YTM0ZjY5OSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZWRnZS5jamhoLm1vbSIsICJwYXRoIjogIi9qZTV4M3BCTjF2ZXozTlF1ZE5rQiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

