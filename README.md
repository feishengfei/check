
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                         | ip                     | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:----------------------------|:-----------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.58.186.81        | United States | US   | SHARKTECH                   | 64.32.2.26             | Yes (Region: US) |
|  1 | [3](config/3.json)   | 64.32.21.246        | United States | US   | SHARKTECH                   | 107.167.24.162         | Yes (Region: US) |
|  2 | [4](config/4.json)   | 45.199.138.133      | Netherlands   | NL   | YISP B.V.                   | 154.84.1.206           | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 45.199.138.162      | Netherlands   | NL   | YISP B.V.                   | 154.84.1.230           | Yes (Region: NL) |
|  4 | [14](config/14.json) | scaleway.696960.xyz | Netherlands   | NL   | CLOUDFLARENET               | 2a09:bac1:5560::20a:2a | Yes (Region: NL) |
|  5 | [15](config/15.json) | edu1.v-pn.my.id     | Indonesia     | ID   | PT Industri Kreatif Digital | 103.167.34.172         | Yes (Region: ID) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiNDUuNTguMTg2LjgxIiwgInBvcnQiOiAiNTExNDAiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi9mb290ZXJzIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9wYXRoLzE2ODk1ODg0OTc3NjUiLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMzMiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjU1NTIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgNCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjIiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjY1ZWE2NzI3LTQ0NjEtNDdhNy1hNWM0LWZlZjJjNjdmMmY3OSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjQ5MzU1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgNSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAic2NhbGV3YXkuNjk2OTYwLnh5eiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZTM1N2NkNjMtZjFhNS00YzhlLWM0MmUtMjZkYTExMjA3ZmVlIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9yb290LyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE0IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiZWR1MS52LXBuLm15LmlkIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTUiLCAicG9ydCI6IDQ0MywgImlkIjogIjk4NDc2YzJmLTI5NzEtNDMyNi05M2M0LTg5NmE4NTEyNDg0NSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJpa2QyLnZwbi1ha2NlbGx1bGVyLm15LmlkIiwgInBhdGgiOiAiL3YycmF5IiwgInRscyI6ICJ0bHMifQ==
```

