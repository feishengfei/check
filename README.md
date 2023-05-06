
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp                    | ip                    | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:-----------------------|:----------------------|:-----------------|
|  0 | [2](config/2.json)   | 154.84.1.50      | Netherlands   | NL   | YISP B.V.              | 154.84.1.121          | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 154.85.0.234     | United States | US   | AS-GLOBALTELEHOST      | 169.197.141.187       | Yes (Region: US) |
|  2 | [14](config/14.json) | hd.mamadcucu.com | Germany       | DE   | Hetzner Online GmbH    | 2a01:4f8:c010:7f47::1 | Yes (Region: DE) |
|  3 | [20](config/20.json) | 104.21.44.220    | Argentina     | AR   | InterBS S.R.L. BAEHOST | 131.255.7.29          | Yes (Region: AR) |
|  4 | [28](config/28.json) | 156.245.8.126    | Netherlands   | NL   | YISP B.V.              | 154.84.1.164          | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTU0Ljg0LjEuNTAiLCAicG9ydCI6ICI0OTkyMCIsICJpZCI6ICJiZDI0OWUzNy03MzU5LTQxZWUtODRhNy0wOWU0OWUwZWM1YzQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiMTU0Ljg1LjAuMjM0IiwgInBvcnQiOiAiNTYxMjAiLCAiaWQiOiAiMDc4ZWIyNGQtOGQxZC00ZmJkLWI5MTQtZWU1OGE4OTdhMzVlIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiaGQubWFtYWRjdWN1LmNvbSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE0IiwgInBvcnQiOiAyMDk1LCAiaWQiOiAiMTkzNTBkNjQtNjg2OC00YTY0LWU1MDEtOWMwZGY5MDNkNzg4IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogImgzLm1hbWFkY3VjdS5jb20iLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTA0LjIxLjQ0LjIyMCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIwIiwgInBvcnQiOiAyMDg2LCAiaWQiOiAiMzExZjNjNGItOTBhMS0zYzVjLWE0ZmUtMjE1Y2M3YzkwZDAyIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogImFnMDEtY2RuLm15bjFkZXMuY29tIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDI4IiwgImFkZCI6ICIxNTYuMjQ1LjguMTI2IiwgInBvcnQiOiAiNDc2MjIiLCAiaWQiOiAiM2NhOTEyZGEtNmFjMi00MThmLWI5Y2YtNDViNmY2OTQ1NzliIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

