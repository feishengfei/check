
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn              | cc   | isp                                  | ip                                    | chatgpt          |
|---:|:---------------------|:----------------------|:----------------|:-----|:-------------------------------------|:--------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 38.91.100.27          | United States   | US   | AS-GLOBALTELEHOST                    | 38.91.100.27                          | Yes (Region: US) |
|  1 | [2](config/2.json)   | 38.91.100.27          | United States   | US   | AS-GLOBALTELEHOST                    | 38.91.100.27                          | Yes (Region: US) |
|  2 | [4](config/4.json)   | 96.30.197.59          | United States   | US   | AS-CHOOPA                            | 2001:19f0:5401:2ed1:5400:4ff:fe9d:709 | Yes (Region: US) |
|  3 | [5](config/5.json)   | 45.87.153.246         | The Netherlands | NL   | Stark Industries Solutions Ltd       | 45.87.153.246                         | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 45.8.147.80           | Sweden          | SE   | Stark Industries Solutions Ltd       | 45.8.147.80                           | Yes (Region: SE) |
|  5 | [7](config/7.json)   | 217.160.45.31         | Germany         | DE   | IONOS SE                             | 217.160.45.31                         | Yes (Region: DE) |
|  6 | [8](config/8.json)   | 51.158.150.173        | France          | FR   | Scaleway S.a.s.                      | 51.158.150.173                        | Yes (Region: FR) |
|  7 | [12](config/12.json) | 198.2.200.37          | United States   | US   | PEG-SV                               | 142.4.98.185                          | Yes (Region: US) |
|  8 | [20](config/20.json) | 217.182.198.219       | Germany         | DE   | OVH SAS                              | 217.182.198.219                       | Yes (Region: DE) |
|  9 | [25](config/25.json) | data-us-v1.shwjfkw.cn | United States   | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138                       | Yes (Region: US) |
| 10 | [41](config/41.json) | 192.74.249.4          | China           | CN   | PEG-SV                               | 192.74.249.1                          | Yes (Region: US) |
| 11 | [43](config/43.json) | 154.90.39.63          | Malaysia        | MY   | Kaopu Cloud HK Limited               | 154.90.39.63                          | Yes (Region: MY) |
| 12 | [44](config/44.json) | 132.145.132.227       | United States   | US   | ORACLE-BMC-31898                     | 132.145.132.227                       | Yes (Region: US) |

## Valid
```
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.100.27:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%201
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.91.100.27:5004#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%202
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTRlNTRcdTZjYmJcdTRlOWFcdTZkMzJcdTRlOWFcdTcyNzlcdTUxNzBcdTU5MjdDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiOTYuMzAuMTk3LjU5IiwgInBvcnQiOiAiNTYyNzIiLCAiaWQiOiAiOGU4ZDVhMTAtN2ZkMC00ODE4LTgyNjUtYTRkYzRhNTY5ZDMxIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%205
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%206
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@51.158.150.173:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E5%B7%B4%E9%BB%8EOnline%20S.A.S%208
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgMTIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@217.182.198.219:2376#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%20SAS%2020
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTc5ZmJcdTUyYTggMjUiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
vmess://eyJhZGQiOiAiMTkyLjc0LjI0OS40IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuMzc3OTA5NTgueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNDEiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU0LjkwLjM5LjYzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZlx1NzI3OVx1NTIyYlx1ODg0Y1x1NjUzZlx1NTMzYSA0MyIsICJwb3J0IjogNDUzNDMsICJpZCI6ICIwOGFhODQ5OS1kNjE2LTRmZjEtZDZhYi1jZTBjNTIyODI0YWEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTVmMTdcdTU0MDlcdTVjM2NcdTRlOWFcdTVkZGVcdTk2M2ZcdTRlYzBcdTY3MmNPcmFjbGVcdTRlOTFcdThiYTFcdTdiOTdcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNDQiLCAiYWRkIjogIjEzMi4xNDUuMTMyLjIyNyIsICJwb3J0IjogIjM3MTIxIiwgImlkIjogIjkzODQ1YjUwLTI2ZjYtNDIwMy1mNWFkLTRkMjMxZDRlOGY0NSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

