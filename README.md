
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                            | ip                             | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:-------------------------------|:-------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 52.142.161.9    | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.161.9                   | Yes (Region: GB) |
|  1 | [5](config/5.json)   | 45.159.249.231  | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                 | Yes (Region: FI) |
|  2 | [9](config/9.json)   | 198.2.202.81    | China           | CN   | PEG-SV                         | 142.4.102.244                  | Yes (Region: US) |
|  3 | [27](config/27.json) | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                   | Yes (Region: US) |
|  4 | [34](config/34.json) | 45.58.145.200   | The Netherlands | NL   | SHARKTECH                      | 45.58.145.194                  | Yes (Region: US) |
|  5 | [41](config/41.json) | 38.91.107.37    | United States   | US   | AS-GLOBALTELEHOST              | 38.91.107.37                   | Yes (Region: US) |
|  6 | [53](config/53.json) | 45.58.153.24    | The Netherlands | NL   | SHARKTECH                      | 45.58.149.130                  | Yes (Region: US) |
|  7 | [54](config/54.json) | 38.75.136.49    | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49                   | Yes (Region: US) |
|  8 | [56](config/56.json) | 45.121.48.172   | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.172                  | Yes (Region: TW) |
|  9 | [71](config/71.json) | 103.159.206.35  | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35                 | Yes (Region: TW) |
| 10 | [73](config/73.json) | 172.105.226.166 | Japan           | JP   | Akamai Connected Cloud         | 2400:8902::f03c:94ff:febb:ef7a | Yes (Region: JP) |
| 11 | [75](config/75.json) | 45.121.48.196   | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196                  | Yes (Region: TW) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo2NExiS0huQjNJTzc1OXVlRW5oZ01H@52.142.161.9:34424#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%204
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%205
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDkiLCAic2N5IjogImF1dG8iLCAic25pIjogInd3dy42NTgyNTUyNC54eXoiLCAidGxzIjogInRscyIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2027
vmess://eyJhZGQiOiAiNDUuNTguMTQ1LjIwMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMzQiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNTU1NDVmOWUtYTU2MS00NTRhLThkYzAtOGJjMTEwZTZiMWM5IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTE2NTIxMDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJ0bHMiOiAidGxzIn0=
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.107.37:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2041
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNTMiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2054
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDU2IiwgImFkZCI6ICI0NS4xMjEuNDguMTcyIiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiZGJhNTFhMmUtYTc4OC00M2I3LTlhYzQtOWY3Y2MxMjU1ZjE1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTAzLjE1OS4yMDYuMzUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTlhXHU1OTJhXHU1NzMwXHU1MzNhICA3MSIsICJwb3J0IjogMzE5NDUsICJpZCI6ICJlMmU1MTFiMC03ZGVmLTRlMWItZDIzOC02Y2I1MzkxYjJlM2YiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTcyLjEwNS4yMjYuMTY2IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0xpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA3MyIsICJwb3J0IjogMzYxNzMsICJpZCI6ICI1ZGU4MDhkMS1iNzA3LTQ2MmMtODNmMy02ODczOTUwNGFkNzAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDc1IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiMGVkMzU2MjktOTE5YS00ODkxLWJhMGYtMTNjZDE5OGY4NjNiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

