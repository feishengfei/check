
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                     | addr                | cn              | cc   | isp                             | ip                                     | chatgpt          |
|---:|:-----------------------|:--------------------|:----------------|:-----|:--------------------------------|:---------------------------------------|:-----------------|
|  0 | [4](config/4.json)     | 52.142.161.9        | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK     | 52.142.161.9                           | Yes (Region: GB) |
|  1 | [6](config/6.json)     | 112.28.208.10       | Japan           | JP   | BGPNET Global ASN               | 134.122.133.144                        | Yes (Region: SG) |
|  2 | [7](config/7.json)     | 38.75.136.49        | United States   | US   | AS-GLOBALTELEHOST               | 38.75.136.49                           | Yes (Region: US) |
|  3 | [11](config/11.json)   | 64.176.58.15        | Japan           | JP   | AS-CHOOPA                       | 2401:c080:3800:3dec:5400:4ff:feaa:9fd8 | Yes (Region: JP) |
|  4 | [12](config/12.json)   | kr4.36routes.online | South Korea     | KR   | AMAZON-02                       | 52.78.234.241                          | Yes (Region: KR) |
|  5 | [13](config/13.json)   | 45.159.249.231      | Finland         | FI   | Stark Industries Solutions Ltd  | 45.159.249.231                         | Yes (Region: FI) |
|  6 | [15](config/15.json)   | 198.2.202.81        | China           | CN   | PEG-SV                          | 142.4.102.244                          | Yes (Region: US) |
|  7 | [20](config/20.json)   | 64.176.39.31        | Japan           | JP   | AS-CHOOPA                       | 2401:c080:3800:3dba:5400:4ff:feaa:9fd7 | Yes (Region: JP) |
|  8 | [23](config/23.json)   | 64.176.37.216       | Japan           | JP   | AS-CHOOPA                       | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
|  9 | [28](config/28.json)   | 139.162.125.97      | Japan           | JP   | Akamai Connected Cloud          | 2400:8902::f03c:94ff:fee2:6e90         | Yes (Region: JP) |
| 10 | [37](config/37.json)   | 38.91.107.37        | United States   | US   | AS-GLOBALTELEHOST               | 38.91.107.37                           | Yes (Region: US) |
| 11 | [41](config/41.json)   | 64.176.58.7         | Japan           | JP   | AS-CHOOPA                       | 2401:c080:3800:3dbf:5400:4ff:feaa:9fd4 | Yes (Region: JP) |
| 12 | [47](config/47.json)   | 8.219.240.120       | Singapore       | SG   | Alibaba US Technology Co., Ltd. | 8.219.240.120                          | Yes (Region: SG) |
| 13 | [66](config/66.json)   | 45.58.153.24        | The Netherlands | NL   | SHARKTECH                       | 45.58.149.130                          | Yes (Region: US) |
| 14 | [74](config/74.json)   | 38.91.107.37        | United States   | US   | AS-GLOBALTELEHOST               | 38.91.107.37                           | Yes (Region: US) |
| 15 | [90](config/90.json)   | 45.121.48.196       | Taiwan          | TW   | EMGINECONCEPT-01                | 45.121.48.196                          | Yes (Region: TW) |
| 16 | [91](config/91.json)   | 45.58.145.200       | The Netherlands | NL   | SHARKTECH                       | 45.58.145.194                          | Yes (Region: US) |
| 17 | [93](config/93.json)   | 167.179.111.237     | Japan           | JP   | AS-CHOOPA                       | 2001:19f0:7001:244:5400:4ff:feab:d9e2  | Yes (Region: JP) |
| 18 | [105](config/105.json) | 113.20.28.102       | Indonesia       | ID   | ARDH GLOBAL INDONESIA, PT       | 113.20.28.102                          | Yes (Region: ID) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%204
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggNiIsICJhZGQiOiAiMTEyLjI4LjIwOC4xMCIsICJwb3J0IjogIjQ2NjAyIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%207
vmess://eyJhZGQiOiAiNjQuMTc2LjU4LjE1IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJhZGNiZTE2MC0zMDEwLTQ4M2QtYjQzOC1kNjA1N2Y0NjViMWQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQ2MTU0IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDExIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk3ZTlcdTU2ZmRcdTk5OTZcdTVjMTRBbWF6b25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTIiLCAiYWRkIjogImtyNC4zNnJvdXRlcy5vbmxpbmUiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI4ZWZjN2U5ZC03MTZlLTQ0MGMtODU3My01YzUyZThjNTAzZTMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2013
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDE1IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNjQuMTc2LjM5LjMxIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YSAyMCIsICJwb3J0IjogNTYyNjIsICJpZCI6ICI1OTBmMjc0NC1lOWQxLTRmMmMtYTM4NC1kMzViNzM2YmNhNDEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMjMiLCAicG9ydCI6IDQ1OTMwLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTM5LjE2Mi4xMjUuOTciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjXHU0ZTFjXHU0ZWFjXHU5MGZkXHU1NGMxXHU1ZGRkXHU1MzNhTGlub2RlXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDI4IiwgInBvcnQiOiA0OTQ5OSwgImlkIjogIjNjZTFkMmUzLTBlMWItNGIwMC05MjFiLWZjYzBmOGFiZTFmNiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2037
vmess://eyJhZGQiOiAiNjQuMTc2LjU4LjciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhIDQxIiwgInBvcnQiOiAxNDQzMSwgImlkIjogImZmNjgxYmE2LTU1ZjUtNGU3OS04ZjQwLWFkNmJiZGYxNDA0NCIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMmRcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgNDciLCAiYWRkIjogIjguMjE5LjI0MC4xMjAiLCAicG9ydCI6ICIzMjk2OSIsICJpZCI6ICI5NTI0OTAyMC1mYmI3LTQ1OTItZWZjZS02YWQzOTU0YzNmYWQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNjYiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2074
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDkwIiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiMGVkMzU2MjktOTE5YS00ODkxLWJhMGYtMTNjZDE5OGY4NjNiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOTEiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNTU1NDVmOWUtYTU2MS00NTRhLThkYzAtOGJjMTEwZTZiMWM5IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTE2NTIxMDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTY3LjE3OS4xMTEuMjM3IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0Nob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA5MyIsICJwb3J0IjogMTQ5MzUsICJpZCI6ICJlOTYxODk0Zi04ZTkwLTQ3MmYtOThkMy0wOTQwMmU0YmU0NTMiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMzguNTQuODIuNTQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MzRlXHU3NmRiXHU5ODdmQ29nZW50XHU5MDFhXHU0ZmUxXHU1MTZjXHU1M2Y4IDEwMSIsICJwb3J0IjogNDE2MDQsICJpZCI6ICI1NGRlNTBlNS01ZTRiLTQ0M2YtZDliOC05ZTllMGVlZTg2NWMiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTEzLjIwLjI4LjEwMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDEwNSIsICJwb3J0IjogMjIxODgsICJpZCI6ICIwMDY3N2ViNC05MWMyLTQxZjEtZTc5MC05NjNiOWEwOTNmZDUiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

