
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)
    
    
|    | id                   | addr           | ip            | chatgpt          | netflix        | tiktok           |
|---:|:---------------------|:---------------|:--------------|:-----------------|:---------------|:-----------------|
|  0 | [1](config/1.json)   | 142.4.104.201  | 198.2.193.61  | IP is BLOCKED    | Originals Only | Yes (Region: US) |
|  1 | [2](config/2.json)   | 192.74.228.172 | 142.0.129.201 | IP is BLOCKED    | Originals Only | Yes (Region: US) |
|  2 | [5](config/5.json)   | 156.245.8.53   | 154.84.1.230  | Yes (Region: NL) | Originals Only | Yes (Region: NL) |
|  3 | [11](config/11.json) | 172.99.188.99  | 172.99.188.99 | Yes (Region: NL) | Originals Only | Yes (Region: NL) |
|  4 | [23](config/23.json) | 85.208.108.60  | 85.208.108.58 | Yes (Region: JP) | Originals Only | Yes (Region: JP) |
|  5 | [28](config/28.json) | 85.208.108.60  | 85.208.108.58 | Yes (Region: JP) | Originals Only | Yes (Region: JP) |
|  6 | [30](config/30.json) | 172.99.188.99  | 172.99.188.99 | Yes (Region: NL) | Originals Only | Yes (Region: NL) |
|  7 | [31](config/31.json) | 85.208.108.60  | 85.208.108.58 | Yes (Region: JP) | Originals Only | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAxIiwgImFkZCI6ICIxNDIuNC4xMDQuMjAxIiwgInBvcnQiOiAiNTA1MDIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTkyLjc0LjIyOC4xNzIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDI4NTcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjUzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNjVlYTY3MjctNDQ2MS00N2E3LWE1YzQtZmVmMmM2N2YyZjc5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0MTExLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@172.99.188.99:5004#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2011
ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0@85.208.108.60:8881#github.com/freefq%20-%20%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AFArabic%20Computer%20System%20Co.%2023
ss://YWVzLTI1Ni1nY206ekROVmVkUkZQUWV4Rzl2@85.208.108.60:6379#github.com/freefq%20-%20%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AFArabic%20Computer%20System%20Co.%2028
ss://YWVzLTI1Ni1nY206ekROVmVkUkZQUWV4Rzl2@172.99.188.99:6379#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2030
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@85.208.108.60:2376#github.com/freefq%20-%20%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AFArabic%20Computer%20System%20Co.%2031
```

## Exception
```
ss://YWVzLTI1Ni1nY206WTZSOXBBdHZ4eHptR0M@ak1663.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:5000#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2032
```

## Todo
```
trojan://MkoKA2iMSX@or.blowm1k.club:31263#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%204
```

