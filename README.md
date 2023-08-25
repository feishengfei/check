
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn             | cc   | isp                    | ip             | chatgpt          |
|---:|:---------------------|:-------------------|:---------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [5](config/5.json)   | 156.225.67.243     | Netherlands    | NL   | YISP B.V.              | 154.84.1.37    | Yes (Region: NL) |
|  1 | [6](config/6.json)   | 54.36.174.181      | Poland         | PL   | OVH SAS                | 54.36.174.181  | Yes (Region: FR) |
|  2 | [8](config/8.json)   | dongtaiwang3.com   | Poland         | PL   | OVH SAS                | 54.36.174.181  | Yes (Region: FR) |
|  3 | [15](config/15.json) | 156.225.67.152     | Netherlands    | NL   | YISP B.V.              | 154.84.1.194   | Yes (Region: NL) |
|  4 | [17](config/17.json) | 64.32.4.53         | United States  | US   | SHARKTECH              | 107.167.13.162 | Yes (Region: US) |
|  5 | [19](config/19.json) | 153.101.64.221     | Japan          | JP   | MIKU NETWORK LIMITED   | 37.128.246.18  | Yes (Region: JP) |
|  6 | [26](config/26.json) | wi.saintink.eu.org | United Kingdom | GB   | Akamai Connected Cloud | 139.162.207.44 | Yes (Region: GB) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjQzIiwgInBvcnQiOiAiNDM1ODIiLCAiaWQiOiAiOTkwMDA2YmQtY2IyMC00ODJmLTljOTctZjVmYzY1MzU5NjA1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@54.36.174.181:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%206
vmess://eyJhZGQiOiAiZG9uZ3RhaXdhbmczLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJkLmZyZWVoMS54eXoiLCAiaWQiOiAiNmRlZGRiN2YtZTU1Ny00MmRiLWJmYTAtY2Y0MGIzNmIyN2UyIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOShzaG9waWZ5KSA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNTIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJhN2ZhOGYxNC00ZmI2LTQyODAtOTAwNS1kNmJiZTk5YzVkYTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDY0MTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMTUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuNC41MyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAicG9ydCI6IDQzNTU2LCAiaWQiOiAiODY1MzAwNGYtZGU2Ny00NGMyLTljY2UtZTA4MzA5MzNmYjAzIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiXHVkODNjXHVkZGZhXHVkODNjXHVkZGY4VVNcdTdmOGVcdTU2ZmQoeW91dHViZVx1OTYzZlx1NGYxZlx1NzlkMVx1NjI4MCkiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjNWZcdTgyY2ZcdTc3MDFcdTgwNTRcdTkwMWEgMTkiLCAiYWRkIjogIjE1My4xMDEuNjQuMjIxIiwgInBvcnQiOiAiNDAwMTEiLCAidHlwZSI6ICJub25lIiwgImlkIjogImRjOTllZWRlLWQwZjktNDBiMi1hYWE1LTE4MGNhZThmN2MwZSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcXdlMTIzMzIxZXdxIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI2IiwgImFkZCI6ICJ3aS5zYWludGluay5ldS5vcmciLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzdWIyLnNhaW50aW5rLmV1Lm9yZyIsICJwYXRoIjogIi92dWsyLjBiYWQuY29tL2NoYXQiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

