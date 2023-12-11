
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn          | cc   | isp                            | ip              | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:------------|:-----|:-------------------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 94.131.12.58                                                                                    | Switzerland | CH   | Stark Industries Solutions Ltd | 94.131.12.58    | Yes (Region: CH) |
|  1 | [3](config/3.json)   | 45.159.249.231                                                                                  | Finland     | FI   | Stark Industries Solutions Ltd | 45.159.249.231  | Yes (Region: FI) |
|  2 | [4](config/4.json)   | 183.233.187.214                                                                                 | China       | CN   | CNSERVERS                      | 192.151.223.154 | Yes (Region: US) |
|  3 | [8](config/8.json)   | xyfxhiogo.site                                                                                  | Italy       | IT   | G-Core Labs S.A.               | 45.92.70.19     | Yes (Region: IT) |
|  4 | [11](config/11.json) | ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  5 | [14](config/14.json) | 54.36.174.181                                                                                   | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  6 | [19](config/19.json) | www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCMHJ5NTZYMkF4ZkZnY2dJN3NIRFdE@94.131.12.58:26669#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%202
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%203
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggNCIsICJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgInBvcnQiOiAiNTA5NjUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInh5ZnhoaW9nby5zaXRlIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjRmYTM1ZWE0LTY2OGUtNGQ3Yi05YmJjLWI4MzY4MTA2MDYxNyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAieHlmeGhpb2dvLnNpdGUiLCAicGF0aCI6ICIva3dobXZ3cyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2011
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@54.36.174.181:7307#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2014
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:7001#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2019
```

