



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRLXEOYV%2F20251102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251102T122721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIQDFGkdUPOuzz%2FXNMzMF04YE6LeEzCngux4IDbx%2BZsfGJQIgCa9fjBijq03QTc8qQK%2Fdy4RQHNVlmQySYhafVJmkRk4q%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDNssacegJ696YLQLDSrcA4bnWxnb8vbSTY%2BW3pSiYisQBf0KJuJdOWxN1o1Qj0RAiSBepPnHq9gish9VIU1Oq8kIuftKSIqnbqwwUzIazQ9cUtibwXqYWXrzd%2FWPHEyrMDMLDtnbnk4OSzAH98Ah6WSO1qR%2Bj9KeFYNV0CZ4p2iD81vhDyw1D5Xlf%2Bg0Ho9KE8mCKcpspE6DXu2Lml7%2Fowld4ypvaUxGBUWIUFznNC6p%2FKciwtr6R8Q2pYrjO4k1ufbnMEMe4mWfBi%2FjBlanxst6Z2QtuQ9y624f77YiHDiYsXiUnH9k8%2BiEYcI5Mas4UMMLpDsC1IScQwLUDDjKlU3bjSkXTmnk1Qb4BJBi9%2BOkEHTZ4A3grsxtiZINnh7eB0gzXwe7gyLv5pteY%2BQeaP8SFA%2B0G09vZvmQwkXff%2BS57hpe7ppNs3by7rOQAvdjSIsbOlyc2W2U9UpmT7%2Fk%2FXHYWXcbKnVOs%2FUtJZ08XWCBq2hAGJAaqgcjqEhzwzIPP7MZ4ziLci539Wb6UnlWqNdmFyPReZcHQuoLUsxnfYmsz9yXliho%2FzPwn9yek2FrnUyOjoiege291rAqmWxxxZf%2BppK80ImOD1OGaKnB08jRy89XZrhaZYFjduE%2FybADY8dg1yhQ4E7Tqq4cMKqMncgGOqUBRlAsngeTg1YZLyeaxyOSNgSmv3bT%2FC3OEryMdmqPs7wCfEfzfPzMEAwejyMB8ms5P%2BuVWZ0NZPCbLdw6g59%2FlXoy2Wv1YFb2W3hngRARos1NWucSLJym%2FmkI4udWDfUs5oZN7W7dZjy9if%2F6AQB2z7BztLm2l3bNU3MdGTzSZ3Lp0ig%2FAAOEsMvIF0xB%2F8uRX1i3ck62gzPQmsR0NRvUXySrzc14&X-Amz-Signature=306238c197d3f1ee8645b34f27ef832fc9bdcce54d293b8ddc50da3628054ea6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRLXEOYV%2F20251102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251102T122721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIQDFGkdUPOuzz%2FXNMzMF04YE6LeEzCngux4IDbx%2BZsfGJQIgCa9fjBijq03QTc8qQK%2Fdy4RQHNVlmQySYhafVJmkRk4q%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDNssacegJ696YLQLDSrcA4bnWxnb8vbSTY%2BW3pSiYisQBf0KJuJdOWxN1o1Qj0RAiSBepPnHq9gish9VIU1Oq8kIuftKSIqnbqwwUzIazQ9cUtibwXqYWXrzd%2FWPHEyrMDMLDtnbnk4OSzAH98Ah6WSO1qR%2Bj9KeFYNV0CZ4p2iD81vhDyw1D5Xlf%2Bg0Ho9KE8mCKcpspE6DXu2Lml7%2Fowld4ypvaUxGBUWIUFznNC6p%2FKciwtr6R8Q2pYrjO4k1ufbnMEMe4mWfBi%2FjBlanxst6Z2QtuQ9y624f77YiHDiYsXiUnH9k8%2BiEYcI5Mas4UMMLpDsC1IScQwLUDDjKlU3bjSkXTmnk1Qb4BJBi9%2BOkEHTZ4A3grsxtiZINnh7eB0gzXwe7gyLv5pteY%2BQeaP8SFA%2B0G09vZvmQwkXff%2BS57hpe7ppNs3by7rOQAvdjSIsbOlyc2W2U9UpmT7%2Fk%2FXHYWXcbKnVOs%2FUtJZ08XWCBq2hAGJAaqgcjqEhzwzIPP7MZ4ziLci539Wb6UnlWqNdmFyPReZcHQuoLUsxnfYmsz9yXliho%2FzPwn9yek2FrnUyOjoiege291rAqmWxxxZf%2BppK80ImOD1OGaKnB08jRy89XZrhaZYFjduE%2FybADY8dg1yhQ4E7Tqq4cMKqMncgGOqUBRlAsngeTg1YZLyeaxyOSNgSmv3bT%2FC3OEryMdmqPs7wCfEfzfPzMEAwejyMB8ms5P%2BuVWZ0NZPCbLdw6g59%2FlXoy2Wv1YFb2W3hngRARos1NWucSLJym%2FmkI4udWDfUs5oZN7W7dZjy9if%2F6AQB2z7BztLm2l3bNU3MdGTzSZ3Lp0ig%2FAAOEsMvIF0xB%2F8uRX1i3ck62gzPQmsR0NRvUXySrzc14&X-Amz-Signature=2475d942d9b56251da8afbcc3b75c9588f802ef24d212b398112480a9f719b9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







