
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn   | cc   | isp   | ip             | chatgpt          |
|---:|:---------------------|:-----------------|:-----|:-----|:------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 156.225.67.243   |      |      |       | 154.84.1.37    | Yes (Region: NL) |
|  1 | [7](config/7.json)   | 172.64.130.176   |      |      |       | 213.162.210.46 | Yes (Region: ES) |
|  2 | [8](config/8.json)   | vless.wyhkaa0.cf |      |      |       | 54.36.174.181  | Yes (Region: FR) |
|  3 | [10](config/10.json) | 64.32.4.54       |      |      |       | 107.167.13.162 | Yes (Region: US) |
|  4 | [11](config/11.json) | 156.225.67.78    |      |      |       | 46.182.107.216 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjQzIiwgInBvcnQiOiAiNDM1ODIiLCAiaWQiOiAiOTkwMDA2YmQtY2IyMC00ODJmLTljOTctZjVmYzY1MzU5NjA1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTcyLjY0LjEzMC4xNzYiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAieGJ5LmRhb3poYW5nLmxpbmsiLCAiaWQiOiAiZjI5ODJkYjItMjNlMy00MzBiLWFmNTQtZTgzYmE4NDIwNWZkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIiIsICJwb3J0IjogIjgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA3IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInZsZXNzLnd5aGthYTAuY2YiLCAicG9ydCI6IDgwLCAiaWQiOiAiODdkMGFhNWQtMDlkZi00Nzg1LWQ5NWQtNmEwZGVlZDQ3M2JlIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ2bGVzcy53eWhrYWEwLmNmIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuNC41NCIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNDM1NTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3Ljc4IiwgInBvcnQiOiAiNDIyMzkiLCAiaWQiOiAiM2UwMTZjNGQtOTg2ZS00MmRmLTgzOGMtNjA0NmYzZDg5ZWNmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDM1IiwgImFkZCI6ICIxNy53eWhrYWEwLmdxIiwgInBvcnQiOiAyMDk1LCAiaWQiOiAiMWUzNjY1NWItN2QyOC00NTEzLWQ3ZjgtNWYxYTBjMDBhMDdkIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICIxNy53eWhrYWEwLmdxIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJ0bHMiOiAiIn0=
```

