
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn          | cc   | isp                            | ip              | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:------------|:-----|:-------------------------------|:----------------|:-----------------|
|  0 | [1](config/1.json)   | 183.233.187.214                                                                                 | China       | CN   | CNSERVERS                      | 192.151.223.154 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 94.131.12.58                                                                                    | Switzerland | CH   | Stark Industries Solutions Ltd | 94.131.12.58    | Yes (Region: CH) |
|  2 | [5](config/5.json)   | 94.131.115.129                                                                                  | Sweden      | SE   | Stark Industries Solutions Ltd | 94.131.115.129  | Yes (Region: SE) |
|  3 | [8](config/8.json)   | 183.237.20.148                                                                                  | Germany     | DE   | OVH SAS                        | 51.77.66.34     | Yes (Region: DE) |
|  4 | [10](config/10.json) | xyfxhiogo.site                                                                                  | Italy       | IT   | G-Core Labs S.A.               | 45.92.70.19     | Yes (Region: IT) |
|  5 | [14](config/14.json) | 45.159.249.231                                                                                  | Finland     | FI   | Stark Industries Solutions Ltd | 45.159.249.231  | Yes (Region: FI) |
|  6 | [15](config/15.json) | ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  7 | [20](config/20.json) | 54.36.174.181                                                                                   | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  8 | [21](config/21.json) | 54.36.174.181                                                                                   | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMSIsICJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgInBvcnQiOiAiNTA5NjUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCMHJ5NTZYMkF4ZkZnY2dJN3NIRFdE@94.131.12.58:26669#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpiTlVlMGpSOXJ6c3ZMRXpmUG1JNE9m@94.131.115.129:38108#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%205
vmess://eyJhZGQiOiAiMTgzLjIzNy4yMC4xNDgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTI3MDcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWU3Zlx1NGUxY1x1NzcwMVx1NzlmYlx1NTJhOCA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICJ4eWZ4aGlvZ28uc2l0ZSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI0ZmEzNWVhNC02NjhlLTRkN2ItOWJiYy1iODM2ODEwNjA2MTciLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInh5ZnhoaW9nby5zaXRlIiwgInBhdGgiOiAiL2t3aG12d3MiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2014
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2015
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@54.36.174.181:2375#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2020
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@54.36.174.181:7307#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2021
```

