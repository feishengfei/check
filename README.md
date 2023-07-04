
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr           | cn            | cc   | isp        | ip             | chatgpt          |
|---:|:-------------------|:---------------|:--------------|:-----|:-----------|:---------------|:-----------------|
|  0 | [2](config/2.json) | 107.167.7.12   | United States | US   | SHARKTECH  | 107.167.18.50  | Yes (Region: US) |
|  1 | [3](config/3.json) | 137.175.9.205  | United States | US   | PEGTECHINC | 142.4.118.225  | Yes (Region: US) |
|  2 | [4](config/4.json) | 156.245.8.157  | Netherlands   | NL   | YISP B.V.  | 154.84.1.138   | Yes (Region: NL) |
|  3 | [5](config/5.json) | 64.32.24.213   | United States | US   | SHARKTECH  | 170.178.189.58 | Yes (Region: US) |
|  4 | [6](config/6.json) | 154.84.1.113   | Netherlands   | NL   | YISP B.V.  | 154.84.1.40    | Yes (Region: NL) |
|  5 | [7](config/7.json) | 156.225.67.131 | Netherlands   | NL   | YISP B.V.  | 154.84.1.219   | Yes (Region: NL) |
|  6 | [8](config/8.json) | 45.199.138.95  | United States | US   | CNSERVERS  | 23.225.9.234   | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTA3LjE2Ny43LjEyIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJiZGVlMjAyYy04ZmFlLTQ0MWYtYTU4OC03YmM0ZDM4ODcwMTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0MTY1NCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlx1NWUwMlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDMiLCAiYWRkIjogIjEzNy4xNzUuOS4yMDUiLCAicG9ydCI6ICI1NzkwMiIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC4xNTciLCAicG9ydCI6ICIzOTczNCIsICJpZCI6ICIxMTExN2Q0Yy0zYjZhLTRlNzYtOGJjYy0yYjQxYjNlOWNhOTMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjEzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ4NjU5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTU0Ljg0LjEuMTEzIiwgInBvcnQiOiAiNDc4NTIiLCAiaWQiOiAiNWE0ZDY5YWQtMjBhOS00OTQxLWIyMjMtODdiYmQwOWY1ZjUyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDciLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTMxIiwgInBvcnQiOiAiNDg4ODQiLCAiaWQiOiAiNTE1YmNiNGQtMGJhMS00Y2FlLTg3Y2YtYTA0NzAwN2VlYzU0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA4IiwgImFkZCI6ICI0NS4xOTkuMTM4Ljk1IiwgInBvcnQiOiAiNDk5MjEiLCAiaWQiOiAiZDMxMzM0ODQtZjJiZi00YjBjLThkMzgtZjhlNjQ1YjY1Njg3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

