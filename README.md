
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp                               | ip            | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:----------------------------------|:--------------|:-----------------|
|  0 | [3](config/3.json)   | 198.2.202.85                | China         | CN   | PEG-SV                            | 142.4.102.244 | Yes (Region: US) |
|  1 | [5](config/5.json)   | 198.2.202.88                | China         | CN   | PEG-SV                            | 142.4.102.244 | Yes (Region: US) |
|  2 | [6](config/6.json)   | 45.199.138.222              | Netherlands   | NL   | YISP B.V.                         | 154.84.1.122  | Yes (Region: NL) |
|  3 | [8](config/8.json)   | us01.shawbrothersstudio.com | United States | US   | HVC-AS                            | 38.180.5.0    | Yes (Region: US) |
|  4 | [9](config/9.json)   | www.75409854.xyz            | United States | US   | SHARKTECH                         | 107.167.22.10 | Yes (Region: US) |
|  5 | [13](config/13.json) | 67.21.90.5                  | United States | US   | SHARKTECH                         | 107.167.22.10 | Yes (Region: US) |
|  6 | [14](config/14.json) | 45.199.138.186              | Netherlands   | NL   | YISP B.V.                         | 154.84.1.122  | Yes (Region: NL) |
|  7 | [21](config/21.json) | jscm01.celerlink.one        | Taiwan        | TW   | Data Communication Business Group | 111.250.4.5   | Yes (Region: TW) |

## Valid
```
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjg1IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk1MDMyOTA5MTY0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDMiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjg4IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk1OTkzMDcxMDI5IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4yMjIiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE2OTMwNDgiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpMYW02bWdJMFpuSXFUNDU5Q1RUT0pS@us01.shawbrothersstudio.com:19922#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%208
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwb3J0IjogNDQzLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiNjcuMjEuOTAuNSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAicG9ydCI6IDQ0MywgImlkIjogIjI4ZGQ2YzI2LTA1YTUtNGJiYS04YTVkLTA1MmI3MGFjMTNiMiIsICJhaWQiOiAiNjQiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xODYiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTY1OTgwMTM4NTEiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToyNzM5Y2U4NWQzYjllMTQ1@jscm01.celerlink.one:41021#github.com/freefq%20-%20%E6%B1%9F%E8%8B%8F%E7%9C%81%E7%9B%90%E5%9F%8E%E5%B8%82%E7%A7%BB%E5%8A%A8%2021
```

