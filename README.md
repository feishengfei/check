
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn             | cc   | isp                  | ip              | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:---------------|:-----|:---------------------|:----------------|:-----------------|
|  0 | [4](config/4.json)   | la1.121219.xyz                                                                                  | United States  | US   | HVC-AS               | 47.87.214.154   | Yes (Region: US) |
|  1 | [6](config/6.json)   | 64.32.21.241                                                                                    | United States  | US   | SHARKTECH            | 107.167.24.162  | Yes (Region: US) |
|  2 | [7](config/7.json)   | ak1749.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | United Kingdom | GB   | OVH SAS              | 145.239.6.202   | Yes (Region: GB) |
|  3 | [8](config/8.json)   | la3.121219.xyz                                                                                  | United States  | US   | AS-GLOBALTELEHOST    | 169.197.141.187 | Yes (Region: US) |
|  4 | [10](config/10.json) | sj3.121219.xyz                                                                                  | United States  | US   | ASN-QUADRANET-GLOBAL | 47.87.151.196   | Yes (Region: US) |
|  5 | [16](config/16.json) | 169.197.141.187                                                                                 | United States  | US   | AS-GLOBALTELEHOST    | 169.197.141.187 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAibGExLjEyMTIxOS54eXoiLCAiYWlkIjogMiwgImhvc3QiOiAiIiwgImlkIjogIjY0YjNkODJmLWQ2NzMtM2JiMC1iZjNhLWZkYzMzOGY0YWFkOSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvdjJyYXkiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmXHU5NjNmXHU5MWNjXHU0ZTkxIDQiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuMjEuMjQxIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNTdmOTNlOTItZWJiOS00ZjE2LTliZGMtODIyNWQyMDEwOTk1IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0MzEzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@ak1749.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:4444#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%20%207
vmess://eyJhZGQiOiAibGEzLjEyMTIxOS54eXoiLCAiYWlkIjogNCwgImhvc3QiOiAiIiwgImlkIjogIjY0YjNkODJmLWQ2NzMtM2JiMC1iZjNhLWZkYzMzOGY0YWFkOSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvdjJyYXkiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmXHU5NjNmXHU5MWNjXHU0ZTkxIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAic2ozLjEyMTIxOS54eXoiLCAiYWlkIjogNCwgImhvc3QiOiAiIiwgImlkIjogIjY0YjNkODJmLWQ2NzMtM2JiMC1iZjNhLWZkYzMzOGY0YWFkOSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvdjJyYXkiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmXHU5NjNmXHU5MWNjXHU0ZTkxIDEwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@169.197.141.187:8091#github.com/freefq%20-%20%E5%8C%97%E7%BE%8E%E5%9C%B0%E5%8C%BA%20%2016
```

