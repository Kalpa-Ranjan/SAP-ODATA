



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD4OGBS2%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T020047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQDY7U%2BxRm5Z2B7Ssg5C9NsGsIk7LiOKXRqveuZog9hHCAIhAM5v6ZxY5W3XcRtq1%2BXLZe1sIzer4FD53S2n3%2Be6OkWPKv8DCAIQABoMNjM3NDIzMTgzODA1IgxDSiJmm6n%2FwEe9KwMq3ANe4sB52AC4IgY8usDUHFcv85IaBI26paOMyi9evhvjjjFtPsYEc%2F4M3z5WHsoNPuMxOL4Ln2BPxXLvd07YHT8Ip1BVq0xD8dTEMY3MziN9vibTgrl1uJ9uiosspzOF5E9N8SewufCqpsoqtWQQyEAWs%2BS8abaBDzljkytcO0mVD3eWsuS%2FszTL6%2BA%2BjDzXMCuKpizzaQCO22DeLNqPS4UsPyeo%2Fs0axOJHuxRHhibqyGMMEsSzaqCHFRQ1m3lv2UpUvnhIoCGdG4uF2QUqzxcbRfstlIQcO3GlVlef51aOk%2BgCZJjxMLUflIJaJdCiKjGx1Oua9BkB0winnV3K5CCU3VUFu58xxCqNyTKtgQmy0LnVKNd91VSsHFYDv9x5UQaBtVzC6giJix2VShIWNvLyyUX5yk%2BpETSOS%2FYL92vaTAlh0Sxnt6BgX1sTgSfzqk0XiL5hpMJGQLCBaFmI880bo29kYApko01UHQUpSL1pnacwDIKZvZInW6%2B5v3yzCiHf1LqZ7lp4L7eGHMRoHepNInTMoLEeXhIefgfyxma40oYehLinWzfS%2Bm8%2F2lBl3pfpmQ2NclOZxgd0nnBJZR20biDT0ipsYeulsux5YQtcojEUxZlthMngfawCFjCa48TTBjqkAbza%2F%2F4ADZbnGLSinbPxcumrsUfmXiA66U0RyjLvmzHxcSXFl6zb4I1L3UZ%2F5m0MEt5Q4f%2Blcq07QnCsFPJR6fFvC1wqnoMOVWZ7g%2BT5YwdMu%2BcEQUIB2Oc%2FHTfWRDsYKrXp0dwraVHXrxKUYD1fEgDI6RlP0%2FOVpD5qz4sWvUSikRdW6%2Bl%2BpR4l5Z6WOj9mxfSGJyBG5Q3QhnhVIaZUvbfVZL8L&X-Amz-Signature=ab06c7c3726939566e1891a2671302d4047258751c3c368a932f6d653d163aa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD4OGBS2%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T020047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQDY7U%2BxRm5Z2B7Ssg5C9NsGsIk7LiOKXRqveuZog9hHCAIhAM5v6ZxY5W3XcRtq1%2BXLZe1sIzer4FD53S2n3%2Be6OkWPKv8DCAIQABoMNjM3NDIzMTgzODA1IgxDSiJmm6n%2FwEe9KwMq3ANe4sB52AC4IgY8usDUHFcv85IaBI26paOMyi9evhvjjjFtPsYEc%2F4M3z5WHsoNPuMxOL4Ln2BPxXLvd07YHT8Ip1BVq0xD8dTEMY3MziN9vibTgrl1uJ9uiosspzOF5E9N8SewufCqpsoqtWQQyEAWs%2BS8abaBDzljkytcO0mVD3eWsuS%2FszTL6%2BA%2BjDzXMCuKpizzaQCO22DeLNqPS4UsPyeo%2Fs0axOJHuxRHhibqyGMMEsSzaqCHFRQ1m3lv2UpUvnhIoCGdG4uF2QUqzxcbRfstlIQcO3GlVlef51aOk%2BgCZJjxMLUflIJaJdCiKjGx1Oua9BkB0winnV3K5CCU3VUFu58xxCqNyTKtgQmy0LnVKNd91VSsHFYDv9x5UQaBtVzC6giJix2VShIWNvLyyUX5yk%2BpETSOS%2FYL92vaTAlh0Sxnt6BgX1sTgSfzqk0XiL5hpMJGQLCBaFmI880bo29kYApko01UHQUpSL1pnacwDIKZvZInW6%2B5v3yzCiHf1LqZ7lp4L7eGHMRoHepNInTMoLEeXhIefgfyxma40oYehLinWzfS%2Bm8%2F2lBl3pfpmQ2NclOZxgd0nnBJZR20biDT0ipsYeulsux5YQtcojEUxZlthMngfawCFjCa48TTBjqkAbza%2F%2F4ADZbnGLSinbPxcumrsUfmXiA66U0RyjLvmzHxcSXFl6zb4I1L3UZ%2F5m0MEt5Q4f%2Blcq07QnCsFPJR6fFvC1wqnoMOVWZ7g%2BT5YwdMu%2BcEQUIB2Oc%2FHTfWRDsYKrXp0dwraVHXrxKUYD1fEgDI6RlP0%2FOVpD5qz4sWvUSikRdW6%2Bl%2BpR4l5Z6WOj9mxfSGJyBG5Q3QhnhVIaZUvbfVZL8L&X-Amz-Signature=de5673fd3ed64b335210e44e4de85de281541200bb3da8a887718578dbfea789&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







