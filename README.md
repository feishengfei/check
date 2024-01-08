
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn             | cc   | isp                                  | ip              | chatgpt          |
|---:|:---------------------|:----------------------|:---------------|:-----|:-------------------------------------|:----------------|:-----------------|
|  0 | [1](config/1.json)   | 51.142.78.104         | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK          | 51.142.78.104   | Yes (Region: GB) |
|  1 | [2](config/2.json)   | 51.145.68.57          | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK          | 51.145.68.57    | Yes (Region: GB) |
|  2 | [3](config/3.json)   | 51.142.73.20          | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK          | 51.142.73.20    | Yes (Region: GB) |
|  3 | [10](config/10.json) | 38.54.185.112         | China          | CN   | PEG-SV                               | 192.74.239.146  | Yes (Region: US) |
|  4 | [12](config/12.json) | 112.28.208.10         | Japan          | JP   | BGPNET Global ASN                    | 134.122.133.144 | Yes (Region: SG) |
|  5 | [29](config/29.json) | 145.239.6.202         | United Kingdom | GB   | OVH SAS                              | 145.239.6.202   | Yes (Region: GB) |
|  6 | [36](config/36.json) | data-us-v1.shwjfkw.cn | United States  | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138 | Yes (Region: US) |
|  7 | [38](config/38.json) | 38.54.185.111         | China          | CN   | PEG-SV                               | 192.74.239.146  | Yes (Region: US) |
|  8 | [41](config/41.json) | 38.54.108.222         | United States  | US   | Kaopu Cloud HK Limited               | 38.54.108.222   | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo4S2psMzdCRXhRdUtTRGdSaGNGTUM5@51.142.78.104:34817#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%201
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpLbEpsWFhlOUtqUVg0bWg0eEMwNWM5@51.145.68.57:13751#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%202
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp0QW9XenVLdk5PUHJzTGM0ZkFFT25v@51.142.73.20:6961#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%203
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMTAiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMTA5MTEzMzQwOSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjExMi4yOC4yMDguMTAiLCAicG9ydCI6ICI0NjYwMiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@145.239.6.202:4444#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%20%2029
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTc5ZmJcdTUyYTggMzYiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMzgiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMDY1NzYyNTE4MSIsICJ0bHMiOiAidGxzIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.54.108.222:8119#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2041
```

