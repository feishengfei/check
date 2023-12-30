
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:---------------------|:------------------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 51.141.100.112          | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 51.141.100.112                         | Yes (Region: GB) |
|  1 | [3](config/3.json)   | 51.141.100.85           | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 51.141.100.85                          | Yes (Region: GB) |
|  2 | [4](config/4.json)   | 45.87.153.246           | The Netherlands | NL   | Stark Industries Solutions Ltd | 45.87.153.246                          | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 52.142.146.57           | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
|  4 | [7](config/7.json)   | 52.142.161.9            | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  5 | [8](config/8.json)   | 51.141.127.238          | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 51.141.127.238                         | Yes (Region: GB) |
|  6 | [9](config/9.json)   | 217.160.45.31           | Germany         | DE   | IONOS SE                       | 217.160.45.31                          | Yes (Region: DE) |
|  7 | [13](config/13.json) | 45.8.146.35             | United States   | US   | Stark Industries Solutions Ltd | 45.8.146.35                            | Yes (Region: US) |
|  8 | [14](config/14.json) | 45.159.249.231          | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  9 | [16](config/16.json) | 94.131.12.245           | Switzerland     | CH   | Stark Industries Solutions Ltd | 94.131.12.245                          | Yes (Region: CH) |
| 10 | [18](config/18.json) | 45.8.147.80             | Sweden          | SE   | Stark Industries Solutions Ltd | 45.8.147.80                            | Yes (Region: SE) |
| 11 | [19](config/19.json) | 198.2.202.81            | China           | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
| 12 | [35](config/35.json) | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 13 | [53](config/53.json) | 45.121.48.196           | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196                          | Yes (Region: TW) |
| 14 | [54](config/54.json) | afrhms16v.bestxray.buzz | United Kingdom  | GB   | Akamai Connected Cloud         | 2a01:7e00::f03c:94ff:febc:f335         | Yes (Region: GB) |
| 15 | [75](config/75.json) | 64.176.37.216           | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
| 16 | [77](config/77.json) | 45.58.145.200           | The Netherlands | NL   | SHARKTECH                      | 45.58.145.194                          | Yes (Region: US) |
| 17 | [78](config/78.json) | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 18 | [86](config/86.json) | 103.159.206.35          | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35                         | Yes (Region: TW) |
| 19 | [89](config/89.json) | 142.171.202.130         | United States   | US   | MULTA-ASN1                     | 2607:f130:109:0:d6ae:52ff:febb:b11b    | Yes (Region: US) |
| 20 | [95](config/95.json) | 45.121.48.172           | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.172                          | Yes (Region: TW) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprWWxLR25QUk53Vms0UlFFaTdvcVFz@51.141.100.112:24007#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%202
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOSzRLVHBINEdiV3pua0p5d1Y3Vm1B@51.141.100.85:28521#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%204
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%205
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%207
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpNSzJRbng2Nnprd3BRUXo4eVRYVkNG@51.141.127.238:32413#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%208
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpVMUVZUlFwVThyTEdSS3ZETWZSNkZ2@45.8.146.35:47413#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2013
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2014
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpBSzRKMXNSdDJ2M2RMRFVWQzJQNWxq@94.131.12.245:37726#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%2016
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2018
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDE5IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2035
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDUzIiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDU0IiwgImFkZCI6ICJhZnJobXMxNnYuYmVzdHhyYXkuYnV6eiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJmNTg0ZGUxNS0yMDM0LTQxNzAtYTcyMy1mNDhjMmJhZTVlMGYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi9saW5rd3MiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNzUiLCAiYWRkIjogIjY0LjE3Ni4zNy4yMTYiLCAicG9ydCI6ICI0NTkzMCIsICJpZCI6ICJiMjkzMGIwZC0wMmI0LTQ1ZGMtODAyNS1hM2MxOTg3OWQ0YWIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI2NC4xNzYuMzcuMjE2IiwgInBhdGgiOiAiL3ZtZXNzIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjUxNjUyMTA5Lnh5eiIsICJpZCI6ICI1NTU0NWY5ZS1hNTYxLTQ1NGEtOGRjMC04YmMxMTBlNmIxYzkiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJwb3J0IjogMzAwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODM3N1x1NTE3MFx1NTMxN1x1ODM3N1x1NTE3MFx1NzcwMVx1OTYzZlx1NTljNlx1NjVhZlx1NzI3OVx1NGUzOVNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA3NyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2078
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDg2IiwgImFkZCI6ICIxMDMuMTU5LjIwNi4zNSIsICJwb3J0IjogIjMxOTQ1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiZTJlNTExYjAtN2RlZi00ZTFiLWQyMzgtNmNiNTM5MWIyZTNmIiwgInNuaSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUyYTBcdTYyZmZcdTU5MjcgIDg5IiwgImFkZCI6ICIxNDIuMTcxLjIwMi4xMzAiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy44Nzk4MTUzMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyNjUwOTkyNDkxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE3MiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDk1IiwgInBvcnQiOiAxMDAwMSwgImlkIjogImRiYTUxYTJlLWE3ODgtNDNiNy05YWM0LTlmN2NjMTI1NWYxNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
```

