
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn            | cc   | isp                              | ip                                  | chatgpt          |
|---:|:---------------------|:----------------------|:--------------|:-----|:---------------------------------|:------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 107.167.16.85         | United States | US   | SHARKTECH                        | 170.178.189.50                      | Yes (Region: US) |
|  1 | [8](config/8.json)   | 156.225.67.104        | Netherlands   | NL   | YISP B.V.                        | 154.84.1.44                         | Yes (Region: NL) |
|  2 | [11](config/11.json) | cfcdn3.sanfencdn9.com | Japan         | JP   | Eons Data Communications Limited | 38.207.152.110                      | Yes (Region: US) |
|  3 | [15](config/15.json) | 167.88.63.119         | United States | US   | AS-GLOBALTELEHOST                | 167.88.63.119                       | Yes (Region: US) |
|  4 | [16](config/16.json) | 45.199.138.191        | Netherlands   | NL   | YISP B.V.                        | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMyIsICJhZGQiOiAibjE2OTc3NjU3NzIuaXp3aHZhbi5jbiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJiYTk4NDY3OC1jYTgxLTQ0NDMtYTlkYS01OGFkZWE0M2Q1YjAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm4xNjk3NzY1NzcyLml6d2h2YW4uY24iLCAicGF0aCI6ICIvIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTA3LjE2Ny4xNi44NSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJwb3J0IjogNDQzLCAiaWQiOiAiNzY0MGExZTctOTcwMS00MjhlLWE0YjItMTliM2U3ZGQ2ZjlmIiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTExMDkwNTcueHl6IiwgInBhdGgiOiAiL3BhdGgvMDgwODIyMjcyOTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDgiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MjM5ODg4OTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDExIiwgImFkZCI6ICJjZmNkbjMuc2FuZmVuY2RuOS5jb20iLCAicG9ydCI6ICI4MCIsICJpZCI6ICI2OTgxMTVlNC0xNDk0LTRmNGEtODVhOS03NmNkMDExZDNhYzYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImpwMTdhYWI3MmE3LmNodnNpZmV0cmoueHl6IiwgInBhdGgiOiAiL3ZpZGVvL3V1YkNkSnRLIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiIsICJmcCI6ICIifQ==
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@167.88.63.119:8090#github.com/freefq%20-%20%E7%91%9E%E5%85%B8%20%2015
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNiIsICJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAicG9ydCI6ICIzMDAwMCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk2MjUxNTIyNDM4IiwgImhvc3QiOiAid3d3LjQyMDc3MjMwLnh5eiIsICJ0bHMiOiAidGxzIn0=
```

