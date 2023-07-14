
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.162 | Netherlands   | NL   | YISP B.V.         | 154.84.1.230   | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.245.8.83   | Netherlands   | NL   | YISP B.V.         | 154.84.1.161   | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 154.85.1.123   | Netherlands   | NL   | YISP B.V.         | 154.84.1.232   | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 37.120.193.102 | Serbia        | RS   | M247 Europe SRL   | 146.70.111.194 | Yes (Region: RS) |
|  4 | [8](config/8.json)   | 104.20.107.231 | Netherlands   | NL   | YISP B.V.         | 154.84.1.197   | Yes (Region: NL) |
|  5 | [11](config/11.json) | 104.20.18.54   | United States | US   | 24.hk global BGP  | 163.197.245.87 | Yes (Region: US) |
|  6 | [14](config/14.json) | 202.79.174.157 | South Korea   | KR   | BGPNET Global ASN | 202.79.174.146 | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE2MiIsICJwb3J0IjogIjQ5MzUzIiwgImlkIjogIjY1ZWE2NzI3LTQ0NjEtNDdhNy1hNWM0LWZlZjJjNjdmMmY3OSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDMiLCAiYWRkIjogIjE1Ni4yNDUuOC44MyIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMTIzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMTMwYzlmMmUtNDJiMS00ZWJmLWIzNDUtZTI2NDU2YTA2MWY5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0MDI5OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMzcuMTIwLjE5My4xMDIiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjU3XHU5YTZjXHU1YzNjXHU0ZTlhICA3IiwgInBvcnQiOiA1MjkyMCwgImlkIjogIjU3MTcwZmYwLTcxODAtNDY2NC04ZjYxLThkZWJkZGEzNDVmNyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjIwLjEwNy4yMzEiLCAiYWlkIjogMCwgImhvc3QiOiAieWxrcy52dGNzcy50b3AiLCAiaWQiOiAiMjk4NTMwZGYtODQxOC00YmM2LWJmZjItZWVlZTU5NWJmNWNkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9xd2VyIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTA0LjIwLjE4LjU0IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTEiLCAicG9ydCI6IDIwOTUsICJpZCI6ICI4YzRlNWU4My04YmUyLTQ2MzgtZTNmNi1hMDk4ZWU0ODQxOTMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiaGsud3loa2FhMC50ayIsICJwYXRoIjogIi9AaGthYTAiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMjAyLjc5LjE3NC4xNTciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmQkdQLk5FVCBDTjJcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAicG9ydCI6IDU1MjY0LCAiaWQiOiAiMTIxYzljODktN2QxMS00ZjQ5LTkxMTItZGMxZTg1MzYzZjZmIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
```

