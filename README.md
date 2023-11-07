
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn            | cc   | isp                               | ip                                     | chatgpt          |
|---:|:---------------------|:-----------------------|:--------------|:-----|:----------------------------------|:---------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 45.77.167.137          | United States | US   | AS-CHOOPA                         | 2001:19f0:9002:1c94:5400:4ff:fe6f:be77 | Yes (Region: US) |
|  1 | [7](config/7.json)   | n1697685464.aaigefm.cn | United States | US   | Alibaba US Technology Co., Ltd.   | 47.76.44.192                           | Yes (Region: US) |
|  2 | [10](config/10.json) | 156.225.67.106         | Netherlands   | NL   | YISP B.V.                         | 154.84.1.44                            | Yes (Region: NL) |
|  3 | [12](config/12.json) | n1697555560.aaigefm.cn | United States | US   | Alibaba US Technology Co., Ltd.   | 47.76.35.240                           | Yes (Region: US) |
|  4 | [17](config/17.json) | 120.233.43.47          | Taiwan        | TW   | Data Communication Business Group | 211.20.157.213                         | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTRmNWJcdTdmNTdcdTkxY2NcdThmYmVcdTVkZGVcdThmYzhcdTk2M2ZcdTViYzZDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNDUuNzcuMTY3LjEzNyIsICJwb3J0IjogODAsICJpZCI6ICJmZjg1YTJlYi01Y2VmLTQ5YTMtZTk2OS1mNTI3ZmY4ZjQxNjciLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInRtcy5kaW5ndGFsay5jb20iLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgNyIsICJhZGQiOiAibjE2OTc2ODU0NjQuYWFpZ2VmbS5jbiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIxODcwMDJmZC1iOGFkLTRkMzYtYjRmYi0xYTMyMjRjYzk5ZTIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm4xNjk3Njg1NDY0LmFhaWdlZm0uY24iLCAicGF0aCI6ICIvIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEwIiwgImFkZCI6ICIxNTYuMjI1LjY3LjEwNiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICIyOWE1ZDQ4ZS0yNGYxLTQ4ZmQtYTVlMS05YTQ2Y2IzMTAzMmYiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNDE3NTgxMTIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5ODY3MTYwMDk4NiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMTIiLCAiYWRkIjogIm4xNjk3NTU1NTYwLmFhaWdlZm0uY24iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNTY2OTFjM2MtYjlhNS00NDBmLWE2NzgtNDc4NjE4ODU0ZTc1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJuMTY5NzU1NTU2MC5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTciLCAiYWRkIjogIjEyMC4yMzMuNDMuNDciLCAicG9ydCI6ICIxMTAxMyIsICJpZCI6ICI4NWRiNjY1Mi1hNzQ3LTNhMGEtYTE3MC00MjI3MzYwNzY0MTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

