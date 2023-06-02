
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn            | cc   | isp        | ip                                    | chatgpt          |
|---:|:---------------------|:-------------------|:--------------|:-----|:-----------|:--------------------------------------|:-----------------|
|  0 | [6](config/6.json)   | 38.63.0.69         | United States | US   | PEGTECHINC | 38.63.0.65                            | Yes (Region: US) |
|  1 | [8](config/8.json)   | 23.224.110.184     | Netherlands   | NL   | YISP B.V.  | 154.84.1.145                          | Yes (Region: NL) |
|  2 | [10](config/10.json) | 156.249.18.9       | Netherlands   | NL   | YISP B.V.  | 154.84.1.40                           | Yes (Region: NL) |
|  3 | [17](config/17.json) | new8.huvicloud.com | United States | US   | PONYNET    | 205.185.127.57                        | Yes (Region: US) |
|  4 | [21](config/21.json) | 8.v2-ray.cyou      |               |      |            | 18.179.36.139                         | Yes (Region: JP) |
|  5 | [23](config/23.json) | cdn.yuntujisu.ml   | United States | US   | PONYNET    | 2605:6400:20:1fa6:c288:57d0:989e:4654 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMzguNjMuMC42OSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjE5NDU4MTYyLnh5eiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY4Mzk1NTY5Mzg0OCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggNiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMjMuMjI0LjExMC4xODQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMDgwNzEyMzQyMzEwIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNkNvcGVyYXRpb24gQ29sb2N0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjE1Ni4yNDkuMTguOSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI1YTRkNjlhZC0yMGE5LTQ5NDEtYjIyMy04N2JiZDA5ZjVmNTIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNDg2NDM3MDAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4NDMwNjI3MjQzMCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAibmV3OC5odXZpY2xvdWQuY29tIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTciLCAicG9ydCI6IDQ0MywgImlkIjogImExMWNhNzYwLTllZjktNGE2My05NWM5LTRjNWMzMmQ1NjI1MSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMjEiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIzIiwgImFkZCI6ICJjZG4ueXVudHVqaXN1Lm1sIiwgInBvcnQiOiAyMDk1LCAiaWQiOiAiZDU5YjI0YjEtYjQ3NS00ZDQ0LWJlNDYtYTE4NTYzYTg3NzExIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJuYW5vdXMueXRqczExNDUxNC5tbCIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

