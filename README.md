
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                     | addr          | cn              | cc   | isp                                      | ip                                     | chatgpt          |
|---:|:-----------------------|:--------------|:----------------|:-----|:-----------------------------------------|:---------------------------------------|:-----------------|
|  0 | [9](config/9.json)     | 154.90.39.63  | Malaysia        | MY   | Kaopu Cloud HK Limited                   | 154.90.39.63                           | Yes (Region: MY) |
|  1 | [12](config/12.json)   | 217.160.45.31 | Germany         | DE   | IONOS SE                                 | 217.160.45.31                          | Yes (Region: DE) |
|  2 | [24](config/24.json)   | 198.2.202.81  | China           | CN   | PEG-SV                                   | 142.4.102.244                          | Yes (Region: US) |
|  3 | [46](config/46.json)   | 45.58.145.200 | The Netherlands | NL   | SHARKTECH                                | 45.58.145.194                          | Yes (Region: US) |
|  4 | [52](config/52.json)   | 112.28.208.10 | Japan           | JP   | BGPNET Global ASN                        | 134.122.133.144                        | Yes (Region: SG) |
|  5 | [53](config/53.json)   | 52.142.146.57 | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 52.142.146.57                          | Yes (Region: GB) |
|  6 | [67](config/67.json)   | 38.91.107.37  | United States   | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                           | Yes (Region: US) |
|  7 | [78](config/78.json)   | 45.121.48.172 | Taiwan          | TW   | EMGINECONCEPT-01                         | 45.121.48.172                          | Yes (Region: TW) |
|  8 | [83](config/83.json)   | 123.58.197.70 | Taiwan          | TW   | UCLOUD INFORMATION TECHNOLOGY HK LIMITED | 123.58.197.70                          | Yes (Region: TW) |
|  9 | [94](config/94.json)   | 38.91.107.37  | United States   | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                           | Yes (Region: US) |
| 10 | [105](config/105.json) | 64.176.37.216 | Japan           | JP   | AS-CHOOPA                                | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
| 11 | [106](config/106.json) | 45.121.48.196 | Taiwan          | TW   | EMGINECONCEPT-01                         | 45.121.48.196                          | Yes (Region: TW) |

## Valid
```
vmess://eyJhZGQiOiAiMTU0LjkwLjM5LjYzIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwOGFhODQ5OS1kNjE2LTRmZjEtZDZhYi1jZTBjNTIyODI0YWEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDUzNDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZlx1NzI3OVx1NTIyYlx1ODg0Y1x1NjUzZlx1NTMzYSA5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAxMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDI0IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjUxNjUyMTA5Lnh5eiIsICJpZCI6ICI1NTU0NWY5ZS1hNTYxLTQ1NGEtOGRjMC04YmMxMTBlNmIxYzkiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJwb3J0IjogMzAwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODM3N1x1NTE3MFx1NTMxN1x1ODM3N1x1NTE3MFx1NzcwMVx1OTYzZlx1NTljNlx1NjVhZlx1NzI3OVx1NGUzOVNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0NiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggNTIiLCAiYWRkIjogIjExMi4yOC4yMDguMTAiLCAicG9ydCI6ICI0NjYwMiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2053
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2067
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDc4IiwgImFkZCI6ICI0NS4xMjEuNDguMTcyIiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiZGJhNTFhMmUtYTc4OC00M2I3LTlhYzQtOWY3Y2MxMjU1ZjE1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjYjNcdTUzNTdcdTc3MDFcdTkwZDFcdTVkZGVcdTVlMDJcdTZjYjNcdTUzNTdcdTRlYmZcdTYwNjlcdTc5ZDFcdTYyODBcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggODMiLCAiYWRkIjogIjEyMy41OC4xOTcuNzAiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNGNhMDE5NmMtMDVlNy00NWViLTkwMzYtNjkyYzIwMWY0NWZiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2094
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMTA1IiwgInBvcnQiOiA0NTkzMCwgImlkIjogImIyOTMwYjBkLTAyYjQtNDVkYy04MDI1LWEzYzE5ODc5ZDRhYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDEwNiIsICJhZGQiOiAiNDUuMTIxLjQ4LjE5NiIsICJwb3J0IjogIjEwMDAxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZWQzNTYyOS05MTlhLTQ4OTEtYmEwZi0xM2NkMTk4Zjg2M2IiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
```

