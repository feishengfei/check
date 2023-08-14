
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn          | cc   | isp       | ip             | chatgpt          |
|---:|:---------------------|:---------------------|:------------|:-----|:----------|:---------------|:-----------------|
|  0 | [4](config/4.json)   | 183.232.249.189      | Hong Kong   | HK   | CNSERVERS | 172.247.175.42 | Yes (Region: US) |
|  1 | [5](config/5.json)   | 156.245.8.185        | Netherlands | NL   | YISP B.V. | 154.84.1.161   | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 156.245.8.240        | Netherlands | NL   | YISP B.V. | 154.84.1.44    | Yes (Region: NL) |
|  3 | [8](config/8.json)   | cfcdn2.sanfencdn.net | Poland      | PL   | OVH SAS   | 54.36.174.181  | Yes (Region: FR) |
|  4 | [10](config/10.json) | 156.245.8.166        | Netherlands | NL   | YISP B.V. | 154.84.1.140   | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTgzLjIzMi4yNDkuMTg5IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU5OTAyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE4NSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjIwMTYzMzIyLnh5eiIsICJpZCI6ICJkNzczNTA1OC0xZGFjLTQ2MTgtOTlmZi0wYWEwNDQxZWMyZDciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MTc1MDI1OTAxMiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0MCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NDMyNiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmY2RuMi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiMjA1MiIsICJpZCI6ICI3OGQ2ZmE4OC0wZDI3LTQxNGYtOGY1MS0xZTE2MTg2ZDU4OGYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVzNy5zYW5mZW5jZG4yLmNvbSIsICJwYXRoIjogIi96aC1jbiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE2NiIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjEyNDYwMTU4Lnh5eiIsICJpZCI6ICJiOGRmM2VmMS04ODdmLTRlZTQtODU1Zi00ZjgwNDE2YzI0NjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MTgwMTc4NTM2OSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDEwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

