
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn              | cc   | isp                            | ip                | chatgpt          |
|---:|:---------------------|:----------------|:----------------|:-----|:-------------------------------|:------------------|:-----------------|
|  0 | [2](config/2.json)   | 38.75.136.135   | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.135     | Yes (Region: US) |
|  1 | [4](config/4.json)   | 38.75.136.135   | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.135     | Yes (Region: US) |
|  2 | [9](config/9.json)   | 45.87.153.246   | The Netherlands | NL   | Stark Industries Solutions Ltd | 45.87.153.246     | Yes (Region: NL) |
|  3 | [13](config/13.json) | 217.160.45.31   | Germany         | DE   | IONOS SE                       | 217.160.45.31     | Yes (Region: DE) |
|  4 | [14](config/14.json) | 192.74.249.4    | China           | CN   | PEG-SV                         | 192.74.249.1      | Yes (Region: US) |
|  5 | [20](config/20.json) | 198.2.200.37    | United States   | US   | PEG-SV                         | 142.4.98.185      | Yes (Region: US) |
|  6 | [33](config/33.json) | us2.awslcn.info | United States   | US   | DIGITALOCEAN-ASN               | 159.223.119.235   | Yes (Region: US) |
|  7 | [35](config/35.json) | 217.182.198.219 | Germany         | DE   | OVH SAS                        | 217.182.198.219   | Yes (Region: DE) |
|  8 | [40](config/40.json) | 77.246.101.245  | The Netherlands | NL   | Servers Tech Fzco              | 77.246.101.245    | Yes (Region: NL) |
|  9 | [42](config/42.json) | cm1.awslcn.info | Australia       | AU   | AS-CHOOPA                      | 149.28.177.17     | Yes (Region: US) |
| 10 | [50](config/50.json) | 162.159.129.87  | The Netherlands | NL   | Aeza International Ltd         | 2a12:5940:14a8::2 | Yes (Region: NL) |
| 11 | [54](config/54.json) | 45.8.147.80     | Sweden          | SE   | Stark Industries Solutions Ltd | 45.8.147.80       | Yes (Region: SE) |
| 12 | [56](config/56.json) | 38.75.136.49    | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49      | Yes (Region: US) |
| 13 | [71](config/71.json) | 103.159.206.35  | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35    | Yes (Region: TW) |
| 14 | [72](config/72.json) | 154.90.39.63    | Malaysia        | MY   | Kaopu Cloud HK Limited         | 154.90.39.63      | Yes (Region: MY) |

## Valid
```
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@38.75.136.135:7002#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%202
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.75.136.135:8118#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%204
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%209
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCAxMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTkyLjc0LjI0OS40IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuMzc3OTA5NTgueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgMjAiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMzMiLCAiYWRkIjogInVzMi5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1MjU3IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogInVzMi5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@217.182.198.219:2376#github.com/freefq%20-%20%E6%B3%95%E5%9B%BDOVH%20SAS%2035
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp5eC1QOWF5Z05NLVYtYm9PMVVHUWVn@77.246.101.245:1165#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2040
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggNDIiLCAiYWRkIjogImNtMS5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1Mjg2IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImNtMS5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTc5ZmJcdTUyYTggNDQiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDUwIiwgImFkZCI6ICIxNjIuMTU5LjEyOS44NyIsICJwb3J0IjogIjIwOTYiLCAiaWQiOiAiMTIwMDllNTctNmZkOC00NmQ2LTk0YWYtNTM5NTE0YTdlN2M3IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzMS5zaGFyZ2guc2hvcCIsICJwYXRoIjogIi8iLCAidGxzIjogInRscyIsICJzbmkiOiAiczU2Nzg1NDMuc2hhcmdoLnNob3AiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2054
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2056
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDcxIiwgImFkZCI6ICIxMDMuMTU5LjIwNi4zNSIsICJwb3J0IjogIjMxOTQ1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiZTJlNTExYjAtN2RlZi00ZTFiLWQyMzgtNmNiNTM5MWIyZTNmIiwgInNuaSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIn0=
vmess://eyJhZGQiOiAiMTU0LjkwLjM5LjYzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZlx1NzI3OVx1NTIyYlx1ODg0Y1x1NjUzZlx1NTMzYSA3MiIsICJwb3J0IjogNDUzNDMsICJpZCI6ICIwOGFhODQ5OS1kNjE2LTRmZjEtZDZhYi1jZTBjNTIyODI0YWEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

