
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                     | addr                | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:-----------------------|:--------------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [4](config/4.json)     | 38.75.136.49        | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49                           | Yes (Region: US) |
|  1 | [5](config/5.json)     | 217.160.45.31       | Germany         | DE   | IONOS SE                       | 217.160.45.31                          | Yes (Region: DE) |
|  2 | [6](config/6.json)     | 52.142.161.9        | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  3 | [9](config/9.json)     | 52.142.146.57       | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
|  4 | [11](config/11.json)   | 112.28.208.10       | Japan           | JP   | BGPNET Global ASN              | 134.122.133.144                        | Yes (Region: SG) |
|  5 | [14](config/14.json)   | us3.36routes.online | United States   | US   | AMAZON-02                      | 34.218.242.184                         | Yes (Region: US) |
|  6 | [17](config/17.json)   | 45.159.249.231      | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  7 | [18](config/18.json)   | kr2.36routes.online | South Korea     | KR   | AMAZON-02                      | 3.35.133.188                           | Yes (Region: US) |
|  8 | [19](config/19.json)   | 38.91.107.37        | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  9 | [22](config/22.json)   | 38.91.107.37        | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 10 | [26](config/26.json)   | 198.2.202.81        | China           | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
| 11 | [48](config/48.json)   | 38.91.107.37        | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 12 | [67](config/67.json)   | 45.58.145.200       | The Netherlands | NL   | SHARKTECH                      | 45.58.145.194                          | Yes (Region: US) |
| 13 | [87](config/87.json)   | 64.176.59.68        | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3d77:5400:4ff:feaa:a946 | Yes (Region: JP) |
| 14 | [101](config/101.json) | 45.121.48.196       | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196                          | Yes (Region: TW) |
| 15 | [103](config/103.json) | 38.54.86.217        | Philippines     | PH   | Kaopu Cloud HK Limited         | 38.54.86.217                           | Yes (Region: PH) |
| 16 | [106](config/106.json) | 64.176.39.31        | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3dba:5400:4ff:feaa:9fd7 | Yes (Region: JP) |
| 17 | [110](config/110.json) | 45.121.48.172       | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.172                          | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMmRcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMiIsICJhZGQiOiAiOC4yMTkuMjQwLjEyMCIsICJwb3J0IjogIjMyOTY5IiwgImlkIjogIjk1MjQ5MDIwLWZiYjctNDU5Mi1lZmNlLTZhZDM5NTRjM2ZhZCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMyIsICJhZGQiOiAiNDcuMjM2LjIyLjMiLCAicG9ydCI6ICI0Nzg4NSIsICJpZCI6ICIyZmI3YWEzNy1lMTk1LTQ0ZjEtZjAwMC01NzI3NjEwZDIyZTMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%204
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%206
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%209
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggMTEiLCAiYWRkIjogIjExMi4yOC4yMDguMTAiLCAicG9ydCI6ICI0NjYwMiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSAiLCAiYWRkIjogInVzMy4zNnJvdXRlcy5vbmxpbmUiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI4ZWZjN2U5ZC03MTZlLTQ0MGMtODU3My01YzUyZThjNTAzZTMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2016
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk3ZTlcdTU2ZmRcdTk5OTZcdTVjMTRBbWF6b25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAiYWRkIjogImtyMi4zNnJvdXRlcy5vbmxpbmUiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI4ZWZjN2U5ZC03MTZlLTQ0MGMtODU3My01YzUyZThjNTAzZTMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2018
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2021
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDI1IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2047
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNjYiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNTU1NDVmOWUtYTU2MS00NTRhLThkYzAtOGJjMTEwZTZiMWM5IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTE2NTIxMDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjU5LjY4IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1ODIxYWMyMS04ZTNmLTRjOGItODMyZC1hNTUxOTBjOTQ0ZTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjU5MzUwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDg2IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDEwMCIsICJhZGQiOiAiNDUuMTIxLjQ4LjE5NiIsICJwb3J0IjogIjEwMDAxIiwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMTAyIiwgImFkZCI6ICIzOC41NC44Ni4yMTciLCAicG9ydCI6ICI1NjUwMiIsICJpZCI6ICJkMjA3NDdhZC1lNjg5LTQxMTEtYTQ2ZS1kNWNmMjFmZjQ4MjciLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMTc2LjM5LjMxIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAxMDUiLCAicG9ydCI6IDU2MjYyLCAiaWQiOiAiNTkwZjI3NDQtZTlkMS00ZjJjLWEzODQtZDM1YjczNmJjYTQxIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDEwOSIsICJhZGQiOiAiNDUuMTIxLjQ4LjE3MiIsICJwb3J0IjogIjEwMDAxIiwgImlkIjogImRiYTUxYTJlLWE3ODgtNDNiNy05YWM0LTlmN2NjMTI1NWYxNSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

