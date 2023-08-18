
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp            | ip                                   | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:---------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 108.166.203.181 | United States | US   | MULTA-ASN1     | 173.82.156.42                        | Yes (Region: US) |
|  1 | [3](config/3.json)   | 64.32.21.246    | United States | US   | SHARKTECH      | 107.167.24.162                       | Yes (Region: US) |
|  2 | [4](config/4.json)   | 156.225.67.73   | Netherlands   | NL   | YISP B.V.      | 154.84.1.19                          | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 64.32.4.53      | United States | US   | SHARKTECH      | 107.167.13.162                       | Yes (Region: US) |
|  4 | [6](config/6.json)   | 156.225.67.242  | Netherlands   | NL   | YISP B.V.      | 154.84.1.37                          | Yes (Region: NL) |
|  5 | [7](config/7.json)   | 45.199.138.136  | Netherlands   | NL   | YISP B.V.      | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  6 | [8](config/8.json)   | cdn-yx.syjd.xyz | Poland        | PL   | OVH SAS        | 54.36.174.181                        | Yes (Region: FR) |
|  7 | [18](config/18.json) | 45.199.138.173  | Netherlands   | NL   | YISP B.V.      | 154.84.1.129                         | Yes (Region: NL) |
|  8 | [19](config/19.json) | 212.113.106.243 | Austria       | AT   | AEZA GROUP Ltd | 212.113.106.243                      | Yes (Region: AT) |

## Valid
```
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNjhhNDkxYi03NjRjLTQ0ZDEtODFhNC0zMGRlMTYxMzA4NjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0NDk0NSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICIzMTkwOSIsICJpZCI6ICIyMTE1NWVmZC04ZTI5LTQzZDItOTViYy1mZTMxOTBlY2IxYzYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiNjQuMzIuNC41MyIsICJwb3J0IjogIjQzNTU2IiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJkcDQuc2Nwcm94eS50b3AiLCAicGF0aCI6ICIvc2hpcmtlciIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjQyIiwgInBvcnQiOiAiNDMzNzAiLCAiaWQiOiAiOTkwMDA2YmQtY2IyMC00ODJmLTljOTctZjVmYzY1MzU5NjA1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEzNiIsICJwb3J0IjogIjQ1MjQ5IiwgImlkIjogIjc0M2JkYzg3LTFkZWEtNDFiZi1hYTBiLTUxZGZiYmZlYzhhYSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiY2RuLXl4LnN5amQueHl6IiwgImFpZCI6IDAsICJob3N0IjogImNkbi11cy5zeWpkLnh5eiIsICJpZCI6ICIyNTI1OGFmMC1jYTA4LTQzYTgtYTYzOC02YzAzOWMzM2RhMjEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2NkbiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxOCIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNzMiLCAicG9ydCI6ICI0MzA3NCIsICJpZCI6ICIyMGIzMDkxNi1lMjAzLTQxMmUtOGVjMC05MDBmM2FjZDUxMjgiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiXHVkODNjXHVkZGZhXHVkODNjXHVkZGY4VVNcdTdmOGVcdTU2ZmQoeW91dHViZVx1OTYzZlx1NGYxZlx1NzlkMVx1NjI4MCkiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp3NWRyQUw3UGZDSXdRMnljVXVvRHNWMkxz@212.113.106.243:13022#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2019
```

