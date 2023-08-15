
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn             | cc   | isp                    | ip                        | chatgpt          |
|---:|:---------------------|:-------------------|:---------------|:-----|:-----------------------|:--------------------------|:-----------------|
|  0 | [2](config/2.json)   | 198.2.197.67       | China          | CN   | PEG-SV                 | 142.4.105.25              | Yes (Region: US) |
|  1 | [3](config/3.json)   | 64.32.4.53         | United States  | US   | SHARKTECH              | 107.167.13.162            | Yes (Region: US) |
|  2 | [4](config/4.json)   | 156.225.67.151     | Netherlands    | NL   | YISP B.V.              | 154.84.1.194              | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 45.199.138.181     | Netherlands    | NL   | YISP B.V.              | 154.84.1.229              | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 108.166.203.183    | United States  | US   | MULTA-ASN1             | 173.82.156.42             | Yes (Region: US) |
|  5 | [7](config/7.json)   | 64.32.20.97        | United States  | US   | SHARKTECH              | 64.32.0.58                | Yes (Region: US) |
|  6 | [8](config/8.json)   | dongtaiwang3.com   | Poland         | PL   | OVH SAS                | 54.36.174.181             | Yes (Region: FR) |
|  7 | [9](config/9.json)   | 156.245.8.150      | Netherlands    | NL   | YISP B.V.              | 154.84.1.148              | Yes (Region: NL) |
|  8 | [16](config/16.json) | wi.saintink.eu.org | United Kingdom | GB   | Akamai Connected Cloud | 139.162.246.27            | Yes (Region: GB) |
|  9 | [28](config/28.json) | 152.70.242.51      | Singapore      | SG   | Datacamp Limited       | 5.180.78.163              | Yes (Region: TW) |
| 10 | [29](config/29.json) | 140.83.63.38       | Japan          | JP   | ORACLE-BMC-31898       | 140.83.63.38              | Yes (Region: JP) |
| 11 | [30](config/30.json) | Shopify.com        | France         | FR   | CLOUDFLARENET          | 2a09:bac5:3262:be::13:266 | Yes (Region: FR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAyIiwgImFkZCI6ICIxOTguMi4xOTcuNjciLCAicG9ydCI6ICI0OTkxMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogInYyc2cwMS5mdXFpYW5ncmVuLmNvbSIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuNC41MyIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiODY1MzAwNGYtZGU2Ny00NGMyLTljY2UtZTA4MzA5MzNmYjAzIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDM1NTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNTEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJhN2ZhOGYxNC00ZmI2LTQyODAtOTAwNS1kNmJiZTk5YzVkYTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDY0MTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4MSIsICJwb3J0IjogIjQ1Njk1IiwgImlkIjogImQzMTMzNDg0LWYyYmYtNGIwYy04ZDM4LWY4ZTY0NWI2NTY4NyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMjY4YTQ5MWItNzY0Yy00NGQxLTgxYTQtMzBkZTE2MTMwODY3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0OTQ1LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuMjAuOTciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJjMWJhZDlhNi0xNDgyLTQ5NDEtYTBjNC1lODVmM2NiYmNiNWEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDAwMzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogImRvbmd0YWl3YW5nMy5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNmRlZGRiN2YtZTU1Ny00MmRiLWJmYTAtY2Y0MGIzNmIyN2UyIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJkLmZyZWVoMS54eXoiLCAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDkiLCAiYWRkIjogIjE1Ni4yNDUuOC4xNTAiLCAicG9ydCI6ICI0NDE2OSIsICJpZCI6ICI4NGQxZGUxMS1jZTEyLTRhMTUtODMxMi0xMzM4MzU2ZDRhYzQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVmYjdcdTU2ZmRcdTllZDFcdTY4ZWVcdTVkZGVcdTZjZDVcdTUxNzBcdTUxNGJcdTc5OGZDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTYiLCAiYWRkIjogIndpLnNhaW50aW5rLmV1Lm9yZyIsICJwb3J0IjogIjQ0MyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92dWsyLjBiYWQuY29tL2NoYXQiLCAiaG9zdCI6ICJzdWIyLnNhaW50aW5rLmV1Lm9yZyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTUyLjcwLjI0Mi41MSIsICJhaWQiOiAiMSIsICJhbHBuIjogIiIsICJob3N0IjogImMuY24tZGIudG9wIiwgImlkIjogImU3MzRiODNhLTUzMjQtM2JmMC1iMWEzLTFjZjNlMzk5YjZmZiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvZGIiLCAicG9ydCI6ICI4MDgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAyOCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTQwLjgzLjYzLjM4IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiOTRjNWVmMzctNGQ4Mi00OWY5LWM2MjQtZjAxMjU5Mzc0YTE3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDI0NDQ1LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWEgIDI5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiU2hvcGlmeS5jb20iLCAiYWlkIjogMCwgImhvc3QiOiAiRnIuY2xvdWRmbGFyZS5xdWVzdCIsICJpZCI6ICIyNTBmNDMzMS04YzNlLTRiODctYTg2Yi01YzVmYmY5ZGRiYTgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FyaWVzIiwgInBvcnQiOiAyMDg2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDMwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

