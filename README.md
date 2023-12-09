
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn            | cc   | isp                             | ip                                     | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:--------------|:-----|:--------------------------------|:---------------------------------------|:-----------------|
|  0 | [5](config/5.json)   | 47.236.2.149                                                                                    | Singapore     | SG   | Alibaba US Technology Co., Ltd. | 47.236.2.149                           | Yes (Region: SG) |
|  1 | [11](config/11.json) | 64.176.39.31                                                                                    | Japan         | JP   | AS-CHOOPA                       | 2401:c080:3800:3dba:5400:4ff:feaa:9fd7 | Yes (Region: JP) |
|  2 | [12](config/12.json) | 64.176.55.150                                                                                   | Japan         | JP   | AS-CHOOPA                       | 2401:c080:3800:3de2:5400:4ff:feaa:a943 | Yes (Region: JP) |
|  3 | [20](config/20.json) | 64.31.55.5                                                                                      | United States | US   | LIMESTONENETWORKS               | 64.31.55.5                             | Yes (Region: US) |
|  4 | [26](config/26.json) | www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland        | PL   | OVH SAS                         | 54.36.174.181                          | Yes (Region: FR) |
|  5 | [29](config/29.json) | 47.236.111.83                                                                                   | Singapore     | SG   | Alibaba US Technology Co., Ltd. | 47.236.111.83                          | Yes (Region: SG) |
|  6 | [35](config/35.json) | 103.159.206.35                                                                                  | Taiwan        | TW   | EMGINECONCEPT-01                | 103.159.206.35                         | Yes (Region: TW) |
|  7 | [45](config/45.json) | 107.189.29.193                                                                                  | Luxembourg    | LU   | PONYNET                         | 107.189.29.193                         | Yes (Region: LU) |
|  8 | [49](config/49.json) | 64.176.37.216                                                                                   | Japan         | JP   | AS-CHOOPA                       | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
|  9 | [64](config/64.json) | 45.121.48.196                                                                                   | Taiwan        | TW   | EMGINECONCEPT-01                | 45.121.48.196                          | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgNSIsICJhZGQiOiAiNDcuMjM2LjIuMTQ5IiwgInBvcnQiOiAiNjY2NiIsICJpZCI6ICJjZDc2MTAwZS0zYTRhLTQ2NDgtOTZjMC1iMjIzNzZkZmFmYTEiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMTc2LjM5LjMxIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1OTBmMjc0NC1lOWQxLTRmMmMtYTM4NC1kMzViNzM2YmNhNDEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjU2MjYyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDExIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiNjQuMTc2LjU1LjE1MCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTgxMWEzZWUtZjhkNC00M2Y4LTliY2ItOGE4ZjBhODVlMWQ4IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NTg4OSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAxMiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@64.31.55.5:11223#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%BE%97%E5%85%8B%E8%90%A8%E6%96%AF%E5%B7%9E%E8%BE%BE%E6%8B%89%E6%96%AFLimestone%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%2020
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:7001#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2026
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMjkiLCAiYWRkIjogIjQ3LjIzNi4xMTEuODMiLCAicG9ydCI6ICIzMTA5MSIsICJpZCI6ICJmMGVhZmQ2Yi1hZDM5LTQ4NzUtOWIyOS03MjIyMzdkMTU1ZjMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImUyZTUxMWIwLTdkZWYtNGUxYi1kMjM4LTZjYjUzOTFiMmUzZiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiMzE5NDUiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDM1IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTA3LjE4OS4yOS4xOTMiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzE3XHU3ZjhlXHU1NzMwXHU1MzNhICA0NSIsICJwb3J0IjogMjEyODAsICJpZCI6ICIyZDIzYjcxZi03OGUxLTRmMTctYTdjYy0xZWYwNGE5MTBhNGMiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NTkzMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSA0OSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE5NiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDY0IiwgInBvcnQiOiAxMDAwMSwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
```

