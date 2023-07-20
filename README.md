
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr           | cn          | cc   | isp                    | ip                             | chatgpt          |
|---:|:-------------------|:---------------|:------------|:-----|:-----------------------|:-------------------------------|:-----------------|
|  0 | [2](config/2.json) | 156.225.67.238 | Netherlands | NL   | YISP B.V.              | 154.84.1.197                   | Yes (Region: NL) |
|  1 | [3](config/3.json) | 156.249.18.127 | Netherlands | NL   | YISP B.V.              | 154.84.1.138                   | Yes (Region: NL) |
|  2 | [4](config/4.json) | 156.245.8.84   | Netherlands | NL   | YISP B.V.              | 154.84.1.161                   | Yes (Region: NL) |
|  3 | [7](config/7.json) | sg.669990.xyz  | Singapore   | SG   | Akamai Connected Cloud | 2400:8901::f03c:93ff:feb1:3bcf | Yes (Region: SG) |
|  4 | [8](config/8.json) | cdn.ikuan.dev  | Netherlands | NL   | YISP B.V.              | 154.84.1.197                   | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjM4IiwgInBvcnQiOiAiNDg5MjEiLCAiaWQiOiAiOWMwMjZlZmUtNmFmMC00NjVmLWI4YzAtM2Y1OGM4YzJkNGM1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTU2LjI0OS4xOC4xMjciLCAicG9ydCI6ICI0ODEwMCIsICJpZCI6ICIxMTExN2Q0Yy0zYjZhLTRlNzYtOGJjYy0yYjQxYjNlOWNhOTMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC44NCIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvdnBuamFudGl0IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAic2cuNjY5OTkwLnh5eiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiODkwNGUzNzgtZjY2Ny00MWVkLTkwODctMDA4MWU5YWM0NDZlIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0MDQ1LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDciLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiY2RuLmlrdWFuLmRldiIsICJhaWQiOiAwLCAiaG9zdCI6ICJmcmVlZm9yZ2Z3LmlrdWFuLmRldiIsICJpZCI6ICIzMTg1YzJmMy00MjQ2LTQ5YzQtYmE4YS01ZWE4ZmIyZWY2YjgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0ZyZWVGb3JHRlciLCAicG9ydCI6IDIwNTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

