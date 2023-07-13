
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn             | cc   | isp                    | ip              | chatgpt          |
|---:|:---------------------|:-------------------------|:---------------|:-----|:-----------------------|:----------------|:-----------------|
|  0 | [6](config/6.json)   | 107.167.7.22             | United States  | US   | SHARKTECH              | 107.167.18.50   | Yes (Region: US) |
|  1 | [8](config/8.json)   | cf-lt.sharecentre.online | Netherlands    | NL   | YISP B.V.              | 154.84.1.197    | Yes (Region: NL) |
|  2 | [10](config/10.json) | 54.38.154.182            | United Kingdom | GB   | OVH SAS                | 51.89.42.212    | Yes (Region: GB) |
|  3 | [13](config/13.json) | vus5.0bad.com            | United States  | US   | Akamai Connected Cloud | 172.105.158.137 | Yes (Region: US) |
|  4 | [14](config/14.json) | cfcdn2.sanfencdn.net     | United States  | US   | COGENT-174             | 38.207.156.102  | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTA3LjE2Ny43LjIyIiwgInBvcnQiOiAiNDE2NTQiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJkZWUyMDJjLThmYWUtNDQxZi1hNTg4LTdiYzRkMzg4NzAxOSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjVmNzUxYzZlLTUwYjEtNDc5Ny1iYThlLTZmZmUzMjRhMGJjZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZHAzLnNjcHJveHkudG9wIiwgInBhdGgiOiAiL3NoaXJrZXIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNTQuMzguMTU0LjE4MiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1NDkwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2Y2Q1XHU1NmZkT1ZIXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDEwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAidnVzNS4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9jaGF0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZExpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiY2ZjZG4yLnNhbmZlbmNkbi5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAidXMyLnNhbmZlbmNkbjEuY29tIiwgImlkIjogIjgyMTZlMWZkLTdmNjctNDQwZC05YTYzLTUxZDBmNmMzOGIxMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvemgtY24iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxNCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

