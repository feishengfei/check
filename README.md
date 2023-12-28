
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                     | addr                    | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:-----------------------|:------------------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [3](config/3.json)     | 172.233.188.217         | United States   | US   | Akamai Connected Cloud         | 2a01:7e04::f03c:94ff:fe28:322a         | Yes (Region: US) |
|  1 | [6](config/6.json)     | 198.2.202.81            | China           | CN   | PEG-SV                         | 142.4.102.244                          | Yes (Region: US) |
|  2 | [7](config/7.json)     | 52.142.161.9            | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                           | Yes (Region: GB) |
|  3 | [11](config/11.json)   | 45.159.249.231          | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  4 | [15](config/15.json)   | 94.131.12.245           | Switzerland     | CH   | Stark Industries Solutions Ltd | 94.131.12.245                          | Yes (Region: CH) |
|  5 | [18](config/18.json)   | 64.176.42.137           | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3c78:5400:4ff:feaa:a94b | Yes (Region: JP) |
|  6 | [38](config/38.json)   | us2.awslcn.info         | United States   | US   | DIGITALOCEAN-ASN               | 159.223.119.235                        | Yes (Region: US) |
|  7 | [41](config/41.json)   | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
|  8 | [49](config/49.json)   | cm1.awslcn.info         | Australia       | AU   | AS-CHOOPA                      | 149.28.177.17                          | Yes (Region: US) |
|  9 | [50](config/50.json)   | 38.75.136.49            | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49                           | Yes (Region: US) |
| 10 | [57](config/57.json)   | afrhms16v.bestxray.buzz | United Kingdom  | GB   | Akamai Connected Cloud         | 2a01:7e00::f03c:94ff:febc:f335         | Yes (Region: GB) |
| 11 | [78](config/78.json)   | 45.58.145.200           | The Netherlands | NL   | SHARKTECH                      | 45.58.145.194                          | Yes (Region: US) |
| 12 | [79](config/79.json)   | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 13 | [88](config/88.json)   | 38.91.107.37            | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                           | Yes (Region: US) |
| 14 | [94](config/94.json)   | 45.121.48.172           | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.172                          | Yes (Region: TW) |
| 15 | [103](config/103.json) | 45.121.48.196           | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196                          | Yes (Region: TW) |
| 16 | [105](config/105.json) | 103.159.206.35          | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35                         | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRBa2FtYWlcdTc5ZDFcdTYyODBcdTUxNmNcdTUzZjhDRE5cdTdmNTFcdTdlZGNcdTgyODJcdTcwYjkgMyIsICJhZGQiOiAiMTcyLjIzMy4xODguMjE3IiwgInBvcnQiOiAiNTU1NzkiLCAiaWQiOiAiNjEwZjdiNzYtYTRlMi00YjVhLWM0NTgtOTZlNjljYmZmYjVlIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDYiLCAic2N5IjogImF1dG8iLCAic25pIjogInd3dy42NTgyNTUyNC54eXoiLCAidGxzIjogInRscyIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%207
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2011
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpBSzRKMXNSdDJ2M2RMRFVWQzJQNWxq@94.131.12.245:37726#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%2015
vmess://eyJhZGQiOiAiNjQuMTc2LjQyLjEzNyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMTgiLCAicG9ydCI6IDIwODg2LCAiaWQiOiAiZjU3NGIyMzctM2ViZi00MDVjLWQ1NDAtNTQxNTMwZmU1ZWQ3IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMzgiLCAiYWRkIjogInVzMi5hd3NsY24uaW5mbyIsICJwb3J0IjogMjUyNTcsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAiIiwgImlkIjogIjkzZWM3MjYxLTFjOTItNDE0OS04NDhhLTI2YjZmYjlmYzRjZSIsICJob3N0IjogInVzMi5hd3NsY24uaW5mbyIsICJwYXRoIjogIi8ifQ==
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2041
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggNDkiLCAiYWRkIjogImNtMS5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1Mjg2IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImNtMS5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2050
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDU3IiwgImFkZCI6ICJhZnJobXMxNnYuYmVzdHhyYXkuYnV6eiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJmNTg0ZGUxNS0yMDM0LTQxNzAtYTcyMy1mNDhjMmJhZTVlMGYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi9saW5rd3MiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjUxNjUyMTA5Lnh5eiIsICJpZCI6ICI1NTU0NWY5ZS1hNTYxLTQ1NGEtOGRjMC04YmMxMTBlNmIxYzkiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJwb3J0IjogMzAwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODM3N1x1NTE3MFx1NTMxN1x1ODM3N1x1NTE3MFx1NzcwMVx1OTYzZlx1NTljNlx1NjVhZlx1NzI3OVx1NGUzOVNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA3OCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2079
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.91.107.37:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2088
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDk0IiwgImFkZCI6ICI0NS4xMjEuNDguMTcyIiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiZGJhNTFhMmUtYTc4OC00M2I3LTlhYzQtOWY3Y2MxMjU1ZjE1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDEwMyIsICJhZGQiOiAiNDUuMTIxLjQ4LjE5NiIsICJwb3J0IjogIjEwMDAxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZWQzNTYyOS05MTlhLTQ4OTEtYmEwZi0xM2NkMTk4Zjg2M2IiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDEwNSIsICJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAicG9ydCI6ICIzMTk0NSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAiIiwgImlkIjogImUyZTUxMWIwLTdkZWYtNGUxYi1kMjM4LTZjYjUzOTFiMmUzZiIsICJzbmkiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyJ9
```

