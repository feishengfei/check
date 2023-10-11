
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp                    | ip              | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:-----------------------|:----------------|:-----------------|
|  0 | [4](config/4.json)   | 198.2.202.88                | China         | CN   | PEG-SV                 | 142.4.102.244   | Yes (Region: US) |
|  1 | [9](config/9.json)   | 45.199.138.186              | Netherlands   | NL   | YISP B.V.              | 154.84.1.122    | Yes (Region: NL) |
|  2 | [10](config/10.json) | cfcdn2.sanfencdn9.com       | Singapore     | SG   | Akamai Connected Cloud | 139.144.117.211 | Yes (Region: US) |
|  3 | [11](config/11.json) | us01.shawbrothersstudio.com | United States | US   | HVC-AS                 | 38.180.5.0      | Yes (Region: US) |
|  4 | [12](config/12.json) | 67.21.90.5                  | United States | US   | SHARKTECH              | 107.167.22.10   | Yes (Region: US) |
|  5 | [13](config/13.json) | 45.199.138.222              | Netherlands   | NL   | YISP B.V.              | 154.84.1.122    | Yes (Region: NL) |
|  6 | [17](config/17.json) | www.75409854.xyz            | United States | US   | SHARKTECH              | 107.167.22.10   | Yes (Region: US) |
|  7 | [21](config/21.json) | 198.2.202.85                | China         | CN   | PEG-SV                 | 142.4.102.244   | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjg4IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk1OTkzMDcxMDI5IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDQiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xODYiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTY1OTgwMTM4NTEiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICJjZmNkbjIuc2FuZmVuY2RuOS5jb20iLCAicG9ydCI6ICIyMDUyIiwgImlkIjogIjcwZGQzZGFhLWI5NjMtNGRkOS1hY2Q5LTEzZDg2ZWQzOGYxOSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAic2cxNzM1MjhjZWYucWNyeWVjaHZxdy54eXoiLCAicGF0aCI6ICIvdmlkZW8veGVYdUhvSG8iLCAidGxzIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpMYW02bWdJMFpuSXFUNDU5Q1RUT0pS@us01.shawbrothersstudio.com:19922#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2011
vmess://eyJhZGQiOiAiNjcuMjEuOTAuNSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTIiLCAicG9ydCI6IDQ0MywgImlkIjogIjI4ZGQ2YzI2LTA1YTUtNGJiYS04YTVkLTA1MmI3MGFjMTNiMiIsICJhaWQiOiAiNjQiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4yMjIiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE2OTMwNDgiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAiYWRkIjogInd3dy43NTQwOTg1NC54eXoiLCAicG9ydCI6IDQ0MywgImlkIjogIjI4ZGQ2YzI2LTA1YTUtNGJiYS04YTVkLTA1MmI3MGFjMTNiMiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy43NTQwOTg1NC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0NDI5OTA4NzQ4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjg1IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk1MDMyOTA5MTY0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDIxIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

