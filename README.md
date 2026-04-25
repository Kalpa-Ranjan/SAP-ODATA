



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665TRAP4D%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T015854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXTDpxSimSKzeiCndNLUkXTFI%2FA1KNDWNCTaIl71UcBgIhAKsqkjuUj8n7hHTJ7XJXX99VblRaIzCGStEINDuXQOf3KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyw8dcWJwejDQ0g%2BQwq3AMK31Fsdh0jqVkF5d695eV5bEyuLs99spVa5aPfQMpiMhiFbwVMrhHpaLt49%2Bds6qrmNEgPHkRqLKg7n4Qo%2B69LLLXIynn2itOo%2FESIIyLa%2FgZI8C285MkI%2F8VuhO9uOAyOgQ8YFDznP7x6gnWR1allr9lk4QtD32mW8wOc%2BNm7IL%2BKo1jha2XW58LERbdAvAj2Ug%2BSyGARHbfz0xEQr7X%2Blnam8Ho7wPEHJEWnErAAkGvxXx8hYwrIZeduout4B4rViuxr2atKIZjQpPOpSN8ApbXCDHgqOQk4ZBV1QQsPZ2rlw3z28y%2F9rvdxRSHewVDXt0OvXZ37qQ%2BmOlWtFKl3NBiwze1rvGJibmmgTL1LHMy2YSZsckvELvOiLcdS30TJKwZQ0GXcENF1G8wMLeLx50Xwxv3rFzI56Gi8IBAWuFlYNDS2uxtijvKtQJInU2%2Bofu%2Ftdwl4qTthQKl1GHWXA9Moh1%2Bmj3vaitad5Z%2FgDuVxcnAl5kDBSAZ5dJNd836DBaVROxWra5KHkr6N37BQfVKM3zQCRJ3BO%2FaUW5ZlG2SHm5Vs67yukQsyk7mjYQVZEnw%2B8xMJ9XsvDLY3IlsMkxa2m%2FVLJDMTQ1Gxv9k866TctOyej6Q287swdzDqurDPBjqkASHG%2BbEFV5t2t61%2Ftl3pqUqw1UCZvsSJ217ThnaKOxRhxyyp0yn%2Fvv76Pcp0nsneKRFpQC%2Fsc54%2FW8x9MqCJDJpGzFRFnN70e%2FxSWoYNDjd3SM4X%2F6arZQ3DgGq47Ep9mnxIq0e%2FgJl1ehAnCEeC6d%2FaqamIcsrxXLl2U1nfqvr7LBfcvaLkGyDDap8jqb8ZGKuh6GMeMmuYgAZ9WffZYA%2BfUbWV&X-Amz-Signature=8ef5dd4bb661d492871c70d1f70a52a4fe706d2a1ed0f515e169456e623577d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665TRAP4D%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T015854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXTDpxSimSKzeiCndNLUkXTFI%2FA1KNDWNCTaIl71UcBgIhAKsqkjuUj8n7hHTJ7XJXX99VblRaIzCGStEINDuXQOf3KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyw8dcWJwejDQ0g%2BQwq3AMK31Fsdh0jqVkF5d695eV5bEyuLs99spVa5aPfQMpiMhiFbwVMrhHpaLt49%2Bds6qrmNEgPHkRqLKg7n4Qo%2B69LLLXIynn2itOo%2FESIIyLa%2FgZI8C285MkI%2F8VuhO9uOAyOgQ8YFDznP7x6gnWR1allr9lk4QtD32mW8wOc%2BNm7IL%2BKo1jha2XW58LERbdAvAj2Ug%2BSyGARHbfz0xEQr7X%2Blnam8Ho7wPEHJEWnErAAkGvxXx8hYwrIZeduout4B4rViuxr2atKIZjQpPOpSN8ApbXCDHgqOQk4ZBV1QQsPZ2rlw3z28y%2F9rvdxRSHewVDXt0OvXZ37qQ%2BmOlWtFKl3NBiwze1rvGJibmmgTL1LHMy2YSZsckvELvOiLcdS30TJKwZQ0GXcENF1G8wMLeLx50Xwxv3rFzI56Gi8IBAWuFlYNDS2uxtijvKtQJInU2%2Bofu%2Ftdwl4qTthQKl1GHWXA9Moh1%2Bmj3vaitad5Z%2FgDuVxcnAl5kDBSAZ5dJNd836DBaVROxWra5KHkr6N37BQfVKM3zQCRJ3BO%2FaUW5ZlG2SHm5Vs67yukQsyk7mjYQVZEnw%2B8xMJ9XsvDLY3IlsMkxa2m%2FVLJDMTQ1Gxv9k866TctOyej6Q287swdzDqurDPBjqkASHG%2BbEFV5t2t61%2Ftl3pqUqw1UCZvsSJ217ThnaKOxRhxyyp0yn%2Fvv76Pcp0nsneKRFpQC%2Fsc54%2FW8x9MqCJDJpGzFRFnN70e%2FxSWoYNDjd3SM4X%2F6arZQ3DgGq47Ep9mnxIq0e%2FgJl1ehAnCEeC6d%2FaqamIcsrxXLl2U1nfqvr7LBfcvaLkGyDDap8jqb8ZGKuh6GMeMmuYgAZ9WffZYA%2BfUbWV&X-Amz-Signature=c48af3da610d7ca929fc7bfa9c2a4512d76ca8e699ce0be074bcc0669e318547&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







