
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                              | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:---------------------------------|:---------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 38.75.136.49    | United States   | US   | AS-GLOBALTELEHOST                | 38.75.136.49                           | Yes (Region: US) |
|  1 | [2](config/2.json)   | 172.105.226.166 | Japan           | JP   | Akamai Connected Cloud           | 2400:8902::f03c:94ff:febb:ef7a         | Yes (Region: JP) |
|  2 | [8](config/8.json)   | 52.142.161.9    | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK      | 52.142.161.9                           | Yes (Region: GB) |
|  3 | [10](config/10.json) | 45.87.153.246   | The Netherlands | NL   | Stark Industries Solutions Ltd   | 45.87.153.246                          | Yes (Region: NL) |
|  4 | [11](config/11.json) | 52.142.146.57   | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK      | 52.142.146.57                          | Yes (Region: GB) |
|  5 | [13](config/13.json) | 38.54.86.217    | Philippines     | PH   | Kaopu Cloud HK Limited           | 38.54.86.217                           | Yes (Region: PH) |
|  6 | [21](config/21.json) | cm1.awslcn.info | Malaysia        | MY   | TM TECHNOLOGY SERVICES SDN. BHD. | 118.101.192.180                        | Yes (Region: US) |
|  7 | [25](config/25.json) | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST                | 38.91.107.37                           | Yes (Region: US) |
|  8 | [26](config/26.json) | 198.2.202.81    | China           | CN   | PEG-SV                           | 142.4.102.244                          | Yes (Region: US) |
|  9 | [36](config/36.json) | 148.135.33.94   | United States   | US   | MULTA-ASN1                       | 2607:f130:109:0:d6ae:52ff:febb:b49f    | Yes (Region: US) |
| 10 | [38](config/38.json) | 113.20.28.102   | Indonesia       | ID   | ARDH GLOBAL INDONESIA, PT        | 113.20.28.102                          | Yes (Region: ID) |
| 11 | [60](config/60.json) | 138.201.147.115 | Germany         | DE   | Hetzner Online GmbH              | 138.201.147.115                        | Yes (Region: DE) |
| 12 | [64](config/64.json) | 45.58.153.24    | The Netherlands | NL   | SHARKTECH                        | 45.58.149.130                          | Yes (Region: US) |
| 13 | [72](config/72.json) | sg.qrfly.link   | Singapore       | SG   | ORACLE-BMC-31898                 | 152.69.215.149                         | Yes (Region: SG) |
| 14 | [74](config/74.json) | 45.58.145.200   | The Netherlands | NL   | SHARKTECH                        | 45.58.145.194                          | Yes (Region: US) |
| 15 | [75](config/75.json) | 45.121.48.196   | Taiwan          | TW   | EMGINECONCEPT-01                 | 45.121.48.196                          | Yes (Region: TW) |
| 16 | [83](config/83.json) | 202.182.107.52  | Japan           | JP   | AS-CHOOPA                        | 2001:19f0:7001:1f4f:5400:4ff:feaa:a437 | Yes (Region: JP) |
| 17 | [86](config/86.json) | 103.159.206.35  | Taiwan          | TW   | EMGINECONCEPT-01                 | 103.159.206.35                         | Yes (Region: TW) |

## Valid
```
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%201
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNMaW5vZGVcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTcyLjEwNS4yMjYuMTY2IiwgInBvcnQiOiAiMzYxNzMiLCAiaWQiOiAiNWRlODA4ZDEtYjcwNy00NjJjLTgzZjMtNjg3Mzk1MDRhZDcwIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%208
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2010
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2011
vmess://eyJhZGQiOiAiMzguNTQuODYuMjE3IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTM0ZVx1NzZkYlx1OTg3ZkNvZ2VudFx1OTAxYVx1NGZlMVx1NTE2Y1x1NTNmOCAxMyIsICJwb3J0IjogNTY1MDIsICJpZCI6ICJkMjA3NDdhZC1lNjg5LTQxMTEtYTQ2ZS1kNWNmMjFmZjQ4MjciLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMjEiLCAiYWRkIjogImNtMS5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1MjU4IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImNtMS5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2025
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDI2IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTQ4LjEzNS4zMy45NCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMwOTk0MTA0Lnh5eiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMzIzMTI2Mjg3NSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTc0NWVcdTUxNzggIDM2IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTEzLjIwLjI4LjEwMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDM4IiwgInBvcnQiOiAyMjE4OCwgImlkIjogIjAwNjc3ZWI0LTkxYzItNDFmMS1lNzkwLTk2M2I5YTA5M2ZkNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTM4LjIwMS4xNDcuMTE1IiwgImFpZCI6IDAsICJob3N0IjogIjEzOC4yMDEuMTQ3LjExNSIsICJpZCI6ICIzOTZiNjE0Yi02NmNkLTQ1MWQtYTg5YS0zODFhN2YzOWEwOGEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogODg4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZmI3XHU1NmZkSGV0em5lciA2MCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNjQiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
ss://YWVzLTEyOC1nY206YjI2NGU0NGEtNTc4Yy00Y2U2LWJiOGQtY2QzMWFlMzMyMDFm@sg.qrfly.link:20702#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2072
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNzQiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNTU1NDVmOWUtYTU2MS00NTRhLThkYzAtOGJjMTEwZTZiMWM5IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTE2NTIxMDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDc1IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiMGVkMzU2MjktOTE5YS00ODkxLWJhMGYtMTNjZDE5OGY4NjNiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMjAyLjE4Mi4xMDcuNTIiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjXHU0ZTFjXHU0ZWFjQ2hvb3BhXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDgzIiwgInBvcnQiOiAxMjYyNiwgImlkIjogIjRiMDFlNTE3LWY5OGEtNGRiZC04MDJiLTAyMzMwMmFmYzJmNyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTlhXHU1OTJhXHU1NzMwXHU1MzNhICA4NiIsICJwb3J0IjogMzE5NDUsICJpZCI6ICJlMmU1MTFiMC03ZGVmLTRlMWItZDIzOC02Y2I1MzkxYjJlM2YiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
```

