
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn              | cc   | isp                                  | ip                             | chatgpt          |
|---:|:---------------------|:----------------------|:----------------|:-----|:-------------------------------------|:-------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 51.145.68.57          | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK          | 51.145.68.57                   | Yes (Region: GB) |
|  1 | [5](config/5.json)   | 38.54.108.222         | United States   | US   | Kaopu Cloud HK Limited               | 38.54.108.222                  | Yes (Region: US) |
|  2 | [6](config/6.json)   | 51.142.75.225         | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK          | 51.142.75.225                  | Yes (Region: GB) |
|  3 | [8](config/8.json)   | 38.68.134.202         | United States   | US   | AS-GLOBALTELEHOST                    | 38.68.134.202                  | Yes (Region: US) |
|  4 | [9](config/9.json)   | 217.160.45.31         | Germany         | DE   | IONOS SE                             | 217.160.45.31                  | Yes (Region: DE) |
|  5 | [12](config/12.json) | 38.54.185.112         | China           | CN   | PEG-SV                               | 192.74.239.146                 | Yes (Region: US) |
|  6 | [15](config/15.json) | 154.90.39.63          | Malaysia        | MY   | Kaopu Cloud HK Limited               | 154.90.39.63                   | Yes (Region: MY) |
|  7 | [17](config/17.json) | 38.54.185.111         | China           | CN   | PEG-SV                               | 192.74.239.146                 | Yes (Region: US) |
|  8 | [18](config/18.json) | 104.237.128.72        | United States   | US   | Akamai Connected Cloud               | 2600:3c00::f03c:94ff:fe28:f769 | Yes (Region: US) |
|  9 | [20](config/20.json) | 45.87.153.246         | The Netherlands | NL   | Stark Industries Solutions Ltd       | 45.87.153.246                  | Yes (Region: NL) |
| 10 | [27](config/27.json) | 38.68.134.202         | United States   | US   | AS-GLOBALTELEHOST                    | 38.68.134.202                  | Yes (Region: US) |
| 11 | [32](config/32.json) | data-us-v1.shwjfkw.cn | United States   | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138                | Yes (Region: US) |
| 12 | [40](config/40.json) | 45.58.153.24          | The Netherlands | NL   | SHARKTECH                            | 45.58.149.130                  | Yes (Region: US) |
| 13 | [41](config/41.json) | 103.159.206.35        | Taiwan          | TW   | EMGINECONCEPT-01                     | 103.159.206.35                 | Yes (Region: TW) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpLbEpsWFhlOUtqUVg0bWg0eEMwNWM5@51.145.68.57:13751#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%202
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.54.108.222:8119#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%205
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpPRVlobFZRbVAxbmVkSUlJbE1nTm01@51.142.75.225:47430#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%206
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@38.68.134.202:8091#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%208
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA5IiwgInNjeSI6ICJhZXMtMTI4LWdjbSIsICJ0bHMiOiAibm9uZSIsICJ0eXBlIjogIm5vbmUiLCAidiI6IDJ9
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMTIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMTA5MTEzMzQwOSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTU0LjkwLjM5LjYzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZlx1NzI3OVx1NTIyYlx1ODg0Y1x1NjUzZlx1NTMzYSAxNSIsICJwb3J0IjogNDUzNDMsICJpZCI6ICIwOGFhODQ5OS1kNjE2LTRmZjEtZDZhYi1jZTBjNTIyODI0YWEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMTciLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMDY1NzYyNTE4MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTY1YjBcdTZjZmRcdTg5N2ZcdTVkZGVMaW5vZGVcdTUxNmNcdTUzZjggMTgiLCAiYWRkIjogIjEwNC4yMzcuMTI4LjcyIiwgInBvcnQiOiAiMTQ0MzIiLCAiaWQiOiAiNGMwOWI3NzYtNmY4My00YmYyLWY3ZjctNGUyODZkYmJiNmRhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2020
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.68.134.202:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2027
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTc5ZmJcdTUyYTggMzIiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNDAiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDQxIiwgImFkZCI6ICIxMDMuMTU5LjIwNi4zNSIsICJwb3J0IjogIjMxOTQ1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiZTJlNTExYjAtN2RlZi00ZTFiLWQyMzgtNmNiNTM5MWIyZTNmIiwgInNuaSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIn0=
```

