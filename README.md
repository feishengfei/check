
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp               | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:------------------|:---------------------------------------|:-----------------|
|  0 | [5](config/5.json)   | 64.176.37.216   | Japan         | JP   | AS-CHOOPA         | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
|  1 | [12](config/12.json) | 146.190.97.8    |               |      |                   | 146.190.97.8                           | Yes (Region: SG) |
|  2 | [22](config/22.json) | 64.176.58.15    | Japan         | JP   | AS-CHOOPA         | 2401:c080:3800:3dec:5400:4ff:feaa:9fd8 | Yes (Region: JP) |
|  3 | [27](config/27.json) | 64.31.55.5      | United States | US   | LIMESTONENETWORKS | 64.31.55.5                             | Yes (Region: US) |
|  4 | [38](config/38.json) | 64.176.47.200   | Japan         | JP   | AS-CHOOPA         | 2401:c080:3800:3ba0:5400:4ff:feaa:a942 | Yes (Region: JP) |
|  5 | [41](config/41.json) | 45.121.48.196   | Taiwan        | TW   | EMGINECONCEPT-01  | 45.121.48.196                          | Yes (Region: TW) |
|  6 | [45](config/45.json) | 54.36.174.181   | Poland        | PL   | OVH SAS           | 54.36.174.181                          | Yes (Region: FR) |
|  7 | [49](config/49.json) | 142.171.229.164 | United States | US   | MULTA-ASN1        | 142.171.229.164                        | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NTkzMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSA1IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTQ2LjE5MC45Ny44IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIm0ubGlua2VkaW4uY29tIiwgImlkIjogIjI2Yzk3NTcxLTI1NzMtNDRmZS1lNjJhLTIyOTk5NDM1ZDIxNyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDY1MDYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDEyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMjIiLCAiYWRkIjogIjY0LjE3Ni41OC4xNSIsICJwb3J0IjogIjQ2MTU0IiwgImlkIjogImFkY2JlMTYwLTMwMTAtNDgzZC1iNDM4LWQ2MDU3ZjQ2NWIxZCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@64.31.55.5:11223#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%BE%97%E5%85%8B%E8%90%A8%E6%96%AF%E5%B7%9E%E8%BE%BE%E6%8B%89%E6%96%AFLimestone%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%2027
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMzgiLCAiYWRkIjogIjY0LjE3Ni40Ny4yMDAiLCAicG9ydCI6ICIyOTQxNCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNGQ1ZThhYTItMDY0MS00MzIzLWU5MmMtMmMwNjFjZGM4ZTM0IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE5NiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDQxIiwgInBvcnQiOiAxMDAwMSwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@54.36.174.181:8091#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2045
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUyYTBcdTYyZmZcdTU5MjcgIDQ5IiwgImFkZCI6ICIxNDIuMTcxLjIyOS4xNjQiLCAicG9ydCI6ICIxMzQ2OSIsICJpZCI6ICIzYjc3YTExNS0wZThhLTQ5MzktZTY0Yy1mMTM5OTQ5NDJjMmUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

