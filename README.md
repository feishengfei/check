
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                              | ip                                     | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:---------------------------------|:---------------------------------------|:-----------------|
|  0 | [13](config/13.json) | 45.77.176.217   | Japan         | JP   | AS-CHOOPA                        | 2001:19f0:7001:21ad:5400:4ff:feaa:a43d | Yes (Region: JP) |
|  1 | [14](config/14.json) | 104.238.182.29  | United States | US   | AS-CHOOPA                        | 2001:19f0:ac00:4abc:5400:4ff:feaa:4caf | Yes (Region: US) |
|  2 | [24](config/24.json) | hk1.awslcn.info | Hong Kong     | HK   | Hong Kong Broadband Network Ltd. | 124.244.178.235                        | Yes (Region: US) |
|  3 | [25](config/25.json) | cm.awslcn.info  | Taiwan        | TW   | ByteVirt LLC                     | 108.165.144.166                        | Yes (Region: US) |
|  4 | [29](config/29.json) | 113.20.28.102   | Indonesia     | ID   | ARDH GLOBAL INDONESIA, PT        | 113.20.28.102                          | Yes (Region: ID) |
|  5 | [45](config/45.json) | 45.121.48.196   | Taiwan        | TW   | EMGINECONCEPT-01                 | 45.121.48.196                          | Yes (Region: TW) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuNzcuMTc2LjIxNyIsICJhaWQiOiAiMCIsICJob3N0IjogIiIsICJpZCI6ICIxZjU3YTFjYy1kMzk1LTRiZGUtYmZjZi1mNjJhOGE0Zjk1NTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjE2MTQyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjXHU0ZTFjXHU0ZWFjQ2hvb3BhXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDEzIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTA0LjIzOC4xODIuMjkiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiNzRjYzgyZmYtZTM5OC00YTBlLWRmOTQtZTVlOWQ2NmFiYmIzIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNTA3MDYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDaG9vcGFcdTUxNmNcdTUzZjhcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMjQiLCAiYWRkIjogImhrMS5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1MjQyIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImhrMS5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMjUiLCAiYWRkIjogImNtLmF3c2xjbi5pbmZvIiwgInBvcnQiOiAiMjUyMzMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjkzZWM3MjYxLTFjOTItNDE0OS04NDhhLTI2YjZmYjlmYzRjZSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiY20uYXdzbGNuLmluZm8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTEzLjIwLjI4LjEwMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDI5IiwgInBvcnQiOiAyMjE4OCwgImlkIjogIjAwNjc3ZWI0LTkxYzItNDFmMS1lNzkwLTk2M2I5YTA5M2ZkNSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDQ1IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiMGVkMzU2MjktOTE5YS00ODkxLWJhMGYtMTNjZDE5OGY4NjNiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

