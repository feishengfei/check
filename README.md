
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp              | ip                | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------|:------------------|:-----------------|
|  0 | [1](config/1.json)   | 140.99.59.230   | United States | US   | DEDIPATH-LLC     | 2.56.121.242      | Yes (Region: US) |
|  1 | [2](config/2.json)   | 141.147.153.244 | Japan         | JP   | ORACLE-BMC-31898 | 141.147.153.244   | Yes (Region: JP) |
|  2 | [3](config/3.json)   | 156.245.8.248   | Netherlands   | NL   | YISP B.V.        | 154.84.1.137      | Yes (Region: NL) |
|  3 | [4](config/4.json)   | 154.84.1.115    | Netherlands   | NL   | YISP B.V.        | 154.84.1.40       | Yes (Region: NL) |
|  4 | [5](config/5.json)   | 192.74.228.187  | United States | US   | PEGTECHINC       | 142.0.129.201     | Yes (Region: US) |
|  5 | [7](config/7.json)   | 45.199.138.171  | Netherlands   | NL   | YISP B.V.        | 154.84.1.129      | Yes (Region: NL) |
|  6 | [8](config/8.json)   | 192.3.150.233   | Netherlands   | NL   | YISP B.V.        | 154.84.1.197      | Yes (Region: NL) |
|  7 | [13](config/13.json) | 104.27.1.133    | Netherlands   | NL   | AEZA GROUP Ltd   | 2a12:5940:5136::2 | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTQwLjk5LjU5LjIzMCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1NTUxMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkRGF0YWJpbGl0eSAxIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTQxLjE0Ny4xNTMuMjQ0IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNDdkNzEzNS0wOTU0LTQ2YWItYTE5MC0xN2I2Yzg2MzBhODUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDE1NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NzQ1ZVx1NTE3OE9yYWNsZSBDb3Jwb3JhdGlvbiAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDMiLCAiYWRkIjogIjE1Ni4yNDUuOC4yNDgiLCAicG9ydCI6ICI0MzM5MCIsICJpZCI6ICI5NjRiZjQ5OS05ZWMwLTQzNzgtOTJiNi04N2Q4ZDg2MWIyZDAiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU0Ljg0LjEuMTE1IiwgInBvcnQiOiAiNDc4NTIiLCAiaWQiOiAiNWE0ZDY5YWQtMjBhOS00OTQxLWIyMjMtODdiYmQwOWY1ZjUyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTkyLjc0LjIyOC4xODciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDI4NTcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3MSIsICJwb3J0IjogIjQyMDA4IiwgImlkIjogIjIwYjMwOTE2LWUyMDMtNDEyZS04ZWMwLTkwMGYzYWNkNTEyOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTkyLjMuMTUwLjIzMyIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiYTZhMzdlMDQtNWU4MS00NGM5LWJlNTMtYmFhM2ZmNDZlYjhiIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi84Y2RhNDhiMyIsICJwb3J0IjogODQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEzIiwgImFkZCI6ICIxMDQuMjcuMS4xMzMiLCAicG9ydCI6IDQ0MywgImlkIjogIjI0ODRmNDQ0LTBlMDAtNWEwZi1iOGYxLTRmZTJhMjU1MGQ2NSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAic2NoZXJlaW5hcHBjbGllbnQuYWxsdXNlcmNvbm5lY3R2MnJheS54eXoiLCAicGF0aCI6ICIvYXBpMDEiLCAidGxzIjogInRscyJ9
```

