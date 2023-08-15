
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp           | ip                                   | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:--------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 198.2.197.67        | China         | CN   | PEG-SV        | 142.4.105.25                         | Yes (Region: US) |
|  1 | [3](config/3.json)   | 45.199.138.134      | Netherlands   | NL   | YISP B.V.     | 154.84.1.206                         | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 45.199.138.136      | Netherlands   | NL   | YISP B.V.     | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  3 | [6](config/6.json)   | 64.32.4.53          | United States | US   | SHARKTECH     | 107.167.13.162                       | Yes (Region: US) |
|  4 | [8](config/8.json)   | 156.245.8.205       | Poland        | PL   | OVH SAS       | 54.36.174.181                        | Yes (Region: FR) |
|  5 | [11](config/11.json) | 156.225.67.158      | Netherlands   | NL   | YISP B.V.     | 154.84.1.197                         | Yes (Region: NL) |
|  6 | [18](config/18.json) | pzl.p237875155.buzz | United States | US   | CLOUDFLARENET | 23.94.122.129                        | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAyIiwgImFkZCI6ICIxOTguMi4xOTcuNjciLCAicG9ydCI6ICI0OTkxMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogInYyc2cwMS5mdXFpYW5ncmVuLmNvbSIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjEzNCIsICJwb3J0IjogIjQxMzkzIiwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEzNiIsICJwb3J0IjogIjQ5NDQ5IiwgImlkIjogIjc0M2JkYzg3LTFkZWEtNDFiZi1hYTBiLTUxZGZiYmZlYzhhYSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuNC41MyIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiODY1MzAwNGYtZGU2Ny00NGMyLTljY2UtZTA4MzA5MzNmYjAzIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDM1NTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjIwNSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjEzMzQwMTk4Lnh5eiIsICJpZCI6ICIzZmQ2MzdhZC00NmZlLTRmODUtYTZlOC04NmIwMGJjYTExMjIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MjAwNTk4NTY4NSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3LjE1OCIsICJwb3J0IjogIjQ4OTM3IiwgImlkIjogIjljMDI2ZWZlLTZhZjAtNDY1Zi1iOGMwLTNmNThjOGMyZDRjNSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAicHpsLnAyMzc4NzUxNTUuYnV6eiIsICJhaWQiOiAwLCAiaG9zdCI6ICJwemwucDIzNzg3NTE1NS5idXp6IiwgImlkIjogIjliNzhiN2ZlLTQ3YTMtNDFlYi1kNjk1LTIyNjkyYWM4MzVhMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcHpsMjM3ODc1MTU1IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAidmRlMi4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9jaGF0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZFx1OWVkMVx1NjhlZVx1NWRkZVx1NmNkNVx1NTE3MFx1NTE0Ylx1Nzk4Zkxpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyNiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

