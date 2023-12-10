
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn              | cc   | isp                             | ip                                     | chatgpt          |
|---:|:---------------------|:-----------------------|:----------------|:-----|:--------------------------------|:---------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 95.164.87.138          | The Netherlands | NL   | Stark Industries Solutions Ltd  | 95.164.87.138                          | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 183.240.232.93         | Hong Kong       | HK   | CNSERVERS                       | 23.224.212.138                         | Yes (Region: US) |
|  2 | [18](config/18.json) | 64.31.55.5             | United States   | US   | LIMESTONENETWORKS               | 64.31.55.5                             | Yes (Region: US) |
|  3 | [22](config/22.json) | n1701761456.gxpnmtg.cn | United States   | US   | Alibaba US Technology Co., Ltd. | 47.76.182.214                          | Yes (Region: US) |
|  4 | [33](config/33.json) | 8.222.187.112          | Singapore       | SG   | Alibaba US Technology Co., Ltd. | 8.222.187.112                          | Yes (Region: SG) |
|  5 | [41](config/41.json) | 64.176.58.15           | Japan           | JP   | AS-CHOOPA                       | 2401:c080:3800:3dec:5400:4ff:feaa:9fd8 | Yes (Region: JP) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkUFc2U0toVmZxRGV2QmZkcnQ1ZUpn@95.164.87.138:63830#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%204
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggOCIsICJhZGQiOiAiMTgzLjI0MC4yMzIuOTMiLCAicG9ydCI6ICIzNDAwMSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@64.31.55.5:11223#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%BE%97%E5%85%8B%E8%90%A8%E6%96%AF%E5%B7%9E%E8%BE%BE%E6%8B%89%E6%96%AFLimestone%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%2018
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMjIiLCAiYWRkIjogIm4xNzAxNzYxNDU2Lmd4cG5tdGcuY24iLCAicG9ydCI6ICI0NDMiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAidGxzIjogInRscyIsICJpZCI6ICJiY2U0MDZlZC0xNDM1LTRhZmQtYmI4MS01NGVlMjFiNjk2YTciLCAic25pIjogIm4xNzAxNzYxNDU2Lmd4cG5tdGcuY24iLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMmRcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMzMiLCAiYWRkIjogIjguMjIyLjE4Ny4xMTIiLCAicG9ydCI6ICI0NDU3NCIsICJpZCI6ICJiMThkYzViYS02MmI3LTQ0MjMtYWFjYy1mMTg0ZGExNWMwMzMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNDEiLCAiYWRkIjogIjY0LjE3Ni41OC4xNSIsICJwb3J0IjogIjQ2MTU0IiwgImlkIjogImFkY2JlMTYwLTMwMTAtNDgzZC1iNDM4LWQ2MDU3ZjQ2NWIxZCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

