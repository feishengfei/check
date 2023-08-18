
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp        | ip                                   | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------|:-------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 45.199.138.173  | Netherlands   | NL   | YISP B.V.  | 154.84.1.129                         | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 45.199.138.195  | Netherlands   | NL   | YISP B.V.  | 154.84.1.128                         | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 45.199.138.136  | Netherlands   | NL   | YISP B.V.  | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 156.245.8.151   | Netherlands   | NL   | YISP B.V.  | 154.84.1.148                         | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 216.24.57.1     | Poland        | PL   | OVH SAS    | 54.36.174.181                        | Yes (Region: FR) |
|  5 | [10](config/10.json) | 156.225.67.73   | Netherlands   | NL   | YISP B.V.  | 154.84.1.19                          | Yes (Region: NL) |
|  6 | [16](config/16.json) | 64.32.20.103    | United States | US   | SHARKTECH  | 64.32.0.58                           | Yes (Region: US) |
|  7 | [18](config/18.json) | 156.245.8.234   | Netherlands   | NL   | YISP B.V.  | 154.84.1.139                         | Yes (Region: NL) |
|  8 | [21](config/21.json) | 156.249.18.21   | Netherlands   | NL   | YISP B.V.  | 154.84.1.161                         | Yes (Region: NL) |
|  9 | [23](config/23.json) | 108.166.203.181 | United States | US   | MULTA-ASN1 | 173.82.156.42                        | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3MyIsICJwb3J0IjogIjQzMDc0IiwgImlkIjogIjIwYjMwOTE2LWUyMDMtNDEyZS04ZWMwLTkwMGYzYWNkNTEyOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTUiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJmZTVmNjllNy1lMTgzLTQzOWItOTUwYi05NjYxZWYwNjUxZjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjMzMzU4IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgNCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEzNiIsICJwb3J0IjogIjQ1MjQ5IiwgImlkIjogIjc0M2JkYzg3LTFkZWEtNDFiZi1hYTBiLTUxZGZiYmZlYzhhYSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE1MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg0ZDFkZTExLWNlMTItNGExNS04MzEyLTEzMzgzNTZkNGFjNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NDE2OSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMjE2LjI0LjU3LjEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiZGQyLjE4MDguY2YiLCAiaWQiOiAiYTdlZTg1ZjQtMjUyOC00MTJlLTk5NGYtY2U2NWY1NDc1NGU0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogImE3ZWU4NWY0IiwgInBvcnQiOiAiNDQzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1ZGRlIDgiLCAic2N5IjogImF1dG8iLCAic25pIjogImRkMi4xODA4LmNmIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEwIiwgImFkZCI6ICIxNTYuMjI1LjY3LjczIiwgInBvcnQiOiAiMzE5MDkiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuMjAuMTAzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYzFiYWQ5YTYtMTQ4Mi00OTQxLWEwYzQtZTg1ZjNjYmJjYjVhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQwMDM5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjIzNCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjkyODczODg5Lnh5eiIsICJpZCI6ICI2MTkzMTE2ZC05NmY5LTRkN2EtOWJlNS01YmIwNmE2OWFmMGIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MjI3MDMyMzM5NiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4yMSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjIwMTYzMzIyLnh5eiIsICJpZCI6ICJkNzczNTA1OC0xZGFjLTQ2MTgtOTlmZi0wYWEwNDQxZWMyZDciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MjIwMzM0MzY3MyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjEiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNjhhNDkxYi03NjRjLTQ0ZDEtODFhNC0zMGRlMTYxMzA4NjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0NDk0NSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIzIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
```

