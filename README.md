
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp             | ip                                   | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:----------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.58.186.91    | United States | US   | SHARKTECH       | 64.32.2.26                           | Yes (Region: US) |
|  1 | [3](config/3.json)   | 108.186.192.230 | United States | US   | PEGTECHINC      | 192.74.245.225                       | Yes (Region: US) |
|  2 | [7](config/7.json)   | 45.199.138.140  | Netherlands   | NL   | YISP B.V.       | 154.84.1.128                         | Yes (Region: NL) |
|  3 | [9](config/9.json)   | 45.199.138.136  | Netherlands   | NL   | YISP B.V.       | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: US) |
|  4 | [13](config/13.json) | cdn.ikuan.dev   | United States | US   | AS-COLOCROSSING | 198.46.173.131                       | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuNTguMTg2LjkxIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDUxMTQwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDMiLCAiYWRkIjogIjEwOC4xODYuMTkyLjIzMCIsICJwb3J0IjogIjQ1NTAyIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvcGF0aC8xNjg5MTU3MDgxODU4IiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0MCIsICJwb3J0IjogIjQ5MTExIiwgImlkIjogImZlNWY2OWU3LWUxODMtNDM5Yi05NTBiLTk2NjFlZjA2NTFmMiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA5IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEzNiIsICJwb3J0IjogIjQ4MzQ0IiwgImlkIjogIjc0M2JkYzg3LTFkZWEtNDFiZi1hYTBiLTUxZGZiYmZlYzhhYSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2RuLmlrdWFuLmRldiIsICJhaWQiOiAwLCAiaG9zdCI6ICJmcmVlZm9yZ2Z3LmlrdWFuLmRldiIsICJpZCI6ICIzMTg1YzJmMy00MjQ2LTQ5YzQtYmE4YS01ZWE4ZmIyZWY2YjgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0ZyZWVGb3JHRlciLCAicG9ydCI6IDIwNTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

