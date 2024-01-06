
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn             | cc   | isp                         | ip             | chatgpt          |
|---:|:---------------------|:---------------|:---------------|:-----|:----------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 192.74.249.4   | China          | CN   | PEG-SV                      | 192.74.249.1   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 38.68.134.202  | United States  | US   | AS-GLOBALTELEHOST           | 38.68.134.202  | Yes (Region: US) |
|  2 | [6](config/6.json)   | 217.160.45.31  | Germany        | DE   | IONOS SE                    | 217.160.45.31  | Yes (Region: DE) |
|  3 | [9](config/9.json)   | 198.2.200.37   | United States  | US   | PEG-SV                      | 142.4.98.185   | Yes (Region: US) |
|  4 | [50](config/50.json) | 51.158.150.168 | France         | FR   | Scaleway S.a.s.             | 51.158.150.168 | Yes (Region: FR) |
|  5 | [51](config/51.json) | 51.145.68.57   | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK | 51.145.68.57   | Yes (Region: GB) |
|  6 | [54](config/54.json) | 38.54.108.222  | United States  | US   | Kaopu Cloud HK Limited      | 38.54.108.222  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTkyLjc0LjI0OS40IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuMzc3OTA5NTgueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@38.68.134.202:8091#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%203
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA2IiwgInNjeSI6ICJhZXMtMTI4LWdjbSIsICJ0bHMiOiAibm9uZSIsICJ0eXBlIjogIm5vbmUiLCAidiI6IDJ9
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgOSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMzkiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@51.158.150.168:4444#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E5%B7%B4%E9%BB%8EOnline%20S.A.S%2050
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpLbEpsWFhlOUtqUVg0bWg0eEMwNWM5@51.145.68.57:13751#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%2051
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.54.108.222:8119#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2054
```

