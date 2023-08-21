
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp                             | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:--------------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 64.32.21.246   | United States | US   | SHARKTECH                       | 107.167.24.162 | Yes (Region: US) |
|  1 | [5](config/5.json)   | 45.199.138.158 | Netherlands   | NL   | YISP B.V.                       | 154.84.1.231   | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 156.225.67.78  | Netherlands   | NL   | YISP B.V.                       | 46.182.107.216 | Yes (Region: US) |
|  3 | [8](config/8.json)   | 104.31.16.27   | Poland        | PL   | OVH SAS                         | 54.36.174.181  | Yes (Region: FR) |
|  4 | [11](config/11.json) | 46.182.107.102 | Netherlands   | NL   | YISP B.V.                       | 154.84.1.137   | Yes (Region: NL) |
|  5 | [13](config/13.json) | vau1.0bad.com  | Australia     | AU   | Akamai Connected Cloud          | 172.105.162.17 | Yes (Region: AU) |
|  6 | [14](config/14.json) | vfly3.win      | Japan         | JP   | Alibaba US Technology Co., Ltd. | 47.245.30.19   | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNTdmOTNlOTItZWJiOS00ZjE2LTliZGMtODIyNWQyMDEwOTk1IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0MzEzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE1OCIsICJwb3J0IjogIjMyMTQ0IiwgImlkIjogImY1MjUwYzRlLWY4NTUtNGVmZi1iNzNjLWEwMjIyNmQ0MmZlNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzgiLCAicG9ydCI6ICI0MjIzOSIsICJpZCI6ICIzZTAxNmM0ZC05ODZlLTQyZGYtODM4Yy02MDQ2ZjNkODllY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjEwNC4zMS4xNi4yNyIsICJwb3J0IjogIjgwIiwgImlkIjogIjU4ZmUxNTQyLTUyOTAtNDBhZC04MTVhLTc3NzA3YTgxYWZlNSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiY2E1LnRlaG1lMi5mdW4iLCAicGF0aCI6ICIvSU9lYmhMTWhsMUNUYkZIYkw5NW15ZlJYMiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzAgIDExIiwgImFkZCI6ICI0Ni4xODIuMTA3LjEwMiIsICJwb3J0IjogIjM4NjUxIiwgImlkIjogIjk2NGJmNDk5LTllYzAtNDM3OC05MmI2LTg3ZDhkODYxYjJkMCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAidmF1MS4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJ2YXUxLjBiYWQuY29tIiwgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvY2hhdCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTY1YjBcdTUzNTdcdTVhMDFcdTVjMTRcdTU4ZWJcdTVkZGVcdTYwODlcdTVjM2NMaW5vZGVcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAidmZseTMud2luIiwgImFpZCI6IDAsICJob3N0IjogInZmbHkzLndpbiIsICJpZCI6ICI5NjgxZjk5ZS1kMjUxLTQ3N2EtZDc3Ny0xZDAxZWU1NTA0ODEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL215YmxvZyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE0IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

