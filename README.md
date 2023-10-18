
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn             | cc   | isp                 | ip            | chatgpt          |
|---:|:---------------------|:---------------|:---------------|:-----|:--------------------|:--------------|:-----------------|
|  0 | [2](config/2.json)   | 104.17.27.2    | United States  | US   | Hetzner Online GmbH | 5.161.197.252 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 154.85.1.244   | Netherlands    | NL   | YISP B.V.           | 154.84.1.216  | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 156.225.67.104 | Netherlands    | NL   | YISP B.V.           | 154.84.1.44   | Yes (Region: NL) |
|  3 | [11](config/11.json) | 51vfly1.win    | Germany        | DE   | Contabo GmbH        | 5.189.166.24  | Yes (Region: DE) |
|  4 | [13](config/13.json) | 45.199.138.186 | Netherlands    | NL   | YISP B.V.           | 154.84.1.122  | Yes (Region: NL) |
|  5 | [14](config/14.json) | octavi.cfd     | United Kingdom | GB   | AS-GLOBALTELEHOST   | 149.7.16.248  | Yes (Region: CA) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIiLCAiYWRkIjogIjEwNC4xNy4yNy4yIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiNzJkNDYxNTItZWUwYi00NjEwLWVmYjEtZmZiMGY3ODZiODQ4IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJteTIuZ2FtZWRheWxpb24uYnV6eiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODExNTM2MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNTF2Zmx5MS53aW4iLCAiYWlkIjogMCwgImhvc3QiOiAiNTF2Zmx5MS53aW4iLCAiaWQiOiAiOTY4MWY5OWUtZDI1MS00NzdhLWQ3NzctMWQwMWVlNTUwNDgxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9teWJsb2ciLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMyIsICJhZGQiOiAiNDUuMTk5LjEzOC4xODYiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjE5MjI5MzYyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTczNzY3ODI4NzkiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAib2N0YXZpLmNmZCIsICJhaWQiOiAxLCAiaG9zdCI6ICJvY3RhdmkuY2ZkIiwgImlkIjogIjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICJsaW5rdndzIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTQiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

