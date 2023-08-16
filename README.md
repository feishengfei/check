
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn             | cc   | isp                    | ip             | chatgpt          |
|---:|:---------------------|:-------------------|:---------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 198.2.197.67       | China          | CN   | PEG-SV                 | 142.4.105.25   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 64.32.4.53         | United States  | US   | SHARKTECH              | 107.167.13.162 | Yes (Region: US) |
|  2 | [4](config/4.json)   | 37.120.193.102     | Serbia         | RS   | M247 Europe SRL        | 146.70.111.194 | Yes (Region: RS) |
|  3 | [6](config/6.json)   | 45.199.138.149     | Netherlands    | NL   | YISP B.V.              | 46.182.107.123 | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 198.41.198.160     | Poland         | PL   | OVH SAS                | 54.36.174.181  | Yes (Region: FR) |
|  5 | [10](config/10.json) | wi.saintink.eu.org | United Kingdom | GB   | Akamai Connected Cloud | 109.74.192.74  | Yes (Region: GB) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAyIiwgImFkZCI6ICIxOTguMi4xOTcuNjciLCAicG9ydCI6ICI0OTkxMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogInYyc2cwMS5mdXFpYW5ncmVuLmNvbSIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuNC41MyIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiODY1MzAwNGYtZGU2Ny00NGMyLTljY2UtZTA4MzA5MzNmYjAzIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDM1NTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMzcuMTIwLjE5My4xMDIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI1NzE3MGZmMC03MTgwLTQ2NjQtOGY2MS04ZGViZGRhMzQ1ZjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTI5MjAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y1N1x1OWE2Y1x1NWMzY1x1NGU5YSAgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0OSIsICJwb3J0IjogIjQyOTIyIiwgImlkIjogImY5ZmEzYTljLWY3ZDUtNDE0Zi04OGU2LTY5NzA1ODVkOTk0OSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTk4LjQxLjE5OC4xNjAiLCAiYWlkIjogMCwgImhvc3QiOiAiZWNjLnZ0Y3NzLnRvcCIsICJpZCI6ICIwYWZiOGIyYy0xNDlhLTQ5YTgtZTkwZi1kNzc4ODRhYzkyMmYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2JsdWUwNCIsICJwb3J0IjogMjA4MiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWEgIDEwIiwgImFkZCI6ICJ3aS5zYWludGluay5ldS5vcmciLCAicG9ydCI6ICI0NDMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvdnVrMi4wYmFkLmNvbS9jaGF0IiwgImhvc3QiOiAic3ViMi5zYWludGluay5ldS5vcmciLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiU2hvcGlmeS5jb20iLCAiYWlkIjogMCwgImhvc3QiOiAiRnIuY2xvdWRmbGFyZS5xdWVzdCIsICJpZCI6ICIyNTBmNDMzMS04YzNlLTRiODctYTg2Yi01YzVmYmY5ZGRiYTgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FyaWVzIiwgInBvcnQiOiAyMDg2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDIwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

