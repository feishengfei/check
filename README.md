
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp           | ip                         | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:--------------|:---------------------------|:-----------------|
|  0 | [1](config/1.json)   | 64.32.4.53          | United States | US   | SHARKTECH     | 107.167.13.162             | Yes (Region: US) |
|  1 | [2](config/2.json)   | 219.76.13.183       |               |      |               | 5.180.78.163               | Yes (Region: SG) |
|  2 | [5](config/5.json)   | pzl.p237875155.buzz | United States | US   | CLOUDFLARENET | 2a09:bac1:7680:99d8::4:329 | Yes (Region: US) |
|  3 | [7](config/7.json)   | 45.199.138.161      | Netherlands   | NL   | YISP B.V.     | 46.182.107.129             | Yes (Region: NL) |
|  4 | [13](config/13.json) | 219.76.13.167       |               |      |               | 5.180.78.163               | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJhZGQiOiAiNjQuMzIuNC41MyIsICJwb3J0IjogIjQzNTU2IiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMjE5Ljc2LjEzLjE4MyIsICJhaWQiOiAxLCAiaG9zdCI6ICJhLmRiLWxpbmsuaW4iLCAiaWQiOiAiN2ZjYjRhMjctZjgxOC0zMzc3LWFmNTYtY2MwOGJjYjQyYjVkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9kYiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTc1MzVcdThiYWZcdTc2YzhcdTc5ZDFcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggMiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAicHpsLnAyMzc4NzUxNTUuYnV6eiIsICJhaWQiOiAxLCAiaG9zdCI6ICJwemwucDIzNzg3NTE1NS5idXp6IiwgImlkIjogIjliNzhiN2ZlLTQ3YTMtNDFlYi1kNjk1LTIyNjkyYWM4MzVhMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcHpsMjM3ODc1MTU1IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgNSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjEiLCAiYWlkIjogNjQsICJob3N0IjogImNhLmlsb3Zlc2NwLmNvbSIsICJpZCI6ICI5NTQ5YTJjZi0xMjliLTQzYTEtODhkYi1lZjdmNjQ4ZGU3NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9zaGlya2VyIiwgInBvcnQiOiA0NjczNSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgNyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMjE5Ljc2LjEzLjE2NyIsICJhaWQiOiAxLCAiaG9zdCI6ICJlLmNuLWRiLnRvcCIsICJpZCI6ICI3ZmNiNGEyNy1mODE4LTMzNzctYWY1Ni1jYzA4YmNiNDJiNWQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2RiIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZlx1NzUzNVx1OGJhZlx1NzZjOFx1NzlkMVx1NjcwOVx1OTY1MFx1NTE2Y1x1NTNmOCAxMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

