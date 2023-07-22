
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp                         | ip             | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:----------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 45.199.138.133   | Netherlands   | NL   | YISP B.V.                   | 154.84.1.206   | Yes (Region: NL) |
|  1 | [8](config/8.json)   | dongtaiwang2.com | Singapore     | SG   | Akamai Connected Cloud      | 139.162.58.23  | Yes (Region: US) |
|  2 | [10](config/10.json) | 64.32.21.246     | United States | US   | SHARKTECH                   | 107.167.24.162 | Yes (Region: US) |
|  3 | [12](config/12.json) | edu1.v-pn.my.id  | Indonesia     | ID   | PT Industri Kreatif Digital | 103.167.34.172 | Yes (Region: ID) |
|  4 | [15](config/15.json) | 45.199.138.162   | Netherlands   | NL   | YISP B.V.                   | 154.84.1.230   | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMzMiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjU1NTIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiZG9uZ3RhaXdhbmcyLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIyLmZyZWVrMS54eXoiLCAiaWQiOiAiMjVhOWYzYjktMWU2ZC00MGJkLTk2OGItZTA4MThjMWIxOTZmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOShzaG9waWZ5KSA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjY0LjMyLjIxLjI0NiIsICJwb3J0IjogIjQ0MzEzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI1N2Y5M2U5Mi1lYmI5LTRmMTYtOWJkYy04MjI1ZDIwMTA5OTUiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvcGF0aC8xNjg5NTg4NDk3NzY1IiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiZWR1MS52LXBuLm15LmlkIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTIiLCAicG9ydCI6IDQ0MywgImlkIjogIjk4NDc2YzJmLTI5NzEtNDMyNi05M2M0LTg5NmE4NTEyNDg0NSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJpa2QyLnZwbi1ha2NlbGx1bGVyLm15LmlkIiwgInBhdGgiOiAiL3YycmF5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjIiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjY1ZWE2NzI3LTQ0NjEtNDdhNy1hNWM0LWZlZjJjNjdmMmY3OSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjQ5MzU1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgMTUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
```

