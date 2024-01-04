
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn              | cc   | isp                                  | ip              | chatgpt          |
|---:|:---------------------|:----------------------|:----------------|:-----|:-------------------------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 45.87.153.246         | The Netherlands | NL   | Stark Industries Solutions Ltd       | 45.87.153.246   | Yes (Region: NL) |
|  1 | [6](config/6.json)   | 51.158.150.173        | France          | FR   | Scaleway S.a.s.                      | 51.158.150.173  | Yes (Region: FR) |
|  2 | [7](config/7.json)   | 38.121.43.65          | United States   | US   | AS-GLOBALTELEHOST                    | 38.121.43.65    | Yes (Region: US) |
|  3 | [11](config/11.json) | 198.2.200.37          | United States   | US   | PEG-SV                               | 142.4.98.185    | Yes (Region: US) |
|  4 | [14](config/14.json) | 45.8.147.80           | Sweden          | SE   | Stark Industries Solutions Ltd       | 45.8.147.80     | Yes (Region: SE) |
|  5 | [15](config/15.json) | 192.74.249.4          | China           | CN   | PEG-SV                               | 192.74.249.1    | Yes (Region: US) |
|  6 | [16](config/16.json) | 217.160.45.31         | Germany         | DE   | IONOS SE                             | 217.160.45.31   | Yes (Region: DE) |
|  7 | [20](config/20.json) | 217.182.198.219       | Germany         | DE   | OVH SAS                              | 217.182.198.219 | Yes (Region: DE) |
|  8 | [35](config/35.json) | data-us-v1.shwjfkw.cn | United States   | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138 | Yes (Region: US) |
|  9 | [37](config/37.json) | 77.246.101.245        | The Netherlands | NL   | Servers Tech Fzco                    | 77.246.101.245  | Yes (Region: NL) |
| 10 | [45](config/45.json) | 145.239.6.202         | United Kingdom  | GB   | OVH SAS                              | 145.239.6.202   | Yes (Region: GB) |
| 11 | [57](config/57.json) | 54.36.174.181         | Poland          | PL   | OVH SAS                              | 54.36.174.181   | Yes (Region: FR) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%203
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@51.158.150.173:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E5%B7%B4%E9%BB%8EOnline%20S.A.S%206
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.121.43.65:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%207
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgMTEiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2014
vmess://eyJhZGQiOiAiMTkyLjc0LjI0OS40IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuMzc3OTA5NTgueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAxNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@217.182.198.219:2376#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%20SAS%2020
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTc5ZmJcdTUyYTggMzUiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp5eC1QOWF5Z05NLVYtYm9PMVVHUWVn@77.246.101.245:1165#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2037
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@145.239.6.202:4444#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%20%2045
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@54.36.174.181:7002#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2057
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTVmMTdcdTU0MDlcdTVjM2NcdTRlOWFcdTVkZGVcdTk2M2ZcdTRlYzBcdTY3MmNPcmFjbGVcdTRlOTFcdThiYTFcdTdiOTdcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNjAiLCAiYWRkIjogIjEzMi4xNDUuMTMyLjIyNyIsICJwb3J0IjogIjM3MTIxIiwgImlkIjogIjkzODQ1YjUwLTI2ZjYtNDIwMy1mNWFkLTRkMjMxZDRlOGY0NSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

