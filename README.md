
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn             | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:------------------------|:---------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 156.225.67.116          | Netherlands    | NL   | YISP B.V.         | 154.84.1.148   | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 156.249.18.158          | Netherlands    | NL   | YISP B.V.         | 154.84.1.134   | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 156.245.8.205           | Netherlands    | NL   | YISP B.V.         | 154.84.1.36    | Yes (Region: NL) |
|  3 | [8](config/8.json)   | frankfurt.csi7lahsc.com | Germany        | DE   | AS-GLOBALTELEHOST | 193.108.118.34 | Yes (Region: DE) |
|  4 | [11](config/11.json) | 51.195.209.132          | United Kingdom | GB   | OVH SAS           | 51.195.209.132 | Yes (Region: FR) |
|  5 | [14](config/14.json) | cf.durov.ir             | United States  | US   | DEDIPATH-LLC      | 45.12.109.10   | Yes (Region: US) |
|  6 | [24](config/24.json) | 8.v2-ray.cyou           | Japan          | JP   | AMAZON-02         | 18.179.36.139  | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTE2IiwgInBvcnQiOiAiNDQ2NzciLCAiaWQiOiAiODRkMWRlMTEtY2UxMi00YTE1LTgzMTItMTMzODM1NmQ0YWM0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU2LjI0OS4xOC4xNTgiLCAicG9ydCI6ICI0Mzk5OCIsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAiYWRkIjogIjE1Ni4yNDUuOC4yMDUiLCAicG9ydCI6ICI0ODU4OCIsICJpZCI6ICIzZmQ2MzdhZC00NmZlLTRmODUtYTZlOC04NmIwMGJjYTExMjIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTZPcmFjbGUgQ29ycG9yYXRpb24gOCIsICJhZGQiOiAiZnJhbmtmdXJ0LmNzaTdsYWhzYy5jb20iLCAicG9ydCI6ICI5MDAxIiwgImlkIjogImUyYjc1NDlmLTY2N2YtNDFlOC1kNTAxLWFlNTlmYzgyZGI2MCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZnJhbmtmdXJ0LmNzaTdsYWhzYy5jb20iLCAicGF0aCI6ICIvdmlkZW8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNTEuMTk1LjIwOS4xMzIiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImE4NTNkOTFlLWMyOGItNDJjOC1lZTA4LWE0NTc3MTAwNWNjMiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvP2VkPTIwNDgiLCAicG9ydCI6ICIyMDAyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4MmYxXHU1NmZkXHU3OTNlXHU0ZjFhXHU0ZmRkXHU5NjY5XHU1Yjg5XHU1MTY4XHU5MGU4IDExIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICJjZi5kdXJvdi5pciIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJjNzY1NDk4MC03MmZlLTQ5MmQtOGI2Zi1hNGNiNTVjOTRjMmUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImRlZGlwYXRoLmlpaW8ud2lraSIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMjQiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

