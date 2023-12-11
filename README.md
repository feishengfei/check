
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 95.164.87.138                                                                                   | The Netherlands | NL   | Stark Industries Solutions Ltd | 95.164.87.138                          | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 64.31.55.5                                                                                      | United States   | US   | LIMESTONENETWORKS              | 64.31.55.5                             | Yes (Region: US) |
|  2 | [5](config/5.json)   | 94.131.12.58                                                                                    | Switzerland     | CH   | Stark Industries Solutions Ltd | 94.131.12.58                           | Yes (Region: CH) |
|  3 | [7](config/7.json)   | ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland          | PL   | OVH SAS                        | 54.36.174.181                          | Yes (Region: FR) |
|  4 | [14](config/14.json) | 183.233.187.214                                                                                 | China           | CN   | CNSERVERS                      | 192.151.223.154                        | Yes (Region: US) |
|  5 | [30](config/30.json) | www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland          | PL   | OVH SAS                        | 54.36.174.181                          | Yes (Region: FR) |
|  6 | [31](config/31.json) | 64.176.58.15                                                                                    | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3dec:5400:4ff:feaa:9fd8 | Yes (Region: JP) |
|  7 | [32](config/32.json) | 45.91.81.15                                                                                     | United States   | US   | FD-298-8796                    | 45.91.81.15                            | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkUFc2U0toVmZxRGV2QmZkcnQ1ZUpn@95.164.87.138:63830#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%202
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@64.31.55.5:11223#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%BE%97%E5%85%8B%E8%90%A8%E6%96%AF%E5%B7%9E%E8%BE%BE%E6%8B%89%E6%96%AFLimestone%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCMHJ5NTZYMkF4ZkZnY2dJN3NIRFdE@94.131.12.58:26669#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%205
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%207
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMTQiLCAiYWRkIjogIjE4My4yMzMuMTg3LjIxNCIsICJwb3J0IjogIjUwOTY1IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:7001#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2030
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMzEiLCAiYWRkIjogIjY0LjE3Ni41OC4xNSIsICJwb3J0IjogIjQ2MTU0IiwgImlkIjogImFkY2JlMTYwLTMwMTAtNDgzZC1iNDM4LWQ2MDU3ZjQ2NWIxZCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZLVVJVTiBDTE9VRCBJTkMgMzIiLCAiYWRkIjogIjQ1LjkxLjgxLjE1IiwgInBvcnQiOiAiNTk2NjUiLCAiaWQiOiAiMjE5N2I5MzgtYTkwNC00MmQxLWNmMjItZTY4ZDVjYTIzNzI2IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

