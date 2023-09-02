
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp       | ip            | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:----------|:--------------|:-----------------|
|  0 | [4](config/4.json)   | 156.245.8.144        |               |      |           | 154.84.1.134  | Yes (Region: NL) |
|  1 | [7](config/7.json)   | 154.84.1.11          | Netherlands   | NL   | YISP B.V. | 154.84.1.178  | Yes (Region: NL) |
|  2 | [8](config/8.json)   | Tokyo.mfa.ee         |               |      |           | 54.36.174.181 | Yes (Region: FR) |
|  3 | [9](config/9.json)   | 156.249.18.26        | Netherlands   | NL   | YISP B.V. | 154.84.1.158  | Yes (Region: NL) |
|  4 | [10](config/10.json) | 156.245.8.168        | Netherlands   | NL   | YISP B.V. | 154.84.1.140  | Yes (Region: NL) |
|  5 | [23](config/23.json) | ci.outline-vpn.cloud | United States | US   | SHARKTECH | 67.21.72.34   | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0NCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMyMTU5ODc3Lnh5eiIsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTQyNzMxMjYzMDE0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZiAgNCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU0Ljg0LjEuMTEiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy40NzczNDY0Ny54eXoiLCAiaWQiOiAiOTM1MDNkZDUtMjQ1YS00ZWIxLWFlMmEtNTdhYjlmMmIzYzI5IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTM1NjQzMTI4OTMiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDciLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiVG9reW8ubWZhLmVlIiwgImFpZCI6IDAsICJob3N0IjogInZucHQuaWlpby53aWtpIiwgImlkIjogIjk5Mjg4OWE3LTI5NmUtNGE0NC05OGMyLTBlYjg5YWY0NDExZCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAyMDUyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4yNiIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjE2MDQ2NjI2Lnh5eiIsICJpZCI6ICIzYTNjOGE5Yy0zMzRlLTQzNjAtYWRiOC1hODBhNTdkZGNiYmYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MzU2NDMxMjg5MyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE2OCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjEyNDYwMTU4Lnh5eiIsICJpZCI6ICJiOGRmM2VmMS04ODdmLTRlZTQtODU1Zi00ZjgwNDE2YzI0NjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5Mjg3MzkyNzU4NyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDEwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2kub3V0bGluZS12cG4uY2xvdWQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIzIiwgInBvcnQiOiA0MzEyMywgImlkIjogIjI1NjZkMDBmLTIxOGMtNDhmNy05YTM2LTEzZDNkNmYxYTcyNCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

