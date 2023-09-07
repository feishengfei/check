
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp               | ip                                   | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:------------------|:-------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | ci.outline-vpn.cloud | United States | US   | SHARKTECH         | 67.21.72.34                          | Yes (Region: US) |
|  1 | [6](config/6.json)   | 154.85.1.245         | Netherlands   | NL   | YISP B.V.         | 154.84.1.206                         | Yes (Region: NL) |
|  2 | [8](config/8.json)   | 19.kccic2pa.xyz      | Poland        | PL   | OVH SAS           | 54.36.174.181                        | Yes (Region: FR) |
|  3 | [9](config/9.json)   | 45.199.138.135       | Netherlands   | NL   | YISP B.V.         | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  4 | [10](config/10.json) | 45.199.138.198       | United States | US   | NovoServe B.V.    | 45.199.138.43                        | Yes (Region: MU) |
|  5 | [11](config/11.json) | 162.251.62.115       | United States | US   | AS-GLOBALTELEHOST | 162.251.62.115                       | Yes (Region: US) |
|  6 | [12](config/12.json) | 04.kccic2pa.xyz      | United States | US   | OVH SAS           | 15.204.10.95                         | Yes (Region: US) |
|  7 | [13](config/13.json) | 40.kccic2pa.xyz      | United States | US   | OVH SAS           | 51.81.211.205                        | Yes (Region: US) |
|  8 | [20](config/20.json) | 162.159.58.231       | France        | FR   | SYNLINQ           | 103.252.90.249                       | Yes (Region: FR) |
|  9 | [25](config/25.json) | cloudqwq.cf          | France        | FR   | SYNLINQ           | 103.252.90.249                       | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiY2kub3V0bGluZS12cG4uY2xvdWQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMxMjMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMjQ1IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU1ODIxLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggOCIsICJhZGQiOiAiMTkua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMTkiLCAidHlwZSI6ICJub25lIiwgImlkIjogImI4OWQ1N2I3LWRmNzYtNGExYi05MDU0LWIzOGI0OTdhOGI1MCIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL2lrdW4iLCAiaG9zdCI6ICIxOS5rY2NpYzJwYS54eXoiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMzUiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI3NDNiZGM4Ny0xZGVhLTQxYmYtYWEwYi01MWRmYmJmZWM4YWEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTYxMjksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI2ZmE1NjBkNC0zNWM1LTQ5NjgtYWRmYy04MTJjNTI4NzhiODQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzcxMzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDEwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTYyLjI1MS42Mi4xMTUiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjA0NjIxYmFlLWFiMzYtMTFlYy1iOTA5LTAyNDJhYzEyMDAwMiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAyMjMyNCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAxMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjA0LmtjY2ljMnBhLnh5eiIsICJwb3J0IjogIjUwMDA0IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJiODlkNTdiNy1kZjc2LTRhMWItOTA1NC1iMzhiNDk3YThiNTAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9pa3VuIiwgImhvc3QiOiAiMDQua2NjaWMycGEueHl6IiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMTMiLCAiYWRkIjogIjQwLmtjY2ljMnBhLnh5eiIsICJwb3J0IjogIjUwMDQwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJiODlkNTdiNy1kZjc2LTRhMWItOTA1NC1iMzhiNDk3YThiNTAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9pa3VuIiwgImhvc3QiOiAiNDAua2NjaWMycGEueHl6IiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTYyLjE1OS41OC4yMzEiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRFYXN5RE5TIEFueWNhc3RcdTgyODJcdTcwYjkoQ2xvdWRmbGFyZVx1ODI4Mlx1NzBiOSkgMjUiLCAiYWRkIjogImNsb3VkcXdxLmNmIiwgInBvcnQiOiA4MCwgImlkIjogImNkMGM1NzBmLTc1N2MtNDhkMi1hMWI2LWMwOTQwNDMxY2M0NyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
```

