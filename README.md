
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn             | cc   | isp                    | ip             | chatgpt          |
|---:|:---------------------|:-------------------------|:---------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.180           | Netherlands    | NL   | YISP B.V.              | 154.84.1.229   | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.225.67.95            | Netherlands    | NL   | YISP B.V.              | 154.84.1.40    | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 107.167.16.202           | United States  | US   | SHARKTECH              | 67.21.87.226   | Yes (Region: US) |
|  3 | [8](config/8.json)   | ru1.mianfenyun012.eu.org | Poland         | PL   | OVH SAS                | 54.36.174.181  | Yes (Region: FR) |
|  4 | [12](config/12.json) | wi.saintink.eu.org       | United Kingdom | GB   | Akamai Connected Cloud | 139.162.224.92 | Yes (Region: GB) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4MCIsICJwb3J0IjogIjU0OTA1IiwgImlkIjogImQzMTMzNDg0LWYyYmYtNGIwYy04ZDM4LWY4ZTY0NWI2NTY4NyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuOTUiLCAicG9ydCI6ICI0OTk4MSIsICJpZCI6ICI1YTRkNjlhZC0yMGE5LTQ5NDEtYjIyMy04N2JiZDA5ZjVmNTIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTA3LjE2Ny4xNi4yMDIiLCAicG9ydCI6IDQ0MywgImlkIjogIjhjNjc5YjgxLTg0ZmMtNDNjZS05NTUzLWRkY2E1NzVhNjk0OSIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy44NzEzNTUzMC54eXoiLCAicGF0aCI6ICIvcGF0aC8wODA4MjIyNzI5MTQiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAicnUxLm1pYW5mZW55dW4wMTIuZXUub3JnIiwgImFpZCI6IDAsICJob3N0IjogInJ1MS5taWFuZmVueXVuMDEyLmV1Lm9yZyIsICJpZCI6ICIxMjA3OGRjMi02OWEzLTRlNTYtOTI1MC03MGMzNDZiY2YxNmUiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2pkYnA2MDYiLCAicG9ydCI6IDgwODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICJ3aS5zYWludGluay5ldS5vcmciLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzdWIyLnNhaW50aW5rLmV1Lm9yZyIsICJwYXRoIjogIi92dWsyLjBiYWQuY29tL2NoYXQiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

