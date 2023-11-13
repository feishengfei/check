
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn            | cc   | isp                             | ip             | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:--------------|:-----|:--------------------------------|:---------------|:-----------------|
|  0 | [6](config/6.json)   | 198.2.193.152                                                                                   | China         | CN   | PEG-SV                          | 198.2.193.145  | Yes (Region: US) |
|  1 | [15](config/15.json) | 183.233.187.214                                                                                 | Hong Kong     | HK   | CNSERVERS                       | 172.247.18.74  | Yes (Region: US) |
|  2 | [18](config/18.json) | ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland        | PL   | OVH SAS                         | 54.36.174.181  | Yes (Region: FR) |
|  3 | [26](config/26.json) | tg_mfbpn_d4.52vpn.eu.org                                                                        | Hong Kong     | HK   | Vertex Connectivity LLC         | 23.158.104.198 | Yes (Region: JP) |
|  4 | [27](config/27.json) | n1697555560.aaigefm.cn                                                                          | United States | US   | Alibaba US Technology Co., Ltd. | 47.76.35.240   | Yes (Region: US) |
|  5 | [29](config/29.json) | 54.36.174.181                                                                                   | Poland        | PL   | OVH SAS                         | 54.36.174.181  | Yes (Region: FR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA2IiwgImFkZCI6ICIxOTguMi4xOTMuMTUyIiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiNjhkMjM4Y2UtM2NhMS00NmRjLWI4MzMtYTA5MTZjODI5YWQzIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjI4MjUxNjU4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTk2MjQ3MjMyMTMiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMTUiLCAiYWRkIjogIjE4My4yMzMuMTg3LjIxNCIsICJwb3J0IjogIjM4OTYyIiwgImlkIjogIjc3MGVlNzMwLTI0NTAtNGUzYy1hNmM2LTM5MzJiZDMyYWZiZCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2018
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMjUiLCAiYWRkIjogIm4xNjk5MjUzNzY5LmFhaWdlZm0uY24iLCAicG9ydCI6IDQ0MywgImlkIjogIjk4MmZhZGQxLTNlNWYtNGFhMy04NTUyLWVkNmZkYTIzNDE0YSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAibjE2OTkyNTM3NjkuYWFpZ2VmbS5jbiIsICJwYXRoIjogIi8iLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjYiLCAiYWRkIjogInRnX21mYnBuX2Q0LjUydnBuLmV1Lm9yZyIsICJwb3J0IjogIjExMDAyIiwgImlkIjogIjg1ZGI2NjUyLWE3NDctM2EwYS1hMTcwLTQyMjczNjA3NjQxMCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMjciLCAiYWRkIjogIm4xNjk3NTU1NTYwLmFhaWdlZm0uY24iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNTY2OTFjM2MtYjlhNS00NDBmLWE2NzgtNDc4NjE4ODU0ZTc1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJuMTY5NzU1NTU2MC5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@54.36.174.181:6697#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2029
```

