



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6VXG3K%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T012117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIECuDs1ohFFQ4UJZt%2FbK4wIrmKkqkZ%2FhozPCHo0V7xtEAiEA9HN3%2BLxkQ%2FPvfygiedyS6rFhIkTJJysOAYc23QKtztwqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBfJuIwXSzmn4vgAyrcAyrIULqWJeiMXJuZVvLbRWFu%2FqTvX7f5vbUUB%2FhAPrRKWUiYEEiQapLVj5FSm5up6JOewW95CToQTXbcUAYpYxyW3h8FFMEP2GM7dgTo2DYqxg2OKS0IDxN01Fs9Le9Eoj2PBJsIyi6H%2F9Ex7pcBVq9HXBoySjKO0iwgENLLeJZWoYyHVJr1PQuXRJA0tbGt8h5cdhf4kRhiXLj47hUA7pBQdXT4i7C%2Bn5eRN08gkq%2BAEEh2%2FtqVb093HQuJn0vyWpduWE98HA0z85tovfw0eUvqh3RLzdwkoh1qz12sBhJHniEokcQOd0gqoLMXEY6%2Fc%2BSEdqxpP7JXoYqf5Qo07sqBUYnLkNNFmT0iULufa4cW%2BkElVpEXzIy5LTTLsTR%2FDti77uY1kykyrD9FyR9iwIQyZP3ZL2t2KBjJW7%2FZF01dkoQJB2cUWJEgMVrGCBKdA0ay5lIWMGrW4NiM6ddCj9o%2FdgGdCs%2FIqjP%2BlRgph9EkCNQknWL1UbW%2BZDctsmnpcMo%2F1eU8YCxaoaYWoByeyIM16aTESaxeTsHxzkNbs1y7QrWLBKgVOiry7BaeBE%2BkadHJ7YNuIkJCMzJVbHOtlCKocsv18JL%2BmXVrc17SA7ReCHS0FZnkNGlD1XVTMNKwwMsGOqUBEo3fyh2gbGnbo2jVCBNB8DqY4Xpdr1aBJqwCsPfIN%2B2OLk3mJKBgG2AmQbvkg2LGSQsMc0KcXa7%2FVqJ2Y%2FN5j2DTKi69hgOWF34CpTikGBuND%2BapyMSw37Y3OuchmphdqFMDgfhYuCO9Rf981VO6JRBmX0ZPLZKOEHpjDCbEV%2BIAQ6kxWob3HwWC075qR0hW80hPiWpzV3sQdbQJkN0hUVxtCNZY&X-Amz-Signature=d2b0e5768cd51152332e34401ea79cfd74d0e135e3010d926e029b579c028973&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V6VXG3K%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T012117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIECuDs1ohFFQ4UJZt%2FbK4wIrmKkqkZ%2FhozPCHo0V7xtEAiEA9HN3%2BLxkQ%2FPvfygiedyS6rFhIkTJJysOAYc23QKtztwqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBfJuIwXSzmn4vgAyrcAyrIULqWJeiMXJuZVvLbRWFu%2FqTvX7f5vbUUB%2FhAPrRKWUiYEEiQapLVj5FSm5up6JOewW95CToQTXbcUAYpYxyW3h8FFMEP2GM7dgTo2DYqxg2OKS0IDxN01Fs9Le9Eoj2PBJsIyi6H%2F9Ex7pcBVq9HXBoySjKO0iwgENLLeJZWoYyHVJr1PQuXRJA0tbGt8h5cdhf4kRhiXLj47hUA7pBQdXT4i7C%2Bn5eRN08gkq%2BAEEh2%2FtqVb093HQuJn0vyWpduWE98HA0z85tovfw0eUvqh3RLzdwkoh1qz12sBhJHniEokcQOd0gqoLMXEY6%2Fc%2BSEdqxpP7JXoYqf5Qo07sqBUYnLkNNFmT0iULufa4cW%2BkElVpEXzIy5LTTLsTR%2FDti77uY1kykyrD9FyR9iwIQyZP3ZL2t2KBjJW7%2FZF01dkoQJB2cUWJEgMVrGCBKdA0ay5lIWMGrW4NiM6ddCj9o%2FdgGdCs%2FIqjP%2BlRgph9EkCNQknWL1UbW%2BZDctsmnpcMo%2F1eU8YCxaoaYWoByeyIM16aTESaxeTsHxzkNbs1y7QrWLBKgVOiry7BaeBE%2BkadHJ7YNuIkJCMzJVbHOtlCKocsv18JL%2BmXVrc17SA7ReCHS0FZnkNGlD1XVTMNKwwMsGOqUBEo3fyh2gbGnbo2jVCBNB8DqY4Xpdr1aBJqwCsPfIN%2B2OLk3mJKBgG2AmQbvkg2LGSQsMc0KcXa7%2FVqJ2Y%2FN5j2DTKi69hgOWF34CpTikGBuND%2BapyMSw37Y3OuchmphdqFMDgfhYuCO9Rf981VO6JRBmX0ZPLZKOEHpjDCbEV%2BIAQ6kxWob3HwWC075qR0hW80hPiWpzV3sQdbQJkN0hUVxtCNZY&X-Amz-Signature=9fc46f00a637f2425f118e0a0aa826e251a3d78aeaadc85610a2be3f4c0fd796&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







