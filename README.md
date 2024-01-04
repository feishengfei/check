
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                            | ip              | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:-------------------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 38.121.43.65    | United States   | US   | AS-GLOBALTELEHOST              | 38.121.43.65    | Yes (Region: US) |
|  1 | [3](config/3.json)   | 45.87.153.246   | The Netherlands | NL   | Stark Industries Solutions Ltd | 45.87.153.246   | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 38.68.134.85    | United States   | US   | AS-GLOBALTELEHOST              | 38.68.134.85    | Yes (Region: US) |
|  3 | [5](config/5.json)   | 217.160.45.31   | Germany         | DE   | IONOS SE                       | 217.160.45.31   | Yes (Region: DE) |
|  4 | [7](config/7.json)   | 38.121.43.65    | United States   | US   | AS-GLOBALTELEHOST              | 38.121.43.65    | Yes (Region: US) |
|  5 | [8](config/8.json)   | 198.2.200.37    | United States   | US   | PEG-SV                         | 142.4.98.185    | Yes (Region: US) |
|  6 | [9](config/9.json)   | 38.75.136.49    | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49    | Yes (Region: US) |
|  7 | [14](config/14.json) | 77.246.101.245  | The Netherlands | NL   | Servers Tech Fzco              | 77.246.101.245  | Yes (Region: NL) |
|  8 | [21](config/21.json) | 145.239.6.202   | United Kingdom  | GB   | OVH SAS                        | 145.239.6.202   | Yes (Region: GB) |
|  9 | [24](config/24.json) | 217.182.198.219 | Germany         | DE   | OVH SAS                        | 217.182.198.219 | Yes (Region: DE) |
| 10 | [48](config/48.json) | 45.121.48.172   | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.172   | Yes (Region: TW) |
| 11 | [51](config/51.json) | 103.159.206.35  | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35  | Yes (Region: TW) |
| 12 | [53](config/53.json) | 192.74.249.4    | China           | CN   | PEG-SV                         | 192.74.249.1    | Yes (Region: US) |
| 13 | [55](config/55.json) | 45.8.147.80     | Sweden          | SE   | Stark Industries Solutions Ltd | 45.8.147.80     | Yes (Region: SE) |
| 14 | [56](config/56.json) | 45.121.48.196   | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196   | Yes (Region: TW) |

## Valid
```
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@38.121.43.65:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%202
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%203
ss://YWVzLTI1Ni1nY206VEV6amZBWXEySWp0dW9T@38.68.134.85:6679#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%204
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.121.43.65:7001#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%207
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgOCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%209
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp5eC1QOWF5Z05NLVYtYm9PMVVHUWVn@77.246.101.245:1165#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2014
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@145.239.6.202:4444#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%20%2021
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@217.182.198.219:2376#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%20SAS%2024
vmess://eyJhZGQiOiAiNDUuMTIxLjQ4LjE3MiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDQ4IiwgInBvcnQiOiAxMDAwMSwgImlkIjogImRiYTUxYTJlLWE3ODgtNDNiNy05YWM0LTlmN2NjMTI1NWYxNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDUxIiwgImFkZCI6ICIxMDMuMTU5LjIwNi4zNSIsICJwb3J0IjogIjMxOTQ1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiZTJlNTExYjAtN2RlZi00ZTFiLWQyMzgtNmNiNTM5MWIyZTNmIiwgInNuaSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIn0=
vmess://eyJhZGQiOiAiMTkyLjc0LjI0OS40IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuMzc3OTA5NTgueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNTMiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2055
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDU2IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
```

