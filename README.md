
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                            | cn            | cc   | isp                 | ip                          | chatgpt          |
|---:|:---------------------|:--------------------------------|:--------------|:-----|:--------------------|:----------------------------|:-----------------|
|  0 | [5](config/5.json)   | 156.225.67.117                  | Netherlands   | NL   | YISP B.V.           | 154.84.1.148                | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 67.21.84.214                    | United States | US   | AS-GLOBALTELEHOST   | 169.197.141.187             | Yes (Region: US) |
|  2 | [10](config/10.json) | scaleway.696960.xyz             | Netherlands   | NL   | CLOUDFLARENET       | 2a09:bac5:4e26:1478::20a:28 | Yes (Region: NL) |
|  3 | [12](config/12.json) | gtm-sg-6wr31eq5o8g.gtm-i1d8.com | Singapore     | SG   | Melbikomas UAB      | 185.230.245.202             | Yes (Region: SG) |
|  4 | [16](config/16.json) | 140.99.48.42                    | United States | US   | DEDIPATH-LLC        | 193.202.44.242              | Yes (Region: US) |
|  5 | [18](config/18.json) | d.mamadcucu.com                 | Germany       | DE   | Hetzner Online GmbH | 2a01:4f8:1c17:e4ca::1       | Yes (Region: DE) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTE3IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjg0ZDFkZTExLWNlMTItNGExNS04MzEyLTEzMzgzNTZkNGFjNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy41NzQyNDM0OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjgzMzQ2MDY1MjE3IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYjlhMzA1YTktMWZmMi00ZWMxLWIzMzgtOTMzNTU1ODMzYmFhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM2MDg4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAic2NhbGV3YXkuNjk2OTYwLnh5eiIsICJhaWQiOiAwLCAiaG9zdCI6ICJzY2FsZXdheS42OTY5NjAueHl6IiwgImlkIjogImUzNTdjZDYzLWYxYTUtNGM4ZS1jNDJlLTI2ZGExMTIwN2ZlZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcm9vdC8iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTEyOC1nY206S2FkMFg5@gtm-sg-6wr31eq5o8g.gtm-i1d8.com:2051#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2012
vmess://eyJhZGQiOiAiMTQwLjk5LjQ4LjQyIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU2MTAyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmREYXRhYmlsaXR5IDE2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZiMjdcdTc2ZGYgIDE4IiwgImFkZCI6ICJkLm1hbWFkY3VjdS5jb20iLCAicG9ydCI6ICI4ODgwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJjMTgwOGY3OS1mNTRkLTQ0MGMtZGJiMS1jZDIxYTJmMGVmOGYiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImkyLm1hbWFkY3VjdS5jb20iLCAidGxzIjogIiJ9
```

