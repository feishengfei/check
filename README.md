
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn            | cc   | isp                              | ip                                   | chatgpt          |
|---:|:---------------------|:----------------------|:--------------|:-----|:---------------------------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 198.2.193.146         | China         | CN   | PEG-SV                           | 198.2.193.145                        | Yes (Region: US) |
|  1 | [3](config/3.json)   | 156.225.67.104        | Netherlands   | NL   | YISP B.V.                        | 154.84.1.44                          | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 107.167.16.85         | United States | US   | SHARKTECH                        | 170.178.189.50                       | Yes (Region: US) |
|  3 | [7](config/7.json)   | 142.4.119.18          | United States | US   | PEG-SV                           | 38.53.92.161                         | Yes (Region: US) |
|  4 | [13](config/13.json) | cfcdn3.sanfencdn9.com | Japan         | JP   | Eons Data Communications Limited | 38.207.152.110                       | Yes (Region: US) |
|  5 | [14](config/14.json) | 45.199.138.152        | Netherlands   | NL   | YISP B.V.                        | 2a02:2a38:1:2796:ae1f:6bff:fe24:8940 | Yes (Region: NL) |
|  6 | [15](config/15.json) | 156.245.8.170         | Netherlands   | NL   | YISP B.V.                        | 154.84.1.158                         | Yes (Region: NL) |
|  7 | [20](config/20.json) | 156.245.8.130         | Netherlands   | NL   | YISP B.V.                        | 154.84.1.121                         | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAyIiwgImFkZCI6ICIxOTguMi4xOTMuMTQ2IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjY4ZDIzOGNlLTNjYTEtNDZkYy1iODMzLWEwOTE2YzgyOWFkMyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODI1MTY1OC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MjM5ODg4OTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MjM5ODg4OTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTA3LjE2Ny4xNi44NSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJwb3J0IjogNDQzLCAiaWQiOiAiNzY0MGExZTctOTcwMS00MjhlLWE0YjItMTliM2U3ZGQ2ZjlmIiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNTExMDkwNTcueHl6IiwgInBhdGgiOiAiL3BhdGgvMDgwODIyMjcyOTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA3IiwgImFkZCI6ICIxNDIuNC4xMTkuMTgiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3Ljc3NjQ2NzUwLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTgzMjgxMzkwMzgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEzIiwgImFkZCI6ICJjZmNkbjMuc2FuZmVuY2RuOS5jb20iLCAicG9ydCI6ICI4MCIsICJpZCI6ICI2OTgxMTVlNC0xNDk0LTRmNGEtODVhOS03NmNkMDExZDNhYzYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImpwMTdhYWI3MmE3LmNodnNpZmV0cmoueHl6IiwgInBhdGgiOiAiL3ZpZGVvL3V1YkNkSnRLIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiIsICJmcCI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNCIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNTIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTQ2OTBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjMyNTIyMTc4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTgzMjgxMzkwMzgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE1IiwgImFkZCI6ICIxNTYuMjQ1LjguMTcwIiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjNhM2M4YTljLTMzNGUtNDM2MC1hZGI4LWE4MGE1N2RkY2JiZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4xNjA0NjYyNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MzI4MTM5MDM4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDIwIiwgImFkZCI6ICIxNTYuMjQ1LjguMTMwIiwgInBvcnQiOiAzMDAwMCwgImlkIjogImJkMjQ5ZTM3LTczNTktNDFlZS04NGE3LTA5ZTQ5ZTBlYzVjNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40NzUyMzM3NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MzI4MTM5MDM4IiwgInRscyI6ICJ0bHMifQ==
```

