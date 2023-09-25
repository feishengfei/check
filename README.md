
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                           | cn            | cc   | isp                              | ip                  | chatgpt          |
|---:|:---------------------|:-------------------------------|:--------------|:-----|:---------------------------------|:--------------------|:-----------------|
|  0 | [8](config/8.json)   | 64.32.24.222                   | Poland        | PL   | OVH SAS                          | 54.36.174.181       | Yes (Region: FR) |
|  1 | [10](config/10.json) | 107.167.16.85                  | United States | US   | SHARKTECH                        | 170.178.189.50      | Yes (Region: US) |
|  2 | [11](config/11.json) | 156.225.67.48                  | Netherlands   | NL   | YISP B.V.                        | 154.84.1.164        | Yes (Region: NL) |
|  3 | [17](config/17.json) | ci.outline-vpn.cloud           | United States | US   | SHARKTECH                        | 67.21.72.34         | Yes (Region: US) |
|  4 | [23](config/23.json) | vxyfa-1080-v2-2.d-kcd.tuil.xyz | Japan         | JP   | Eons Data Communications Limited | 2404:c140:221:4c::a | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjIyIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzA4MDgyMjI3MjkxNCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjEwNy4xNjcuMTYuODUiLCAicG9ydCI6IDQ0MywgImlkIjogIjc2NDBhMWU3LTk3MDEtNDI4ZS1hNGIyLTE5YjNlN2RkNmY5ZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41MTEwOTA1Ny54eXoiLCAicGF0aCI6ICIvcGF0aC8wODA4MjIyNzI5MTQiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny40OCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NTQ5MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAxMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiY2kub3V0bGluZS12cG4uY2xvdWQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDE3IiwgInBvcnQiOiA0MzEyMywgImlkIjogIjI1NjZkMDBmLTIxOGMtNDhmNy05YTM2LTEzZDNkNmYxYTcyNCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggMjMiLCAiYWRkIjogInZ4eWZhLTEwODAtdjItMi5kLWtjZC50dWlsLnh5eiIsICJwb3J0IjogIjM5OTI4IiwgImlkIjogImE1OTBlNjkyLTRjOGQtNDJkZC1iYTgwLWIxNzY1YTM0ZjY5OSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZWRnZS5jamhoLm1vbSIsICJwYXRoIjogIi9qZTV4M3BCTjF2ZXozTlF1ZE5rQiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

