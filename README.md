



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE6UZL3K%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T130224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDg4ilkRq%2BZAMtiyhxtHZFlQldj%2FF2IjhHicItk6qIwLAiBw5Lb3M4v5VRCZfkZQqpeXUeSiSw%2F7x3apYhfyMzAdDir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMP%2BaBj44EZ3lJcsqFKtwDgwdC%2FLcyHCsz5pbmr28MBqiRWth5tXmeB9hG%2FamssTlJalcI4Mk60e8cGI7aVxH31ANz4icqBZFqPHXdH5JaJrqmzs1hkUS8C6Mq2Or4FXy%2FZspXCrXNtnUrEKPQqoQznNjmH11MDy8gW%2FPcnDYIpQkYTmxOmQ3AZsI%2Bo%2BLs7io045BUKjBQ7QJK5oCdWFAJyShrtZRjz6XCELfTqgfsJxb%2FiJsFDMVJb7kXqrYl0lFUH4OxeAlVnMGgKxnqK9h8GOfa%2FJomHAr%2FOzn7cNt6zV4nK6tu8OEZCNo9LuTfJdpcN%2BlgJnDfmkmo76EV%2F2REiTHc0y%2BfRJW3EfqB1W8EQ1F7YfMUmZTnjKaKwCqqR9zL4LLFfkT8eC%2FjH0%2FfgxOl9DMVG1bwinVdw0sgNKJqE%2FiaeHw0Uo7VliUuLrJ6%2Fl9E6ybQ4w8OTGvj2FsLITQImhYu21QnrNvNzlcRhodwRFUOns0XbF5Gunk9rSczwZiqJbe2OQrep%2FVFZ8jOS2569qUSKiNS3qX4Z6uOqR2FClQK3ykutVqV5Gkv9aacqh9ipM0jji7VoFZE8Au0cEnxzbziG7Kf6x6IWskuX3VEgUbDGuQYTX6EMuQQObzQUzVBiG1BULMqZ%2FEgD9Mw8qDt0gY6pgFVtF4HPPf5dwmvA9J6vIifUswT%2FtAfl%2FhviO1FsRy3Flnx1WFye0e7C1ulFLnjbK0FUrDgsZlcerAqojbOoQcEJZ05xYxE09ZBjbEOcDCpihTtJQwZ6WWYwgqhCjzvhXl6y0CfRff93Ml%2FjSQy8DGQoRCOvFBOQNv9wwA6IJ5YFHWSoYdDpTiLwt0j0n3J5I6h6SCg23hhFxe5ist%2Fy6WyCmW6jcGY&X-Amz-Signature=025d3f3c48a19882506dbb40f6e5119130a08f43f4d60153c2853a2b435dbf62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE6UZL3K%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T130224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDg4ilkRq%2BZAMtiyhxtHZFlQldj%2FF2IjhHicItk6qIwLAiBw5Lb3M4v5VRCZfkZQqpeXUeSiSw%2F7x3apYhfyMzAdDir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMP%2BaBj44EZ3lJcsqFKtwDgwdC%2FLcyHCsz5pbmr28MBqiRWth5tXmeB9hG%2FamssTlJalcI4Mk60e8cGI7aVxH31ANz4icqBZFqPHXdH5JaJrqmzs1hkUS8C6Mq2Or4FXy%2FZspXCrXNtnUrEKPQqoQznNjmH11MDy8gW%2FPcnDYIpQkYTmxOmQ3AZsI%2Bo%2BLs7io045BUKjBQ7QJK5oCdWFAJyShrtZRjz6XCELfTqgfsJxb%2FiJsFDMVJb7kXqrYl0lFUH4OxeAlVnMGgKxnqK9h8GOfa%2FJomHAr%2FOzn7cNt6zV4nK6tu8OEZCNo9LuTfJdpcN%2BlgJnDfmkmo76EV%2F2REiTHc0y%2BfRJW3EfqB1W8EQ1F7YfMUmZTnjKaKwCqqR9zL4LLFfkT8eC%2FjH0%2FfgxOl9DMVG1bwinVdw0sgNKJqE%2FiaeHw0Uo7VliUuLrJ6%2Fl9E6ybQ4w8OTGvj2FsLITQImhYu21QnrNvNzlcRhodwRFUOns0XbF5Gunk9rSczwZiqJbe2OQrep%2FVFZ8jOS2569qUSKiNS3qX4Z6uOqR2FClQK3ykutVqV5Gkv9aacqh9ipM0jji7VoFZE8Au0cEnxzbziG7Kf6x6IWskuX3VEgUbDGuQYTX6EMuQQObzQUzVBiG1BULMqZ%2FEgD9Mw8qDt0gY6pgFVtF4HPPf5dwmvA9J6vIifUswT%2FtAfl%2FhviO1FsRy3Flnx1WFye0e7C1ulFLnjbK0FUrDgsZlcerAqojbOoQcEJZ05xYxE09ZBjbEOcDCpihTtJQwZ6WWYwgqhCjzvhXl6y0CfRff93Ml%2FjSQy8DGQoRCOvFBOQNv9wwA6IJ5YFHWSoYdDpTiLwt0j0n3J5I6h6SCg23hhFxe5ist%2Fy6WyCmW6jcGY&X-Amz-Signature=621f970461cbf8b7b56c2c11ac5af78ee4717e5e329d53ac2a87201149f2ad88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







