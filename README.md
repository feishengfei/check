
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp              | ip              | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:-----------------|:----------------|:-----------------|
|  0 | [4](config/4.json)   | 64.32.20.97      | United States | US   | SHARKTECH        | 64.32.0.58      | Yes (Region: US) |
|  1 | [6](config/6.json)   | 156.225.67.198   | Netherlands   | NL   | YISP B.V.        | 154.84.1.137    | Yes (Region: NL) |
|  2 | [7](config/7.json)   | 198.2.197.67     | China         | CN   | PEG-SV           | 142.4.105.25    | Yes (Region: US) |
|  3 | [8](config/8.json)   | dongtaiwang3.com | Poland        | PL   | OVH SAS          | 54.36.174.181   | Yes (Region: FR) |
|  4 | [11](config/11.json) | 141.147.153.244  | Japan         | JP   | ORACLE-BMC-31898 | 141.147.153.244 | Yes (Region: JP) |
|  5 | [20](config/20.json) | 45.199.138.176   | United States | US   | NovoServe B.V.   | 45.199.138.43   | Yes (Region: US) |
|  6 | [25](config/25.json) | 146.190.106.128  | Singapore     | SG   | DIGITALOCEAN-ASN | 146.190.106.128 | Yes (Region: SG) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMjAuOTciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJjMWJhZDlhNi0xNDgyLTQ5NDEtYTBjNC1lODVmM2NiYmNiNWEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDAwMzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xOTgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5NjRiZjQ5OS05ZWMwLTQzNzgtOTJiNi04N2Q4ZDg2MWIyZDAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzg4NzEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA3IiwgImFkZCI6ICIxOTguMi4xOTcuNjciLCAicG9ydCI6ICI0OTkxMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogInYyc2cwMS5mdXFpYW5ncmVuLmNvbSIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogImRvbmd0YWl3YW5nMy5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNmRlZGRiN2YtZTU1Ny00MmRiLWJmYTAtY2Y0MGIzNmIyN2UyIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJkLmZyZWVoMS54eXoiLCAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTQxLjE0Ny4xNTMuMjQ0IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNDdkNzEzNS0wOTU0LTQ2YWItYTE5MC0xN2I2Yzg2MzBhODUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDE1NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NzQ1ZVx1NTE3OE9yYWNsZSBDb3Jwb3JhdGlvbiAxMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNzYiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI2ZmE1NjBkNC0zNWM1LTQ5NjgtYWRmYy04MTJjNTI4NzhiODQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzY5MTcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDIwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiU2hvcGlmeS5jb20iLCAiYWlkIjogMCwgImhvc3QiOiAiRnIuY2xvdWRmbGFyZS5xdWVzdCIsICJpZCI6ICIyNTBmNDMzMS04YzNlLTRiODctYTg2Yi01YzVmYmY5ZGRiYTgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FyaWVzIiwgInBvcnQiOiAyMDg2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDIyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTQ2LjE5MC4xMDYuMTI4IiwgImFpZCI6IDAsICJob3N0IjogInpvb20udXMiLCAiaWQiOiAiNWE1ZWM2NGQtYmFmZi00OWJiLWFiNmEtZDU5NzhkYzUzZTRhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi90aGFydXdhZnJlZSIsICJwb3J0IjogMTIyODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMjUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

