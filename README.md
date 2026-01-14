



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTANDKA%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T123628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIQCkK9kxJjETbnxZVuGonvvokTv4e1JIoPD1cobnbWnJjAIgPNup%2Bc6r8wSmzRu57N3HVca4MV2%2FJOlZJwJahuR1A6cq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDA%2FQXntLwTNH7MHGlyrcA07ZOQj8jvGe0uEyfo2zHoISbV%2BprF%2FNH9NORipLveAu9uAwW4gEMVFMoXhfqDkhXME8uAwG%2F2hsX7qR8XOmKsrV3KDIcWueUa%2BvBdktl6O%2Fg%2BHt%2Bi%2BUOxu%2FHvuBrVqlglh8oRWy7vcFFHDcq%2BHAeX3rx8yh1PRiOGNfwrwlCBtric1iJNkvUvXhzSGNupOwQk6o3FfUfpdiEAVEd1ostleQL5JeJrBcg75fiA5Dhpe0TTDur%2Bwz30CGCQG%2FgrfrTDl1817eIN3lDQHitGgQxJXzPTV81hea6vOQ9GoKzavXdjeVhkzcQgt38hxNYWxPGSyOv5Hp7dCsv25VlqD%2F7Tyl5KE%2FqCEDemFigiRsQkTUJSyjfvO7yl1w5IKhDv1pzmpHD8FZGX1PddtVdNphbKURsM0jdXApSezVvrALqdNrdqhVZ5%2FdnFXMkVgMmGEwVhARgvHlePT8hy8pSXeHAgEF96KHzwe68seg1u8rq%2FcYPO4NXG9loZ7AEfmKLrT6Q9UzGOrLraaCRIAHo5Tb7eSw9Jkf5u6l063JQhKobwE3qBkwb%2FUEfacd99f%2F4keKLfN8v7GntDq0YRoxzDgwpWehOHubkUPlRyCkOb0ZHNnJlbtZiioUFLfBbwsWMKSRnssGOqUBmamfm8WiNaEze5Wt%2BmjjNBIWFmk5XnT%2BiArZhhlDPgo1bwU4%2FKfKpcnBkkor5kM4jL4W4Za8O3BhBd4MljorOwX1BaYjm7NwOwzxfBYXbC2whLbP0kSfE0xGM5%2FCIaTcwIxVuxJvHBaU%2FwTNZXRw2biam5no70DgCjshpC1M8kB41RtgKQmDf1CcvRIZrWn4HaQIHIaArscMf85Ibqz3idQ7OCRG&X-Amz-Signature=2575294ba42b5621f812fd7fb00704872786ee0a72044b61c9fd418c0e023e6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTANDKA%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T123628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIQCkK9kxJjETbnxZVuGonvvokTv4e1JIoPD1cobnbWnJjAIgPNup%2Bc6r8wSmzRu57N3HVca4MV2%2FJOlZJwJahuR1A6cq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDA%2FQXntLwTNH7MHGlyrcA07ZOQj8jvGe0uEyfo2zHoISbV%2BprF%2FNH9NORipLveAu9uAwW4gEMVFMoXhfqDkhXME8uAwG%2F2hsX7qR8XOmKsrV3KDIcWueUa%2BvBdktl6O%2Fg%2BHt%2Bi%2BUOxu%2FHvuBrVqlglh8oRWy7vcFFHDcq%2BHAeX3rx8yh1PRiOGNfwrwlCBtric1iJNkvUvXhzSGNupOwQk6o3FfUfpdiEAVEd1ostleQL5JeJrBcg75fiA5Dhpe0TTDur%2Bwz30CGCQG%2FgrfrTDl1817eIN3lDQHitGgQxJXzPTV81hea6vOQ9GoKzavXdjeVhkzcQgt38hxNYWxPGSyOv5Hp7dCsv25VlqD%2F7Tyl5KE%2FqCEDemFigiRsQkTUJSyjfvO7yl1w5IKhDv1pzmpHD8FZGX1PddtVdNphbKURsM0jdXApSezVvrALqdNrdqhVZ5%2FdnFXMkVgMmGEwVhARgvHlePT8hy8pSXeHAgEF96KHzwe68seg1u8rq%2FcYPO4NXG9loZ7AEfmKLrT6Q9UzGOrLraaCRIAHo5Tb7eSw9Jkf5u6l063JQhKobwE3qBkwb%2FUEfacd99f%2F4keKLfN8v7GntDq0YRoxzDgwpWehOHubkUPlRyCkOb0ZHNnJlbtZiioUFLfBbwsWMKSRnssGOqUBmamfm8WiNaEze5Wt%2BmjjNBIWFmk5XnT%2BiArZhhlDPgo1bwU4%2FKfKpcnBkkor5kM4jL4W4Za8O3BhBd4MljorOwX1BaYjm7NwOwzxfBYXbC2whLbP0kSfE0xGM5%2FCIaTcwIxVuxJvHBaU%2FwTNZXRw2biam5no70DgCjshpC1M8kB41RtgKQmDf1CcvRIZrWn4HaQIHIaArscMf85Ibqz3idQ7OCRG&X-Amz-Signature=14ed04f363dfc32381f60a964808a0cf0c0354ff551921dfe8abddd1954986a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







