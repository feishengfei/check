
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn            | cc   | isp                             | ip            | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:--------------|:-----|:--------------------------------|:--------------|:-----------------|
|  0 | [4](config/4.json)   | 198.2.193.152                                                                                   | China         | CN   | PEG-SV                          | 198.2.193.145 | Yes (Region: US) |
|  1 | [14](config/14.json) | 45.199.138.146                                                                                  | Netherlands   | NL   | YISP B.V.                       | 154.84.1.122  | Yes (Region: NL) |
|  2 | [30](config/30.json) | bjcu.xzyunjiasu.icu                                                                             | United States | US   | PONYNET                         | 209.141.58.10 | Yes (Region: US) |
|  3 | [33](config/33.json) | n1697685464.aaigefm.cn                                                                          | United States | US   | Alibaba US Technology Co., Ltd. | 47.76.44.192  | Yes (Region: US) |
|  4 | [34](config/34.json) | ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland        | PL   | OVH SAS                         | 54.36.174.181 | Yes (Region: FR) |
|  5 | [37](config/37.json) | 54.36.174.181                                                                                   | Poland        | PL   | OVH SAS                         | 54.36.174.181 | Yes (Region: FR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA0IiwgImFkZCI6ICIxOTguMi4xOTMuMTUyIiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiNjhkMjM4Y2UtM2NhMS00NmRjLWI4MzMtYTA5MTZjODI5YWQzIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjI4MjUxNjU4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTk2MjQ3MjMyMTMiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNCIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNDYiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjE5MjI5MzYyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkxOTMxMDAzODgiLCAidGxzIjogInRscyJ9
ss://YWVzLTI1Ni1nY206NWM4YjIxMGEtMmYwMC00MjkyLTk2NGItMDUyODFjN2FkNWQx@bjcu.xzyunjiasu.icu:33952#github.com/freefq%20-%20%E6%B9%96%E5%8D%97%E7%9C%81%E8%81%94%E9%80%9A%2030
vmess://eyJhZGQiOiAibjE2OTc2ODU0NjQuYWFpZ2VmbS5jbiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMzMiLCAicG9ydCI6IDQ0MywgImlkIjogIjE4NzAwMmZkLWI4YWQtNGQzNi1iNGZiLTFhMzIyNGNjOTllMiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJuMTY5NzY4NTQ2NC5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2034
ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@54.36.174.181:6697#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2037
```

