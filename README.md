
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn             | cc   | isp                    | ip             | chatgpt          |
|---:|:---------------------|:-----------------|:---------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 173.82.67.195    | United States  | US   | MULTA-ASN1             | 23.234.230.34  | Yes (Region: US) |
|  1 | [4](config/4.json)   | 156.225.67.159   | Netherlands    | NL   | YISP B.V.              | 154.84.1.197   | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 156.245.8.84     | Netherlands    | NL   | YISP B.V.              | 154.84.1.161   | Yes (Region: NL) |
|  3 | [8](config/8.json)   | dongtaiwang3.com | Netherlands    | NL   | YISP B.V.              | 154.84.1.197   | Yes (Region: NL) |
|  4 | [10](config/10.json) | 156.249.18.127   | Netherlands    | NL   | YISP B.V.              | 154.84.1.138   | Yes (Region: NL) |
|  5 | [13](config/13.json) | vus5.0bad.com    | United States  | US   | Akamai Connected Cloud | 170.187.203.13 | Yes (Region: US) |
|  6 | [20](config/20.json) | vuk2.0bad.com    | United Kingdom | GB   | Akamai Connected Cloud | 178.79.176.203 | Yes (Region: GB) |

## Valid
```
vmess://eyJhZGQiOiAiMTczLjgyLjY3LjE5NSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjgyNjIwYTZlLWRiZmQtNGQ1Ny04YTU5LTkwMDRhNGJiOWU5MiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNDQxMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNTkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5YzAyNmVmZS02YWYwLTQ2NWYtYjhjMC0zZjU4YzhjMmQ0YzUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDg5MjEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDYiLCAiYWRkIjogIjE1Ni4yNDUuOC44NCIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvdnBuamFudGl0IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogImRvbmd0YWl3YW5nMy5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNmRlZGRiN2YtZTU1Ny00MmRiLWJmYTAtY2Y0MGIzNmIyN2UyIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJkLmZyZWVoMS54eXoiLCAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjE1Ni4yNDkuMTguMTI3IiwgInBvcnQiOiAiNDgxMDAiLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDEzIiwgImFkZCI6ICJ2dXM1LjBiYWQuY29tIiwgInBvcnQiOiA0NDMsICJpZCI6ICI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInZ1czUuMGJhZC5jb20iLCAicGF0aCI6ICIvY2hhdCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAidnVrMi4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9jaGF0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODJmMVx1NTZmZFx1NGYyNlx1NjU2Nkxpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyMCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

