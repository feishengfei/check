
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp       | ip           | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:----------|:-------------|:-----------------|
|  0 | [5](config/5.json)   | 142.4.99.72    | United States | US   | PEG-SV    | 142.4.99.65  | Yes (Region: US) |
|  1 | [7](config/7.json)   | 156.245.8.168  | Netherlands   | NL   | YISP B.V. | 154.84.1.140 | Yes (Region: NL) |
|  2 | [10](config/10.json) | 156.249.18.29  | Netherlands   | NL   | YISP B.V. | 154.84.1.158 | Yes (Region: NL) |
|  3 | [13](config/13.json) | 156.245.8.144  | Netherlands   | NL   | YISP B.V. | 154.84.1.134 | Yes (Region: NL) |
|  4 | [21](config/21.json) | 156.225.67.205 | Netherlands   | NL   | YISP B.V. | 154.84.1.161 | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA1IiwgImFkZCI6ICIxNDIuNC45OS43MiIsICJwb3J0IjogNDQzLCAiaWQiOiAiYjY1ZGE0YWYtYTEyYS00YTU5LTkzMTYtNDU0OWUxMmJhNjJjIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjczMzMyNDYzLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ2MDQ4MjA0NzgiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE2OCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjEyNDYwMTU4Lnh5eiIsICJpZCI6ICJiOGRmM2VmMS04ODdmLTRlZTQtODU1Zi00ZjgwNDE2YzI0NjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY4NDMxNjc5MDQzMyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDciLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjE1Ni4yNDkuMTguMjkiLCAicG9ydCI6IDQ0MywgImlkIjogIjNhM2M4YTljLTMzNGUtNDM2MC1hZGI4LWE4MGE1N2RkY2JiZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4xNjA0NjYyNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0NjA0ODIwNDc4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDEzIiwgImFkZCI6ICIxNTYuMjQ1LjguMTQ0IiwgInBvcnQiOiA0NDMsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMzIxNTk4NzcueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDYwNDgyMDQ3OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIxIiwgImFkZCI6ICIxNTYuMjI1LjY3LjIwNSIsICJwb3J0IjogNDQzLCAiaWQiOiAiZDc3MzUwNTgtMWRhYy00NjE4LTk5ZmYtMGFhMDQ0MWVjMmQ3IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjIwMTYzMzIyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ2MDQ4MjA0NzgiLCAidGxzIjogInRscyJ9
```

