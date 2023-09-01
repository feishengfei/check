
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                 | cn            | cc   | isp                                      | ip                                   | chatgpt          |
|---:|:---------------------|:-------------------------------------|:--------------|:-----|:-----------------------------------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.173                       | Netherlands   | NL   | YISP B.V.                                | 154.84.1.129                         | Yes (Region: NL) |
|  1 | [4](config/4.json)   | gamespeed-gateway-1.numastergame.com | Taiwan        | TW   | Data Communication Business Group        | 61.219.15.82                         | Yes (Region: TW) |
|  2 | [5](config/5.json)   | cfcdn2.sanfencdn.net                 | United States | US   | Eons Data Communications Limited         | 38.207.156.104                       | Yes (Region: US) |
|  3 | [6](config/6.json)   | 156.225.67.102                       | Netherlands   | NL   | YISP B.V.                                | 2a02:2a38:1:2796:ae1f:6bff:fe98:4940 | Yes (Region: NL) |
|  4 | [7](config/7.json)   | 9524.outline-vpn.cloud               | Sweden        | SE   | M247 Europe SRL                          | 37.120.209.122                       | Yes (Region: SE) |
|  5 | [8](config/8.json)   | pkl173131369.top                     | Poland        | PL   | OVH SAS                                  | 54.36.174.181                        | Yes (Region: FR) |
|  6 | [11](config/11.json) | 172.64.153.211                       | Sweden        | SE   | Stark Industries Solutions Ltd           | 94.131.115.68                        | Yes (Region: SE) |
|  7 | [14](config/14.json) | 156.225.67.78                        | Netherlands   | NL   | YISP B.V.                                | 46.182.107.216                       | Yes (Region: NL) |
|  8 | [25](config/25.json) | 5.wyhkaa0.gq                         | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 38.102.235.136                       | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3MyIsICJwb3J0IjogIjQxNDM0IiwgImlkIjogIjIwYjMwOTE2LWUyMDMtNDEyZS04ZWMwLTkwMGYzYWNkNTEyOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIiwgImZwIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgNCIsICJhZGQiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgInBvcnQiOiAiMTE4NzIiLCAiaWQiOiAiMDkxM2IxYWMtMWY2Yy00MzZiLTk5YjQtYTVkNmUzNDNkMDI1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiY2ZjZG4yLnNhbmZlbmNkbi5uZXQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA1IiwgInBvcnQiOiA0NDMsICJpZCI6ICI0ODg0MzIzMi01OGU3LTQyOWYtOTBmYi0zODA5MDc0Y2MwYmIiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAidXM0LnNhbmZlbmNkbjEuY29tIiwgInBhdGgiOiAiL3poLWNuIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMDIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTM3OTcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiOTUyNC5vdXRsaW5lLXZwbi5jbG91ZCIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImRjMGNmMjJkLWUzNWMtNGI3Ny04OTI0LTk3N2Y2ODQ0OTA5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNDk5ODIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmNTdcdTlhNmNcdTVjM2NcdTRlOWEgIDciLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVjNzFcdTRlMWNcdTc3MDFcdTcwZGZcdTUzZjBcdTVlMDJcdTgwNTRcdTkwMWEgOCIsICJhZGQiOiAicGtsMTczMTMxMzY5LnRvcCIsICJwb3J0IjogIjQ1OTA4IiwgImlkIjogIjc2ZTdjYzg2LThhOGYtNDYxZC1lOTU2LWE0OGQyNTFiNjA5YyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4yMTEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAic2NoZXJlc3dlZC5zb2Z0d2FyZW5ld3Muc3RvcmUiLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkwMSIsICJwb3J0IjogIjQ0MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTEiLCAic2N5IjogImF1dG8iLCAic25pIjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE0IiwgImFkZCI6ICIxNTYuMjI1LjY3Ljc4IiwgInBvcnQiOiAiNDM4NDciLCAiaWQiOiAiM2UwMTZjNGQtOTg2ZS00MmRmLTgzOGMtNjA0NmYzZDg5ZWNmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI1IiwgImFkZCI6ICI1Lnd5aGthYTAuZ3EiLCAicG9ydCI6IDIwOTUsICJpZCI6ICIyNzMzZThjYi1iMDc0LTRkNjYtZTdjMC05OWYxZGI0NjVlNGMiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogIjUud3loa2FhMC5ncSIsICJwYXRoIjogIi9URzpAaGthYTAiLCAidGxzIjogIiJ9
```

