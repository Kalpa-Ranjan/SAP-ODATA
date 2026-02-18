



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DCFNKE6%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T014918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZxKVjyOrYmDksBdO8fmbnCa1c45OeHX2f9z51Z69K7AiEAyTtq5M0DNEyfw7K4Peq%2BhkFV3S2BGWX%2FOBmE5AqqA58q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBW2NSTUn532apQFYSrcAylI4LjOscD5Joceq62lAxvqYDoIPzFu5P3dJ5nqJV%2Blq0PdcCdNNExseOBYfrFQCvRsm2pMdVSgunh3%2FE3X8Tfjnz5lx5vVXkKI89f6VRP6jEqq3IbzjVrl470cFuZMjgao838GR4jEgYg5kYE78u3N%2BEXx7Hx2EU8eapbivasNcZyl8%2F2gfIzkM5TEmTcPlYbe9xkdVomsOdl%2Fqbt7VgAXnG7NHyeCP94jEVHcpP5spayuQCKzFYQSyW5RlHfgJlRHQgazyUo5s5%2B6R8rmIAjIw0y2S3ZJ%2FpReFPWV0dY2%2Fa%2B84jhx7Elmpxc9BySxVllaN1VK3E2af0W3vv%2BWfQefVL9CcoblbZYRLEZifnTpuR27j2G8Znolx9Ds7WBwptZdRg3mTNd07nsOXq9AYu22FW5U51pIYzkNfnCfL1n%2FTiR8jvm7zYjJqK1KoX9SkrfXt66MzNtaQfuL%2FF4iHbJH0eOYtMg41HFtZeI6%2BvoXpoA8lKlv4KZBlEV1jTUmEyaCHodF%2BjJCV7vV1v2uotrsWPway1ACZMWKpbEqfoPUWahyydlV6wWvjZzwkOJqmsyyYE7dAwNbD0h8D0ritFfd1QBE7FmpWKWceMhLgPA8QVKgivMrMBr49Gl%2BMLaf1MwGOqUB9oPN9cXMAybETwNJAn97BACZHn%2BdKQdNWM6W85kOT5LFPd9UauL4liykqy8Ohv0ExDfLlNHmmjNi1PiraOnCsQx284tgolq7XmaYfxZHekhGSYzO2UAJYTpiSYx5VyTVPe0FSEMZWGNHdMByAor0yu%2FwCWegwIJ3B0KIxagBsmZPMNKCInsiujzbG6dEKN1TsNMiVKmHwCHON2aKjTctlXP23Tz3&X-Amz-Signature=39a07fb986bdd779010de9dba0dc193b0aa5a2f23895c3eed698a0dd159b5a76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DCFNKE6%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T014918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDZxKVjyOrYmDksBdO8fmbnCa1c45OeHX2f9z51Z69K7AiEAyTtq5M0DNEyfw7K4Peq%2BhkFV3S2BGWX%2FOBmE5AqqA58q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBW2NSTUn532apQFYSrcAylI4LjOscD5Joceq62lAxvqYDoIPzFu5P3dJ5nqJV%2Blq0PdcCdNNExseOBYfrFQCvRsm2pMdVSgunh3%2FE3X8Tfjnz5lx5vVXkKI89f6VRP6jEqq3IbzjVrl470cFuZMjgao838GR4jEgYg5kYE78u3N%2BEXx7Hx2EU8eapbivasNcZyl8%2F2gfIzkM5TEmTcPlYbe9xkdVomsOdl%2Fqbt7VgAXnG7NHyeCP94jEVHcpP5spayuQCKzFYQSyW5RlHfgJlRHQgazyUo5s5%2B6R8rmIAjIw0y2S3ZJ%2FpReFPWV0dY2%2Fa%2B84jhx7Elmpxc9BySxVllaN1VK3E2af0W3vv%2BWfQefVL9CcoblbZYRLEZifnTpuR27j2G8Znolx9Ds7WBwptZdRg3mTNd07nsOXq9AYu22FW5U51pIYzkNfnCfL1n%2FTiR8jvm7zYjJqK1KoX9SkrfXt66MzNtaQfuL%2FF4iHbJH0eOYtMg41HFtZeI6%2BvoXpoA8lKlv4KZBlEV1jTUmEyaCHodF%2BjJCV7vV1v2uotrsWPway1ACZMWKpbEqfoPUWahyydlV6wWvjZzwkOJqmsyyYE7dAwNbD0h8D0ritFfd1QBE7FmpWKWceMhLgPA8QVKgivMrMBr49Gl%2BMLaf1MwGOqUB9oPN9cXMAybETwNJAn97BACZHn%2BdKQdNWM6W85kOT5LFPd9UauL4liykqy8Ohv0ExDfLlNHmmjNi1PiraOnCsQx284tgolq7XmaYfxZHekhGSYzO2UAJYTpiSYx5VyTVPe0FSEMZWGNHdMByAor0yu%2FwCWegwIJ3B0KIxagBsmZPMNKCInsiujzbG6dEKN1TsNMiVKmHwCHON2aKjTctlXP23Tz3&X-Amz-Signature=1f3147f34481220847c673f3c42f59f8ff6ca98eb737139410fca5f9e457f782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







