
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn              | cc   | isp                                      | ip                                    | chatgpt          |
|---:|:---------------------|:------------------------|:----------------|:-----|:-----------------------------------------|:--------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 52.142.146.57           | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 52.142.146.57                         | Yes (Region: GB) |
|  1 | [3](config/3.json)   | 51.141.101.197          | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 51.141.101.197                        | Yes (Region: GB) |
|  2 | [5](config/5.json)   | 217.160.45.31           | Germany         | DE   | IONOS SE                                 | 217.160.45.31                         | Yes (Region: DE) |
|  3 | [6](config/6.json)   | 52.142.161.9            | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 52.142.161.9                          | Yes (Region: GB) |
|  4 | [7](config/7.json)   | 51.141.100.112          | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 51.141.100.112                        | Yes (Region: GB) |
|  5 | [17](config/17.json) | 94.131.12.245           | Switzerland     | CH   | Stark Industries Solutions Ltd           | 94.131.12.245                         | Yes (Region: CH) |
|  6 | [20](config/20.json) | 198.2.200.37            | United States   | US   | PEG-SV                                   | 142.4.98.185                          | Yes (Region: US) |
|  7 | [24](config/24.json) | 167.179.111.237         | Japan           | JP   | AS-CHOOPA                                | 2001:19f0:7001:244:5400:4ff:feab:d9e2 | Yes (Region: JP) |
|  8 | [26](config/26.json) | 45.77.245.47            | Singapore       | SG   | AS-CHOOPA                                | 45.77.245.47                          | Yes (Region: SG) |
|  9 | [29](config/29.json) | 45.159.249.231          | Finland         | FI   | Stark Industries Solutions Ltd           | 45.159.249.231                        | Yes (Region: FI) |
| 10 | [30](config/30.json) | 142.171.202.130         | United States   | US   | MULTA-ASN1                               | 2607:f130:109:0:d6ae:52ff:febb:b11b   | Yes (Region: US) |
| 11 | [33](config/33.json) | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                          | Yes (Region: US) |
| 12 | [45](config/45.json) | afrhms16v.bestxray.buzz | United Kingdom  | GB   | Akamai Connected Cloud                   | 139.162.227.16                        | Yes (Region: GB) |
| 13 | [61](config/61.json) | 103.159.206.35          | Taiwan          | TW   | EMGINECONCEPT-01                         | 103.159.206.35                        | Yes (Region: TW) |
| 14 | [62](config/62.json) | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                          | Yes (Region: US) |
| 15 | [69](config/69.json) | 45.58.145.200           | The Netherlands | NL   | SHARKTECH                                | 45.58.145.194                         | Yes (Region: US) |
| 16 | [73](config/73.json) | 45.121.48.172           | Taiwan          | TW   | EMGINECONCEPT-01                         | 45.121.48.172                         | Yes (Region: TW) |
| 17 | [74](config/74.json) | 45.58.153.24            | The Netherlands | NL   | SHARKTECH                                | 45.58.149.130                         | Yes (Region: US) |
| 18 | [75](config/75.json) | 45.121.48.196           | Taiwan          | TW   | EMGINECONCEPT-01                         | 45.121.48.196                         | Yes (Region: TW) |
| 19 | [76](config/76.json) | 123.58.197.70           | Taiwan          | TW   | UCLOUD INFORMATION TECHNOLOGY HK LIMITED | 123.58.197.70                         | Yes (Region: TW) |
| 20 | [77](config/77.json) | 38.75.136.49            | United States   | US   | AS-GLOBALTELEHOST                        | 38.75.136.49                          | Yes (Region: US) |
| 21 | [78](config/78.json) | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                          | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%201
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcGJOWHlnU3lFRmpTaGdNaDd0V0hY@51.141.101.197:65167#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%203
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%206
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprWWxLR25QUk53Vms0UlFFaTdvcVFz@51.141.100.112:24007#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%207
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpBSzRKMXNSdDJ2M2RMRFVWQzJQNWxq@94.131.12.245:37726#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%2017
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgMjAiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTY3LjE3OS4xMTEuMjM3IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJlOTYxODk0Zi04ZTkwLTQ3MmYtOThkMy0wOTQwMmU0YmU0NTMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTQ5MzUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0Nob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuNzcuMjQ1LjQ3IiwgImFpZCI6ICIwIiwgImhvc3QiOiAibS56b29tLnVzIiwgImlkIjogIjM3MGY4ZGZjLTczYjItNGQxMy1hM2VhLTczMzBmMDMzM2E2OSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvRGlhbG9nIHpvb20iLCAicG9ydCI6ICI1Mjk5MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjViMFx1NTJhMFx1NTc2MUNob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyNiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2029
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUyYTBcdTYyZmZcdTU5MjcgIDMwIiwgImFkZCI6ICIxNDIuMTcxLjIwMi4xMzAiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy44Nzk4MTUzMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyNjUwOTkyNDkxIiwgInRscyI6ICJ0bHMifQ==
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2033
vmess://eyJhZGQiOiAiYWZyaG1zMTZ2LmJlc3R4cmF5LmJ1enoiLCAiYWlkIjogMCwgImhvc3QiOiAiYWZyaG1zMTZ2LmJlc3R4cmF5LmJ1enoiLCAiaWQiOiAiZjU4NGRlMTUtMjAzNC00MTcwLWE3MjMtZjQ4YzJiYWU1ZTBmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9saW5rd3MiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA0NSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDYxIiwgImFkZCI6ICIxMDMuMTU5LjIwNi4zNSIsICJwb3J0IjogIjMxOTQ1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiZTJlNTExYjAtN2RlZi00ZTFiLWQyMzgtNmNiNTM5MWIyZTNmIiwgInNuaSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIn0=
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2062
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjUxNjUyMTA5Lnh5eiIsICJpZCI6ICI1NTU0NWY5ZS1hNTYxLTQ1NGEtOGRjMC04YmMxMTBlNmIxYzkiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJwb3J0IjogMzAwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODM3N1x1NTE3MFx1NTMxN1x1ODM3N1x1NTE3MFx1NzcwMVx1OTYzZlx1NTljNlx1NjVhZlx1NzI3OVx1NGUzOVNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2OSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE3MiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDczIiwgInBvcnQiOiAxMDAwMSwgImlkIjogImRiYTUxYTJlLWE3ODgtNDNiNy05YWM0LTlmN2NjMTI1NWYxNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuNTguMTUzLjI0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgImlkIjogIjQyNDJmOWUwLTZiN2UtNDI1Ny05ZTkzLTdhZDM4MDE1YzQ2YSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMzkyMjU1MzU1IiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4Mzc3XHU1MTcwXHU1MzE3XHU4Mzc3XHU1MTcwXHU3NzAxXHU5NjNmXHU1OWM2XHU2NWFmXHU3Mjc5XHU0ZTM5U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDc0IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDc1IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjYjNcdTUzNTdcdTc3MDFcdTkwZDFcdTVkZGVcdTVlMDJcdTZjYjNcdTUzNTdcdTRlYmZcdTYwNjlcdTc5ZDFcdTYyODBcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggNzYiLCAiYWRkIjogIjEyMy41OC4xOTcuNzAiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNGNhMDE5NmMtMDVlNy00NWViLTkwMzYtNjkyYzIwMWY0NWZiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2077
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2078
```

