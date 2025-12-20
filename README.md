



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DGE3UCX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T062409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBTWI4QDWFt4%2BUjSvBUKf6VkMxnDaQARG6vAhf%2F%2BPgIcAiEAmPfy7KPu99tlzH2%2BFaQ3d8VBJjw%2BTzVESxXd6%2FYt2pgqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjr7Pmb5LKzELUEDircAxFBI0HZpdPl%2BYXalY%2B9IcYmU7oGxMbXAPJaaMuE62d%2BrqMthY78JO48F1gqrby4VMz7Up82UUvQBFz0Um503NIEdsxRfl96gs6deIQTA%2BvICVoLIJlHS4k1bThgyVYHksgb6HBIIWwvvR6Z3YOLGMZ%2BM2%2FAzglqQqqIalOvDeV7mr4oOnFa4nn8l190vnYFerZUZySU3fIJGZkMxeZsImtdgi9WkKXUXVRb77rKhiYUD4gnLwP2slJj0f9DYRKw4D4ppZ6RkJFUVzD%2Bj0kud8KJWCN0jSWbCsJS86edqO1b6jgyMV0XBrzm0%2BwFp8nhGpP4IQA63Lt3XiolAN3w39%2FsBP79his6hXErcLaX3Rt2ycc0f6Q2KKLRbSfzv2cb02yeeaIkIBDET8bpKRJrF8kYkWIGTD%2FPM%2B%2BnklpA1rKBaOmz5zF4J64XnVgw75s2yqUVNMnMekkR4x2YxpLkhCX3e3gZbjkF0cYOOIXeDfc8vGbNKZit%2Fxa3%2FQD7T%2BpBgtQnFUqaWWxNmlXTzaoXS5Ut4%2FjjpvyNMo4GnudQ8LF41Y41kCz9x46neIhbeKawn2rjrhSWnkCm8jZ0El6q9qvPefzcpm8W7WKEsPmtpFlgJP8gzgTTcZ9N083gMP%2FvmMoGOqUBQ4il%2BAYyTSxkeFObxlBWQ3LUHlTUf2dVUoOuZ%2FRD1XSzCDfZzmiIojxQLruMciFhaN72Aj2HGIcGu1XI9KHK5Hw76LuZmTD%2Fdd1UJ5ddr8fpK78N3UEIbHkavvAF7aS1L7Xbuf0DMF0BSSPjXr6YT3XBnoH9Ey4okvlOZxW%2BiI7Kra4xUV78CzaNU6LjUcfELwYRD%2FA%2BJ7wmfbFL3XO0siO%2Bardz&X-Amz-Signature=01d44cc1a215cc7fe9719f9ad2211fe62fde7d342ec29186cf3f8874b4780d1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DGE3UCX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T062409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBTWI4QDWFt4%2BUjSvBUKf6VkMxnDaQARG6vAhf%2F%2BPgIcAiEAmPfy7KPu99tlzH2%2BFaQ3d8VBJjw%2BTzVESxXd6%2FYt2pgqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjr7Pmb5LKzELUEDircAxFBI0HZpdPl%2BYXalY%2B9IcYmU7oGxMbXAPJaaMuE62d%2BrqMthY78JO48F1gqrby4VMz7Up82UUvQBFz0Um503NIEdsxRfl96gs6deIQTA%2BvICVoLIJlHS4k1bThgyVYHksgb6HBIIWwvvR6Z3YOLGMZ%2BM2%2FAzglqQqqIalOvDeV7mr4oOnFa4nn8l190vnYFerZUZySU3fIJGZkMxeZsImtdgi9WkKXUXVRb77rKhiYUD4gnLwP2slJj0f9DYRKw4D4ppZ6RkJFUVzD%2Bj0kud8KJWCN0jSWbCsJS86edqO1b6jgyMV0XBrzm0%2BwFp8nhGpP4IQA63Lt3XiolAN3w39%2FsBP79his6hXErcLaX3Rt2ycc0f6Q2KKLRbSfzv2cb02yeeaIkIBDET8bpKRJrF8kYkWIGTD%2FPM%2B%2BnklpA1rKBaOmz5zF4J64XnVgw75s2yqUVNMnMekkR4x2YxpLkhCX3e3gZbjkF0cYOOIXeDfc8vGbNKZit%2Fxa3%2FQD7T%2BpBgtQnFUqaWWxNmlXTzaoXS5Ut4%2FjjpvyNMo4GnudQ8LF41Y41kCz9x46neIhbeKawn2rjrhSWnkCm8jZ0El6q9qvPefzcpm8W7WKEsPmtpFlgJP8gzgTTcZ9N083gMP%2FvmMoGOqUBQ4il%2BAYyTSxkeFObxlBWQ3LUHlTUf2dVUoOuZ%2FRD1XSzCDfZzmiIojxQLruMciFhaN72Aj2HGIcGu1XI9KHK5Hw76LuZmTD%2Fdd1UJ5ddr8fpK78N3UEIbHkavvAF7aS1L7Xbuf0DMF0BSSPjXr6YT3XBnoH9Ey4okvlOZxW%2BiI7Kra4xUV78CzaNU6LjUcfELwYRD%2FA%2BJ7wmfbFL3XO0siO%2Bardz&X-Amz-Signature=112d87040e353c138af4f1174c5479bf19b578ee0def737f2b202c57646fef8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







