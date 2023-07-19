
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp                              | ip                                   | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:---------------------------------|:-------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 156.249.18.14        | Netherlands   | NL   | YISP B.V.                        | 154.84.1.193                         | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 45.199.138.90        | Netherlands   | NL   | YISP B.V.                        | 154.84.1.159                         | Yes (Region: NL) |
|  2 | [7](config/7.json)   | 45.199.138.136       | Netherlands   | NL   | YISP B.V.                        | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  3 | [8](config/8.json)   | sg.669990.xyz        | Netherlands   | NL   | YISP B.V.                        | 154.84.1.197                         | Yes (Region: NL) |
|  4 | [11](config/11.json) | cdn.ikuan.dev        | United States | US   | AS-COLOCROSSING                  | 198.46.173.131                       | Yes (Region: US) |
|  5 | [17](config/17.json) | cfcdn2.sanfencdn.net | United States | US   | Eons Data Communications Limited | 38.207.156.106                       | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTU2LjI0OS4xOC4xNCIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjkwIiwgInBvcnQiOiAiNDgxMjMiLCAiaWQiOiAiMDc4ZWIyNGQtOGQxZC00ZmJkLWI5MTQtZWU1OGE4OTdhMzVlIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmM1x1ZDgzY1x1ZGRmMU5MXHU4Mzc3XHU1MTcwKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiL2lzYWlmcWFhZ3BpIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEzNiIsICJwb3J0IjogIjQ4MzQ0IiwgImlkIjogIjc0M2JkYzg3LTFkZWEtNDFiZi1hYTBiLTUxZGZiYmZlYzhhYSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAic2cuNjY5OTkwLnh5eiIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiODkwNGUzNzgtZjY2Ny00MWVkLTkwODctMDA4MWU5YWM0NDZlIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NDA0NCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgOCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiY2RuLmlrdWFuLmRldiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDExIiwgInBvcnQiOiAyMDUyLCAiaWQiOiAiMzE4NWMyZjMtNDI0Ni00OWM0LWJhOGEtNWVhOGZiMmVmNmI4IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogImZyZWVmb3JnZncuaWt1YW4uZGV2IiwgInBhdGgiOiAiL0ZyZWVGb3JHRlciLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE3IiwgImFkZCI6ICJjZmNkbjIuc2FuZmVuY2RuLm5ldCIsICJwb3J0IjogMjA1MiwgImlkIjogIjkxYjlkYTQ5LWNiNTMtNGU4Mi05NzMyLTg3MzY5MzQ3MDQ0MCIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAidXM2LnNhbmZlbmNkbjIuY29tIiwgInBhdGgiOiAiL3poLWNuIiwgInRscyI6ICIifQ==
```

