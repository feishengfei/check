
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                    | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------------|:---------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 45.77.176.217   | Japan         | JP   | AS-CHOOPA              | 2001:19f0:7001:21ad:5400:4ff:feaa:a43d | Yes (Region: JP) |
|  1 | [2](config/2.json)   | 38.75.136.21    | United States | US   | AS-GLOBALTELEHOST      | 38.75.136.21                           | Yes (Region: US) |
|  2 | [7](config/7.json)   | 38.91.102.30    | United States | US   | AS-GLOBALTELEHOST      | 38.91.102.30                           | Yes (Region: US) |
|  3 | [11](config/11.json) | 38.68.134.69    | United States | US   | AS-GLOBALTELEHOST      | 38.68.134.69                           | Yes (Region: US) |
|  4 | [15](config/15.json) | 38.75.136.135   | United States | US   | AS-GLOBALTELEHOST      | 38.75.136.135                          | Yes (Region: US) |
|  5 | [17](config/17.json) | 138.2.44.211    | Japan         | JP   | ORACLE-BMC-31898       | 138.2.44.211                           | Yes (Region: JP) |
|  6 | [18](config/18.json) | 129.146.46.181  | United States | US   | ORACLE-BMC-31898       | 129.146.46.181                         | Yes (Region: US) |
|  7 | [19](config/19.json) | 198.57.27.212   | Canada        | CA   | AS-GLOBALTELEHOST      | 198.57.27.212                          | Yes (Region: CA) |
|  8 | [20](config/20.json) | 51.159.106.157  | France        | FR   | Scaleway S.a.s.        | 2001:bc8:1201:501:1618:77ff:fe6e:dec   | Yes (Region: FR) |
|  9 | [21](config/21.json) | 162.251.62.115  | United States | US   | AS-GLOBALTELEHOST      | 162.251.62.115                         | Yes (Region: US) |
| 10 | [22](config/22.json) | 140.83.63.38    | Japan         | JP   | ORACLE-BMC-31898       | 140.83.63.38                           | Yes (Region: JP) |
| 11 | [25](config/25.json) | 38.121.43.97    | United States | US   | AS-GLOBALTELEHOST      | 38.121.43.97                           | Yes (Region: US) |
| 12 | [27](config/27.json) | 148.135.33.94   | United States | US   | MULTA-ASN1             | 2607:f130:109:0:d6ae:52ff:febb:b49f    | Yes (Region: US) |
| 13 | [28](config/28.json) | 38.91.107.37    | United States | US   | AS-GLOBALTELEHOST      | 38.91.107.37                           | Yes (Region: US) |
| 14 | [33](config/33.json) | 198.2.202.81    | China         | CN   | PEG-SV                 | 142.4.102.244                          | Yes (Region: US) |
| 15 | [34](config/34.json) | 167.179.111.237 | Japan         | JP   | AS-CHOOPA              | 2001:19f0:7001:244:5400:4ff:feab:d9e2  | Yes (Region: JP) |
| 16 | [38](config/38.json) | 142.202.48.99   | United States | US   | AS-GLOBALTELEHOST      | 142.202.48.99                          | Yes (Region: US) |
| 17 | [44](config/44.json) | 212.113.106.243 | Austria       | AT   | Aeza International Ltd | 212.113.106.243                        | Yes (Region: AT) |
| 18 | [46](config/46.json) | 51.77.53.200    | Poland        | PL   | OVH SAS                | 51.77.53.200                           | Yes (Region: PL) |
| 19 | [50](config/50.json) | 54.36.174.181   | Poland        | PL   | OVH SAS                | 54.36.174.181                          | Yes (Region: FR) |
| 20 | [52](config/52.json) | 51.77.53.200    | Poland        | PL   | OVH SAS                | 51.77.53.200                           | Yes (Region: PL) |
| 21 | [59](config/59.json) | 142.202.48.99   | United States | US   | AS-GLOBALTELEHOST      | 142.202.48.99                          | Yes (Region: US) |
| 22 | [64](config/64.json) | 51.77.53.200    | Poland        | PL   | OVH SAS                | 51.77.53.200                           | Yes (Region: PL) |
| 23 | [75](config/75.json) | 149.202.82.172  | France        | FR   | OVH SAS                | 149.202.82.172                         | Yes (Region: FR) |
| 24 | [77](config/77.json) | 217.182.198.219 | Germany       | DE   | OVH SAS                | 217.182.198.219                        | Yes (Region: DE) |
| 25 | [85](config/85.json) | 54.36.174.181   | Poland        | PL   | OVH SAS                | 54.36.174.181                          | Yes (Region: FR) |
| 26 | [87](config/87.json) | 154.90.39.63    | Malaysia      | MY   | Kaopu Cloud HK Limited | 154.90.39.63                           | Yes (Region: MY) |
| 27 | [92](config/92.json) | 142.202.48.99   | United States | US   | AS-GLOBALTELEHOST      | 142.202.48.99                          | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuNzcuMTc2LjIxNyIsICJhaWQiOiAiMCIsICJob3N0IjogIiIsICJpZCI6ICIxZjU3YTFjYy1kMzk1LTRiZGUtYmZjZi1mNjJhOGE0Zjk1NTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjE2MTQyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjXHU0ZTFjXHU0ZWFjQ2hvb3BhXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDEiLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@38.75.136.21:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%202
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.102.30:5004#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%207
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@38.68.134.69:8091#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2011
vmess://eyJhZGQiOiAiMTcyLjIzMy4xODguMTY2IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZEFrYW1haVx1NzlkMVx1NjI4MFx1NTE2Y1x1NTNmOENETlx1N2Y1MVx1N2VkY1x1ODI4Mlx1NzBiOSAxMyIsICJwb3J0IjogMTEzOTcsICJpZCI6ICIyMGUwZDY3ZC1mN2FhLTRiYjEtZGFhZS1iN2YyMTczMDZiYmEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.75.136.135:5004#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2015
vmess://eyJhZGQiOiAiMTM4LjIuNDQuMjExIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjU5M2I4NTI1LTBjNDgtNGIwZi1kOWFmLTJkNzNhOTE0ODk3MyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjIwMDgxIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAxNyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTI5LjE0Ni40Ni4xODEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImE3OTdmZjdiLTgxNjEtNDBhNi1kNTc3LTFiMmMyMTNiMzg4NSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNTI0MDgiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTRlOWFcdTUyMjlcdTY4NTFcdTkwYTNcdTVkZGVcdTUxZTRcdTUxZjBcdTU3Y2VPcmFjbGVcdTRlOTFcdThiYTFcdTdiOTdcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTgiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTk4LjU3LjI3LjIxMiIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiMDQ2MjFiYWUtYWIzNi0xMWVjLWI5MDktMDI0MmFjMTIwMDAyIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICIyMjMyNCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTMxN1x1N2Y4ZVx1NTczMFx1NTMzYSAgMTkiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpWVjV2NEdqTWRLc050OGowYmZUVzZ5@51.159.106.157:6917#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E5%B7%B4%E9%BB%8EOnline%20S.A.S%2020
vmess://eyJhZGQiOiAiMTYyLjI1MS42Mi4xMTUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAyMSIsICJwb3J0IjogMjIzMjQsICJpZCI6ICIwNDYyMWJhZS1hYjM2LTExZWMtYjkwOS0wMjQyYWMxMjAwMDIiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTQwLjgzLjYzLjM4IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NmZiM1x1NTkyN1x1NTIyOVx1NGU5YSAgMjIiLCAicG9ydCI6IDI0NDQ1LCAiaWQiOiAiOTRjNWVmMzctNGQ4Mi00OWY5LWM2MjQtZjAxMjU5Mzc0YTE3IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@38.121.43.97:6697#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2025
vmess://eyJhZGQiOiAiMTQ4LjEzNS4zMy45NCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMwOTk0MTA0Lnh5eiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMzIzMTI2Mjg3NSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTc0NWVcdTUxNzggIDI3IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.91.107.37:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2028
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogInd3dy42NTgyNTUyNC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAicG9ydCI6ICIzMDAwMCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDMzIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTY3LjE3OS4xMTEuMjM3IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0Nob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAzNCIsICJwb3J0IjogMTQ5MzUsICJpZCI6ICJlOTYxODk0Zi04ZTkwLTQ3MmYtOThkMy0wOTQwMmU0YmU0NTMiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@142.202.48.99:7306#github.com/freefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2038
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpQMnp4WFBld2xWM0JsZnFxWWlTdGh2dExj@212.113.106.243:12949#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2044
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@51.77.53.200:4444#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%2046
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@54.36.174.181:8091#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2050
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@51.77.53.200:8118#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%2052
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@142.202.48.99:2376#github.com/freefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2059
ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@51.77.53.200:6679#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%2064
ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@149.202.82.172:6697#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%E6%9C%BA%E6%88%BFSAS%E7%A1%AC%E7%9B%98BGP%E4%B8%BB%E6%9C%BA%2075
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@217.182.198.219:2376#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%20SAS%2077
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@54.36.174.181:8118#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2085
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTcyNzlcdTUyMmJcdTg4NGNcdTY1M2ZcdTUzM2EgODciLCAiYWRkIjogIjE1NC45MC4zOS42MyIsICJwb3J0IjogIjQ1MzQzIiwgImlkIjogIjA4YWE4NDk5LWQ2MTYtNGZmMS1kNmFiLWNlMGM1MjI4MjRhYSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@142.202.48.99:8090#github.com/freefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2092
```

