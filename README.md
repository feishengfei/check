
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp              | ip                         | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:-----------------|:---------------------------|:-----------------|
|  0 | [4](config/4.json)   | 139.99.245.164      | Australia     | AU   | OVH SAS          | 139.99.130.144             | Yes (Region: AU) |
|  1 | [6](config/6.json)   | 54.36.174.181       | Poland        | PL   | OVH SAS          | 54.36.174.181              | Yes (Region: FR) |
|  2 | [13](config/13.json) | pzl.p237875155.buzz | United States | US   | AS-COLOCROSSING  | 2a09:bac1:7680:99d8::4:329 | Yes (Region: US) |
|  3 | [15](config/15.json) | 45.199.138.161      | Netherlands   | NL   | YISP B.V.        | 46.182.107.129             | Yes (Region: NL) |
|  4 | [24](config/24.json) | 219.76.13.183       | Singapore     | SG   | Datacamp Limited | 5.180.78.163               | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2NPVkggNCIsICJhZGQiOiAiMTM5Ljk5LjI0NS4xNjQiLCAicG9ydCI6ICI0OTkyMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@54.36.174.181:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%206
vmess://eyJhZGQiOiAicHpsLnAyMzc4NzUxNTUuYnV6eiIsICJhaWQiOiAxLCAiaG9zdCI6ICJwemwucDIzNzg3NTE1NS5idXp6IiwgImlkIjogIjliNzhiN2ZlLTQ3YTMtNDFlYi1kNjk1LTIyNjkyYWM4MzVhMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcHpsMjM3ODc1MTU1IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTMiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjEiLCAiYWlkIjogNjQsICJob3N0IjogImNhLmlsb3Zlc2NwLmNvbSIsICJpZCI6ICI5NTQ5YTJjZi0xMjliLTQzYTEtODhkYi1lZjdmNjQ4ZGU3NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9zaGlya2VyIiwgInBvcnQiOiA0NjczNSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgMTUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMjE5Ljc2LjEzLjE4MyIsICJhaWQiOiAxLCAiaG9zdCI6ICJhLmRiLWxpbmsuaW4iLCAiaWQiOiAiN2ZjYjRhMjctZjgxOC0zMzc3LWFmNTYtY2MwOGJjYjQyYjVkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9kYiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTc1MzVcdThiYWZcdTc2YzhcdTc5ZDFcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggMjQiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

