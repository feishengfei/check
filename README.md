
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp        | ip             | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.10.118    | United States | US   | SHARKTECH  | 64.32.10.114   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 23.234.228.37   | United States | US   | MULTA-ASN1 | 173.82.54.26   | Yes (Region: US) |
|  2 | [6](config/6.json)   | 67.21.91.136    | United States | US   | SHARKTECH  | 67.21.79.130   | Yes (Region: US) |
|  3 | [16](config/16.json) | 142.4.99.83     | China         | CN   | PEGTECHINC | 142.4.99.65    | Yes (Region: US) |
|  4 | [25](config/25.json) | gzdx.jcnode.top | Singapore     | SG   | OVH SAS    | 15.235.184.228 | Yes (Region: SG) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMTAuMTE4IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYzUyOGQ4ZDgtOTRkNi00OGE5LThkZDMtNTI4OTI1NThhNmFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQxMTY5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMjMuMjM0LjIyOC4zNyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImMxNzg1NGJjLTRjNjEtNDBjOC04MTk5LWRhZGIxZGMwZGQxMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MDA4OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjcuMjEuOTEuMTM2IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiZWMxODZjYWQtNTZhYy00MmIzLTgzMDktMTg0ZDBlNzQ4YjA0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDMwOTgzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTQyLjQuOTkuODMiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy43MzMzMjQ2My54eXoiLCAiaWQiOiAiYjY1ZGE0YWYtYTEyYS00YTU5LTkzMTYtNDU0OWUxMmJhNjJjIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2ODQ0OTI1MzYyMzYiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0ggMTYiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://YWVzLTI1Ni1nY206MDUyYmM3NjktMDQ4OS00OWM3LTk3ZjItNTFiM2JiOGU1NDg2@gzdx.jcnode.top:23001#github.com/freefq%20-%20%E6%B5%99%E6%B1%9F%E7%9C%81%E5%98%89%E5%85%B4%E5%B8%82%E7%94%B5%E4%BF%A1IDC%E6%9C%BA%E6%88%BF%2025
```

