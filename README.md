
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                     | addr                    | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:-----------------------|:------------------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)     | 45.159.249.231          | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  1 | [10](config/10.json)   | 142.171.202.130         | United States   | US   | MULTA-ASN1                     | 2607:f130:109:0:d6ae:52ff:febb:b11b    | Yes (Region: US) |
|  2 | [15](config/15.json)   | 94.131.12.245           | Switzerland     | CH   | Stark Industries Solutions Ltd | 94.131.12.245                          | Yes (Region: CH) |
|  3 | [22](config/22.json)   | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  4 | [23](config/23.json)   | 45.8.146.35             | United States   | US   | Stark Industries Solutions Ltd | 45.8.146.35                            | Yes (Region: US) |
|  5 | [29](config/29.json)   | 198.2.202.81            | China           | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
|  6 | [34](config/34.json)   | 217.160.45.31           | Germany         | DE   | IONOS SE                       | 217.160.45.31                          | Yes (Region: DE) |
|  7 | [35](config/35.json)   | cm.awslcn.info          | Taiwan          | TW   | ByteVirt LLC                   | 108.165.144.166                        | Yes (Region: US) |
|  8 | [43](config/43.json)   | 52.142.161.9            | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  9 | [46](config/46.json)   | 45.8.147.80             | Sweden          | SE   | Stark Industries Solutions Ltd | 45.8.147.80                            | Yes (Region: SE) |
| 10 | [52](config/52.json)   | cu.awslcn.info          | Australia       | AU   | AS-CHOOPA                      | 149.28.177.17                          | Yes (Region: US) |
| 11 | [55](config/55.json)   | 52.142.146.57           | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
| 12 | [57](config/57.json)   | afrhms16v.bestxray.buzz | United Kingdom  | GB   | Akamai Connected Cloud         | 139.162.227.16                         | Yes (Region: GB) |
| 13 | [62](config/62.json)   | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 14 | [73](config/73.json)   | 51.141.127.238          | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 51.141.127.238                         | Yes (Region: GB) |
| 15 | [82](config/82.json)   | 45.121.48.172           | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.172                          | Yes (Region: TW) |
| 16 | [89](config/89.json)   | 45.58.145.200           | The Netherlands | NL   | SHARKTECH                      | 45.58.145.194                          | Yes (Region: US) |
| 17 | [91](config/91.json)   | 113.20.28.102           | Indonesia       | ID   | ARDH GLOBAL INDONESIA, PT      | 113.20.28.102                          | Yes (Region: ID) |
| 18 | [92](config/92.json)   | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 19 | [100](config/100.json) | 103.159.206.35          | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35                         | Yes (Region: TW) |
| 20 | [106](config/106.json) | 154.90.39.63            | Malaysia        | MY   | Kaopu Cloud HK Limited         | 154.90.39.63                           | Yes (Region: MY) |
| 21 | [110](config/110.json) | 45.121.48.196           | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196                          | Yes (Region: TW) |
| 22 | [116](config/116.json) | 64.176.59.68            | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3d77:5400:4ff:feaa:a946 | Yes (Region: JP) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%202
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUyYTBcdTYyZmZcdTU5MjcgIDEwIiwgImFkZCI6ICIxNDIuMTcxLjIwMi4xMzAiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy44Nzk4MTUzMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyNjUwOTkyNDkxIiwgInRscyI6ICJ0bHMifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpBSzRKMXNSdDJ2M2RMRFVWQzJQNWxq@94.131.12.245:37726#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%2015
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2022
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVMUVZUlFwVThyTEdSS3ZETWZSNkZ2@45.8.146.35:47413#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2023
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDI5IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAzNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMzUiLCAiYWRkIjogImNtLmF3c2xjbi5pbmZvIiwgInBvcnQiOiAyNTIzMywgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiOTNlYzcyNjEtMWM5Mi00MTQ5LTg0OGEtMjZiNmZiOWZjNGNlIiwgImhvc3QiOiAiY20uYXdzbGNuLmluZm8iLCAicGF0aCI6ICIvIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2043
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2046
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZlNTZcdTUzNTdcdTc3MDFcdTgwNTRcdTkwMWEgNTIiLCAiYWRkIjogImN1LmF3c2xjbi5pbmZvIiwgInBvcnQiOiAiMjUyODYiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjkzZWM3MjYxLTFjOTItNDE0OS04NDhhLTI2YjZmYjlmYzRjZSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiY3UuYXdzbGNuLmluZm8iLCAidGxzIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2055
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDU3IiwgImFkZCI6ICJhZnJobXMxNnYuYmVzdHhyYXkuYnV6eiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJmNTg0ZGUxNS0yMDM0LTQxNzAtYTcyMy1mNDhjMmJhZTVlMGYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi9saW5rd3MiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2062
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpNSzJRbng2Nnprd3BRUXo4eVRYVkNG@51.141.127.238:32413#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%2073
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE3MiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDgyIiwgInBvcnQiOiAxMDAwMSwgImlkIjogImRiYTUxYTJlLWE3ODgtNDNiNy05YWM0LTlmN2NjMTI1NWYxNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjUxNjUyMTA5Lnh5eiIsICJpZCI6ICI1NTU0NWY5ZS1hNTYxLTQ1NGEtOGRjMC04YmMxMTBlNmIxYzkiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJwb3J0IjogMzAwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODM3N1x1NTE3MFx1NTMxN1x1ODM3N1x1NTE3MFx1NzcwMVx1OTYzZlx1NTljNlx1NjVhZlx1NzI3OVx1NGUzOVNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA4OSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTEzLjIwLjI4LjEwMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDkxIiwgInBvcnQiOiAyMjE4OCwgImlkIjogIjAwNjc3ZWI0LTkxYzItNDFmMS1lNzkwLTk2M2I5YTA5M2ZkNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2092
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDEwMCIsICJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAicG9ydCI6ICIzMTk0NSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAiIiwgImlkIjogImUyZTUxMWIwLTdkZWYtNGUxYi1kMjM4LTZjYjUzOTFiMmUzZiIsICJzbmkiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTcyNzlcdTUyMmJcdTg4NGNcdTY1M2ZcdTUzM2EgMTA2IiwgImFkZCI6ICIxNTQuOTAuMzkuNjMiLCAicG9ydCI6ICI0NTM0MyIsICJpZCI6ICIwOGFhODQ5OS1kNjE2LTRmZjEtZDZhYi1jZTBjNTIyODI0YWEiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDExMCIsICJhZGQiOiAiNDUuMTIxLjQ4LjE5NiIsICJwb3J0IjogIjEwMDAxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZWQzNTYyOS05MTlhLTQ4OTEtYmEwZi0xM2NkMTk4Zjg2M2IiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTgzLjE4MS4zNi4xOTQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjICAxMTEiLCAicG9ydCI6IDQxNTk3LCAiaWQiOiAiNGE2ZWFhMmQtNTYwMy00YzA1LWQ5NjctZmI2ZjQyMjUwYTVhIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMTE2IiwgImFkZCI6ICI2NC4xNzYuNTkuNjgiLCAicG9ydCI6ICI1OTM1MCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNTgyMWFjMjEtOGUzZi00YzhiLTgzMmQtYTU1MTkwYzk0NGU5IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
```

