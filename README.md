
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn             | cc   | isp                            | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:---------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 38.75.136.49    | United States  | US   | AS-GLOBALTELEHOST              | 38.75.136.49                           | Yes (Region: US) |
|  1 | [3](config/3.json)   | 149.28.19.63    | Japan          | JP   | AS-CHOOPA                      | 2001:19f0:7001:316a:5400:4ff:feaa:a955 | Yes (Region: JP) |
|  2 | [5](config/5.json)   | 167.179.111.237 | Japan          | JP   | AS-CHOOPA                      | 2001:19f0:7001:244:5400:4ff:feab:d9e2  | Yes (Region: JP) |
|  3 | [11](config/11.json) | 52.142.161.9    | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  4 | [12](config/12.json) | 52.142.146.57   | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
|  5 | [15](config/15.json) | 38.91.107.37    | United States  | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  6 | [21](config/21.json) | 45.159.249.231  | Finland        | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  7 | [28](config/28.json) | 38.91.107.37    | United States  | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  8 | [30](config/30.json) | 38.91.107.37    | United States  | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  9 | [35](config/35.json) | 198.2.202.81    | China          | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
| 10 | [47](config/47.json) | sg.qrfly.link   |                |      |                                | 152.69.215.149                         | Yes (Region: SG) |
| 11 | [54](config/54.json) | 123.58.197.70   |                |      |                                | 123.58.197.70                          | Yes (Region: TW) |
| 12 | [60](config/60.json) | 112.28.208.10   |                |      |                                | 134.122.133.144                        | Yes (Region: SG) |
| 13 | [68](config/68.json) | 45.58.145.200   |                |      |                                | 45.58.145.194                          | Yes (Region: US) |
| 14 | [81](config/81.json) | 45.58.153.24    |                |      |                                | 45.58.149.130                          | Yes (Region: US) |
| 15 | [84](config/84.json) | 103.159.206.35  |                |      |                                | 103.159.206.35                         | Yes (Region: TW) |
| 16 | [92](config/92.json) | 45.121.48.172   |                |      |                                | 45.121.48.172                          | Yes (Region: TW) |

## Valid
```
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%202
vmess://eyJhZGQiOiAiMTQ5LjI4LjE5LjYzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0Nob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAzIiwgInBvcnQiOiA0MjI4MCwgImlkIjogIjgyM2NhMGQ0LWE3ZjgtNGU5OS04MDkwLTIzNTFmNzE4ZDEwNiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTY3LjE3OS4xMTEuMjM3IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0Nob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA1IiwgInBvcnQiOiAxNDkzNSwgImlkIjogImU5NjE4OTRmLThlOTAtNDcyZi05OGQzLTA5NDAyZTRiZTQ1MyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2011
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2012
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2015
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2021
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2028
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2030
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDM1IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
ss://YWVzLTEyOC1nY206YjI2NGU0NGEtNTc4Yy00Y2U2LWJiOGQtY2QzMWFlMzMyMDFm@sg.qrfly.link:20702#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2047
vmess://eyJhZGQiOiAiMTIzLjU4LjE5Ny43MCIsICJhaWQiOiAwLCAiaG9zdCI6ICIxMjMuNTguMTk3LjcwIiwgImlkIjogIjRjYTAxOTZjLTA1ZTctNDVlYi05MDM2LTY5MmMyMDFmNDVmYiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NmNiM1x1NTM1N1x1NzcwMVx1OTBkMVx1NWRkZVx1NWUwMlx1NmNiM1x1NTM1N1x1NGViZlx1NjA2OVx1NzlkMVx1NjI4MFx1NjcwOVx1OTY1MFx1NTE2Y1x1NTNmOCA1NCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggNjAiLCAiYWRkIjogIjExMi4yOC4yMDguMTAiLCAicG9ydCI6ICI0NjYwMiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNjgiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNTU1NDVmOWUtYTU2MS00NTRhLThkYzAtOGJjMTEwZTZiMWM5IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTE2NTIxMDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgODEiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTlhXHU1OTJhXHU1NzMwXHU1MzNhICA4NCIsICJwb3J0IjogMzE5NDUsICJpZCI6ICJlMmU1MTFiMC03ZGVmLTRlMWItZDIzOC02Y2I1MzkxYjJlM2YiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDkyIiwgImFkZCI6ICI0NS4xMjEuNDguMTcyIiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiZGJhNTFhMmUtYTc4OC00M2I3LTlhYzQtOWY3Y2MxMjU1ZjE1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

