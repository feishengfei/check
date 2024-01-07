
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                            | ip              | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:-------------------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 38.68.134.202   | United States   | US   | AS-GLOBALTELEHOST              | 38.68.134.202   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 51.158.150.168  | France          | FR   | Scaleway S.a.s.                | 51.158.150.168  | Yes (Region: FR) |
|  2 | [4](config/4.json)   | 45.87.153.246   | The Netherlands | NL   | Stark Industries Solutions Ltd | 45.87.153.246   | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 51.145.68.57    | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 51.145.68.57    | Yes (Region: GB) |
|  4 | [6](config/6.json)   | 139.180.211.152 | Singapore       | SG   | AS-CHOOPA                      | 139.180.211.152 | Yes (Region: SG) |
|  5 | [7](config/7.json)   | 51.142.73.20    | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 51.142.73.20    | Yes (Region: GB) |
|  6 | [8](config/8.json)   | 38.68.134.202   | United States   | US   | AS-GLOBALTELEHOST              | 38.68.134.202   | Yes (Region: US) |
|  7 | [9](config/9.json)   | 38.54.185.111   | China           | CN   | PEG-SV                         | 192.74.239.146  | Yes (Region: US) |
|  8 | [10](config/10.json) | 217.160.45.31   | Germany         | DE   | IONOS SE                       | 217.160.45.31   | Yes (Region: DE) |
|  9 | [11](config/11.json) | 112.28.208.10   | Japan           | JP   | BGPNET Global ASN              | 134.122.133.144 | Yes (Region: SG) |
| 10 | [12](config/12.json) | 38.54.185.112   | China           | CN   | PEG-SV                         | 192.74.239.146  | Yes (Region: US) |
| 11 | [13](config/13.json) | 38.68.134.202   | United States   | US   | AS-GLOBALTELEHOST              | 38.68.134.202   | Yes (Region: US) |

## Valid
```
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@38.68.134.202:8091#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%202
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@51.158.150.168:4444#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E5%B7%B4%E9%BB%8EOnline%20S.A.S%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%204
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpLbEpsWFhlOUtqUVg0bWg0eEMwNWM5@51.145.68.57:13751#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%205
vmess://eyJhZGQiOiAiMTM5LjE4MC4yMTEuMTUyIiwgImFpZCI6ICIwIiwgImhvc3QiOiAibS56b29tLnVzIiwgImlkIjogIjBkNGY2NDdiLTBkOTYtNDgyMC05ZGU4LTAxODYxNTYxODVkZCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvRGlhbG9nIFpvb20iLCAicG9ydCI6ICIxODA2MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjViMFx1NTJhMFx1NTc2MUNob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp0QW9XenVLdk5PUHJzTGM0ZkFFT25v@51.142.73.20:6961#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%207
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@38.68.134.202:2375#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%208
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggOSIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogInd3dy43MzY2NDk5OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAwNjU3NjI1MTgxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAxMCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggMTEiLCAiYWRkIjogIjExMi4yOC4yMDguMTAiLCAicG9ydCI6ICI0NjYwMiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMTIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMTA5MTEzMzQwOSIsICJ0bHMiOiAidGxzIn0=
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.68.134.202:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2013
```

