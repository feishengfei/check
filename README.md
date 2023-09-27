
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp              | ip                            | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------------|:------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.206 | Netherlands   | NL   | YISP B.V.        | 154.84.1.129                  | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.245.8.146  | Netherlands   | NL   | YISP B.V.        | 154.84.1.134                  | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 45.199.138.180 | Netherlands   | NL   | YISP B.V.        | 154.84.1.229                  | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 156.225.67.48  | Netherlands   | NL   | YISP B.V.        | 154.84.1.164                  | Yes (Region: NL) |
|  4 | [7](config/7.json)   | 192.74.228.188 | United States | US   | PEG-SV           | 142.0.129.201                 | Yes (Region: US) |
|  5 | [8](config/8.json)   | 107.167.16.85  | Poland        | PL   | OVH SAS          | 54.36.174.181                 | Yes (Region: FR) |
|  6 | [9](config/9.json)   | 156.245.8.248  | Netherlands   | NL   | YISP B.V.        | 154.84.1.137                  | Yes (Region: NL) |
|  7 | [16](config/16.json) | 135.148.67.88  | United States | US   | OVH SAS          | 2604:2dc0:100:5844::2e6a:6563 | Yes (Region: US) |
|  8 | [17](config/17.json) | 146.190.93.191 | Singapore     | SG   | DIGITALOCEAN-ASN | 146.190.93.191                | Yes (Region: SG) |
|  9 | [24](config/24.json) | 154.85.1.244   | Netherlands   | NL   | YISP B.V.        | 154.84.1.206                  | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyIiwgImFkZCI6ICI0NS4xOTkuMTM4LjIwNiIsICJwb3J0IjogIjQ0MDk0IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIyMGIzMDkxNi1lMjAzLTQxMmUtOGVjMC05MDBmM2FjZDUxMjgiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYzYjRiODI5LTdmMDEtNGUyNi1iMDM3LWYwNGIxZjA5ODc2NSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Mjk1MiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4MCIsICJwb3J0IjogIjU0ODg1IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJkMzEzMzQ4NC1mMmJmLTRiMGMtOGQzOC1mOGU2NDViNjU2ODciLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny40OCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NTQ5MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA3IiwgImFkZCI6ICIxOTIuNzQuMjI4LjE4OCIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTkyNzQ3MDYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDg1OTYwNTMyMSIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiMTA3LjE2Ny4xNi44NSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNzY0MGExZTctOTcwMS00MjhlLWE0YjItMTliM2U3ZGQ2ZjlmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjUxMTA5MDU3Lnh5eiIsICJwYXRoIjogIi9wYXRoLzA4MDgyMjI3MjkxNCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0OCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjk2NGJmNDk5LTllYzAtNDM3OC05MmI2LTg3ZDhkODYxYjJkMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MTY3MSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTphOWRJWGhQQXVTRENLVVBV@135.148.67.88:2087#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2016
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDE3IiwgImFkZCI6ICIxNDYuMTkwLjkzLjE5MSIsICJwb3J0IjogIjQ0Mjk1IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwYTJiMTY1Mi1kYzE2LTQ3MWEtZjdlZi1mMTFlMmJmNTQ3OTMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU0OTgyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

