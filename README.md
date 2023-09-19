
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr              | cn            | cc   | isp            | ip              | chatgpt          |
|---:|:---------------------|:------------------|:--------------|:-----|:---------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 107.167.30.149    | United States | US   | SHARKTECH      | 170.178.185.146 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 45.199.138.216    | Netherlands   | NL   | YISP B.V.      | 46.182.107.123  | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.245.8.144     | Netherlands   | NL   | YISP B.V.      | 154.84.1.134    | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 45.199.138.211    | United States | US   | NovoServe B.V. | 45.199.138.43   | Yes (Region: MU) |
|  4 | [6](config/6.json)   | 45.199.138.161    | Netherlands   | NL   | YISP B.V.      | 46.182.107.129  | Yes (Region: NL) |
|  5 | [7](config/7.json)   | 154.85.1.243      | Netherlands   | NL   | YISP B.V.      | 154.84.1.206    | Yes (Region: NL) |
|  6 | [8](config/8.json)   | 172.64.203.172    | Poland        | PL   | OVH SAS        | 54.36.174.181   | Yes (Region: FR) |
|  7 | [16](config/16.json) | 156.245.8.142     | Netherlands   | NL   | YISP B.V.      | 154.84.1.139    | Yes (Region: NL) |
|  8 | [24](config/24.json) | api.jquery.com    |               |      |                | 23.158.56.233   | Yes (Region: US) |
|  9 | [28](config/28.json) | mt.servermeli.xyz |               |      |                | 65.109.179.194  | Yes (Region: FI) |
| 10 | [33](config/33.json) | vfly3.win         |               |      |                | 47.245.30.19    | Yes (Region: JP) |
| 11 | [42](config/42.json) | 156.245.8.152     |               |      |                | 154.84.1.148    | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTA3LjE2Ny4zMC4xNDkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI1OGU1NjBiNC1iYmE2LTQ4NDMtYmU1Zi04MzMyMTAyMmZhMGQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDM5MDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlx1NWUwMlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjIxNiIsICJwb3J0IjogIjQ2NjU1IiwgImlkIjogImY5ZmEzYTljLWY3ZDUtNDE0Zi04OGU2LTY5NzA1ODVkOTk0OSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC4xNDQiLCAicG9ydCI6ICI0Mjk1MiIsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjIxMSIsICJwb3J0IjogIjUzNTM1IiwgImlkIjogIjZmYTU2MGQ0LTM1YzUtNDk2OC1hZGZjLTgxMmM1Mjg3OGI4NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE2MSIsICJwb3J0IjogIjQ1NTIyIiwgImlkIjogIjk1NDlhMmNmLTEyOWItNDNhMS04OGRiLWVmN2Y2NDhkZTc0YSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTU0Ljg1LjEuMjQzIiwgInBvcnQiOiAiMzIyODIiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjE3Mi42NC4yMDMuMTcyIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiNWY3NTFjNmUtNTBiMS00Nzk3LWJhOGUtNmZmZTMyNGEwYmNlIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJjYS5pbG92ZXNjcC5jb20iLCAicGF0aCI6ICIvc2hpcmtlciIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE2IiwgImFkZCI6ICIxNTYuMjQ1LjguMTQyIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy45Mjg3Mzg4OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk1MDMyOTA5MTY0IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI0IiwgImFkZCI6ICJhcGkuanF1ZXJ5LmNvbSIsICJwb3J0IjogNDQzLCAiaWQiOiAiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzdWIueWlmZW5qaWNoYW5nLnRvcCIsICJwYXRoIjogIi9vbGl2LmJlYXV0eTo0NDMvbGlua3Z3cyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAibXQuc2VydmVybWVsaS54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiZmxsNS5hcHBtYW5hZ2U1LmlyIiwgImlkIjogIjFlNDA0ZTgwLTZhODQtNDY3Yi05ZmU5LThhMjc3OTRkZGM0MyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAyMDg3LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTZkMWJcdTY3NDlcdTc3ZjYgMjgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAidmZseTMud2luIiwgImFpZCI6IDAsICJob3N0IjogInZmbHkzLndpbiIsICJpZCI6ICI5NjgxZjk5ZS1kMjUxLTQ3N2EtZDc3Ny0xZDAxZWU1NTA0ODEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL215YmxvZyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDMzIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQyIiwgImFkZCI6ICIxNTYuMjQ1LjguMTUyIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjg0ZDFkZTExLWNlMTItNGExNS04MzEyLTEzMzgzNTZkNGFjNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy41NzQyNDM0OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0OTQ3NjY1Mzg4IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
```

