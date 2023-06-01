
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp              | ip                                    | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:-----------------|:--------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 156.249.18.9     | Netherlands   | NL   | YISP B.V.        | 154.84.1.40                           | Yes (Region: NL) |
|  1 | [7](config/7.json)   | cdn.noice.id     | Singapore     | SG   | DIGITALOCEAN-ASN | 143.198.94.243                        | Yes (Region: SG) |
|  2 | [8](config/8.json)   | hk516.wyhkaa0.ml | Netherlands   | NL   | YISP B.V.        | 154.84.1.145                          | Yes (Region: NL) |
|  3 | [13](config/13.json) | cdn.yuntujisu.ml | United States | US   | PONYNET          | 2605:6400:20:1fa6:c288:57d0:989e:4654 | Yes (Region: US) |
|  4 | [14](config/14.json) | 8.v2-ray.cyou    | Japan         | JP   | AMAZON-02        | 18.179.36.139                         | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU2LjI0OS4xOC45IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40ODY0MzcwMC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjg0MzA2MjcyNDMwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgNyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiaGs1MTYud3loa2FhMC5tbCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY3ZWNcdTU3ZDRcdTViZTggIDgiLCAicG9ydCI6IDIwOTUsICJpZCI6ICJiMGQ3ODkyMi01NDAxLTQxNGUtZDljNy03ZDE5NjgwZjU4MjMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiaGs1MTYud3loa2FhMC5tbCIsICJwYXRoIjogIi90Z0Boa2FhMCIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiY2RuLnl1bnR1amlzdS5tbCIsICJhaWQiOiAwLCAiaG9zdCI6ICJuYW5vdXMueXRqczExNDUxNC5tbCIsICJpZCI6ICJkNTliMjRiMS1iNDc1LTRkNDQtYmU0Ni1hMTg1NjNhODc3MTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogMjA5NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTQiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

