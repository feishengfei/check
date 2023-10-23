
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp          | ip            | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-------------|:--------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.98.225    | China         | CN   | PEG-SV       | 142.0.129.201 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 104.233.249.242 | China         | CN   | PEG-SV       | 142.4.99.65   | Yes (Region: US) |
|  2 | [4](config/4.json)   | 142.4.112.135   | United States | US   | PEG-SV       | 38.54.250.33  | Yes (Region: US) |
|  3 | [5](config/5.json)   | 45.199.138.186  | Netherlands   | NL   | YISP B.V.    | 154.84.1.122  | Yes (Region: NL) |
|  4 | [9](config/9.json)   | 156.249.18.4    | Netherlands   | NL   | YISP B.V.    | 154.84.1.148  | Yes (Region: NL) |
|  5 | [16](config/16.json) | 156.225.67.104  | Netherlands   | NL   | YISP B.V.    | 154.84.1.44   | Yes (Region: NL) |
|  6 | [19](config/19.json) | 51vfly1.win     | Germany       | DE   | Contabo GmbH | 5.189.166.24  | Yes (Region: DE) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC45OC4yMjUiLCAicG9ydCI6IDQ0MywgImlkIjogIjA1MWI4NDRmLWVmZTMtNDg0Ny05MmFhLTY2YjVkZTBiNmQ0ZSIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41OTI3NDcwNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3OTgwMTAxMjQ5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNQRUcgVEVDSCAzIiwgImFkZCI6ICIxMDQuMjMzLjI0OS4yNDIiLCAicG9ydCI6IDQ0MywgImlkIjogImI2NWRhNGFmLWExMmEtNGE1OS05MzE2LTQ1NDllMTJiYTYyYyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy43MzMzMjQ2My54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3OTgwMTAxMjQ5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA0IiwgImFkZCI6ICIxNDIuNC4xMTIuMTM1IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy44MDEyODY5My54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3OTgwMTAxMjQ5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NzM3Njc4Mjg3OSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAiMTU2LjI0OS4xOC40IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjg0ZDFkZTExLWNlMTItNGExNS04MzEyLTEzMzgzNTZkNGFjNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41NzQyNDM0OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3NzE5NTA2Mjc1IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE2IiwgImFkZCI6ICIxNTYuMjI1LjY3LjEwNCIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE5IiwgImFkZCI6ICI1MXZmbHkxLndpbiIsICJwb3J0IjogNDQzLCAiaWQiOiAiOTY4MWY5OWUtZDI1MS00NzdhLWQ3NzctMWQwMWVlNTUwNDgxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICI1MXZmbHkxLndpbiIsICJwYXRoIjogIi9teWJsb2ciLCAidGxzIjogInRscyJ9
```

