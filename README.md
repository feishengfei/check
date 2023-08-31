
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn            | cc   | isp                            | ip              | chatgpt          |
|---:|:---------------------|:------------------------|:--------------|:-----|:-------------------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 137.175.88.217          | China         | CN   | PEG-SV                         | 142.4.109.161   | Yes (Region: US) |
|  1 | [4](config/4.json)   | 107.167.30.132          | United States | US   | SHARKTECH                      | 170.178.185.146 | Yes (Region: US) |
|  2 | [8](config/8.json)   | v2nodep-hk4.hkss.online | Poland        | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  3 | [10](config/10.json) | 172.64.153.211          | Sweden        | SE   | Stark Industries Solutions Ltd | 94.131.115.68   | Yes (Region: SE) |
|  4 | [18](config/18.json) | 45.199.138.148          | Netherlands   | NL   | YISP B.V.                      | 46.182.107.123  | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTM3LjE3NS44OC4yMTciLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQwMDIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAzIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTA3LjE2Ny4zMC4xMzIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI1OGU1NjBiNC1iYmE2LTQ4NDMtYmU1Zi04MzMyMTAyMmZhMGQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDM5MDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlx1NWUwMlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTc1MzVcdThiYWZcdTc2YzhcdTc5ZDFcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggOCIsICJhZGQiOiAidjJub2RlcC1oazQuaGtzcy5vbmxpbmUiLCAicG9ydCI6ICI1NTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjQ2NjRlNzYwLWY1ZjMtM2NjMi04YmIzLTA0Zjg1YWE3ZmViYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL21wNCIsICJob3N0IjogInYybm9kZXAtaGs0Lmhrc3Mub25saW5lIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4yMTEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAic2NoZXJlc3dlZC5zb2Z0d2FyZW5ld3Muc3RvcmUiLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkwMSIsICJwb3J0IjogIjQ0MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTAiLCAic2N5IjogImF1dG8iLCAic25pIjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNDgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmOWZhM2E5Yy1mN2Q1LTQxNGYtODhlNi02OTcwNTg1ZDk5NDkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzEyMzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDE4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

