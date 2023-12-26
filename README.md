
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 149.28.19.63    | Japan           | JP   | AS-CHOOPA                      | 2001:19f0:7001:316a:5400:4ff:feaa:a955 | Yes (Region: JP) |
|  1 | [7](config/7.json)   | 52.142.146.57   | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
|  2 | [8](config/8.json)   | 38.75.136.49    | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49                           | Yes (Region: US) |
|  3 | [13](config/13.json) | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  4 | [14](config/14.json) | 52.142.161.9    | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  5 | [16](config/16.json) | 148.135.33.94   | United States   | US   | MULTA-ASN1                     | 2607:f130:109:0:d6ae:52ff:febb:b49f    | Yes (Region: US) |
|  6 | [17](config/17.json) | 167.179.111.237 | Japan           | JP   | AS-CHOOPA                      | 2001:19f0:7001:244:5400:4ff:feab:d9e2  | Yes (Region: JP) |
|  7 | [20](config/20.json) | 154.90.39.63    | Malaysia        | MY   | Kaopu Cloud HK Limited         | 154.90.39.63                           | Yes (Region: MY) |
|  8 | [27](config/27.json) | 64.176.47.200   | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3ba0:5400:4ff:feaa:a942 | Yes (Region: JP) |
|  9 | [34](config/34.json) | 64.176.59.68    | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3d77:5400:4ff:feaa:a946 | Yes (Region: JP) |
| 10 | [38](config/38.json) | 198.2.202.81    | China           | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
| 11 | [39](config/39.json) | 38.54.82.54     | Thailand        | TH   | Kaopu Cloud HK Limited         | 38.54.82.54                            | Yes (Region: TH) |
| 12 | [41](config/41.json) | 64.176.37.216   | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
| 13 | [42](config/42.json) | 64.176.42.137   | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3c78:5400:4ff:feaa:a94b | Yes (Region: JP) |
| 14 | [44](config/44.json) | 113.20.28.102   | Indonesia       | ID   | ARDH GLOBAL INDONESIA, PT      | 113.20.28.102                          | Yes (Region: ID) |
| 15 | [48](config/48.json) | sg.qrfly.link   | Singapore       | SG   | ORACLE-BMC-31898               | 129.150.32.143                         | Yes (Region: SG) |
| 16 | [52](config/52.json) | 202.182.107.52  | Japan           | JP   | AS-CHOOPA                      | 2001:19f0:7001:1f4f:5400:4ff:feaa:a437 | Yes (Region: JP) |
| 17 | [69](config/69.json) | 45.159.249.231  | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
| 18 | [71](config/71.json) | 45.58.145.200   | The Netherlands | NL   | SHARKTECH                      | 45.58.145.194                          | Yes (Region: US) |
| 19 | [78](config/78.json) | 45.58.153.24    | The Netherlands | NL   | SHARKTECH                      | 45.58.149.130                          | Yes (Region: US) |
| 20 | [86](config/86.json) | 103.159.206.35  | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35                         | Yes (Region: TW) |
| 21 | [87](config/87.json) | 45.121.48.196   | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196                          | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJhZGQiOiAiMTQ5LjI4LjE5LjYzIiwgInBvcnQiOiAiNDIyODAiLCAiaWQiOiAiODIzY2EwZDQtYTdmOC00ZTk5LTgwOTAtMjM1MWY3MThkMTA2IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%207
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%208
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2013
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2014
vmess://eyJhZGQiOiAiMTQ4LjEzNS4zMy45NCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMwOTk0MTA0Lnh5eiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMzIzMTI2Mjg3NSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTc0NWVcdTUxNzggIDE2IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTY3LjE3OS4xMTEuMjM3IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0Nob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxNyIsICJwb3J0IjogMTQ5MzUsICJpZCI6ICJlOTYxODk0Zi04ZTkwLTQ3MmYtOThkMy0wOTQwMmU0YmU0NTMiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiOC4yMTkuNTkuNjMiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTJkXHU1NmZkXHU5NjNmXHU5MWNjXHU0ZTkxIDE4IiwgInBvcnQiOiAxMjY4MSwgImlkIjogImNjNThjYmRjLWMzNmYtNDJmNC05MjU0LThmNGZjNTY0MjQ2YiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTcyNzlcdTUyMmJcdTg4NGNcdTY1M2ZcdTUzM2EgMjAiLCAiYWRkIjogIjE1NC45MC4zOS42MyIsICJwb3J0IjogIjQ1MzQzIiwgImlkIjogIjA4YWE4NDk5LWQ2MTYtNGZmMS1kNmFiLWNlMGM1MjI4MjRhYSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjQ3LjIwMCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGQ1ZThhYTItMDY0MS00MzIzLWU5MmMtMmMwNjFjZGM4ZTM0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICIyOTQxNCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAyNyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjU5LjY4IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1ODIxYWMyMS04ZTNmLTRjOGItODMyZC1hNTUxOTBjOTQ0ZTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjU5MzUwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDM0IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDM4IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMzkiLCAiYWRkIjogIjM4LjU0LjgyLjU0IiwgInBvcnQiOiAiNDE2MDQiLCAiaWQiOiAiNTRkZTUwZTUtNWU0Yi00NDNmLWQ5YjgtOWU5ZTBlZWU4NjVjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNDEiLCAicG9ydCI6IDQ1OTMwLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMTc2LjQyLjEzNyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNDIiLCAicG9ydCI6IDIwODg2LCAiaWQiOiAiZjU3NGIyMzctM2ViZi00MDVjLWQ1NDAtNTQxNTMwZmU1ZWQ3IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTEzLjIwLjI4LjEwMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDQ0IiwgInBvcnQiOiAyMjE4OCwgImlkIjogIjAwNjc3ZWI0LTkxYzItNDFmMS1lNzkwLTk2M2I5YTA5M2ZkNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://YWVzLTEyOC1nY206YjI2NGU0NGEtNTc4Yy00Y2U2LWJiOGQtY2QzMWFlMzMyMDFm@sg.qrfly.link:20702#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2048
vmess://eyJhZGQiOiAiMjAyLjE4Mi4xMDcuNTIiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjXHU0ZTFjXHU0ZWFjQ2hvb3BhXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUyIiwgInBvcnQiOiAxMjYyNiwgImlkIjogIjRiMDFlNTE3LWY5OGEtNGRiZC04MDJiLTAyMzMwMmFmYzJmNyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2069
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNzEiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNTU1NDVmOWUtYTU2MS00NTRhLThkYzAtOGJjMTEwZTZiMWM5IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTE2NTIxMDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNzgiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTlhXHU1OTJhXHU1NzMwXHU1MzNhICA4NiIsICJwb3J0IjogMzE5NDUsICJpZCI6ICJlMmU1MTFiMC03ZGVmLTRlMWItZDIzOC02Y2I1MzkxYjJlM2YiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDg3IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiMGVkMzU2MjktOTE5YS00ODkxLWJhMGYtMTNjZDE5OGY4NjNiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

