
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp              | ip                        | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------------|:--------------------------|:-----------------|
|  0 | [6](config/6.json)   | 156.225.67.47  | Netherlands   | NL   | YISP B.V.        | 154.84.1.164              | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 188.114.98.139 | Netherlands   | NL   | YISP B.V.        | 154.84.1.230              | Yes (Region: NL) |
|  2 | [9](config/9.json)   | Shopify.com    | France        | FR   | CLOUDFLARENET    | 2a09:bac5:3264:be::13:298 | Yes (Region: FR) |
|  3 | [18](config/18.json) | 156.245.8.143  | Netherlands   | NL   | YISP B.V.        | 154.84.1.139              | Yes (Region: NL) |
|  4 | [21](config/21.json) | 104.20.18.54   | United States | US   | 24.hk global BGP | 163.197.245.87            | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny40NyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0ODEyMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTg4LjExNC45OC4xMzkiLCAiYWlkIjogMCwgImhvc3QiOiAiZWNjLnZ0Y3NzLnRvcCIsICJpZCI6ICI1NGQ0YTVlOS02NDQxLTQ0MmMtY2FiNy0wNTYyMGNiZTRmN2QiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3F3ZXIwMSIsICJwb3J0IjogODA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZGY0XHU4OTdmXHU1NzIzXHU0ZmRkXHU3ZjU3Q2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDkiLCAiYWRkIjogIlNob3BpZnkuY29tIiwgInBvcnQiOiAiMjA4NiIsICJpZCI6ICIyNTBmNDMzMS04YzNlLTRiODctYTg2Yi01YzVmYmY5ZGRiYTgiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIkZyLmNsb3VkZmxhcmUucXVlc3QiLCAicGF0aCI6ICIvYXJpZXMiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogNDkxNTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZiAgMTgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIxIiwgImFkZCI6ICIxMDQuMjAuMTguNTQiLCAicG9ydCI6ICIyMDk1IiwgImlkIjogIjhjNGU1ZTgzLThiZTItNDYzOC1lM2Y2LWEwOThlZTQ4NDE5MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiaGsud3loa2FhMC50ayIsICJwYXRoIjogIi9AaGthYTAiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

