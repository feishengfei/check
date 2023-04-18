
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp     | ip                    | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:--------|:----------------------|:-----------------|
|  0 | [2](config/2.json)   | 156.225.67.125           |               |      |         | 154.84.1.158          | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.225.67.250           |               |      |         | 154.84.1.36           | Yes (Region: NL) |
|  2 | [7](config/7.json)   | germany1.unlimiteddev.co |               |      |         | 116.202.230.160       | Yes (Region: DE) |
|  3 | [8](config/8.json)   | 16.162.74.222            |               |      |         | 116.202.230.160       | Yes (Region: DE) |
|  4 | [9](config/9.json)   | cf.noaries.de            |               |      |         | 107.189.28.253        | Yes (Region: LU) |
|  5 | [10](config/10.json) | 3.mamadcucu.com          |               |      |         | 2a01:4f9:c011:752c::1 | Yes (Region: FI) |
|  6 | [11](config/11.json) | 4.mamadcucu.com          |               |      |         | 2a01:4f9:c011:605c::1 | Yes (Region: FI) |
|  7 | [17](config/17.json) | 156.245.8.105            |               |      |         | 154.84.1.128          | Yes (Region: NL) |
|  8 | [21](config/21.json) | hinet1261.gfwisbest.xyz  |               |      |         | 1.171.219.239         | Yes (Region: TW) |
|  9 | [25](config/25.json) | new3.hucloud-dns.xyz     | United States | US   | PONYNET | 209.141.33.7          | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMjUiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIzYTNjOGE5Yy0zMzRlLTQzNjAtYWRiOC1hODBhNTdkZGNiYmYiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDM5MjIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yNTAiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIzZmQ2MzdhZC00NmZlLTRmODUtYTZlOC04NmIwMGJjYTExMjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDciLCAiYWRkIjogImdlcm1hbnkxLnVubGltaXRlZGRldi5jbyIsICJwb3J0IjogIjgwIiwgImlkIjogIjk3ZWE3OWE2LTYxNWMtNGFkNy04MDgzLTRmM2I0OWNiZThhMiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZ2VybWFueTEudW5saW1pdGVkZGV2LmNvIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTYuMTYyLjc0LjIyMiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNmZmNjZmNDItMzhkNy00MWM2LTlhMDgtMGQ0OGYyZWYzYWE1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi96aC1jbiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTYwZTBcdTY2NmVIUCA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDkiLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6ICI4MDgwIiwgImlkIjogImEwZjE1M2Q4LWUzMmYtNDFmMy05YmNkLTA3M2Y1NzllMjI2NCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiYnV5dm0uY2xvdWRmbGFyZS5xdWVzdCIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMy5tYW1hZGN1Y3UuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIjMubWFtYWRjdWN1LmNvbSIsICJpZCI6ICI5MjkzNDRlMS00NzNjLTRmZWItYjg2Yi1mZGUzZWUxY2NkMTYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0Fyc2FsYW5UYXVCb3QiLCAicG9ydCI6ICIyMDg2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNC5tYW1hZGN1Y3UuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIjQubWFtYWRjdWN1LmNvbSIsICJpZCI6ICI1MWJhNWE5YS00YjdjLTRjNjItYjRhZS0wZTUzZWM4ZDMwMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0Fyc2FsYW5UYXVCb3QiLCAicG9ydCI6ICI4ODgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjEwNSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImZlNWY2OWU3LWUxODMtNDM5Yi05NTBiLTk2NjFlZjA2NTFmMiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzMDc3OSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAxNyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiaGluZXQxMjYxLmdmd2lzYmVzdC54eXoiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU2NWIwXHU1MzE3XHU1ZTAyXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDIxIiwgInBvcnQiOiAyMjQsICJpZCI6ICIyMjg1MTMzZS1iOWJhLTNmYjUtYTI0Ni05YzdkZGNjMmNkN2EiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAibmV3My5odWNsb3VkLWRucy54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjFjOGFkM2YyLTgzNWMtNGZkYS1iOWI2LTg4MWQzY2FkZmQ4ZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMjUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

