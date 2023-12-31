
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn              | cc   | isp                              | ip                                     | chatgpt          |
|---:|:---------------------|:-----------------|:----------------|:-----|:---------------------------------|:---------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 51.141.101.197   | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK      | 51.141.101.197                         | Yes (Region: GB) |
|  1 | [4](config/4.json)   | 52.142.161.9     | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK      | 52.142.161.9                           | Yes (Region: GB) |
|  2 | [6](config/6.json)   | 217.160.45.31    | Germany         | DE   | IONOS SE                         | 217.160.45.31                          | Yes (Region: DE) |
|  3 | [7](config/7.json)   | 38.91.107.37     | United States   | US   | AS-GLOBALTELEHOST                | 38.91.107.37                           | Yes (Region: US) |
|  4 | [9](config/9.json)   | 45.8.146.35      | United States   | US   | Stark Industries Solutions Ltd   | 45.8.146.35                            | Yes (Region: US) |
|  5 | [11](config/11.json) | 52.142.146.57    | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK      | 52.142.146.57                          | Yes (Region: GB) |
|  6 | [12](config/12.json) | 51.141.100.85    | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK      | 51.141.100.85                          | Yes (Region: GB) |
|  7 | [19](config/19.json) | 45.159.249.231   | Finland         | FI   | Stark Industries Solutions Ltd   | 45.159.249.231                         | Yes (Region: FI) |
|  8 | [25](config/25.json) | 94.131.12.245    | Switzerland     | CH   | Stark Industries Solutions Ltd   | 94.131.12.245                          | Yes (Region: CH) |
|  9 | [27](config/27.json) | 142.171.202.130  | United States   | US   | MULTA-ASN1                       | 2607:f130:109:0:d6ae:52ff:febb:b11b    | Yes (Region: US) |
| 10 | [32](config/32.json) | 198.2.200.37     | United States   | US   | PEG-SV                           | 142.4.98.185                           | Yes (Region: US) |
| 11 | [34](config/34.json) | usc.kalaa.online | United States   | US   | AMAZON-02                        | 18.236.105.133                         | Yes (Region: US) |
| 12 | [43](config/43.json) | cm.awslcn.info   | Malaysia        | MY   | TM TECHNOLOGY SERVICES SDN. BHD. | 58.26.140.91                           | Yes (Region: US) |
| 13 | [47](config/47.json) | 45.8.147.80      | Sweden          | SE   | Stark Industries Solutions Ltd   | 45.8.147.80                            | Yes (Region: SE) |
| 14 | [53](config/53.json) | 38.91.107.37     | United States   | US   | AS-GLOBALTELEHOST                | 38.91.107.37                           | Yes (Region: US) |
| 15 | [65](config/65.json) | 45.58.145.200    | The Netherlands | NL   | SHARKTECH                        | 45.58.145.194                          | Yes (Region: US) |
| 16 | [68](config/68.json) | 45.77.246.27     | Singapore       | SG   | AS-CHOOPA                        | 45.77.246.27                           | Yes (Region: SG) |
| 17 | [76](config/76.json) | 64.176.47.200    | Japan           | JP   | AS-CHOOPA                        | 2401:c080:3800:3ba0:5400:4ff:feaa:a942 | Yes (Region: JP) |
| 18 | [80](config/80.json) | 38.91.107.37     | United States   | US   | AS-GLOBALTELEHOST                | 38.91.107.37                           | Yes (Region: US) |
| 19 | [83](config/83.json) | 38.75.136.49     | United States   | US   | AS-GLOBALTELEHOST                | 38.75.136.49                           | Yes (Region: US) |
| 20 | [86](config/86.json) | 45.121.48.196    | Taiwan          | TW   | EMGINECONCEPT-01                 | 45.121.48.196                          | Yes (Region: TW) |
| 21 | [94](config/94.json) | 139.162.125.97   | Japan           | JP   | Akamai Connected Cloud           | 2400:8902::f03c:94ff:fee2:6e90         | Yes (Region: JP) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcGJOWHlnU3lFRmpTaGdNaDd0V0hY@51.141.101.197:65167#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%204
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%207
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVMUVZUlFwVThyTEdSS3ZETWZSNkZ2@45.8.146.35:47413#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%209
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2011
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOSzRLVHBINEdiV3pua0p5d1Y3Vm1B@51.141.100.85:28521#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%2012
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2019
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpBSzRKMXNSdDJ2M2RMRFVWQzJQNWxq@94.131.12.245:37726#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%2025
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUyYTBcdTYyZmZcdTU5MjcgIDI3IiwgImFkZCI6ICIxNDIuMTcxLjIwMi4xMzAiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy44Nzk4MTUzMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyNjUwOTkyNDkxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgMzIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTRmYzRcdTUyZDJcdTUxODhcdTVkZGVcdTZjZTJcdTcyNzlcdTUxNzBBbWF6b25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMzQiLCAiYWRkIjogInVzYy5rYWxhYS5vbmxpbmUiLCAicG9ydCI6IDgwLCAiaWQiOiAiMWM1NDZlNDAtM2QyMy00OGQwLTk4ZTYtYzhjODFiMWYzNTAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ1c2Mua2FsYWEub25saW5lIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggNDMiLCAiYWRkIjogImNtLmF3c2xjbi5pbmZvIiwgInBvcnQiOiAiMjUyNTgiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjkzZWM3MjYxLTFjOTItNDE0OS04NDhhLTI2YjZmYjlmYzRjZSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiY20uYXdzbGNuLmluZm8iLCAidGxzIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2047
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2053
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjUxNjUyMTA5Lnh5eiIsICJpZCI6ICI1NTU0NWY5ZS1hNTYxLTQ1NGEtOGRjMC04YmMxMTBlNmIxYzkiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJwb3J0IjogMzAwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODM3N1x1NTE3MFx1NTMxN1x1ODM3N1x1NTE3MFx1NzcwMVx1OTYzZlx1NTljNlx1NjVhZlx1NzI3OVx1NGUzOVNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2NSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuNzcuMjQ2LjI3IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIm1lZGlhLWV4cDEubGljZG4uY29tIiwgImlkIjogImQxNTI4Y2JiLWZhMDYtNDY1OS1jYzI1LWM0MDM4N2U3MzQ3ZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvYm9vbnZwbnpvbmUiLCAicG9ydCI6ICIyODQzMyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjViMFx1NTJhMFx1NTc2MUNob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2OCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNzYiLCAiYWRkIjogIjY0LjE3Ni40Ny4yMDAiLCAicG9ydCI6ICIyOTQxNCIsICJpZCI6ICI0ZDVlOGFhMi0wNjQxLTQzMjMtZTkyYy0yYzA2MWNkYzhlMzQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2080
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2083
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDg2IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNcdTkwZmRcdTU0YzFcdTVkZGRcdTUzM2FMaW5vZGVcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOTQiLCAiYWRkIjogIjEzOS4xNjIuMTI1Ljk3IiwgInBvcnQiOiAiNDk0OTkiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjNjZTFkMmUzLTBlMWItNGIwMC05MjFiLWZjYzBmOGFiZTFmNiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL3BhdGgvMTcwMjM5MjI1NTM1NSIsICJob3N0IjogInd3dy43NzkzNTcwNy54eXoiLCAidGxzIjogIiJ9
```

