



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZBGU4C%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T193629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD06gre2T1flEoSSq2OSDwFfpbGrttDhD6DBeCtLVZUHgIgal7NUkAEYz7Ed5un8N5onQ4ESEJorhl8%2BekWOLvmcIgqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLsvPOMcKkvB3zancyrcAwizmQsfEpS551YEvUpUlBlXpvia2XpDa7WcgAHk3ia1f%2BldWgT%2FEQTyZ8HnDAbGjnqEJwReGlQGhaknStjhOfsddrWCCjx5vZj3TS65jlUG0u7P6jH82CXQaBzzOe0Z%2BFOG4eMuEX1H%2FTWFUurbznliIXEx3URH3ewcaGCaZeyNuV0YIY6%2F8GJ9FoMW1s4UZVIvbz5TrroHjao7cAn4mdvzRCeAVr2nzeoEJPZ5wjgsdHsmcSAx7vRc3ksNHMt9%2FzL1RxYLCU1e0AXe0TghP4KtPpEYTr8BEE0HW0m3CGACub8IAsLkMjbwludhNbzqpDDA%2FYre8IDPkw3z2dGY%2BYlhYO47F%2BYzBWvw5FbVFoKHj4pqkblIXSEWFlIwOLIh4laQKW0VZ2ZrRQC%2FvLJFZXFUkhxiNLjyW3d8MEU8dlpKVsiaJWsQX05FQAlJjgb5kv58C9g3SHzQeCIlq%2F%2BEy4ZEPPdWRM0%2FyearkCqTTxT%2F6MebFdi3epNSydXfygnpwn2UhZfmfgV2h93MHxMgQsf7VtUrsxFwtIba%2BRIUAJcLTvwto7ituBAYdTRpAaQQ2Y%2FGLIg%2BsYAQum1WoDdBMUFMnB9kHQyx9%2Bo%2FTUYl3k0EWJhb3v7%2F34RmpuKEMI7Xv9IGOqUBNHunCd1rEnxPjOayO7fs1vQoRKaQ0r8yzMTHY8RujdJFJLTTSxOatG%2BI0DefW9DhZ8VlOsb9nNr4%2FFqPBL46OzHk3jP9drm77d7wVLnAQDFWy4ivRqUrragJBjWctpyjyEVlKwTul62iCmeGdl5rGhit0uy67a61HLvR2HnVd2XnaHtJA7nU6uNexAnNPKeCSOK6VGXkphCkHcbTPZPBu3IaW7ha&X-Amz-Signature=f69df363d224824e854a2aefdf973f78efb0c8e82c55fd9be01e3938168112e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZBGU4C%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T193629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD06gre2T1flEoSSq2OSDwFfpbGrttDhD6DBeCtLVZUHgIgal7NUkAEYz7Ed5un8N5onQ4ESEJorhl8%2BekWOLvmcIgqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLsvPOMcKkvB3zancyrcAwizmQsfEpS551YEvUpUlBlXpvia2XpDa7WcgAHk3ia1f%2BldWgT%2FEQTyZ8HnDAbGjnqEJwReGlQGhaknStjhOfsddrWCCjx5vZj3TS65jlUG0u7P6jH82CXQaBzzOe0Z%2BFOG4eMuEX1H%2FTWFUurbznliIXEx3URH3ewcaGCaZeyNuV0YIY6%2F8GJ9FoMW1s4UZVIvbz5TrroHjao7cAn4mdvzRCeAVr2nzeoEJPZ5wjgsdHsmcSAx7vRc3ksNHMt9%2FzL1RxYLCU1e0AXe0TghP4KtPpEYTr8BEE0HW0m3CGACub8IAsLkMjbwludhNbzqpDDA%2FYre8IDPkw3z2dGY%2BYlhYO47F%2BYzBWvw5FbVFoKHj4pqkblIXSEWFlIwOLIh4laQKW0VZ2ZrRQC%2FvLJFZXFUkhxiNLjyW3d8MEU8dlpKVsiaJWsQX05FQAlJjgb5kv58C9g3SHzQeCIlq%2F%2BEy4ZEPPdWRM0%2FyearkCqTTxT%2F6MebFdi3epNSydXfygnpwn2UhZfmfgV2h93MHxMgQsf7VtUrsxFwtIba%2BRIUAJcLTvwto7ituBAYdTRpAaQQ2Y%2FGLIg%2BsYAQum1WoDdBMUFMnB9kHQyx9%2Bo%2FTUYl3k0EWJhb3v7%2F34RmpuKEMI7Xv9IGOqUBNHunCd1rEnxPjOayO7fs1vQoRKaQ0r8yzMTHY8RujdJFJLTTSxOatG%2BI0DefW9DhZ8VlOsb9nNr4%2FFqPBL46OzHk3jP9drm77d7wVLnAQDFWy4ivRqUrragJBjWctpyjyEVlKwTul62iCmeGdl5rGhit0uy67a61HLvR2HnVd2XnaHtJA7nU6uNexAnNPKeCSOK6VGXkphCkHcbTPZPBu3IaW7ha&X-Amz-Signature=0285364af604a21dce223f05d8d03133147578d9e2e6288d87e641c1fdafe804&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







