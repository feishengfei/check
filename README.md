
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                     | addr            | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:-----------------------|:----------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [3](config/3.json)     | 149.28.19.63    | Japan           | JP   | AS-CHOOPA                      | 2001:19f0:7001:316a:5400:4ff:feaa:a955 | Yes (Region: JP) |
|  1 | [4](config/4.json)     | 52.142.161.9    | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  2 | [7](config/7.json)     | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  3 | [8](config/8.json)     | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  4 | [18](config/18.json)   | 45.159.249.231  | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  5 | [20](config/20.json)   | 138.201.147.115 | Germany         | DE   | Hetzner Online GmbH            | 138.201.147.115                        | Yes (Region: DE) |
|  6 | [21](config/21.json)   | 198.2.202.81    | China           | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
|  7 | [22](config/22.json)   | 38.54.82.54     | Thailand        | TH   | Kaopu Cloud HK Limited         | 38.54.82.54                            | Yes (Region: TH) |
|  8 | [23](config/23.json)   | 64.176.39.31    | Japan           | JP   | AS-CHOOPA                      | 64.176.39.31                           | Yes (Region: JP) |
|  9 | [45](config/45.json)   | 52.142.146.57   | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
| 10 | [68](config/68.json)   | 148.135.33.94   | United States   | US   | MULTA-ASN1                     | 2607:f130:109:0:d6ae:52ff:febb:b49f    | Yes (Region: US) |
| 11 | [72](config/72.json)   | sg.qrfly.link   | Singapore       | SG   | ORACLE-BMC-31898               | 152.69.215.149                         | Yes (Region: SG) |
| 12 | [88](config/88.json)   | 103.159.206.35  | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35                         | Yes (Region: TW) |
| 13 | [90](config/90.json)   | 45.58.153.24    | The Netherlands | NL   | SHARKTECH                      | 45.58.149.130                          | Yes (Region: US) |
| 14 | [94](config/94.json)   | 38.54.86.217    | Philippines     | PH   | Kaopu Cloud HK Limited         | 38.54.86.217                           | Yes (Region: PH) |
| 15 | [95](config/95.json)   | 45.121.48.196   | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196                          | Yes (Region: TW) |
| 16 | [105](config/105.json) | 172.233.188.217 | United States   | US   | Akamai Connected Cloud         | 2a01:7e04::f03c:94ff:fe28:322a         | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%202
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTQ5LjI4LjE5LjYzIiwgInBvcnQiOiAiNDIyODAiLCAiaWQiOiAiODIzY2EwZDQtYTdmOC00ZTk5LTgwOTAtMjM1MWY3MThkMTA2IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%204
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%207
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%208
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2018
vmess://eyJhZGQiOiAiMTM4LjIwMS4xNDcuMTE1IiwgImFpZCI6IDAsICJob3N0IjogIjEzOC4yMDEuMTQ3LjExNSIsICJpZCI6ICIzOTZiNjE0Yi02NmNkLTQ1MWQtYTg5YS0zODFhN2YzOWEwOGEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogODg4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZmI3XHU1NmZkSGV0em5lciAyMCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDIxIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMzguNTQuODIuNTQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MzRlXHU3NmRiXHU5ODdmQ29nZW50XHU5MDFhXHU0ZmUxXHU1MTZjXHU1M2Y4IDIyIiwgInBvcnQiOiA0MTYwNCwgImlkIjogIjU0ZGU1MGU1LTVlNGItNDQzZi1kOWI4LTllOWUwZWVlODY1YyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMTc2LjM5LjMxIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAyMyIsICJwb3J0IjogNTYyNjIsICJpZCI6ICI1OTBmMjc0NC1lOWQxLTRmMmMtYTM4NC1kMzViNzM2YmNhNDEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2045
vmess://eyJhZGQiOiAiMTQ4LjEzNS4zMy45NCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMwOTk0MTA0Lnh5eiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMzIzMTI2Mjg3NSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTc0NWVcdTUxNzggIDY4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://YWVzLTEyOC1nY206YjI2NGU0NGEtNTc4Yy00Y2U2LWJiOGQtY2QzMWFlMzMyMDFm@sg.qrfly.link:20702#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2072
vmess://eyJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTlhXHU1OTJhXHU1NzMwXHU1MzNhICA4OCIsICJwb3J0IjogMzE5NDUsICJpZCI6ICJlMmU1MTFiMC03ZGVmLTRlMWItZDIzOC02Y2I1MzkxYjJlM2YiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOTAiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMzguNTQuODYuMjE3IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTM0ZVx1NzZkYlx1OTg3ZkNvZ2VudFx1OTAxYVx1NGZlMVx1NTE2Y1x1NTNmOCA5NCIsICJwb3J0IjogNTY1MDIsICJpZCI6ICJkMjA3NDdhZC1lNjg5LTQxMTEtYTQ2ZS1kNWNmMjFmZjQ4MjciLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDk1IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiMGVkMzU2MjktOTE5YS00ODkxLWJhMGYtMTNjZDE5OGY4NjNiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTcyLjIzMy4xODguMjE3IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI2MTBmN2I3Ni1hNGUyLTRiNWEtYzQ1OC05NmU2OWNiZmZiNWUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTU1NzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZEFrYW1haVx1NzlkMVx1NjI4MFx1NTE2Y1x1NTNmOENETlx1N2Y1MVx1N2VkY1x1ODI4Mlx1NzBiOSAxMDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

