



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PHRZ5RT%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T131547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQgAG7egL%2FFJyIizLQh9OSZ20e659AE6xrF5tMNHOo4gIgBaJbMt3VzjHycMoVVlh6uHHp%2BMAHkIRkncUEsk3DKLgqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOarrh5OFFqU8geBzircA9aG5V8qyiQzw7BrGbkkc8lXZFt6Y12VNdpJlm3CJ2rQz5NZ0VdQvGeR0dHH9VjSasJR67jlQDca2KyDCPmUqWQsjGRc5Soverr1ZuCu1DyF%2Fq%2Fj%2FQ4rpf9xVIMOIzYpIRFcXpATw9fHP2E7VTH%2BjvZk%2Fxa62ofXlw4r9lim2qx9sOtxf2PELPftn8yPNzP4Ihc87JHI8ZusgRmfaZOiZUyUoqXIgx0NNhKCkjhUGnKliIvQNHOmjvd5PKdNeC5xmXAVb7ICyVu4vFw%2FL0zWQFPGBEvE9X%2B7Lj4241N6Laid4WNDGNcGoDlBJGa14fqoaxp6i%2BFB22STxpT%2BmiO4oRcaQxRzjtCbVapO4Zsrhl7fNYachZpNBkZZr%2Baqe2g2QlhdFDt7hMkCrBz8Pamuy%2F8m80oyKNPBkD69gxdnSiOk1TMHRSvnij8bVL0n7MIEfp9WMh1fhJTEMHoQLj4AhdeivZ7pe9VRiEcBPNYJWIIy%2BqKyLQsgCz6XxIZPvy0FHlyvfHJatU5jowJWAgc5bIn9lMHAPIXsg9KUamkiMogcCR3TSFM2P66Q9g97q8e411DxaKPBLXcTxI4s%2FfO33VTzltpycav9gZjmaOgkKND1KXePYtGSh%2FAc9GjsMJPo%2BM4GOqUB6Y8Y%2BZLHJ5a3BQy9Bwe2%2B7JMVlprE43YwVV0it3W6MtF6uDDuWbXOFKjFOxS%2B6bKxHgx%2FKeo9NTYs4ypORH%2FVmLLokswE3UvcD62bCdYoqYNzUToZbH5k42n70pnj8rIXW5Y5x82fncVkcL63tQKjJeDtc05FF5KCqgro6cxWbIgry1TldnVFv8oRkQqxbFl1vuES7FsD6aLyfGcp0PGo%2BJ0%2BDx5&X-Amz-Signature=9e20f7aee18948d596ead0a6375260d3df37e8e7105c979921b36aeead4aa999&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PHRZ5RT%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T131547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQgAG7egL%2FFJyIizLQh9OSZ20e659AE6xrF5tMNHOo4gIgBaJbMt3VzjHycMoVVlh6uHHp%2BMAHkIRkncUEsk3DKLgqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOarrh5OFFqU8geBzircA9aG5V8qyiQzw7BrGbkkc8lXZFt6Y12VNdpJlm3CJ2rQz5NZ0VdQvGeR0dHH9VjSasJR67jlQDca2KyDCPmUqWQsjGRc5Soverr1ZuCu1DyF%2Fq%2Fj%2FQ4rpf9xVIMOIzYpIRFcXpATw9fHP2E7VTH%2BjvZk%2Fxa62ofXlw4r9lim2qx9sOtxf2PELPftn8yPNzP4Ihc87JHI8ZusgRmfaZOiZUyUoqXIgx0NNhKCkjhUGnKliIvQNHOmjvd5PKdNeC5xmXAVb7ICyVu4vFw%2FL0zWQFPGBEvE9X%2B7Lj4241N6Laid4WNDGNcGoDlBJGa14fqoaxp6i%2BFB22STxpT%2BmiO4oRcaQxRzjtCbVapO4Zsrhl7fNYachZpNBkZZr%2Baqe2g2QlhdFDt7hMkCrBz8Pamuy%2F8m80oyKNPBkD69gxdnSiOk1TMHRSvnij8bVL0n7MIEfp9WMh1fhJTEMHoQLj4AhdeivZ7pe9VRiEcBPNYJWIIy%2BqKyLQsgCz6XxIZPvy0FHlyvfHJatU5jowJWAgc5bIn9lMHAPIXsg9KUamkiMogcCR3TSFM2P66Q9g97q8e411DxaKPBLXcTxI4s%2FfO33VTzltpycav9gZjmaOgkKND1KXePYtGSh%2FAc9GjsMJPo%2BM4GOqUB6Y8Y%2BZLHJ5a3BQy9Bwe2%2B7JMVlprE43YwVV0it3W6MtF6uDDuWbXOFKjFOxS%2B6bKxHgx%2FKeo9NTYs4ypORH%2FVmLLokswE3UvcD62bCdYoqYNzUToZbH5k42n70pnj8rIXW5Y5x82fncVkcL63tQKjJeDtc05FF5KCqgro6cxWbIgry1TldnVFv8oRkQqxbFl1vuES7FsD6aLyfGcp0PGo%2BJ0%2BDx5&X-Amz-Signature=10a5d694715caf77fef9421de2c3102c15a8400eb8f7529670af4f0c642f2a06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







