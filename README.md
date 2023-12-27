
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 172.105.226.166 | Japan           | JP   | Akamai Connected Cloud         | 2400:8902::f03c:94ff:febb:ef7a         | Yes (Region: JP) |
|  1 | [3](config/3.json)   | 52.142.146.57   | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
|  2 | [9](config/9.json)   | 217.160.45.31   | Germany         | DE   | IONOS SE                       | 217.160.45.31                          | Yes (Region: DE) |
|  3 | [12](config/12.json) | 198.2.202.81    | China           | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
|  4 | [23](config/23.json) | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  5 | [25](config/25.json) | 38.75.136.49    | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49                           | Yes (Region: US) |
|  6 | [36](config/36.json) | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  7 | [40](config/40.json) | 45.159.249.231  | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  8 | [42](config/42.json) | 172.234.17.31   | United States   | US   | Akamai Connected Cloud         | 2600:3c06::f03c:94ff:fe28:3214         | Yes (Region: US) |
|  9 | [69](config/69.json) | 64.176.37.216   | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
| 10 | [77](config/77.json) | 113.20.28.102   | Indonesia       | ID   | ARDH GLOBAL INDONESIA, PT      | 113.20.28.102                          | Yes (Region: ID) |
| 11 | [79](config/79.json) | cu.awslcn.info  | Australia       | AU   | AS-CHOOPA                      | 149.28.177.17                          | Yes (Region: US) |
| 12 | [94](config/94.json) | 45.121.48.172   | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.172                          | Yes (Region: TW) |
| 13 | [96](config/96.json) | 38.54.82.54     | Thailand        | TH   | Kaopu Cloud HK Limited         | 38.54.82.54                            | Yes (Region: TH) |
| 14 | [97](config/97.json) | 45.58.145.200   | The Netherlands | NL   | SHARKTECH                      | 45.58.145.194                          | Yes (Region: US) |
| 15 | [99](config/99.json) | cm1.awslcn.info |                 |      |                                | 103.182.16.132                         | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTcyLjEwNS4yMjYuMTY2IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0xpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInBvcnQiOiAzNjE3MywgImlkIjogIjVkZTgwOGQxLWI3MDctNDYyYy04M2YzLTY4NzM5NTA0YWQ3MCIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%203
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDEyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2023
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2025
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2036
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2040
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRBa2FtYWlcdTc5ZDFcdTYyODBcdTUxNmNcdTUzZjhDRE5cdTdmNTFcdTdlZGNcdTgyODJcdTcwYjkgNDIiLCAiYWRkIjogIjE3Mi4yMzQuMTcuMzEiLCAicG9ydCI6ICI0ODc3MSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiZjFjMmJlNjQtOTYxYi00MDdhLWM0ZTAtYjg5MTljYTEyNTNiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNjkiLCAicG9ydCI6IDQ1OTMwLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTEzLjIwLjI4LjEwMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDc3IiwgInBvcnQiOiAyMjE4OCwgImlkIjogIjAwNjc3ZWI0LTkxYzItNDFmMS1lNzkwLTk2M2I5YTA5M2ZkNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZlNTZcdTUzNTdcdTc3MDFcdTgwNTRcdTkwMWEgNzkiLCAiYWRkIjogImN1LmF3c2xjbi5pbmZvIiwgInBvcnQiOiAiMjUyODYiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjkzZWM3MjYxLTFjOTItNDE0OS04NDhhLTI2YjZmYjlmYzRjZSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiY3UuYXdzbGNuLmluZm8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjYjNcdTUzNTdcdTc3MDFcdTkwZDFcdTVkZGVcdTVlMDJcdTZjYjNcdTUzNTdcdTRlYmZcdTYwNjlcdTc5ZDFcdTYyODBcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggOTMiLCAiYWRkIjogIjEyMy41OC4xOTcuNzAiLCAicG9ydCI6ICI0NDMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjRjYTAxOTZjLTA1ZTctNDVlYi05MDM2LTY5MmMyMDFmNDVmYiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDk0IiwgImFkZCI6ICI0NS4xMjEuNDguMTcyIiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiZGJhNTFhMmUtYTc4OC00M2I3LTlhYzQtOWY3Y2MxMjU1ZjE1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMzguNTQuODIuNTQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MzRlXHU3NmRiXHU5ODdmQ29nZW50XHU5MDFhXHU0ZmUxXHU1MTZjXHU1M2Y4IDk2IiwgInBvcnQiOiA0MTYwNCwgImlkIjogIjU0ZGU1MGU1LTVlNGItNDQzZi1kOWI4LTllOWUwZWVlODY1YyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOTciLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNTU1NDVmOWUtYTU2MS00NTRhLThkYzAtOGJjMTEwZTZiMWM5IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTE2NTIxMDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggOTkiLCAiYWRkIjogImNtMS5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1Mjg1IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImNtMS5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
```

