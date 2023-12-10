
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                                  | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-------------------------------------|:---------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 142.171.229.164 | United States | US   | MULTA-ASN1                           | 142.171.229.164                        | Yes (Region: US) |
|  1 | [4](config/4.json)   | 64.31.55.5      | United States | US   | LIMESTONENETWORKS                    | 64.31.55.5                             | Yes (Region: US) |
|  2 | [10](config/10.json) | 43.153.210.169  | Singapore     | SG   | Tencent Building, Kejizhongyi Avenue | 43.153.210.169                         | Yes (Region: SG) |
|  3 | [11](config/11.json) | 43.156.237.238  | Singapore     | SG   | Tencent Building, Kejizhongyi Avenue | 43.156.237.238                         | Yes (Region: SG) |
|  4 | [15](config/15.json) | 23.247.130.248  | France        | FR   | YISU CLOUD LTD                       | 23.247.130.248                         | Yes (Region: FR) |
|  5 | [21](config/21.json) | 45.121.48.193   | Taiwan        | TW   | EMGINECONCEPT-01                     | 45.121.48.193                          | Yes (Region: TW) |
|  6 | [23](config/23.json) | 64.176.58.15    | Japan         | JP   | AS-CHOOPA                            | 2401:c080:3800:3dec:5400:4ff:feaa:9fd8 | Yes (Region: JP) |
|  7 | [34](config/34.json) | 183.240.232.93  | Hong Kong     | HK   | CNSERVERS                            | 23.224.212.138                         | Yes (Region: US) |
|  8 | [44](config/44.json) | 45.121.48.196   | Taiwan        | TW   | EMGINECONCEPT-01                     | 45.121.48.196                          | Yes (Region: TW) |
|  9 | [46](config/46.json) | 64.176.47.69    | Japan         | JP   | AS-CHOOPA                            | 2401:c080:3800:3f58:5400:4ff:feab:cd7b | Yes (Region: JP) |
| 10 | [53](config/53.json) | 47.236.111.83   | Singapore     | SG   | Alibaba US Technology Co., Ltd.      | 47.236.111.83                          | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUyYTBcdTYyZmZcdTU5MjcgIDMiLCAiYWRkIjogIjE0Mi4xNzEuMjI5LjE2NCIsICJwb3J0IjogIjEzNDY5IiwgImlkIjogIjNiNzdhMTE1LTBlOGEtNDkzOS1lNjRjLWYxMzk5NDk0MmMyZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@64.31.55.5:11223#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%BE%97%E5%85%8B%E8%90%A8%E6%96%AF%E5%B7%9E%E8%BE%BE%E6%8B%89%E6%96%AFLimestone%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%204
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmMgIDEwIiwgImFkZCI6ICI0My4xNTMuMjEwLjE2OSIsICJwb3J0IjogIjY2NiIsICJpZCI6ICIzNGEyZjA5My1jMjM2LTRlZGMtZWI2YS02NjNmMWJmYWExMzYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206MTIz@43.156.237.238:10000#github.com/freefq%20-%20%E6%97%A5%E6%9C%AC%20%2011
vmess://eyJhZGQiOiAiMjMuMjQ3LjEzMC4yNDgiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzE3XHU3ZjhlXHU1NzMwXHU1MzNhICAxNSIsICJwb3J0IjogMTcwNTcsICJpZCI6ICI1NjlhMjZlYy0xYTI4LTQyMWQtZGY5YS1lMTVhZWZjMTU1MzEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE5MyIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNDIwMDI2ZDMtNDc0Yi00N2UzLWIyNmItMjNhMjJhYTFmNGY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDEwMDAxLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDIxIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMjMiLCAiYWRkIjogIjY0LjE3Ni41OC4xNSIsICJwb3J0IjogIjQ2MTU0IiwgImlkIjogImFkY2JlMTYwLTMwMTAtNDgzZC1iNDM4LWQ2MDU3ZjQ2NWIxZCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMzQiLCAiYWRkIjogIjE4My4yNDAuMjMyLjkzIiwgInBvcnQiOiAiMzQwMDEiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE5NiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDQ0IiwgInBvcnQiOiAxMDAwMSwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjQ3LjY5IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIzYTc5ZGUzMy1iZmEwLTRkNWEtZDY4MS0zYmZmYjNlYTBlNjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTg3MDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSA0NiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgNTMiLCAiYWRkIjogIjQ3LjIzNi4xMTEuODMiLCAicG9ydCI6ICIzMTA5MSIsICJpZCI6ICJmMGVhZmQ2Yi1hZDM5LTQ4NzUtOWIyOS03MjIyMzdkMTU1ZjMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

