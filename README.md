
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn             | cc   | isp                                      | ip                                     | chatgpt          |
|---:|:---------------------|:---------------|:---------------|:-----|:-----------------------------------------|:---------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 51.141.101.197 |                |      |                                          | 51.141.101.197                         | Yes (Region: GB) |
|  1 | [4](config/4.json)   | 52.142.161.9   | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 52.142.161.9                           | Yes (Region: GB) |
|  2 | [5](config/5.json)   | 45.87.153.246  |                |      |                                          | 45.87.153.246                          | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 52.142.146.57  |                |      |                                          | 52.142.146.57                          | Yes (Region: GB) |
|  4 | [8](config/8.json)   | 51.141.100.112 | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 51.141.100.112                         | Yes (Region: GB) |
|  5 | [11](config/11.json) | 45.159.249.231 |                |      |                                          | 45.159.249.231                         | Yes (Region: FI) |
|  6 | [16](config/16.json) | 38.91.107.37   |                |      |                                          | 38.91.107.37                           | Yes (Region: US) |
|  7 | [18](config/18.json) | 45.8.147.80    | Sweden         | SE   | Stark Industries Solutions Ltd           | 45.8.147.80                            | Yes (Region: SE) |
|  8 | [20](config/20.json) | 38.75.136.49   | United States  | US   | AS-GLOBALTELEHOST                        | 38.75.136.49                           | Yes (Region: US) |
|  9 | [30](config/30.json) | 198.2.200.37   | United States  | US   | PEG-SV                                   | 142.4.98.185                           | Yes (Region: US) |
| 10 | [40](config/40.json) | 38.54.86.217   | Philippines    | PH   | Kaopu Cloud HK Limited                   | 38.54.86.217                           | Yes (Region: PH) |
| 11 | [48](config/48.json) | 38.54.82.54    | Thailand       | TH   | Kaopu Cloud HK Limited                   | 38.54.82.54                            | Yes (Region: TH) |
| 12 | [55](config/55.json) | 64.176.42.137  | Japan          | JP   | AS-CHOOPA                                | 2401:c080:3800:3c78:5400:4ff:feaa:a94b | Yes (Region: JP) |
| 13 | [56](config/56.json) | 38.91.107.37   | United States  | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                           | Yes (Region: US) |
| 14 | [68](config/68.json) | 45.121.48.196  | Taiwan         | TW   | EMGINECONCEPT-01                         | 45.121.48.196                          | Yes (Region: TW) |
| 15 | [72](config/72.json) | 45.121.48.172  | Taiwan         | TW   | EMGINECONCEPT-01                         | 45.121.48.172                          | Yes (Region: TW) |
| 16 | [73](config/73.json) | 64.176.39.31   | Japan          | JP   | AS-CHOOPA                                | 2401:c080:3800:3dba:5400:4ff:feaa:9fd7 | Yes (Region: JP) |
| 17 | [74](config/74.json) | 123.58.197.70  | Taiwan         | TW   | UCLOUD INFORMATION TECHNOLOGY HK LIMITED | 123.58.197.70                          | Yes (Region: TW) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcGJOWHlnU3lFRmpTaGdNaDd0V0hY@51.141.101.197:65167#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%204
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%205
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%207
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprWWxLR25QUk53Vms0UlFFaTdvcVFz@51.141.100.112:24007#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%208
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2011
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2016
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2018
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2020
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgMzAiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggNDAiLCAiYWRkIjogIjM4LjU0Ljg2LjIxNyIsICJwb3J0IjogIjU2NTAyIiwgImlkIjogImQyMDc0N2FkLWU2ODktNDExMS1hNDZlLWQ1Y2YyMWZmNDgyNyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggNDgiLCAiYWRkIjogIjM4LjU0LjgyLjU0IiwgInBvcnQiOiAiNDE2MDQiLCAiaWQiOiAiNTRkZTUwZTUtNWU0Yi00NDNmLWQ5YjgtOWU5ZTBlZWU4NjVjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiMzguNTQuODIuNTQiLCAicGF0aCI6ICIvdnBuZ2lhbmdvbi5jb20iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjQyLjEzNyIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZjU3NGIyMzctM2ViZi00MDVjLWQ1NDAtNTQxNTMwZmU1ZWQ3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDIwODg2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNTUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2056
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDY4IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDcyIiwgImFkZCI6ICI0NS4xMjEuNDguMTcyIiwgInBvcnQiOiAiMTAwMDEiLCAidHlwZSI6ICJub25lIiwgImlkIjogImRiYTUxYTJlLWE3ODgtNDNiNy05YWM0LTlmN2NjMTI1NWYxNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgNzMiLCAiYWRkIjogIjY0LjE3Ni4zOS4zMSIsICJwb3J0IjogIjU2MjYyIiwgImlkIjogIjU5MGYyNzQ0LWU5ZDEtNGYyYy1hMzg0LWQzNWI3MzZiY2E0MSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTIzLjU4LjE5Ny43MCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjYjNcdTUzNTdcdTc3MDFcdTkwZDFcdTVkZGVcdTVlMDJcdTZjYjNcdTUzNTdcdTRlYmZcdTYwNjlcdTc5ZDFcdTYyODBcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggNzQiLCAicG9ydCI6IDQ0MywgImlkIjogIjRjYTAxOTZjLTA1ZTctNDVlYi05MDM2LTY5MmMyMDFmNDVmYiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
```

