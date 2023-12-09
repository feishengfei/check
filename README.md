
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                                      | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------------------------------|:---------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 43.153.210.169  | Singapore     | SG   | Tencent Building, Kejizhongyi Avenue     | 43.153.210.169                         | Yes (Region: SG) |
|  1 | [8](config/8.json)   | 103.179.142.117 | United States | US   | Evoxt Enterprise                         | 2400:8d60:2::1:f799:71a0               | Yes (Region: US) |
|  2 | [12](config/12.json) | 64.31.55.5      | United States | US   | LIMESTONENETWORKS                        | 64.31.55.5                             | Yes (Region: US) |
|  3 | [13](config/13.json) | 8.222.187.112   | Singapore     | SG   | Alibaba US Technology Co., Ltd.          | 8.222.187.112                          | Yes (Region: SG) |
|  4 | [15](config/15.json) | 47.236.2.149    | Singapore     | SG   | Alibaba US Technology Co., Ltd.          | 47.236.2.149                           | Yes (Region: SG) |
|  5 | [18](config/18.json) | 47.236.111.83   | Singapore     | SG   | Alibaba US Technology Co., Ltd.          | 47.236.111.83                          | Yes (Region: SG) |
|  6 | [21](config/21.json) | 47.236.22.3     | Singapore     | SG   | Alibaba US Technology Co., Ltd.          | 47.236.22.3                            | Yes (Region: SG) |
|  7 | [22](config/22.json) | 64.176.37.216   | Japan         | JP   | AS-CHOOPA                                | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
|  8 | [25](config/25.json) | 157.254.231.45  | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 157.254.231.45                         | Yes (Region: US) |
|  9 | [26](config/26.json) | 183.181.36.194  | Japan         | JP   | FreeBit Co.,Ltd.                         | 2001:2e8:62e:0:2:1:0:be                | Yes (Region: JP) |
| 10 | [30](config/30.json) | 64.176.55.150   | Japan         | JP   | AS-CHOOPA                                | 2401:c080:3800:3de2:5400:4ff:feaa:a943 | Yes (Region: JP) |
| 11 | [33](config/33.json) | 64.176.47.200   | Japan         | JP   | AS-CHOOPA                                | 2401:c080:3800:3ba0:5400:4ff:feaa:a942 | Yes (Region: JP) |
| 12 | [34](config/34.json) | 64.176.59.68    | Japan         | JP   | AS-CHOOPA                                | 2401:c080:3800:3d77:5400:4ff:feaa:a946 | Yes (Region: JP) |
| 13 | [36](config/36.json) | 107.189.29.193  | Luxembourg    | LU   | PONYNET                                  | 107.189.29.193                         | Yes (Region: LU) |
| 14 | [44](config/44.json) | 64.176.42.137   | Japan         | JP   | AS-CHOOPA                                | 2401:c080:3800:3c78:5400:4ff:feaa:a94b | Yes (Region: JP) |
| 15 | [68](config/68.json) | 8.222.239.7     | Singapore     | SG   | Alibaba US Technology Co., Ltd.          | 8.222.239.7                            | Yes (Region: SG) |

## Valid
```
vmess://eyJhZGQiOiAiNDMuMTUzLjIxMC4xNjkiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjM0YTJmMDkzLWMyMzYtNGVkYy1lYjZhLTY2M2YxYmZhYTEzNiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNjY2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjICA0IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDgiLCAiYWRkIjogIjEwMy4xNzkuMTQyLjExNyIsICJwb3J0IjogIjI0NjQwIiwgImlkIjogIjExOWEyNWJmLWUzNWUtNDRjMi04YjgxLTI4N2VhOGIyY2FjMCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@64.31.55.5:11223#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%BE%97%E5%85%8B%E8%90%A8%E6%96%AF%E5%B7%9E%E8%BE%BE%E6%8B%89%E6%96%AFLimestone%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%2012
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMmRcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMTMiLCAiYWRkIjogIjguMjIyLjE4Ny4xMTIiLCAicG9ydCI6ICI0NDU3NCIsICJpZCI6ICJiMThkYzViYS02MmI3LTQ0MjMtYWFjYy1mMTg0ZGExNWMwMzMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMTUiLCAiYWRkIjogIjQ3LjIzNi4yLjE0OSIsICJwb3J0IjogIjY2NjYiLCAiaWQiOiAiY2Q3NjEwMGUtM2E0YS00NjQ4LTk2YzAtYjIyMzc2ZGZhZmExIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMTgiLCAiYWRkIjogIjQ3LjIzNi4xMTEuODMiLCAicG9ydCI6ICIzMTA5MSIsICJpZCI6ICJmMGVhZmQ2Yi1hZDM5LTQ4NzUtOWIyOS03MjIyMzdkMTU1ZjMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMjEiLCAiYWRkIjogIjQ3LjIzNi4yMi4zIiwgInBvcnQiOiAiNDc4ODUiLCAiaWQiOiAiMmZiN2FhMzctZTE5NS00NGYxLWYwMDAtNTcyNzYxMGQyMmUzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NTkzMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAyMiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDI1IiwgImFkZCI6ICIxNTcuMjU0LjIzMS40NSIsICJwb3J0IjogIjM4NDYxIiwgImlkIjogIjhmNTNkOTZiLWNiMTMtNDE5Ny1jZDQ0LTM3ZGI5NTgwOWRlNSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTgzLjE4MS4zNi4xOTQiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjRhNmVhYTJkLTU2MDMtNGMwNS1kOTY3LWZiNmY0MjI1MGE1YSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDE1OTciLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmMgIDI2IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiNjQuMTc2LjU1LjE1MCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTgxMWEzZWUtZjhkNC00M2Y4LTliY2ItOGE4ZjBhODVlMWQ4IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NTg4OSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAzMCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiNjQuMTc2LjQ3LjIwMCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGQ1ZThhYTItMDY0MS00MzIzLWU5MmMtMmMwNjFjZGM4ZTM0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICIyOTQxNCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAzMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiNjQuMTc2LjU5LjY4IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1ODIxYWMyMS04ZTNmLTRjOGItODMyZC1hNTUxOTBjOTQ0ZTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjU5MzUwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDM0IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTA3LjE4OS4yOS4xOTMiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjJkMjNiNzFmLTc4ZTEtNGYxNy1hN2NjLTFlZjA0YTkxMGE0YyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiMjEyODAiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTdmOGVcdTU3MzBcdTUzM2EgIDM2IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjQyLjEzNyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNDQiLCAicG9ydCI6IDIwODg2LCAiaWQiOiAiZjU3NGIyMzctM2ViZi00MDVjLWQ1NDAtNTQxNTMwZmU1ZWQ3IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMmRcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgNjgiLCAiYWRkIjogIjguMjIyLjIzOS43IiwgInBvcnQiOiAiMzAzMjciLCAiaWQiOiAiYjMxM2U2NzAtYmZkNC00YjYyLWQzMTQtMGQyOTZlMzYzMTkyIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

