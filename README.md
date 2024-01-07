
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn              | cc   | isp                                  | ip              | chatgpt          |
|---:|:---------------------|:----------------------|:----------------|:-----|:-------------------------------------|:----------------|:-----------------|
|  0 | [1](config/1.json)   | 51.145.68.57          | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK          | 51.145.68.57    | Yes (Region: GB) |
|  1 | [2](config/2.json)   | 51.142.73.20          | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK          | 51.142.73.20    | Yes (Region: GB) |
|  2 | [3](config/3.json)   | 45.87.153.246         |                 |      |                                      | 45.87.153.246   | Yes (Region: NL) |
|  3 | [4](config/4.json)   | 38.68.134.202         | United States   | US   | AS-GLOBALTELEHOST                    | 38.68.134.202   | Yes (Region: US) |
|  4 | [10](config/10.json) | data-us-v1.shwjfkw.cn | United States   | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138 | Yes (Region: US) |
|  5 | [13](config/13.json) | 38.68.134.202         | United States   | US   | AS-GLOBALTELEHOST                    | 38.68.134.202   | Yes (Region: US) |
|  6 | [21](config/21.json) | 51.158.150.168        | France          | FR   | Scaleway S.a.s.                      | 51.158.150.168  | Yes (Region: FR) |
|  7 | [23](config/23.json) | 38.68.134.202         | United States   | US   | AS-GLOBALTELEHOST                    | 38.68.134.202   | Yes (Region: US) |
|  8 | [26](config/26.json) | 45.58.153.24          | The Netherlands | NL   | SHARKTECH                            | 45.58.149.130   | Yes (Region: US) |
|  9 | [27](config/27.json) | 38.54.108.222         | United States   | US   | Kaopu Cloud HK Limited               | 38.54.108.222   | Yes (Region: US) |
| 10 | [29](config/29.json) | 38.54.185.112         | China           | CN   | PEG-SV                               | 192.74.239.146  | Yes (Region: US) |
| 11 | [32](config/32.json) | 217.160.45.31         | Germany         | DE   | IONOS SE                             | 217.160.45.31   | Yes (Region: DE) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpLbEpsWFhlOUtqUVg0bWg0eEMwNWM5@51.145.68.57:13751#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%201
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp0QW9XenVLdk5PUHJzTGM0ZkFFT25v@51.142.73.20:6961#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%202
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%203
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@38.68.134.202:2375#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%204
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTc5ZmJcdTUyYTggMTAiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@38.68.134.202:8091#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2013
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@51.158.150.168:4444#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E5%B7%B4%E9%BB%8EOnline%20S.A.S%2021
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.68.134.202:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2023
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjYiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.54.108.222:8119#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2027
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMjkiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMTA5MTEzMzQwOSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAzMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

