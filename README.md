
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn             | cc   | isp                            | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:---------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 149.28.19.63    | Japan          | JP   | AS-CHOOPA                      | 2001:19f0:7001:316a:5400:4ff:feaa:a955 | Yes (Region: JP) |
|  1 | [3](config/3.json)   | 38.75.136.49    | United States  | US   | AS-GLOBALTELEHOST              | 38.75.136.49                           | Yes (Region: US) |
|  2 | [4](config/4.json)   | 207.148.26.144  | United States  | US   | AS-CHOOPA                      | 2001:19f0:0:4b1e:5400:4ff:fea8:ce07    | Yes (Region: US) |
|  3 | [5](config/5.json)   | 38.91.107.37    | United States  | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  4 | [8](config/8.json)   | 38.91.107.37    | United States  | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  5 | [9](config/9.json)   | 52.142.161.9    | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  6 | [10](config/10.json) | 217.160.45.31   | Germany        | DE   | IONOS SE                       | 217.160.45.31                          | Yes (Region: DE) |
|  7 | [11](config/11.json) | 52.142.146.57   | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
|  8 | [14](config/14.json) | 108.165.113.99  | United States  | US   | US-CLOUDNIUM-01                | 108.165.113.99                         | Yes (Region: US) |
|  9 | [16](config/16.json) | 38.91.107.37    | United States  | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 10 | [25](config/25.json) | 38.54.82.54     | Thailand       | TH   | Kaopu Cloud HK Limited         | 38.54.82.54                            | Yes (Region: TH) |
| 11 | [29](config/29.json) | 167.179.111.237 | Japan          | JP   | AS-CHOOPA                      | 2001:19f0:7001:244:5400:4ff:feab:d9e2  | Yes (Region: JP) |
| 12 | [31](config/31.json) | 64.176.47.200   | Japan          | JP   | AS-CHOOPA                      | 2401:c080:3800:3ba0:5400:4ff:feaa:a942 | Yes (Region: JP) |
| 13 | [37](config/37.json) | 64.176.39.31    | Japan          | JP   | AS-CHOOPA                      | 2401:c080:3800:3dba:5400:4ff:feaa:9fd7 | Yes (Region: JP) |
| 14 | [77](config/77.json) | 45.159.249.231  | Finland        | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
| 15 | [81](config/81.json) | 113.20.28.102   | Indonesia      | ID   | ARDH GLOBAL INDONESIA, PT      | 113.20.28.102                          | Yes (Region: ID) |
| 16 | [82](config/82.json) | 64.176.37.216   | Japan          | JP   | AS-CHOOPA                      | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
| 17 | [90](config/90.json) | 45.121.48.196   | Taiwan         | TW   | EMGINECONCEPT-01               | 45.121.48.196                          | Yes (Region: TW) |
| 18 | [92](config/92.json) | 112.28.208.10   | Japan          | JP   | BGPNET Global ASN              | 134.122.133.144                        | Yes (Region: SG) |
| 19 | [95](config/95.json) | 64.176.59.68    | Japan          | JP   | AS-CHOOPA                      | 2401:c080:3800:3d77:5400:4ff:feaa:a946 | Yes (Region: JP) |
| 20 | [96](config/96.json) | 139.180.202.213 | Japan          | JP   | AS-CHOOPA                      | 2001:19f0:7001:2966:5400:4ff:feaa:e764 | Yes (Region: JP) |
| 21 | [98](config/98.json) | 45.121.48.172   | Taiwan         | TW   | EMGINECONCEPT-01               | 45.121.48.172                          | Yes (Region: TW) |
| 22 | [99](config/99.json) | 144.202.84.47   | United States  | US   | AS-CHOOPA                      | 2001:19f0:8001:1d02:5400:4ff:fea8:d0c2 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTQ5LjI4LjE5LjYzIiwgInBvcnQiOiAiNDIyODAiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjgyM2NhMGQ0LWE3ZjgtNGU5OS04MDkwLTIzNTFmNzE4ZDEwNiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%203
vmess://eyJhZGQiOiAiMjA3LjE0OC4yNi4xNDQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU2NWIwXHU2Y2ZkXHU4OTdmXHU1ZGRlXHU3NmFlXHU2NWFmXHU1MzYxXHU3Mjc5XHU3ZWY0VnVsdHJcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJwb3J0IjogMjI1ODksICJpZCI6ICIxMDg3NzQ0Ni1mOWFhLTRiODQtZWM0My1hNjg4NTIxODE1ZGQiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%205
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%208
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%209
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAxMCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2011
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDE0IiwgImFkZCI6ICIxMDguMTY1LjExMy45OSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJlZjIyZmFkMy02NTJhLTQ4ZmMtZTgwYS00NmZhYTNhNmE3ODciLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2016
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMjUiLCAiYWRkIjogIjM4LjU0LjgyLjU0IiwgInBvcnQiOiAiNDE2MDQiLCAiaWQiOiAiNTRkZTUwZTUtNWU0Yi00NDNmLWQ5YjgtOWU5ZTBlZWU4NjVjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjkiLCAiYWRkIjogIjE2Ny4xNzkuMTExLjIzNyIsICJwb3J0IjogIjE0OTM1IiwgImlkIjogImU5NjE4OTRmLThlOTAtNDcyZi05OGQzLTA5NDAyZTRiZTQ1MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjQ3LjIwMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMzEiLCAicG9ydCI6IDI5NDE0LCAiaWQiOiAiNGQ1ZThhYTItMDY0MS00MzIzLWU5MmMtMmMwNjFjZGM4ZTM0IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMzciLCAiYWRkIjogIjY0LjE3Ni4zOS4zMSIsICJwb3J0IjogIjU2MjYyIiwgImlkIjogIjU5MGYyNzQ0LWU5ZDEtNGYyYy1hMzg0LWQzNWI3MzZiY2E0MSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2077
vmess://eyJhZGQiOiAiMTEzLjIwLjI4LjEwMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDgxIiwgInBvcnQiOiAyMjE4OCwgImlkIjogIjAwNjc3ZWI0LTkxYzItNDFmMS1lNzkwLTk2M2I5YTA5M2ZkNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgODIiLCAicG9ydCI6IDQ1OTMwLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDkwIiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggOTIiLCAiYWRkIjogIjExMi4yOC4yMDguMTAiLCAicG9ydCI6ICI0NjYwMiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMTc2LjU5LjY4IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1ODIxYWMyMS04ZTNmLTRjOGItODMyZC1hNTUxOTBjOTQ0ZTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjU5MzUwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDk1IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOTYiLCAiYWRkIjogIjEzOS4xODAuMjAyLjIxMyIsICJwb3J0IjogIjQyNDM0IiwgImlkIjogImQ5YTdjNTI5LWY5OGItNDI5Yi1lYjI2LWM5MDk3OWM5MTBhMyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDk4IiwgImFkZCI6ICI0NS4xMjEuNDguMTcyIiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiZGJhNTFhMmUtYTc4OC00M2I3LTlhYzQtOWY3Y2MxMjU1ZjE1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZcdTVkZGVcdTg5N2ZcdTk2YzVcdTU2ZmVDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOTkiLCAiYWRkIjogIjE0NC4yMDIuODQuNDciLCAicG9ydCI6ICI1Nzg0OCIsICJpZCI6ICJlNDg2NDNlNy0wNDYyLTQwNTUtZjc5Ni02Y2E2YWE5Zjk0NmQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

