
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                                      | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:-----------------------------------------|:---------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 139.180.202.213 | Japan           | JP   | AS-CHOOPA                                | 2001:19f0:7001:2966:5400:4ff:feaa:e764 | Yes (Region: JP) |
|  1 | [3](config/3.json)   | 52.142.146.57   | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 52.142.146.57                          | Yes (Region: GB) |
|  2 | [4](config/4.json)   | 45.87.153.246   |                 |      |                                          | 45.87.153.246                          | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 38.75.136.49    | United States   | US   | AS-GLOBALTELEHOST                        | 38.75.136.49                           | Yes (Region: US) |
|  4 | [8](config/8.json)   | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                           | Yes (Region: US) |
|  5 | [10](config/10.json) | 132.145.132.227 |                 |      |                                          | 132.145.132.227                        | Yes (Region: US) |
|  6 | [12](config/12.json) | 51.141.101.197  |                 |      |                                          | 51.141.101.197                         | Yes (Region: GB) |
|  7 | [15](config/15.json) | 45.159.249.231  | Finland         | FI   | Stark Industries Solutions Ltd           | 45.159.249.231                         | Yes (Region: FI) |
|  8 | [16](config/16.json) | 45.8.147.80     | Sweden          | SE   | Stark Industries Solutions Ltd           | 45.8.147.80                            | Yes (Region: SE) |
|  9 | [20](config/20.json) | 51.141.100.112  | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK              | 51.141.100.112                         | Yes (Region: GB) |
| 10 | [31](config/31.json) | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                           | Yes (Region: US) |
| 11 | [51](config/51.json) | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST                        | 38.91.107.37                           | Yes (Region: US) |
| 12 | [61](config/61.json) | 45.58.153.24    | The Netherlands | NL   | SHARKTECH                                | 45.58.149.130                          | Yes (Region: US) |
| 13 | [62](config/62.json) | 154.90.39.63    | Malaysia        | MY   | Kaopu Cloud HK Limited                   | 154.90.39.63                           | Yes (Region: MY) |
| 14 | [65](config/65.json) | 38.54.82.54     | Thailand        | TH   | Kaopu Cloud HK Limited                   | 38.54.82.54                            | Yes (Region: TH) |
| 15 | [74](config/74.json) | 123.58.197.70   | Taiwan          | TW   | UCLOUD INFORMATION TECHNOLOGY HK LIMITED | 123.58.197.70                          | Yes (Region: TW) |
| 16 | [75](config/75.json) | 168.235.72.221  | United States   | US   | RAMNODE                                  | 2604:180:f4::1b1                       | Yes (Region: US) |
| 17 | [80](config/80.json) | 64.176.37.216   | Japan           | JP   | AS-CHOOPA                                | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiMTM5LjE4MC4yMDIuMjEzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0Nob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxIiwgInBvcnQiOiA0MjQzNCwgImlkIjogImQ5YTdjNTI5LWY5OGItNDI5Yi1lYjI2LWM5MDk3OWM5MTBhMyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%204
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%207
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%208
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTVmMTdcdTU0MDlcdTVjM2NcdTRlOWFcdTVkZGVcdTk2M2ZcdTRlYzBcdTY3MmNPcmFjbGVcdTRlOTFcdThiYTFcdTdiOTdcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjEzMi4xNDUuMTMyLjIyNyIsICJwb3J0IjogIjM3MTIxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5Mzg0NWI1MC0yNmY2LTQyMDMtZjVhZC00ZDIzMWQ0ZThmNDUiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcGJOWHlnU3lFRmpTaGdNaDd0V0hY@51.141.101.197:65167#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%2012
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2015
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2016
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprWWxLR25QUk53Vms0UlFFaTdvcVFz@51.141.100.112:24007#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E5%A8%81%E5%B0%94%E5%A3%AB%E5%8A%A0%E7%9A%84%E5%A4%ABMicrosoft%E5%85%AC%E5%8F%B8%2020
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2031
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2051
vmess://eyJhZGQiOiAiNDUuNTguMTUzLjI0IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODM3N1x1NTE3MFx1NTMxN1x1ODM3N1x1NTE3MFx1NzcwMVx1OTYzZlx1NTljNlx1NjVhZlx1NzI3OVx1NGUzOVNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2MSIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogInd3dy43NzkzNTcwNy54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyMzkyMjU1MzU1IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTcyNzlcdTUyMmJcdTg4NGNcdTY1M2ZcdTUzM2EgNjIiLCAiYWRkIjogIjE1NC45MC4zOS42MyIsICJwb3J0IjogIjQ1MzQzIiwgImlkIjogIjA4YWE4NDk5LWQ2MTYtNGZmMS1kNmFiLWNlMGM1MjI4MjRhYSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggNjUiLCAiYWRkIjogIjM4LjU0LjgyLjU0IiwgInBvcnQiOiAiNDE2MDQiLCAiaWQiOiAiNTRkZTUwZTUtNWU0Yi00NDNmLWQ5YjgtOWU5ZTBlZWU4NjVjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiMzguNTQuODIuNTQiLCAicGF0aCI6ICIvdnBuZ2lhbmdvbi5jb20iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTIzLjU4LjE5Ny43MCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjYjNcdTUzNTdcdTc3MDFcdTkwZDFcdTVkZGVcdTVlMDJcdTZjYjNcdTUzNTdcdTRlYmZcdTYwNjlcdTc5ZDFcdTYyODBcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggNzQiLCAicG9ydCI6IDQ0MywgImlkIjogIjRjYTAxOTZjLTA1ZTctNDVlYi05MDM2LTY5MmMyMDFmNDVmYiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZSYW1Ob2RlXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDc1IiwgImFkZCI6ICIxNjguMjM1LjcyLjIyMSIsICJwb3J0IjogIjE1NTUxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI2OTUxMDYzMy02YWNiLTQyOTEtYTk4ZS0wY2RjYzliZDVjNTEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgODAiLCAiYWRkIjogIjY0LjE3Ni4zNy4yMTYiLCAicG9ydCI6ICI0NTkzMCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvdm1lc3MiLCAiaG9zdCI6ICI2NC4xNzYuMzcuMjE2IiwgInRscyI6ICIifQ==
```

