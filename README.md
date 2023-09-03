
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr          | cn          | cc   | isp       | ip            | chatgpt          |
|---:|:---------------------|:--------------|:------------|:-----|:----------|:--------------|:-----------------|
|  0 | [2](config/2.json)   | 46.182.107.22 |             |      |           | 154.84.1.16   | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.245.8.247 |             |      |           | 154.84.1.137  | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 154.85.1.245  |             |      |           | 154.84.1.206  | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 156.225.67.95 | Poland      | PL   | OVH SAS   | 54.36.174.181 | Yes (Region: FR) |
|  4 | [10](config/10.json) | 156.245.8.219 | Netherlands | NL   | YISP B.V. | 154.84.1.134  | Yes (Region: NL) |
|  5 | [11](config/11.json) | 156.225.67.23 | Netherlands | NL   | YISP B.V. | 154.84.1.193  | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiNDYuMTgyLjEwNy4yMiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImRlNDkxODAyLTIzM2UtNDdmMi04YzZjLWQxOWJjZjViZDU2YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NDg1NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4Mzc3XHU1MTcwICAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0NyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjk2NGJmNDk5LTllYzAtNDM3OC05MmI2LTg3ZDhkODYxYjJkMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNjUxNywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMjQ1IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ5OTIxLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny45NSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzMTk2NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjIxOSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMyMTU5ODc3Lnh5eiIsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MzY1MDkwMjg5MyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDEwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yMyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzU1NCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAxMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

