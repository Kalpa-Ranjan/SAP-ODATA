



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTMQAEQD%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T082434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAvkTMppYDouaeHj9cJm0urWDw7GnGlxqEVG4Z%2FKclYhAiEAyDSvvs6IOU61a1BKh3JDWGFL8b6e%2FXjb7DUbpHFv6BAq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDGKuxwzm8KHas036YircA0Rzp58Cnv9%2B67ndA8HuvfZn5jDN4VxEcIgVbAM00y4Kn94V0kSroan31H1OdZ57hUtiKg2pKEm5bjEZF0JCMPAVjKbuCXp3Y6L81%2FvZFM5n%2Bg%2F7EDluFEApVFlQcU8pXMaT6wTVnwwwjqmNsPEDXgsFcrIsoxTYLVKsO2fV0tNwpyTsNjRWDgfo4yxFKwJSATv0MAWQEyMBdDwqM6sjKP96iXAu8apbfZxEtFGqki4XF7oqcl%2BS9ruwYQsZ6vOcnoGthJ99MDAWKpy6vbsSD%2Fa6co5OixXh9gUEKViVSi3Qehdx3pwLk%2FB1mjDygQun5fox4hYwetSs4nu0bb%2FDgimA%2F9CQOv65pR4py7OnAzR3R3ZDWqJy43QSqpvCPwfejx6hZEWXAff4lBCLok83fNhkQRolLIUc2G7slAILh7t7%2FxtlAsNsjnfgX65%2BNGhjVfLaX%2B%2Fk%2BHKB8dHNFx962opMCmdYE1JBc7znf8SFDl94Qm7AyFX744x0HOrEBR607bkhcmQm3GMYxkHHbE6x0jSDMTQBZuXaEJGdMMqsx9J0KRGABRldSBBmzZ3FJSAVSnmMPKEvAnQ1b1hrIqY2UAYy7BboOANXEy0PXM%2FEwjLDZkEroftlZAi6Ylf3MI%2BxodMGOqUB8Za9bnJecZ8sJNFtaok3mSKyjTkoRTsFqFy%2BDJMV2JDJIret2cLhsVlmtUubSt1iM1WDHYDnpcRXnmG7v52f5%2FhSefS%2Fu%2BM2VehZPggEpPH%2BM%2Fi2mdJsI0BLVSRTv6jS7NjSR4EtE5JqPvlNbr%2FoseqA3BDDU1sFBBCCD0KjhyUgemn6vb9uku7qpBp3MOGVAoscGKkAoCrQ%2BwBFDy6bSCw5oMEB&X-Amz-Signature=6cb50c2a957837ab824ced8988ab04524c7c65ab1551a2cf64310adb34bc5e9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTMQAEQD%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T082434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAvkTMppYDouaeHj9cJm0urWDw7GnGlxqEVG4Z%2FKclYhAiEAyDSvvs6IOU61a1BKh3JDWGFL8b6e%2FXjb7DUbpHFv6BAq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDGKuxwzm8KHas036YircA0Rzp58Cnv9%2B67ndA8HuvfZn5jDN4VxEcIgVbAM00y4Kn94V0kSroan31H1OdZ57hUtiKg2pKEm5bjEZF0JCMPAVjKbuCXp3Y6L81%2FvZFM5n%2Bg%2F7EDluFEApVFlQcU8pXMaT6wTVnwwwjqmNsPEDXgsFcrIsoxTYLVKsO2fV0tNwpyTsNjRWDgfo4yxFKwJSATv0MAWQEyMBdDwqM6sjKP96iXAu8apbfZxEtFGqki4XF7oqcl%2BS9ruwYQsZ6vOcnoGthJ99MDAWKpy6vbsSD%2Fa6co5OixXh9gUEKViVSi3Qehdx3pwLk%2FB1mjDygQun5fox4hYwetSs4nu0bb%2FDgimA%2F9CQOv65pR4py7OnAzR3R3ZDWqJy43QSqpvCPwfejx6hZEWXAff4lBCLok83fNhkQRolLIUc2G7slAILh7t7%2FxtlAsNsjnfgX65%2BNGhjVfLaX%2B%2Fk%2BHKB8dHNFx962opMCmdYE1JBc7znf8SFDl94Qm7AyFX744x0HOrEBR607bkhcmQm3GMYxkHHbE6x0jSDMTQBZuXaEJGdMMqsx9J0KRGABRldSBBmzZ3FJSAVSnmMPKEvAnQ1b1hrIqY2UAYy7BboOANXEy0PXM%2FEwjLDZkEroftlZAi6Ylf3MI%2BxodMGOqUB8Za9bnJecZ8sJNFtaok3mSKyjTkoRTsFqFy%2BDJMV2JDJIret2cLhsVlmtUubSt1iM1WDHYDnpcRXnmG7v52f5%2FhSefS%2Fu%2BM2VehZPggEpPH%2BM%2Fi2mdJsI0BLVSRTv6jS7NjSR4EtE5JqPvlNbr%2FoseqA3BDDU1sFBBCCD0KjhyUgemn6vb9uku7qpBp3MOGVAoscGKkAoCrQ%2BwBFDy6bSCw5oMEB&X-Amz-Signature=db99a1fbecaa0206447b09ece15837e25326b4400e397bebc897e217297cc66d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







