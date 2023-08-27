
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn            | cc   | isp             | ip                          | chatgpt          |
|---:|:---------------------|:-----------------------|:--------------|:-----|:----------------|:----------------------------|:-----------------|
|  0 | [2](config/2.json)   | ci.outline-vpn.cloud   | United States | US   | SHARKTECH       | 67.21.72.34                 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 9524.outline-vpn.cloud | Sweden        | SE   | M247 Europe SRL | 37.120.209.122              | Yes (Region: SE) |
|  2 | [8](config/8.json)   | wxll.e5outllok.me      | Poland        | PL   | OVH SAS         | 54.36.174.181               | Yes (Region: FR) |
|  3 | [11](config/11.json) | 45.199.138.148         | Netherlands   | NL   | YISP B.V.       | 46.182.107.123              | Yes (Region: NL) |
|  4 | [21](config/21.json) | dx1.992688.xyz         | Germany       | DE   | CLOUDFLARENET   | 2a09:bac1:1e60:1308::1d8:5f | Yes (Region: DE) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiY2kub3V0bGluZS12cG4uY2xvdWQiLCAicG9ydCI6ICI0MzEyMyIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiOTUyNC5vdXRsaW5lLXZwbi5jbG91ZCIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImRjMGNmMjJkLWUzNWMtNGI3Ny04OTI0LTk3N2Y2ODQ0OTA5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNDk5ODIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmNTdcdTlhNmNcdTVjM2NcdTRlOWEgIDMiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAid3hsbC5lNW91dGxsb2subWUiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAid3hsbC5lNW91dGxsb2subWUiLCAiaWQiOiAiZjMxYzBiMzQtOTc3Yi00YzJiLWFjZmEtYmVjZmRmYzFmMjY3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI4MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgOCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNDgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmOWZhM2E5Yy1mN2Q1LTQxNGYtODhlNi02OTcwNTg1ZDk5NDkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzEyMjIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDExIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiZHgxLjk5MjY4OC54eXoiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyMSIsICJwb3J0IjogODA4MCwgImlkIjogIjM2OWVhMmFiLTg0NDYtNDE0Mi1kOGI2LTVhN2RkOWRkZmZkYyIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJldTIuOTkyNjg4Lnh5eiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

