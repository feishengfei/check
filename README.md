
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                            | ip                                    | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:-------------------------------|:--------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.87.153.246   | The Netherlands | NL   | Stark Industries Solutions Ltd | 45.87.153.246                         | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 38.75.136.49    | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49                          | Yes (Region: US) |
|  2 | [6](config/6.json)   | 192.74.249.4    | China           | CN   | PEG-SV                         | 192.74.249.1                          | Yes (Region: US) |
|  3 | [11](config/11.json) | 217.160.45.31   | Germany         | DE   | IONOS SE                       | 217.160.45.31                         | Yes (Region: DE) |
|  4 | [12](config/12.json) | sg1.awslcn.info | Singapore       | SG   | DIGITALOCEAN-ASN               | 128.199.208.54                        | Yes (Region: SG) |
|  5 | [18](config/18.json) | 198.2.200.37    | United States   | US   | PEG-SV                         | 142.4.98.185                          | Yes (Region: US) |
|  6 | [29](config/29.json) | 77.246.101.245  | The Netherlands | NL   | Servers Tech Fzco              | 77.246.101.245                        | Yes (Region: NL) |
|  7 | [35](config/35.json) | cm1.awslcn.info | Australia       | AU   | AS-CHOOPA                      | 149.28.177.17                         | Yes (Region: US) |
|  8 | [37](config/37.json) | 45.8.147.80     | Sweden          | SE   | Stark Industries Solutions Ltd | 45.8.147.80                           | Yes (Region: SE) |
|  9 | [47](config/47.json) | 217.182.198.219 | Germany         | DE   | OVH SAS                        | 217.182.198.219                       | Yes (Region: DE) |
| 10 | [66](config/66.json) | 167.179.111.237 | Japan           | JP   | AS-CHOOPA                      | 2001:19f0:7001:244:5400:4ff:feab:d9e2 | Yes (Region: JP) |
| 11 | [70](config/70.json) | 45.121.48.196   | Taiwan          | TW   | EMGINECONCEPT-01               | 45.121.48.196                         | Yes (Region: TW) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%202
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%204
vmess://eyJhZGQiOiAiMTkyLjc0LjI0OS40IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuMzc3OTA5NTgueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAxMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogInNnMS5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1MjQ2IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogInNnMS5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgMTgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp5eC1QOWF5Z05NLVYtYm9PMVVHUWVn@77.246.101.245:1165#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2029
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMzUiLCAiYWRkIjogImNtMS5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1Mjg2IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImNtMS5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2037
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@217.182.198.219:2376#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%20SAS%2047
vmess://eyJhZGQiOiAiMTY3LjE3OS4xMTEuMjM3IiwgImFpZCI6IDAsICJob3N0IjogIjE2Ny4xNzkuMTExLjIzNyIsICJpZCI6ICJlOTYxODk0Zi04ZTkwLTQ3MmYtOThkMy0wOTQwMmU0YmU0NTMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTQ5MzUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY0Nob29wYVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2NiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDcwIiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjBlZDM1NjI5LTkxOWEtNDg5MS1iYTBmLTEzY2QxOThmODYzYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
```

