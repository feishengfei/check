
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp              | ip                        | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------|:--------------------------|:-----------------|
|  0 | [2](config/2.json)   | 108.166.203.181 | United States | US   | MULTA-ASN1       | 173.82.156.42             | Yes (Region: US) |
|  1 | [3](config/3.json)   | 107.167.30.132  | United States | US   | SHARKTECH        | 170.178.185.146           | Yes (Region: US) |
|  2 | [4](config/4.json)   | 171.22.116.2    | United States | US   | DEDIPATH-LLC     | 45.83.117.98              | Yes (Region: US) |
|  3 | [5](config/5.json)   | 141.147.153.244 | Japan         | JP   | ORACLE-BMC-31898 | 141.147.153.244           | Yes (Region: JP) |
|  4 | [6](config/6.json)   | 198.2.197.67    | China         | CN   | PEG-SV           | 142.4.105.25              | Yes (Region: US) |
|  5 | [7](config/7.json)   | 156.225.67.151  | Netherlands   | NL   | YISP B.V.        | 154.84.1.194              | Yes (Region: NL) |
|  6 | [8](config/8.json)   | 45.63.106.86    | Poland        | PL   | OVH SAS          | 54.36.174.181             | Yes (Region: FR) |
|  7 | [13](config/13.json) | Shopify.com     | France        | FR   | CLOUDFLARENET    | 2a09:bac5:3262:be::13:266 | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgxIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNjhhNDkxYi03NjRjLTQ0ZDEtODFhNC0zMGRlMTYxMzA4NjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0NDk0NSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTA3LjE2Ny4zMC4xMzIiLCAicG9ydCI6ICI0MzkwMCIsICJpZCI6ICI1OGU1NjBiNC1iYmE2LTQ4NDMtYmU1Zi04MzMyMTAyMmZhMGQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiXHVkODNjXHVkZGZhXHVkODNjXHVkZGY4VVNcdTdmOGVcdTU2ZmQoeW91dHViZVx1OTYzZlx1NGYxZlx1NzlkMVx1NjI4MCkiLCAicGF0aCI6ICIvcGF0aC8yNDM1MzUzMjI5MDYiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgyZjFcdTU2ZmQgIDQiLCAiYWRkIjogIjE3MS4yMi4xMTYuMiIsICJwb3J0IjogIjQxNjY1IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTQxLjE0Ny4xNTMuMjQ0IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNDdkNzEzNS0wOTU0LTQ2YWItYTE5MC0xN2I2Yzg2MzBhODUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDE1NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NzQ1ZVx1NTE3OE9yYWNsZSBDb3Jwb3JhdGlvbiA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA2IiwgImFkZCI6ICIxOTguMi4xOTcuNjciLCAicG9ydCI6ICI0OTkxMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogInYyc2cwMS5mdXFpYW5ncmVuLmNvbSIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNTEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJhN2ZhOGYxNC00ZmI2LTQyODAtOTAwNS1kNmJiZTk5YzVkYTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDY0MTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuNjMuMTA2Ljg2IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI0YzkwZDE2Ny1lNjViLTQ0MTktZDQ1NS1lYjYzNTcyNGQyZWQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzc4NjksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENob29wYVx1NTE2Y1x1NTNmOFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiU2hvcGlmeS5jb20iLCAiYWlkIjogMCwgImhvc3QiOiAiRnIuY2xvdWRmbGFyZS5xdWVzdCIsICJpZCI6ICIyNTBmNDMzMS04YzNlLTRiODctYTg2Yi01YzVmYmY5ZGRiYTgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FyaWVzIiwgInBvcnQiOiAyMDg2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDEzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

