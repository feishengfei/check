
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                    | ip              | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:-----------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.99.91         | United States | US   | PEGTECHINC             | 142.4.99.65     | Yes (Region: US) |
|  1 | [4](config/4.json)   | 156.225.67.105      | Netherlands   | NL   | YISP B.V.              | 154.84.1.44     | Yes (Region: NL) |
|  2 | [7](config/7.json)   | cfcdn.sanfencdn.net | United States | US   | Akamai Connected Cloud | 104.237.159.122 | Yes (Region: US) |
|  3 | [8](config/8.json)   | 104.18.1.196        | United States | US   | CNSERVERS              | 23.225.9.234    | Yes (Region: US) |
|  4 | [16](config/16.json) | 45.199.138.121      | Netherlands   | NL   | YISP B.V.              | 46.182.107.129  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuOTkuOTEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0ggMiIsICJwb3J0IjogNDMzNzksICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA1IiwgInBvcnQiOiAiNDkxMDEiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi9pc2FpZnFhYWdwaSIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDciLCAiYWRkIjogImNmY2RuLnNhbmZlbmNkbi5uZXQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiZGE0OGM2MTYtNzViNS00YjE1LWFhOGMtNjJmYjMwMDFlMzUyIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1czUuc2FuZmVuY2RuMS5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAidXMxLnNhbmZlbmNkbjEuY29tIn0=
vmess://eyJhZGQiOiAiMTA0LjE4LjEuMTk2IiwgImFpZCI6IDAsICJob3N0IjogInNnLnhtYmIubmV0IiwgImlkIjogIjA0MjVkMDEwLTE5ZjYtMTFlZS04YmU0LTE1NzdjMTY1MTY3OSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvZmlsZXMiLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNiIsICJhZGQiOiAiNDUuMTk5LjEzOC4xMjEiLCAicG9ydCI6ICI1MTIwNCIsICJpZCI6ICI5NTQ5YTJjZi0xMjliLTQzYTEtODhkYi1lZjdmNjQ4ZGU3NGEiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiXHVkODNjXHVkZGYzXHVkODNjXHVkZGYxTkxcdTgzNzdcdTUxNzAoeW91dHViZVx1OTYzZlx1NGYxZlx1NzlkMVx1NjI4MCkiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
```

