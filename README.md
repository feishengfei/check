
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn          | cc   | isp                         | ip              | chatgpt          |
|---:|:---------------------|:---------------------|:------------|:-----|:----------------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 156.249.18.127       | Netherlands | NL   | YISP B.V.                   | 154.84.1.138    | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 156.245.8.84         | Netherlands | NL   | YISP B.V.                   | 154.84.1.197    | Yes (Region: NL) |
|  2 | [15](config/15.json) | cfcdn3.sanfencdn.net | Singapore   | SG   | Akamai Connected Cloud      | 139.162.19.102  | Yes (Region: US) |
|  3 | [17](config/17.json) | edu1.v-pn.my.id      | Indonesia   | ID   | PT Industri Kreatif Digital | 103.167.34.172  | Yes (Region: ID) |
|  4 | [21](config/21.json) | edu1.ak-celluler.com | Indonesia   | ID   | PT Media Sarana Akses       | 103.217.210.182 | Yes (Region: ID) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTU2LjI0OS4xOC4xMjciLCAicG9ydCI6ICI0ODEwMCIsICJpZCI6ICIxMTExN2Q0Yy0zYjZhLTRlNzYtOGJjYy0yYjQxYjNlOWNhOTMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDgiLCAiYWRkIjogIjE1Ni4yNDUuOC44NCIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvdnBuamFudGl0IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE1IiwgImFkZCI6ICJjZmNkbjMuc2FuZmVuY2RuLm5ldCIsICJwb3J0IjogIjIwNTIiLCAiaWQiOiAiMGUxMjE1ZTQtYWE3YS00N2FjLWJiZjktMjdiODQ1NjVlZWU1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzZzQuc2FuZmVuY2RuMi5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE3IiwgImFkZCI6ICJlZHUxLnYtcG4ubXkuaWQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiOTg0NzZjMmYtMjk3MS00MzI2LTkzYzQtODk2YTg1MTI0ODQ1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJpa2QyLnZwbi1ha2NlbGx1bGVyLm15LmlkIiwgInBhdGgiOiAiL3YycmF5IiwgInRscyI6ICJ0bHMiLCAic25pIjogImlrZDIudnBuLWFrY2VsbHVsZXIubXkuaWQiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIxIiwgImFkZCI6ICJlZHUxLmFrLWNlbGx1bGVyLmNvbSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI2MWExYjUwYS05MDg1LTQzODUtODQwZC0xMGIyM2I2ZGEzYjAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm1zYTEuYWstY2VsbHVsZXIuY29tIiwgInBhdGgiOiAiL3YycmF5IiwgInRscyI6ICJ0bHMiLCAic25pIjogIm1zYTEuYWstY2VsbHVsZXIuY29tIiwgImFscG4iOiAiIn0=
```

