
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                         | ip              | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:----------------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.20.104             | United States | US   | SHARKTECH                   | 64.32.0.58      | Yes (Region: US) |
|  1 | [3](config/3.json)   | 156.245.8.84             | Netherlands   | NL   | YISP B.V.                   | 154.84.1.161    | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 156.249.18.127           | Netherlands   | NL   | YISP B.V.                   | 154.84.1.138    | Yes (Region: NL) |
|  3 | [8](config/8.json)   | cf-lt.sharecentre.online | Netherlands   | NL   | YISP B.V.                   | 154.84.1.197    | Yes (Region: NL) |
|  4 | [14](config/14.json) | edu1.v-pn.my.id          | Indonesia     | ID   | PT Industri Kreatif Digital | 103.167.34.172  | Yes (Region: ID) |
|  5 | [15](config/15.json) | edu1.ak-celluler.com     | Indonesia     | ID   | PT Media Sarana Akses       | 103.217.210.182 | Yes (Region: ID) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMjAuMTA0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYzFiYWQ5YTYtMTQ4Mi00OTQxLWEwYzQtZTg1ZjNjYmJjYjVhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQwMDM5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDMiLCAiYWRkIjogIjE1Ni4yNDUuOC44NCIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvdnBuamFudGl0IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiMTU2LjI0OS4xOC4xMjciLCAicG9ydCI6ICI0ODEwMCIsICJpZCI6ICIxMTExN2Q0Yy0zYjZhLTRlNzYtOGJjYy0yYjQxYjNlOWNhOTMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjVmNzUxYzZlLTUwYjEtNDc5Ny1iYThlLTZmZmUzMjRhMGJjZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZHAzLnNjcHJveHkudG9wIiwgInBhdGgiOiAiL3NoaXJrZXIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICJlZHUxLnYtcG4ubXkuaWQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiOTg0NzZjMmYtMjk3MS00MzI2LTkzYzQtODk2YTg1MTI0ODQ1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJpa2QyLnZwbi1ha2NlbGx1bGVyLm15LmlkIiwgInBhdGgiOiAiL3YycmF5IiwgInRscyI6ICJ0bHMiLCAic25pIjogImlrZDIudnBuLWFrY2VsbHVsZXIubXkuaWQiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE1IiwgImFkZCI6ICJlZHUxLmFrLWNlbGx1bGVyLmNvbSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI2MWExYjUwYS05MDg1LTQzODUtODQwZC0xMGIyM2I2ZGEzYjAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm1zYTEuYWstY2VsbHVsZXIuY29tIiwgInBhdGgiOiAiL3YycmF5IiwgInRscyI6ICJ0bHMiLCAic25pIjogIm1zYTEuYWstY2VsbHVsZXIuY29tIiwgImFscG4iOiAiIn0=
```

