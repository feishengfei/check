
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                    | ip                             | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:-----------------------|:-------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.12.144.79        | United States | US   | DEDIPATH-LLC           | 45.92.126.90                   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 67.21.90.30         | United States | US   | SHARKTECH              | 107.167.22.10                  | Yes (Region: US) |
|  2 | [6](config/6.json)   | 64.32.24.210        | United States | US   | SHARKTECH              | 170.178.189.58                 | Yes (Region: US) |
|  3 | [7](config/7.json)   | 156.225.67.78       | Netherlands   | NL   | YISP B.V.              | 46.182.107.216                 | Yes (Region: NL) |
|  4 | [8](config/8.json)   | visa.com            | United States | US   | AS-GLOBALTELEHOST      | 169.197.141.187                | Yes (Region: US) |
|  5 | [11](config/11.json) | 67.21.77.73         | United States | US   | SHARKTECH              | 107.167.18.42                  | Yes (Region: US) |
|  6 | [15](config/15.json) | 185.143.233.124     | Germany       | DE   | Akamai Connected Cloud | 2a01:7e01::f03c:93ff:fe94:4daa | Yes (Region: DE) |
|  7 | [16](config/16.json) | 104.21.44.220       | Argentina     | AR   | InterBS S.R.L. BAEHOST | 131.255.7.29                   | Yes (Region: AR) |
|  8 | [18](config/18.json) | scaleway.696960.xyz | Netherlands   | NL   | CLOUDFLARENET          | 2a09:bac5:4e26:1478::20a:28    | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZiMjdcdTc2ZGYgIDIiLCAiYWRkIjogIjQ1LjEyLjE0NC43OSIsICJwb3J0IjogIjQ3MTI3IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjcuMjEuOTAuMzAiLCAicG9ydCI6ICI0MjIxNyIsICJpZCI6ICIyOGRkNmMyNi0wNWE1LTRiYmEtOGE1ZC0wNTJiNzBhYzEzYjIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiNjQuMzIuMjQuMjEwIiwgInBvcnQiOiAiNDg2NTkiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDciLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzgiLCAicG9ydCI6ICI0NTA0MyIsICJpZCI6ICIzZTAxNmM0ZC05ODZlLTQyZGYtODM4Yy02MDQ2ZjNkODllY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInZpc2EuY29tIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMzczZjJkNzEtNzljYS00N2E0LTk3NGYtNzliMjU5MGU4YzYwIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzc3JzdWIudjAxLnNzcnN1Yi5jb20iLCAicGF0aCI6ICIvYXBpL3YzL2Rvd25sb2FkLmdldEZpbGUiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAiYWRkIjogIjY3LjIxLjc3LjczIiwgInBvcnQiOiAiNDcxNDAiLCAiaWQiOiAiZmFiYjMwZTgtM2EyYy00MTQ5LTk2NTEtMjc1OGY3NzEyNDgxIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTg1LjE0My4yMzMuMTI0IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImdlci5hcHAtd3BzLnNpdGUiLCAiaWQiOiAiMThmMjBlZDItZGE1OS00OWE3LWY3ZWQtOWIxMGU1OGI0MzJiIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi93ZWIyIiwgInBvcnQiOiAiODg4MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMTUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTA0LjIxLjQ0LjIyMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE2IiwgInBvcnQiOiAyMDg2LCAiaWQiOiAiMzExZjNjNGItOTBhMS0zYzVjLWE0ZmUtMjE1Y2M3YzkwZDAyIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogImFnMDEtY2RuLm15bjFkZXMuY29tIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAic2NhbGV3YXkuNjk2OTYwLnh5eiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE4IiwgInBvcnQiOiA0NDMsICJpZCI6ICJlMzU3Y2Q2My1mMWE1LTRjOGUtYzQyZS0yNmRhMTEyMDdmZWUiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiL3Jvb3QvIiwgInRscyI6ICJ0bHMifQ==
```

