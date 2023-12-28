
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                     | addr            | cn             | cc   | isp                            | ip                                     | chatgpt          |
|---:|:-----------------------|:----------------|:---------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)     | 139.162.125.97  | Japan          | JP   | Akamai Connected Cloud         | 2400:8902::f03c:94ff:fee2:6e90         | Yes (Region: JP) |
|  1 | [7](config/7.json)     | 52.142.161.9    | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  2 | [8](config/8.json)     | 52.142.146.57   | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
|  3 | [9](config/9.json)     | 112.28.208.10   | Japan          | JP   | BGPNET Global ASN              | 134.122.133.144                        | Yes (Region: SG) |
|  4 | [11](config/11.json)   | 45.159.249.231  | Finland        | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  5 | [14](config/14.json)   | 154.90.39.63    | Malaysia       | MY   | Kaopu Cloud HK Limited         | 154.90.39.63                           | Yes (Region: MY) |
|  6 | [16](config/16.json)   | 217.160.45.31   | Germany        | DE   | IONOS SE                       | 217.160.45.31                          | Yes (Region: DE) |
|  7 | [19](config/19.json)   | 198.2.202.81    | China          | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
|  8 | [21](config/21.json)   | 38.91.107.37    | United States  | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  9 | [22](config/22.json)   | 38.91.107.37    | United States  | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 10 | [35](config/35.json)   | 139.180.202.213 | Japan          | JP   | AS-CHOOPA                      | 2001:19f0:7001:2966:5400:4ff:feaa:e764 | Yes (Region: JP) |
| 11 | [53](config/53.json)   | 156.235.89.194  | United States  | US   | Evoxt Enterprise               | 2400:8d60:2::1:dd58:d904               | Yes (Region: US) |
| 12 | [69](config/69.json)   | 108.165.113.99  | United States  | US   | US-CLOUDNIUM-01                | 108.165.113.99                         | Yes (Region: US) |
| 13 | [87](config/87.json)   | 64.176.59.68    | Japan          | JP   | AS-CHOOPA                      | 2401:c080:3800:3d77:5400:4ff:feaa:a946 | Yes (Region: JP) |
| 14 | [88](config/88.json)   | 113.20.28.102   | Indonesia      | ID   | ARDH GLOBAL INDONESIA, PT      | 113.20.28.102                          | Yes (Region: ID) |
| 15 | [97](config/97.json)   | 103.159.206.35  | Taiwan         | TW   | EMGINECONCEPT-01               | 103.159.206.35                         | Yes (Region: TW) |
| 16 | [101](config/101.json) | 207.148.26.144  | United States  | US   | AS-CHOOPA                      | 2001:19f0:0:4b1e:5400:4ff:fea8:ce07    | Yes (Region: US) |
| 17 | [102](config/102.json) | 167.179.111.237 | Japan          | JP   | AS-CHOOPA                      | 2001:19f0:7001:244:5400:4ff:feab:d9e2  | Yes (Region: JP) |
| 18 | [104](config/104.json) | 45.121.48.172   | Taiwan         | TW   | EMGINECONCEPT-01               | 45.121.48.172                          | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNcdTkwZmRcdTU0YzFcdTVkZGRcdTUzM2FMaW5vZGVcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTM5LjE2Mi4xMjUuOTciLCAicG9ydCI6ICI0OTQ5OSIsICJpZCI6ICIzY2UxZDJlMy0wZTFiLTRiMDAtOTIxYi1mY2MwZjhhYmUxZjYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJrcnl4LjY1MTU2OC54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmYzRcdTdmNTdcdTY1YWYgIDUiLCAiYWRkIjogIjkxLjEwNy4xNzIuMTI4IiwgInBvcnQiOiAiMzM1MCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMmJmOTAwYWMtOTA5YS00NjEwLWRjMTgtODZhM2ExMzZiMjg2IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%207
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%208
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggOSIsICJhZGQiOiAiMTEyLjI4LjIwOC4xMCIsICJwb3J0IjogIjQ2NjAyIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2011
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTcyNzlcdTUyMmJcdTg4NGNcdTY1M2ZcdTUzM2EgMTQiLCAiYWRkIjogIjE1NC45MC4zOS42MyIsICJwb3J0IjogIjQ1MzQzIiwgImlkIjogIjA4YWE4NDk5LWQ2MTYtNGZmMS1kNmFiLWNlMGM1MjI4MjRhYSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIjM4LjU0LjM2Ljc0IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAxNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDE5IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2021
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2022
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMzUiLCAiYWRkIjogIjEzOS4xODAuMjAyLjIxMyIsICJwb3J0IjogIjQyNDM0IiwgImlkIjogImQ5YTdjNTI5LWY5OGItNDI5Yi1lYjI2LWM5MDk3OWM5MTBhMyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIzNS44OS4xOTQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2Q2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUzIiwgInBvcnQiOiAxMDAwMSwgImlkIjogIjY1OGM2NmRkLTI3MmYtNDQ0YS1lZDMwLWY2Y2E2YmRlNzM1NyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDY5IiwgImFkZCI6ICIxMDguMTY1LjExMy45OSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJlZjIyZmFkMy02NTJhLTQ4ZmMtZTgwYS00NmZhYTNhNmE3ODciLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjU5LjY4IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1ODIxYWMyMS04ZTNmLTRjOGItODMyZC1hNTUxOTBjOTQ0ZTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjU5MzUwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDg3IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTEzLjIwLjI4LjEwMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDg4IiwgInBvcnQiOiAyMjE4OCwgImlkIjogIjAwNjc3ZWI0LTkxYzItNDFmMS1lNzkwLTk2M2I5YTA5M2ZkNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDk3IiwgImFkZCI6ICIxMDMuMTU5LjIwNi4zNSIsICJwb3J0IjogIjMxOTQ1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiZTJlNTExYjAtN2RlZi00ZTFiLWQyMzgtNmNiNTM5MWIyZTNmIiwgInNuaSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIn0=
vmess://eyJhZGQiOiAiMjA3LjE0OC4yNi4xNDQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU2NWIwXHU2Y2ZkXHU4OTdmXHU1ZGRlXHU3NmFlXHU2NWFmXHU1MzYxXHU3Mjc5XHU3ZWY0VnVsdHJcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAxIiwgInBvcnQiOiAyMjU4OSwgImlkIjogIjEwODc3NDQ2LWY5YWEtNGI4NC1lYzQzLWE2ODg1MjE4MTVkZCIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAyIiwgImFkZCI6ICIxNjcuMTc5LjExMS4yMzciLCAicG9ydCI6ICIxNDkzNSIsICJpZCI6ICJlOTYxODk0Zi04ZTkwLTQ3MmYtOThkMy0wOTQwMmU0YmU0NTMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDEwNCIsICJhZGQiOiAiNDUuMTIxLjQ4LjE3MiIsICJwb3J0IjogIjEwMDAxIiwgImlkIjogImRiYTUxYTJlLWE3ODgtNDNiNy05YWM0LTlmN2NjMTI1NWYxNSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

