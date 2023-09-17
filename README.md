
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                 | ip             | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:--------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.99.73     | United States | US   | PEG-SV              | 142.4.99.65    | Yes (Region: US) |
|  1 | [3](config/3.json)   | 192.18.158.46   | Canada        | CA   | ORACLE-BMC-31898    | 192.18.158.46  | Yes (Region: CA) |
|  2 | [4](config/4.json)   | 142.4.104.167   | United States | US   | PEG-SV              | 198.200.56.113 | Yes (Region: US) |
|  3 | [6](config/6.json)   | 107.148.195.129 | United States | US   | PEG-SV              | 192.74.242.166 | Yes (Region: US) |
|  4 | [8](config/8.json)   | 156.225.67.224  | Poland        | PL   | OVH SAS             | 54.36.174.181  | Yes (Region: FR) |
|  5 | [9](config/9.json)   | 104.31.16.69    | Germany       | DE   | Hetzner Online GmbH | 88.99.190.161  | Yes (Region: DE) |
|  6 | [12](config/12.json) | 45.199.138.163  | Netherlands   | NL   | YISP B.V.           | 154.84.1.230   | Yes (Region: NL) |
|  7 | [14](config/14.json) | 156.245.8.169   | Netherlands   | NL   | YISP B.V.           | 154.84.1.158   | Yes (Region: NL) |
|  8 | [17](config/17.json) | 146.190.93.191  | Singapore     | SG   | DIGITALOCEAN-ASN    | 146.190.93.191 | Yes (Region: SG) |
|  9 | [25](config/25.json) | 156.225.67.76   |               |      |                     | 46.182.107.216 | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC45OS43MyIsICJwb3J0IjogNDQzLCAiaWQiOiAiYjY1ZGE0YWYtYTEyYS00YTU5LTkzMTYtNDU0OWUxMmJhNjJjIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjczMzMyNDYzLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ4NTk2MDUzMjEiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiMTkyLjE4LjE1OC40NiIsICJhaWQiOiAwLCAiaG9zdCI6ICJtZWRpYS1leHAxLmxpY2RuLmNvbSIsICJpZCI6ICIyNDFiYzQ0NS1hZjIyLTQ5MGYtZDY4Yi01ZDkyZWJmMjk1ZjgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL09OSElUIiwgInBvcnQiOiAxODQyNCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA0IiwgImFkZCI6ICIxNDIuNC4xMDQuMTY3IiwgInBvcnQiOiA0NDMsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNzIzMDQyODYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDg1OTYwNTMyMSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA2IiwgImFkZCI6ICIxMDcuMTQ4LjE5NS4xMjkiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4zMDM3MjYxNC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0ODU5NjA1MzIxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDgiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjI0IiwgInBvcnQiOiA0NDMsICJpZCI6ICJlYmVjMmFkZi1lOTQwLTQ0NmYtYmVkNC1kOGM5MTE0M2I1NGEiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTY2NTgxODAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDg1OTYwNTMyMSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTA0LjMxLjE2LjY5IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImdlcm1hbnktb25lLnBvcnQ4ODguc2l0ZSIsICJpZCI6ICIxNWJmMGRiNC1mYmZmLTQ2ZDAtYTQ4Ni1iNmU0YTllNzRhOTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjIwODMiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDkiLCAic2N5IjogImF1dG8iLCAic25pIjogImdlcm1hbnktb25lLnBvcnQ4ODguc2l0ZSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI2NWVhNjcyNy00NDYxLTQ3YTctYTVjNC1mZWYyYzY3ZjJmNzkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDg5MTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDEyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE0IiwgImFkZCI6ICIxNTYuMjQ1LjguMTY5IiwgInBvcnQiOiA0NDMsICJpZCI6ICIzYTNjOGE5Yy0zMzRlLTQzNjAtYWRiOC1hODBhNTdkZGNiYmYiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTYwNDY2MjYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDg1OTYwNTMyMSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTQ2LjE5MC45My4xOTEiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjk0OTQ4NjQ0LTM3Y2UtNDcyZi1kMGViLWNkZjFhMmY5NGVlNiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvU0hBTEFOQSIsICJwb3J0IjogNDA4MTMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMTciLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDI1IiwgImFkZCI6ICIxNTYuMjI1LjY3Ljc2IiwgInBvcnQiOiA0NDMsICJpZCI6ICIzZTAxNmM0ZC05ODZlLTQyZGYtODM4Yy02MDQ2ZjNkODllY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNTY0Mjc5OTQueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDg1OTYwNTMyMSIsICJ0bHMiOiAidGxzIn0=
```

