
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp               | ip                                   | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:------------------|:-------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 45.199.138.152  | Netherlands   | NL   | YISP B.V.         | 2a02:2a38:1:2796:ae1f:6bff:fe24:8940 | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 45.146.82.6     | United States | US   | SPRINTLINK        | 45.146.82.6                          | Yes (Region: US) |
|  2 | [6](config/6.json)   | 45.137.97.140   | United States | US   | AS-GLOBALTELEHOST | 45.137.97.140                        | Yes (Region: US) |
|  3 | [7](config/7.json)   | 141.147.153.244 | Japan         | JP   | ORACLE-BMC-31898  | 141.147.153.244                      | Yes (Region: JP) |
|  4 | [14](config/14.json) | 45.146.82.67    | United States | US   | SPRINTLINK        | 45.146.82.67                         | Yes (Region: US) |
|  5 | [15](config/15.json) | 64.32.4.53      | United States | US   | SHARKTECH         | 107.167.13.162                       | Yes (Region: US) |
|  6 | [21](config/21.json) | 183.232.249.189 | Hong Kong     | HK   | CNSERVERS         | 172.247.175.42                       | Yes (Region: US) |
|  7 | [24](config/24.json) | 156.245.8.185   | Netherlands   | NL   | YISP B.V.         | 154.84.1.161                         | Yes (Region: NL) |
|  8 | [30](config/30.json) | 45.137.97.248   | United States | US   | AS-GLOBALTELEHOST | 45.137.97.248                        | Yes (Region: US) |
|  9 | [37](config/37.json) | 45.199.138.173  | Netherlands   | NL   | YISP B.V.         | 154.84.1.129                         | Yes (Region: NL) |
| 10 | [38](config/38.json) | 156.245.8.166   | Netherlands   | NL   | YISP B.V.         | 154.84.1.140                         | Yes (Region: NL) |
| 11 | [45](config/45.json) | 156.245.8.188   | Netherlands   | NL   | YISP B.V.         | 154.84.1.40                          | Yes (Region: NL) |
| 12 | [47](config/47.json) | 45.137.97.230   | United States | US   | AS-GLOBALTELEHOST | 45.137.97.230                        | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNTIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhNDY5MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDUyMzYsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTQ2LjgyLjYiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogImMwZmE3YTEwLTM2MjItNDkyYS1lMWNmLWI4ZjhmNGRmMzQxMiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvVEc6QGhrYWEwIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTM3Ljk3LjE0MCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiYTA0ZTI5MjMtMWE5Ni00OTk4LWVjODktMjYzNGY3MTk3ZWJmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9URzpAaGthYTAiLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTQxLjE0Ny4xNTMuMjQ0IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNDdkNzEzNS0wOTU0LTQ2YWItYTE5MC0xN2I2Yzg2MzBhODUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDE1NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NzQ1ZVx1NTE3OE9yYWNsZSBDb3Jwb3JhdGlvbiA3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTQ2LjgyLjY3IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIxZTM2NjU1Yi03ZDI4LTQ1MTMtZDdmOC01ZjFhMGMwMGEwN2QiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMTQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuNC41MyIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiODY1MzAwNGYtZGU2Ny00NGMyLTljY2UtZTA4MzA5MzNmYjAzIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDM1NTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTgzLjIzMi4yNDkuMTg5IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU5OTAyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggMjEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE4NSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjIwMTYzMzIyLnh5eiIsICJpZCI6ICJkNzczNTA1OC0xZGFjLTQ2MTgtOTlmZi0wYWEwNDQxZWMyZDciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MTc1MDI1OTAxMiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDI0IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTM3Ljk3LjI0OCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZmJjOGNkNzEtMGMzZS00NzE4LWY3M2YtNjVjNmU0N2ViMDdhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9URzpAaGthYTAiLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDMwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNzMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIyMGIzMDkxNi1lMjAzLTQxMmUtOGVjMC05MDBmM2FjZDUxMjgiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMwMzMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDM3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE2NiIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjEyNDYwMTU4Lnh5eiIsICJpZCI6ICJiOGRmM2VmMS04ODdmLTRlZTQtODU1Zi00ZjgwNDE2YzI0NjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MTgwMTc4NTM2OSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDM4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE4OCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjQ4NjQzNzAwLnh5eiIsICJpZCI6ICI1YTRkNjlhZC0yMGE5LTQ5NDEtYjIyMy04N2JiZDA5ZjVmNTIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MTgzNzQwMjA3MyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQ1IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTM3Ljk3LjIzMCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiYTU0ZmQzYmMtMzc2NC00MGNkLWZmNWEtNDcxNDcwNDE3ZWFjIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9URzpAaGthYTAiLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDQ3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

